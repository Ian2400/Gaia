<!-- ENGINE FILE — replaced by Gaia upgrades. -->

# Stage: Review (Reviewer → Law-keeper → Herald)

Runs per task after tests pass, or standalone via `/{{TEMPLE}} review <ref>`.

## The tribunal

Dispatch both judges — they are read-only and may run in parallel:

- **Reviewer** ({{TEMPLE}}-{{GOD_REVIEWER_SLUG}}): the diff, the task, the
  spec's acceptance criteria. Expect: verdict + ranked findings with failure
  scenarios.
- **Law-keeper** ({{TEMPLE}}-{{GOD_LAW_KEEPER_SLUG}}): the diff, `laws.md`,
  `canonical.md`, the calibration profile's check commands. Expect: LAWFUL or
  violations with citations.

## Adjudicate

- Findings with failure scenarios and cited violations → back to the Builder
  (same iteration counting as the build loop).
- Opinion-grade findings (no failure scenario) → note for the human, do not
  block.
- Law-keeper's proposed new laws → collect for the human; never enforced this
  run.
- Both clean → proceed.
- If the review surface gates this class of work (creative output, risky
  code), the human sees the verdicts before anything proceeds, clean or not.

## The Herald

When all of a feature's tasks stand clean, dispatch the Herald
({{TEMPLE}}-{{GOD_HERALD_SLUG}}): the assembled diff, spec, verdicts (honest
ones — waivers named), calibration profile's conventions. Expect: commit
message, PR description, changelog entry, doc updates.

## The merge gate

Present to the human: the Herald's texts, the verdict summary, the branch.
Offer to open the PR; open it only on their yes. **Never merge.** The human
merges, or tells you explicitly per repository policy — and even then,
re-confirm once per session.

For entertainment temples with the Reveler rostered: offer a playtest pass on
the assembled build before the merge gate, and attach the experience report to
the PR when run.
