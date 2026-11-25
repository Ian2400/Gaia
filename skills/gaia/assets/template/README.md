# The temple template

This directory is the parameterized temple Gaia forges from. The generator
(Phase 2) fills placeholders and writes the result to the user's `~/.claude/`.

## Placeholder conventions

`{{NAME}}` — filled at forge time. Sources:

| Placeholder | Source |
|---|---|
| `{{TEMPLE}}`, `{{TEMPLE_TITLE}}`, `{{PURPOSE}}` | interview step 1 |
| `{{PANTHEON}}`, `{{PANTHEON_DISPLAY}}` | interview step 2 → `../pantheons.json` |
| `{{GOD_<ROLE>}}`, `{{GOD_<ROLE>_SLUG}}` | pantheon table + per-god overrides |
| `{{MODEL_<ROLE>}}` | interview step 8 (cost tiers) |
| `{{GATE_*}}`, `{{WIP_LIMIT}}` | interview step 7 (review surface) |
| `{{LAWS_*}}`, `{{CANONICAL_ENTRIES}}`, `{{GIFT_ENTRIES}}`, `{{DECLINED_GIFTS}}`, `{{ROSTER_ENTRIES}}` | interview steps 3–5, as drafted blocks |
| `{{HERALDRY_*}}` | interview step 6 (announcement conventions) |
| `{{POETICS_*}}` | interview step 9 (creative codex; only when Muse rostered) |
| `{{FORGE_DATE}}`, `{{GAIA_VERSION}}` | the forging itself |

## File classes

- **Engine** (`SKILL.md.tmpl`, `references/*`, `agents/*`): replaced by Gaia
  upgrades. Marked with an ENGINE FILE comment.
- **User data** (`laws.md.tmpl`, `canonical.md.tmpl`, `gifts.md.tmpl`,
  `heraldry.md.tmpl`, `poetics.md.tmpl`, `config.json.tmpl`): forged once,
  then owned by the user; never overwritten. (`poetics.md` is also appended
  to at human gates, by design — it stays user data because the appended
  rulings are the human's.)
- **Cached data** (`calibrations/`, created at run time): safe to delete.

## Forging notes (for the Phase 2 generator)

- Agent files: only the roles in the temple's roster are forged; file name is
  `<temple>-<god-slug>.md` in `~/.claude/agents/`.
- The Orchestrator is NOT an agent file — `SKILL.md.tmpl` becomes the temple's
  entry skill at `~/.claude/skills/<temple>/SKILL.md`.
- `references/*` copy through with only god-name/temple placeholders filled.
- Workflow references use `{{TEMPLE}}-{{GOD_<ROLE>_SLUG}}` agent names; resolve
  them against the forged roster, and strip stages for roles not rostered
  (e.g. Healer dispatch in `build.md` when no Healer exists).
- `poetics.md` is forged only when the Muse is rostered; without a Muse, skip
  the file and strip the Muse/poetics rules from `SKILL.md`.
- **Roster changes re-forge the engine.** The temple editor (spec §5.5) adds
  or retires gods after the forge by re-rendering SKILL.md and references/
  from the then-current template with the new roster — stripped stages must be
  recoverable. Two invariants make this safe, and both are hard rules for the
  generator: no interview answer is ever written into an engine file, and no
  engine content is ever written into a user-data file. A retired god's
  user-data files are kept, dormant.
