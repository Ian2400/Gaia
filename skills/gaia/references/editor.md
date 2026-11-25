# The temple editor

For temples that exist (in `~/.claude/gaia/temples.json`, or adopted from a
`~/.claude/skills/*/SKILL.md` that says it was forged by Gaia). Every
operation is a focused mini-interview touching only what it names; none
re-runs the whole interview. Confirm which temple when the account holds more
than one.

The enabling design (from the template README, both directions): engine files
carry no interview answers, user-data files carry no engine content. So engine
files may be re-forged freely, and user data is never touched except through
these flows with the user ruling on each change.

## Roster a god

1. Pick the role from the fourteen (reserve bench, or a core role previously
   trimmed). New roles beyond the fourteen are v2 — say so plainly; the
   mandate can often ride in an existing role's brief instead.
2. Mini-interview for that role only: deity name (default from the temple's
   pantheon table), model tier, any review-surface gates it adds (a Muse adds
   the creative-output gate question), any codex it needs — rostering a Muse
   runs interview step 9 (poetics) *now*; the user defining it only loosely is
   fine ("not yet ruled" markers, refined at gates and future edits).
3. Render the god's agent file; **re-forge the engine files** (`SKILL.md`,
   `references/*`) from the installed plugin's current template with the new
   roster, so stages stripped at the original forge return. Run the C.1
   verification checks.
4. Preview → the user's yes → install; update `config.json` roster and
   `temples.json`. A dormant codex left by a previously retired god is
   revived, not recreated.

## Retire a god

Confirm what its stage's absence means (no Victor → the Orchestrator's own
checklist at the gate; no Herald → the human writes their own PRs). Then:
remove the agent file, remove the roster entry, re-forge the engine without
its stages. Its user-data files stay, dormant, noted in `temples.json`.

## Amend a codex

Reopen only the named file's interview step (laws → step 4, canon → step 5,
gifts → step 3, heraldry → step 6, poetics → step 9). Amendments merge into
the existing file with new source dates; existing entries are never silently
rewritten — a changed rule keeps its ID with a dated amendment note, and
a withdrawn rule is marked withdrawn, not deleted.

## Change pantheon

Re-skin only: map every rostered role to the new pantheon's names (user
overrides welcome), rename agent files to the new slugs, re-forge engine files
(they embed god names), update `config.json` and `temples.json`. User data is
untouched except god names quoted inside it, which are updated with a dated
note. Warn that in-flight work referencing old agent names should finish
first.

## Upgrade the engine

Compare the temple's engine version (`temples.json`) with the installed
plugin's. Show the template changelog between them if available. On yes:
re-forge all engine files from the current template with the existing roster
and pantheon, run C.1 verification, preview the diff against the installed
engine files, install on confirmation, update the version. User data is never
touched by an upgrade — that is the contract that makes upgrades safe to
offer freely.

## Every operation

Preview before install (forge.md C.2-C.3 rules apply, including collision
stops); save state at each step so an interrupted edit resumes; update
`temples.json` last, after the install succeeds.
