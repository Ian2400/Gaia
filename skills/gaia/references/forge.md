# Phase C: The forging

Turn the interview's answers into an installed temple. Nothing touches
`~/.claude` until the user approves the preview.

## C.1 Render

Work from `assets/template/` (its README defines every placeholder and the
file classes). Into a preview directory —
`~/.claude/gaia/preview/<temple>/` — render:

1. **Agent files** — one per rostered role, from `agents/<role>.md.tmpl`, as
   `agents/<temple>-<god-slug>.md`. Unrostered roles are not rendered.
2. **The entry skill** — `SKILL.md.tmpl` → `skills/<temple>/SKILL.md`, with
   roster-conditional content stripped (no Muse → no Muse/poetics rules; the
   template README lists what strips).
3. **Workflow references** — `references/*.md` → `skills/<temple>/references/`,
   with unrostered roles' stages stripped (no Healer → `build.md` escalates
   straight to the human; no Victor → `review.md` keeps only the
   Orchestrator's own checklist path).
4. **User-data files** — `laws.md`, `canonical.md`, `gifts.md`, `heraldry.md`,
   `config.json`, and `poetics.md` when the Muse is rostered — from the
   drafted interview blocks. Unanswered topics carry their dated "not yet
   ruled" markers.
5. An empty `skills/<temple>/calibrations/` directory.

Invariants (hard rules, both directions): no interview answer in an engine
file; no engine content in a user-data file. If a render would violate either,
the template is wrong — stop and say so rather than patching around it.

After rendering, verify: no `{{` remains in any rendered file; every
`<temple>-<slug>` an engine file references exists as a rendered agent;
`config.json` parses.

## C.2 Preview

Show the user the preview tree (files + one-line purpose each) and offer to
open any file. Re-run `scripts/check_name.py <temple>` now (the account may
have changed since step 1). Amendments here loop back into the relevant
rendered file, not into a re-interview.

## C.3 Install (only on the user's explicit yes)

- Copy `agents/*` into `~/.claude/agents/`, `skills/<temple>/` into
  `~/.claude/skills/<temple>/`.
- **Collisions:** if any destination file exists, stop and list them — never
  overwrite silently. (A same-named temple is editor territory, not forge
  territory.)
- Append the temple to `~/.claude/gaia/temples.json` (create if missing):
  name, title, purpose, pantheon, roster with slugs, engine version
  (this plugin's version from its plugin.json), forge date.
- Delete the state file and the preview directory.

## C.4 First light

Tell the user, concretely: the temple answers to `/<temple>` in any repository
this account opens; its first run in a repo will calibrate (takes a few
minutes, read-only, ends with a profile they confirm); `/gaia` edits the
temple later (roster, pantheon, codices, engine). Suggest a first task in
their own repo small enough to watch the whole assembly line run once.
