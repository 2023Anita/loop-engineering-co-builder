# Core loop model

## The seven stages

1. **Goal** — desired observable outcome and boundaries.
2. **Observe** — current state, environment, evidence, and remaining budget.
3. **Decide** — choose the smallest action that can change an acceptance criterion.
4. **Act** — use an allowed tool inside the current permission envelope.
5. **Verify** — compare evidence with a criterion using an independent signal.
6. **Persist** — write the new state and evidence so the loop can resume.
7. **Route** — continue, repair, block, fail, or complete.

The loop is useful only when verification can change the next decision. A repeated prompt without feedback is repetition, not engineering.

## Two coupled loops

### Task loop

The task loop changes the project or produces the requested artifact. It should be bounded by a finite budget and explicit permissions.

### Improvement loop

The improvement loop changes the loop design. It consumes evidence from task-loop failures and produces a proposal. It must not automatically grant itself broader permissions or modify durable instructions.

## Minimal state machine

```text
designed -> ready -> running -> verifying -> completed
                         |          |
                         v          v
                      repairing <- failed
                         |
                         v
                       running

Any active state -> blocked | budget_exhausted
```

`completed` is evidence-gated. `blocked`, `failed`, and `budget_exhausted` are valid truthful outcomes, not incomplete prose to hide.

## Engineering properties

- **Bounded:** finite work, time, iterations, and permissions.
- **Observable:** current state and evidence are readable.
- **Controllable:** stop and approval gates can interrupt action.
- **Recoverable:** another agent can resume from artifacts.
- **Verifiable:** completion is based on external evidence.
- **Adaptable:** failures can generate reviewable improvements.
