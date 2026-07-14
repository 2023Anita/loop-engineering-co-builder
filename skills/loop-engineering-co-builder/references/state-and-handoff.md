# State and handoff

## State principles

`state.json` is an operational checkpoint, not a diary. Store facts needed for the next decision; keep detailed logs in `evidence/`.

Required fields:

- `schema_version`
- `loop_id`
- `goal`
- `status`
- `iteration`
- `max_iterations`
- `no_progress_count`
- `max_no_progress`
- `completed_criteria`
- `pending_criteria`
- `last_action`
- `last_verification`
- `next_action`
- `blocker`
- `required_approval`
- `evidence`
- `updated_at`

Use ISO 8601 timestamps. Use paths relative to the project when possible. Never store secret values.

## Update discipline

Update state after a meaningful action or a terminal decision. If an action fails, persist the failure and evidence before trying a repair. Do not increment `completed_criteria` from model confidence alone.

Increment `no_progress_count` when an iteration does not change any acceptance criterion, blocker, or validated understanding. Reset it only when evidence shows progress.

## Handoff contract

`handoff.md` must let a fresh agent continue in under five minutes. Include:

1. goal and current status;
2. completed and pending criteria;
3. last successful verification;
4. failed attempts worth avoiding;
5. current blocker and required approval;
6. exact next action and expected evidence;
7. commands needed to validate or resume.

Do not write “continue working” as a next action. Name the file, command, check, or decision.
