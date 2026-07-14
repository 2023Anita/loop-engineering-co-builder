#!/usr/bin/env python3
"""Validate the structure and completion consistency of a loop workspace."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_FILES = (
    "loop-spec.md",
    "state.json",
    "verification-report.md",
    "handoff.md",
    "retrospective.md",
    "improvement-proposal.md",
)
REQUIRED_STATE_KEYS = {
    "schema_version",
    "loop_id",
    "goal",
    "status",
    "iteration",
    "max_iterations",
    "no_progress_count",
    "max_no_progress",
    "completed_criteria",
    "pending_criteria",
    "last_action",
    "last_verification",
    "next_action",
    "blocker",
    "required_approval",
    "evidence",
    "updated_at",
}
STATUSES = {
    "designed",
    "ready",
    "running",
    "verifying",
    "repairing",
    "blocked",
    "failed",
    "completed",
    "budget_exhausted",
}
SPEC_HEADINGS = (
    "Goal and boundaries",
    "Acceptance criteria",
    "Iteration policy",
    "Tool and permission policy",
    "Stop conditions",
    "Recovery and handoff",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("loop_dir", type=Path)
    return parser.parse_args()


def main() -> int:
    root = parse_args().loop_dir.resolve()
    failures: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        failures.append(f"loop directory does not exist: {root}")
    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            failures.append(f"missing required file: {name}")
    if not (root / "evidence").is_dir():
        failures.append("missing evidence directory")

    state = None
    state_path = root / "state.json"
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"invalid state.json: {exc}")

    if isinstance(state, dict):
        missing_keys = sorted(REQUIRED_STATE_KEYS - state.keys())
        if missing_keys:
            failures.append("state.json missing keys: " + ", ".join(missing_keys))
        if state.get("status") not in STATUSES:
            failures.append(f"invalid status: {state.get('status')!r}")
        iteration = state.get("iteration")
        maximum = state.get("max_iterations")
        if not isinstance(iteration, int) or not isinstance(maximum, int):
            failures.append("iteration and max_iterations must be integers")
        elif iteration < 0 or maximum < 1 or iteration > maximum:
            failures.append("iteration counters are inconsistent")
        if state.get("status") == "blocked" and not (
            state.get("blocker") or state.get("required_approval")
        ):
            failures.append("blocked state requires blocker or required_approval")

    spec_path = root / "loop-spec.md"
    spec = spec_path.read_text(encoding="utf-8") if spec_path.is_file() else ""
    for heading in SPEC_HEADINGS:
        if not re.search(rf"^## {re.escape(heading)}\s*$", spec, re.MULTILINE):
            failures.append(f"loop-spec.md missing section: {heading}")
    has_todo = "TODO" in spec
    if has_todo:
        warnings.append("loop-spec.md still contains TODO placeholders")

    report_path = root / "verification-report.md"
    report = report_path.read_text(encoding="utf-8") if report_path.is_file() else ""
    report_passes = bool(re.search(r"Overall status:\s*PASS\b", report, re.IGNORECASE))
    if isinstance(state, dict) and state.get("status") == "completed":
        if has_todo:
            failures.append("completed state cannot retain TODO placeholders in loop-spec.md")
        if not report_passes:
            failures.append("completed state requires Overall status: PASS")
        if state.get("pending_criteria"):
            failures.append("completed state cannot have pending criteria")
        if state.get("required_approval"):
            failures.append("completed state cannot have required approval")
        for evidence in state.get("evidence", []):
            if isinstance(evidence, str) and not (root / evidence).exists():
                failures.append(f"missing evidence path: {evidence}")

    result = {"ok": not failures, "failures": failures, "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
