<!-- ENGINE FILE — replaced by Gaia upgrades. -->

# Stage: Plan (Architect → human gate)

## Dispatch

Send the Architect ({{TEMPLE}}-{{GOD_ARCHITECT_SLUG}}) a standalone brief:

- The request, in the human's own words, plus anything they clarified.
- The repo calibration profile.
- The law, canon, and gift entries plausibly relevant (don't send all three
  files wholesale if they are long — select).
- Where specs live: `specs/<feature-slug>/` (create the slug from the request).

Expect back: paths of `spec.md`, `plan.md`, `tasks.md`, and the five-line
summary.

## Validate before the gate

Reject the plan back to the Architect (with reasons) if:

- `plan.md` has no test strategy, or the strategy is "add tests" without
  substance.
- Any two tasks own the same file.
- A task has no acceptance criteria or no risk level.
- The plan contradicts a law or duplicates a canon entry.
- Task count is out of proportion to the request (a plan nobody can review is
  not a plan).

Maximum two rejection loops; then take the problem to the human instead.

## The human gate

Present to the human: the five-line summary, the task list with risk levels,
and the open questions. Ask for approval, amendment, or rejection — plainly,
one decision. Record the verdict (and any amendments) at the top of `plan.md`
as a dated note. If the review surface gates risky code, mark which tasks the
human must individually clear before build.

Do not proceed to build on silence. Approval is explicit.
