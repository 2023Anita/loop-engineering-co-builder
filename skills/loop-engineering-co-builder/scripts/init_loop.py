#!/usr/bin/env python3
"""Initialize a bounded Loop Engineering workspace from bundled templates."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


TEMPLATE_FILES = (
    "loop-spec.md",
    "state.json",
    "verification-report.md",
    "handoff.md",
    "retrospective.md",
    "improvement-proposal.md",
)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "loop"


def render(template: str, replacements: dict[str, str]) -> str:
    for key, value in replacements.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("goal", help="Concrete goal for the loop")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root")
    parser.add_argument("--slug", help="Stable loop identifier")
    parser.add_argument("--title", help="Human-readable title")
    parser.add_argument("--max-iterations", type=int, default=8)
    parser.add_argument("--max-no-progress", type=int, default=2)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_iterations < 1 or args.max_no_progress < 1:
        print("error: iteration limits must be positive integers", file=sys.stderr)
        return 2

    slug = args.slug or slugify(args.goal)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        print("error: slug must match [a-z0-9][a-z0-9-]*", file=sys.stderr)
        return 2

    title = args.title or args.goal
    templates_dir = Path(__file__).resolve().parent.parent / "templates"
    target = args.root.resolve() / ".loop" / slug
    if target.exists():
        print(f"error: loop already exists: {target}", file=sys.stderr)
        return 1

    missing = [name for name in TEMPLATE_FILES if not (templates_dir / name).is_file()]
    if missing:
        print(f"error: missing bundled templates: {', '.join(missing)}", file=sys.stderr)
        return 1

    target.mkdir(parents=True)
    (target / "evidence").mkdir()
    replacements = {
        "TITLE": title,
        "SLUG": slug,
        "GOAL": args.goal,
        "GOAL_JSON": json.dumps(args.goal, ensure_ascii=False)[1:-1],
        "MAX_ITERATIONS": str(args.max_iterations),
        "MAX_NO_PROGRESS": str(args.max_no_progress),
        "UPDATED_AT": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }
    for name in TEMPLATE_FILES:
        content = (templates_dir / name).read_text(encoding="utf-8")
        (target / name).write_text(render(content, replacements), encoding="utf-8")

    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
