# Source provenance: Anthropic Loop Engineering

This Skill was informed by a user-supplied bilingual subtitle of an Anthropic technical talk and by official public material about agent loops. The raw subtitle is intentionally not redistributed.

## Ideas retained

- A model call is not durable state; the surrounding harness must provide tools, instructions, environment, history, and results.
- A tool call is a request from the model; the harness executes it and returns an observation for the next turn.
- Useful loops need explicit completion criteria, validation, and stopping conditions.
- Permissions should distinguish allowed, approval-required, and denied actions.
- Repeatable workflows differ from ad hoc agent delegation because their stages and checks can be saved and rerun.
- Automated checks and human review are complementary verification layers.

## Claims deliberately constrained

- Personal claims about automating most of one's life are treated as individual practice, not universal advice.
- Optimistic statements about agents doing “almost anything” are bounded by tools, permissions, sandboxing, evidence, cost, and accountable review.
- Claude-specific terms are mapped conceptually to Codex and other runtimes; command and implementation equivalence is not assumed.

## Engineering inference

The reusable abstraction is:

`goal + state + tools + permissions + verification + stop conditions + handoff`

This is an engineering synthesis, not a verbatim course transcript.
