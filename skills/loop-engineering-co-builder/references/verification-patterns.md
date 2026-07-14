# Verification patterns

## Evidence ladder

Prefer the strongest affordable signal:

1. deterministic parser, schema, type, or invariant check;
2. unit, integration, or end-to-end test;
3. build, lint, static analysis, or deployment status;
4. API or repository read-back of external state;
5. screenshot or behavior inspection;
6. rubric-based human review;
7. model self-review.

Model self-review can find issues but should not be the only completion gate for consequential work.

## Criterion mapping

Map every required criterion to one or more checks. Record:

- command or review method;
- exit code or decision;
- evidence path;
- timestamp;
- result: `PASS`, `FAIL`, or `BLOCKED`.

## Avoid circular verification

Circular verification occurs when the producer and verifier share the same assumptions and no external observation. Examples:

- asking the same model whether its article is accurate without checking sources;
- considering `git push` successful without reading repository state;
- declaring a UI fixed because code compiled without inspecting behavior.

Add an independent signal or report the limitation.

## Completion gate

Completion requires:

- all required criteria pass;
- evidence paths exist or external state has been read back;
- no unresolved approval gate remains;
- `verification-report.md` says `Overall status: PASS`;
- `state.json` is consistent with the report.
