# Phase A: The terrain survey

Survey the account before asking anything, so interview questions are specific
and discovered tools become divine-gift candidates. Fast — minutes, not hours.
Everything found is a *candidate* until the user confirms it in interview
step 3.

## A.1 Enumerate (local, read-only)

- **MCP servers / connectors:** `claude mcp list` if available; else read
  `~/.claude.json` and `~/.claude/settings.json` for `mcpServers` entries.
  Note each server's name and, where stated, what it serves.
- **Plugins:** installed plugin list (`claude plugin list` or
  `~/.claude/plugins/`).
- **Skills:** `~/.claude/skills/*/SKILL.md` frontmatter names + descriptions
  (user-level), noting any that are themselves temples.
- **Agents:** `~/.claude/agents/*.md` frontmatter names (needed later for
  collision checks; also reveals existing agent habits).
- **CLIs that matter:** check for `gh`, `git`, common runtimes (node, python,
  etc.) on PATH — one `--version` call each, nothing more.
- **Working repos:** the folders under the user's usual repository root(s), if
  evident — names only, never contents.

## A.2 Usage history (best-effort, never required)

If local session logs are readable, you may skim for recurring task *types*
(not contents). Every inference is presented as a question ("you seem to do a
lot of database work — should the temple staff a Deep-keeper?"), approved or
discarded by the user, and never binding. Formats change often: a failed or
empty read is silently skipped, never retried, never mentioned as an error.

## A.3 Classify into gift candidates

For each finding, draft: what it grants, which roles would wield it
(vocabulary: the fourteen roles), and your confidence it's relevant to this
temple's stated purpose. Order by confidence. This list feeds interview
step 3 — do not finalize `gifts.md` here.

## A.4 Guide mode (sparse terrain)

If the survey finds little (no MCP servers, few tools), switch posture from
surveyor to guide — this is a first-class path for new users and fresh
accounts, not a fallback, and the tone is "let's equip you," never "you're
missing things."

**What ships statically is only the category list** (categories date slowly;
tools date fast):

| Category | Typically serves |
|---|---|
| Version control & PRs | every temple (usually `gh` CLI, no MCP needed) |
| Database access | Deep-keeper work |
| Browser / web testing | Test hunter, Reveler |
| Documentation & search | Architect research |
| Memory / knowledge store | Chronicler |
| Image & asset generation | Muse work |
| Team communication | Herald delivery |

**Options are fetched live, per relevant category** (relevance judged by the
temple's purpose):

1. Query Anthropic's curated MCP subregistry
   (`https://api.anthropic.com/mcp-registry` — check its live docs for the
   current path shape) and/or the official registry
   (`https://registry.modelcontextprotocol.io`, API version `/v0`-ish —
   verify against its OpenAPI docs at call time; the spec is marked unstable).
2. Cross-check promising candidates with a web search against community
   directories that carry quality signals (Glama's quality/maintenance
   ratings, PulseMCP's Official/Reference/Community labels).
3. Propose at most one best-in-class option per category, stating: what it
   does, its source, its official/community status, and that a directory
   listing is not a safety endorsement. The user approves or declines each
   install; help with setup on approval. Decline → record and move on,
   never re-pitch.

**Offline or unreachable registries:** name the relevant categories, say the
lookup is unavailable, and continue — a temple with few gifts is still a
working temple. Never recommend specific tools from memory in place of the
live lookup; memory of "best in class" goes stale faster than categories do.

## A.5 The terrain report

One page: tools found (grouped), gift candidates ranked, gaps (categories
relevant to the purpose with nothing in them), and anything odd (two tools
serving the same need — a canon question for step 4). Show it, let the user
correct it, save it to state. Then the interview.
