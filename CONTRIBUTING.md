# Contributing to NetShield ARP Guardian

The project favors small, explainable changes over large mechanical rewrites.

## Style

- Name helpers after the decision they make, not the implementation detail they happen to use today.
- Comments should explain why a constraint exists or why a less-obvious choice was made.
- Keep detection signals independent and make their evidence visible in the result.
- Avoid comments that merely restate the next line of code.
- Keep simulations safe: they may create observations, but they must not perform ARP poisoning.

## Pull requests

Use the local PR ledger under `docs/pull_requests/` as a model for focused, reviewable changes. Each PR should explain its goal, scope, validation, risk, and rollback path.

## LOC

The repository already exceeds the requested 500K source-line threshold. Do not add duplicate or generated filler solely to increase LOC; new lines should correspond to maintainable behavior, tests, documentation, or clearly justified supporting infrastructure.
