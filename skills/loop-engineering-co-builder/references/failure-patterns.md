# Failure patterns

## Infinite retry

**Signal:** same action and failure repeat without new evidence.

**Response:** stop after the configured no-progress threshold; classify the failure; change strategy or escalate. Do not merely increase retries.

## Goal drift

**Signal:** new work no longer maps to an acceptance criterion.

**Response:** stop, restore scope from `loop-spec.md`, and propose a scope change if genuinely needed.

## Permission creep

**Signal:** repair proposes broader access because the current action is blocked.

**Response:** preserve the block and ask for narrowly scoped approval. Never rewrite the policy from inside the task loop.

## False completion

**Signal:** plausible artifact exists, but evidence or verification is absent.

**Response:** set status to `verifying` or `failed`, not `completed`.

## Context dependence

**Signal:** the next step exists only in conversation history.

**Response:** persist current state, decision, evidence, and exact next action before continuing.

## Verifier gaming

**Signal:** output is optimized to satisfy a weak check while missing the real goal.

**Response:** strengthen acceptance criteria with behavior, independent evidence, or human review.

## Premature self-improvement

**Signal:** one failure triggers a permanent Skill or policy rewrite.

**Response:** collect repeated evidence, write an improvement proposal, assess blast radius and rollback, then wait for approval.
