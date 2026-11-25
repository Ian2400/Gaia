<!-- ENGINE FILE — replaced by Gaia upgrades. -->

# Stage: Build (per task: Builder → Test hunter)

Run per approved task from `tasks.md`, respecting the WIP limit. Parallelize
only tasks with disjoint file ownership and no dependency edges.

## Branch discipline

- One branch per task: `{{TEMPLE}}/<feature-slug>/<task-id>`, cut from the
  feature's integration branch (or the default branch for single-task work).
- The Builder works only there. Commit on the task branch when the task
  passes its stages — never merge branches yourself.

## Dispatch the Builder

Brief ({{TEMPLE}}-{{GOD_BUILDER_SLUG}}), standalone:

- The one task, verbatim from `tasks.md`: files owned, interface contract,
  acceptance criteria, named gifts, risk level.
- `spec.md` goal section, the calibration profile, relevant canon/law/gift
  entries.
- The branch name. For data/infra tasks, dispatch the Deep-keeper instead if
  rostered.

## Dispatch the Test hunter

On the Builder's return, brief ({{TEMPLE}}-{{GOD_TEST_HUNTER_SLUG}}):

- The task (acceptance criteria prominent), the plan's test strategy for it,
  the Builder's "attack first" note, the branch, and the calibration
  profile's test-runner section (command, test locations, naming convention,
  known pass state).

## The loop

- Test hunter FAIL → back to the Builder with the failure verbatim. Count
  iterations per distinct error; at `max_fix_iterations` on the same error,
  stop — dispatch the Healer (if rostered) for diagnosis, else escalate to
  the human with the full trail.
- Test hunter PASS → the task proceeds to review (`review.md`).

Never weaken a test to exit the loop; that path goes through the human only.
