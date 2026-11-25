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
| `{{FORGE_DATE}}`, `{{GAIA_VERSION}}` | the forging itself |

## File classes

- **Engine** (`SKILL.md.tmpl`, `references/*`, `agents/*`): replaced by Gaia
  upgrades. Marked with an ENGINE FILE comment.
- **User data** (`laws.md.tmpl`, `canonical.md.tmpl`, `gifts.md.tmpl`,
  `heraldry.md.tmpl`, `config.json.tmpl`): forged once, then owned by the
  user; never overwritten.
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
