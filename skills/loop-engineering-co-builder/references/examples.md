# Examples

## 1. Technical article loop

- Goal: turn a source transcript into a readable, technically accurate article.
- State: source inventory, claim ledger, outline status, illustration status, publication status.
- Verification: source links, claim checks, structural validator, human editorial review.
- Gates: external publication and account actions require approval.
- Stop: article package passes checks; publication is either verified or explicitly blocked.

## 2. Code repair loop

- Goal: fix one reproducible defect without unrelated refactors.
- State: reproduction, hypothesis, changed files, test results.
- Verification: failing test before fix, passing targeted tests after fix, relevant regression suite.
- Stop: test-backed fix or a documented environmental blocker.
- Anti-pattern: repeatedly changing code without preserving the original failure evidence.

## 3. Research evidence loop

- Goal: answer a bounded research question with traceable evidence.
- State: query variants, screened sources, inclusion reasons, open evidence gaps.
- Verification: primary-source checks, citation-to-claim mapping, date and scope validation.
- Gates: do not upload private manuscripts or sensitive data to third parties.
- Stop: coverage threshold met, contradiction surfaced, or evidence gap reported honestly.

## 4. Safety-blocked loop

- Goal: publish a repository after validation.
- State: local checks pass; no publication approval exists.
- Correct outcome: `blocked` with `required_approval` naming `git commit` and `git push`.
- Incorrect outcome: broadening permissions or treating local readiness as publication success.
