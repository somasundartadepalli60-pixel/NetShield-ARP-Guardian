# PR 071: Tighten input validation

## Goal
Reject malformed ARP observations before they reach stateful services.

## Why this change matters
This incremental change keeps the codebase easier to review than one large rewrite. The intent is to improve one boundary at a time while preserving the defensive, local-first design.

## Scope
- Keep existing public behavior unless the change explicitly documents a compatibility improvement.
- Prefer small, named helpers over clever one-liners.
- Preserve deterministic behavior for simulations and tests.
- Keep security decisions explainable to an operator.

## Review notes
Review focus: verify validation behavior remains isolated from unrelated services.

## Validation
- Run `python -m compileall -q app tests`.
- Run the relevant pytest module(s).
- Check that generated reports and database state remain stable.

## Risk
Low to moderate. This is intended to be merged as an isolated, reviewable step rather than bundled with unrelated behavior changes.

## Rollback
Revert this change independently if validation exposes a regression.
