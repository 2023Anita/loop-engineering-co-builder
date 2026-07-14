# Loop specification schema

`loop-spec.md` is the human-readable contract. Keep each field concrete enough to be tested.

## Required sections

### Identity

- title
- slug
- owner or responsible role
- mode

### Goal and boundaries

- one-sentence goal
- in scope
- out of scope
- non-goals

### Inputs and outputs

- required inputs and where they come from
- expected artifacts and exact paths or destinations
- sensitive-data classification

### Acceptance criteria

Each criterion needs:

| Field | Meaning |
|---|---|
| ID | Stable identifier such as `AC-01` |
| Criterion | Observable result |
| Verifier | Command, inspection, API read, or human gate |
| Evidence | File, log, screenshot, URL, or recorded decision |
| Required | Whether failure blocks completion |

Avoid criteria such as “high quality” unless a rubric or reviewer makes them observable.

### Iteration policy

- maximum iterations
- maximum consecutive no-progress iterations
- retry policy by failure class
- resource or time budget if relevant

### Tool and permission policy

- allowed actions
- approval-required actions
- denied actions
- credentials or secrets policy

### Stop conditions

- success
- failure
- stalled
- blocked
- budget exhausted

### Recovery and handoff

- checkpoint location
- evidence location
- resumption procedure
- escalation target

## Design review

Before setting state to `ready`, confirm:

- every required acceptance criterion has a verifier;
- every risky action has a gate;
- every loop has a finite stopping rule;
- state can be reconstructed without chat history;
- the next action is concrete and in scope.
