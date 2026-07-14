# Loop specification: {{TITLE}}

## Identity

- Slug: `{{SLUG}}`
- Owner: TODO
- Mode: design

## Goal and boundaries

- Goal: {{GOAL}}
- In scope: TODO
- Out of scope: TODO
- Non-goals: TODO

## Inputs and outputs

- Required inputs: TODO
- Expected outputs: TODO
- Sensitive-data classification: TODO

## Acceptance criteria

| ID | Criterion | Verifier | Evidence | Required |
|---|---|---|---|---|
| AC-01 | TODO | TODO | `evidence/` | yes |

## Iteration policy

- Maximum iterations: {{MAX_ITERATIONS}}
- Maximum consecutive no-progress iterations: {{MAX_NO_PROGRESS}}
- Retry policy: diagnose before retry; do not repeat an unchanged failed action

## Tool and permission policy

- Allowed: read-only inspection; project-local validation; TODO
- Approval required: deletion; production writes; publication; external messages; `git commit`; `git push`; TODO
- Denied: out-of-scope actions; secret exfiltration; silent policy changes

## Stop conditions

- Success: all required criteria pass with evidence
- Failure: unrecoverable verifier or dependency failure
- Stalled: {{MAX_NO_PROGRESS}} consecutive iterations without evidence of progress
- Blocked: required input or approval is unavailable
- Budget exhausted: iteration reaches {{MAX_ITERATIONS}} without success

## Recovery and handoff

- Checkpoint: `state.json`
- Evidence: `evidence/`
- Resume: read this file, `state.json`, and `handoff.md`; execute `next_action`
- Escalation: TODO
