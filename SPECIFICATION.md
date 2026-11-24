# Gaia — A Builder of AI Factories

**Status:** Draft v0.3 — for review
**Author:** Ian F Pytlarz (with Claude)
**Last updated:** 2026-11-24

Gaia is not a factory. Gaia is the primordial mother who *forges* factories.

She is a Claude Code **plugin, installed at the user level**. Running `/gaia`
interviews you about one context of your working life — your tools, your rules,
your goals — and raises a **temple**: a bespoke AI factory staffed by a pantheon
of specialized agents, governed by laws drawn from your answers, and installed
in your user account so it travels with you across every repository you open
there.

One account may hold many temples. A work account gets a temple whose
law-keeper enforces institutional policy and whose gods know the local servers
and MCP tools. A personal account might hold two: one for building software,
one for entertainment, each with its own roster and laws. And each temple is
raised to the pantheon of its builder's choosing — Greek by default, but Roman,
Norse, and Hindu pantheons map onto the same factory roles (see §4).

**Lineage:** Gaia generalizes the pattern proven by
[pr-blueprint](https://github.com/Ian2400/pr-blueprint) — a plugin containing a
generator skill plus a parameterized template, where an interview produces a
bespoke artifact. pr-blueprint forges one repo-level review skill; Gaia forges
whole user-level factories.

---

## 1. Design principles

Carried forward from factory research (v0.1), applied to generated factories:

1. **Humans hold the merge gate.** Temple agents may open PRs; only a human merges.
2. **One agent, one job.** Each god has a narrow mandate, defined inputs, and a
   defined shape of return.
3. **Spec before code.** Factory work flows through a gated pipeline
   (specify → plan → tasks → implement → verify); every plan carries a test strategy.
4. **Isolation.** Writing agents work in isolated worktrees/branches; two writers
   never share files.
5. **Reviewers are read-only.** The reviewer and law-keeper can never edit, so
   their judgment stays independent.
6. **Evidence over vibes.** Laws that must always hold are enforced by scripts
   and checks, not prompt text alone.
7. **Bounded concurrency.** 3–5 parallel agents max; an agent stuck 3+
   iterations on one error is stopped and escalated.
8. **Small, reviewable tasks** with explicit file boundaries.

Principles specific to the builder:

9. **Interview once, use everywhere.** Context lives at the account level; the
   user answers questions once per temple, not once per repo.
10. **The terrain shapes the temple.** Gaia surveys the account before asking
    anything, so questions are specific, and discovered tools become **divine
    gifts** the generated agents are explicitly told to reach for. A sparse
    terrain is not a dead end: Gaia then plays guide instead of surveyor,
    suggesting starter connectors and tools worth adding (§5.1).
11. **Roles are fixed; gods are skins.** The factory is written against named
    *roles* (architect, builder, law-keeper…). A pantheon is a lookup table
    from role to deity name, chosen per temple. Greek, Roman, Norse, and Hindu
    ship in v1; adding a pantheon is adding a table, not rewriting agents.
12. **Temples calibrate to each repo.** A temple carries account-wide laws, but
    on first use in a repository it runs a quick survey (stack, CI, lint,
    conventions) and caches a per-repo profile it then honors.
13. **The review surface is the dial.** What separates a work temple from an
    entertainment temple is mostly *what gets surfaced to the human*: a work
    temple gates security and standards tightly; an entertainment temple gates
    creative decisions (art direction, game design choices) tightly to prevent
    slop, while routine code flows with less ceremony. The interview sets this
    dial per temple.
14. **Customization survives upgrades.** A user's laws, rosters, pantheon
    choice, and calibration are data files the Gaia engine never overwrites;
    re-running `/gaia` upgrades engine files and offers a re-interview.

## 2. The cosmology (what exists where)

| Mythic name | Technical reality |
|---|---|
| **Gaia** | The plugin: a generator skill + parameterized temple template, installed from this GitHub repo into any account |
| **A temple** | One generated factory: agents + skills + laws + state, written to the account's user-level `~/.claude/` |
| **A pantheon** | A lookup table mapping factory roles to deity names (Greek, Roman, Norse, Hindu in v1) |
| **The gods** | The agents staffing a temple, named `<temple>-<god>` from its pantheon |
| **The laws** | That temple's constitution: standards, canonical implementations, security policy, noise list — the law-keeper's enforcement material |
| **Divine gifts** | The MCP servers, connectors, and skills Gaia found (or helped install) in the account; agents are told which gifts solve which tasks |
| **The terrain survey** | Gaia's automated inspection of the account before the interview |
| **Repo calibration** | A temple's cached per-repository profile, built on first use |

## 3. The roles (template roster)

Every temple is staffed from this bench of *roles*. The core seven are the
default; the interview trims or extends the roster to fit the temple's purpose.
Deity names come from the temple's pantheon (§4) — the Greek names below are
the default skin.

### Core seven

| Role | Greek default | Duty | Access |
|---|---|---|---|
| **Orchestrator** | Zeus | The main session. Decomposes requests, dispatches gods, enforces WIP limits and kill criteria. Writes no production code. | Full, but delegates |
| **Architect** | Athena | Turns a request into spec + plan + tasks with a mandatory test strategy. The plan is a human gate. | Read-only + spec files |
| **Builder** | Hephaestus | Implements one approved task at a time in an isolated branch, using the divine gifts named for the task. | Read/write, scoped to task |
| **Test&nbsp;hunter** | Artemis | Writes and runs tests, hunts edge cases and regressions. | Read/write tests, run commands |
| **Reviewer** | Apollo | Independent, read-only review of the finished diff. | Read-only |
| **Law-keeper** | Themis | Enforces the temple's laws: standards, canonical implementations, security, conventions. Functional in v1 (§6). | Read-only + checks |
| **Herald** | Hermes | Commit messages, PR descriptions, changelogs, docs. | Read-only + docs |

### Reserve bench (added by interview when the terrain calls for them)

| Role | Greek default | Duty | Likely trigger |
|---|---|---|---|
| **Chronicler** | Mnemosyne | Decision log — records why choices were made | Long-lived projects |
| **Steward** | Hestia | Housekeeping — dependencies, dead code, hygiene | Mature codebases |
| **Deep-keeper** | Poseidon | Data & infrastructure — databases, migrations, environments | DB/warehouse gifts in terrain |
| **Healer** | Asclepius | Debugger — root-cause diagnosis of failures the test hunter can't explain | Complex systems |
| **Victor** | Nike | Release management — tags, release notes, deploy checklists | Repos with release processes |
| **Muse** | The Muses | Creative generation — narrative, design, game content | Entertainment temples |
| **Reveler** | Dionysus | Playtester — experiences the entertainment as a user would | Entertainment temples |

### The assembly line (inside every temple)

```
Human request
   ▼
Orchestrator ── trivial? ──► handle directly
   ▼
Architect: SPEC + PLAN + TASKS ──► ★ HUMAN GATE
   ▼
Builder: implement task N (isolated branch, divine gifts in hand)
   ▼
Test hunter: tests pass ──► fail? loop (max 3, then escalate)
   ▼
Reviewer: read-only review ──► findings? back to Builder
   ▼
Law-keeper: automated gates (the temple's laws)
   ▼
Herald: commit, PR description, docs
   ▼
★ HUMAN GATE: review & merge
```

The pipeline's *stages* are fixed; the **review surface** — which decisions
pause for a human — is per-temple config. An entertainment temple inserts a
human gate on creative output (Muse deliverables, design decisions) and may
relax the code-review gate; a work temple does the opposite.

## 4. Pantheons (role → deity mapping)

Feasibility: **yes.** Because agents are written against roles and deity names
are injected at forge time, supporting a pantheon costs one lookup table
(`pantheons.json`). Agents are named `<temple>-<god>` (e.g. `worktemple-athena`,
`gamehall-loki`), which also solves user-level namespace collisions: both
halves of the name are per-temple.

Proposed v1 mappings (⚠ marks looser fits worth a second opinion):

| Role | Greek | Roman | Norse | Hindu |
|---|---|---|---|---|
| Orchestrator | Zeus | Jupiter | Odin | Indra |
| Architect | Athena | Minerva | Mimir | Brihaspati |
| Builder | Hephaestus | Vulcan | Völundr | Vishvakarma |
| Test hunter | Artemis | Diana | Skadi | Durga ⚠¹ |
| Reviewer | Apollo | Veritas ² | Heimdall | Surya |
| Law-keeper | Themis | Iustitia | Forseti | Yama |
| Herald | Hermes | Mercury | Hermóðr | Narada |
| Chronicler | Mnemosyne | Moneta | Muninn ⚠³ | Chitragupta |
| Steward | Hestia | Vesta | Frigg | Annapurna |
| Deep-keeper | Poseidon | Neptune | Njörðr | Varuna |
| Healer | Asclepius | Aesculapius | Eir | Dhanvantari |
| Victor | Nike | Victoria | Týr ⚠⁴ | Kartikeya |
| Muse | The Muses | The Camenae | Bragi | Saraswati |
| Reveler | Dionysus | Bacchus | Loki ⚠⁵ | Krishna |

¹ Durga is a demon-slayer rather than a huntress — arguably the *better* myth
  for hunting bugs.
² Rome worshipped Apollo under his Greek name, so Veritas (truth personified)
  takes the role to keep the pantheons distinct.
³ Muninn ("memory") is one of Odin's ravens, not a god; Saga (goddess
  associated with history) is the alternative.
⁴ Norse has no clean victory deity; Týr (war, upheld oaths) is nearest. ⁵ Loki
  as playtester is a feature: the trickster who breaks your game is exactly who
  should test it.

Rules: one pantheon per temple (keeps naming coherent); any individual god's
name can be overridden in the interview (your temple, your rites); custom
pantheons are just a user-supplied table.

## 5. The Gaia skill (the generator)

`/gaia` runs once per temple, keeps its own state, and can pause and resume
across sessions (as pr-blueprint does). Its phases:

### 5.1 Terrain survey (automated, before any question)
- Enumerate the account's MCP servers, connectors, installed plugins, and
  user-level skills; note which repos the user commonly works in.
- **May read session/usage history** to infer common task types — but every
  inference drawn from history is presented for approval before it shapes the
  temple, and none is binding: past usage may not reflect what a *new* temple
  is for. History-reading is strictly best-effort and never required: session
  formats vary by platform and change often, so a failed or empty read is
  silently skipped.
- Classify findings into candidate **divine gifts** ("you have a Greenplum MCP
  server — the Deep-keeper could own warehouse tasks").
- **Sparse terrain → guide mode.** When little is installed, Gaia switches from
  surveyor to guide. To avoid shipping a catalog that rots, suggestions are
  **fetched live, not bundled**: the only static piece is a short list of tool
  *categories* most developers need (version control, database, browser/docs,
  memory, image/asset generation…), chosen by the temple's purpose — categories
  date far slower than tools. For each relevant category, Gaia queries
  Anthropic's curated MCP subregistry (`api.anthropic.com/mcp-registry`, which
  conforms to the official registry API at `registry.modelcontextprotocol.io`)
  and cross-checks with a web search against community directories that carry
  quality signals (Glama's quality/maintenance ratings, PulseMCP's
  Official/Reference/Community labels) to propose a current best-in-class
  option. A directory listing is not an endorsement: Gaia states the source and
  official/community status of each suggestion, the user approves every
  install, and Gaia continues gracefully on decline — a temple with few gifts
  is still a working temple. If live sources are unreachable, guide mode names
  the categories and moves on rather than guessing. This path is first-class,
  not a fallback: a less-experienced user, or an experienced one on a fresh
  personal account, should be able to build from nothing.
- Output: a terrain report the interview walks through.

### 5.2 The interview
Topic by topic, each answer drafted into the temple's data files for the user
to revise before moving on:

1. **Temple name & purpose** — purpose (work software / personal software /
   entertainment / other) selects the default roster, pipeline, and review
   surface. The chosen name is sanity-checked by a small bundled script (not an
   agent, for consistency) against installed skills, commands, and agent names,
   so `/olympus` or `/asgard` can't shadow something already present.
2. **Pantheon** — Greek, Roman, Norse, Hindu, or custom; per-god overrides.
3. **Divine gifts** — confirm which surveyed (or newly installed) tools the
   gods reach for, and for what. Declined gifts are never touched.
4. **The laws** — standards, security and data-handling policy, canonical
   implementations, what's noise. Each law gets an ID, the user's reasoning,
   and a source date (pr-blueprint's rule format).
5. **Roster** — core seven confirmed/trimmed; reserve bench offered where the
   terrain or purpose calls for them.
6. **Review surface & autonomy** — which decisions pause for the human
   (creative output? risky code? everything?), whether the Orchestrator pauses
   per task or runs a whole plan, WIP limit.
7. **Cost tiers** — model assignment per role (strong where quality compounds:
   Architect, Builder, Reviewer; cheap where mechanical: Law-keeper checks,
   Herald).

### 5.3 The forging
Writes the temple to the **user level** so it works in every repo the account
opens:

```
~/.claude/
├── agents/
│   ├── <temple>-<architect-god>.md      # generated from role template + pantheon + interview
│   ├── <temple>-<builder-god>.md
│   └── ...                              # one per god in the roster
├── skills/
│   └── <temple>/                        # the temple's entry skill: /<temple>
│       ├── SKILL.md                     # Orchestrator playbook (engine)
│       ├── laws.md                      # standards & rules            (user data)
│       ├── canonical.md                 # one way to do each thing     (user data)
│       ├── gifts.md                     # divine gifts registry        (user data)
│       ├── config.json                  # pantheon, roster, review surface, tiers (user data)
│       ├── references/                  # plan / build / review workflows (engine)
│       └── calibrations/                # per-repo profiles            (cached data)
```

- `/<temple>` is the single entry point; the Orchestrator routes to
  sub-workflows (`/<temple> plan`, `/<temple> build`, `/<temple> review`).
- Engine files vs. user data files are clearly separated; `/gaia` upgrades
  replace only engine files.

### 5.4 Repo calibration (first run per repository)
On a temple's first invocation in a repo: detect stack, test runner, CI, lint
config, existing CLAUDE.md/conventions; draft a one-page profile; show the
user; cache it in `calibrations/`. Later runs load the cache; `/<temple>
recalibrate` refreshes it.

### 5.5 Re-interview & upgrade
`/gaia` on an account with existing temples offers: raise a new temple,
re-interview an existing one (amend laws/roster/gifts/pantheon), or upgrade its
engine. User data files are never overwritten by upgrades.

## 6. The law-keeper works in v1

Themis (or Forseti, or Yama…) is not a v2 promise. The v1 temple ships with
working enforcement, modeled on pr-blueprint:

- **`laws.md`** — rules with IDs, reasoning, and source dates, written during
  the interview and amended by re-interview.
- **`canonical.md`** — the one blessed way to do each common thing in this
  account's world (which library, which pattern, which server), so the Builder
  never grows parallel versions of solved problems. Seeded from the interview's
  divine-gifts and standards answers.
- **Enforcement at the gate:** the Law-keeper stage checks every diff against
  `laws.md` and `canonical.md`, runs whatever linters/checks the repo
  calibration found, and reports violations as findings the Builder must
  resolve or the human must waive. Prompt-level enforcement plus existing repo
  checks in v1; *generated* hooks (hard enforcement) remain v2.

## 7. Repository layout (this repo — the Gaia plugin)

```
Gaia/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── README.md
├── SPECIFICATION.md               # this document
├── LICENSE
├── skills/
│   └── gaia/
│       ├── SKILL.md               # the generator: survey → interview → forge
│       ├── references/            # interview guide, forging steps, upgrade logic,
│       │                          #   guide-mode protocol + tool-category list
│       ├── scripts/
│       │   └── check_name.py      # temple-name collision check (script, not agent)
│       └── assets/
│           ├── pantheons.json     # role → deity tables (Greek, Roman, Norse, Hindu)
│           └── template/          # the parameterized temple
│               ├── SKILL.md.tmpl          # Orchestrator playbook
│               ├── laws.md.tmpl
│               ├── canonical.md.tmpl
│               ├── gifts.md.tmpl
│               ├── config.json.tmpl
│               ├── agents/                # one .md.tmpl per ROLE (core + reserve)
│               └── references/            # plan / build / review workflows
└── docs/                          # diagrams, icon
```

Install (once published):

```
claude plugin marketplace add Ian2400/Gaia
claude plugin install gaia@gaia
```

Then, in any account: `/gaia`.

## 8. Build phases

1. **Phase 0 — Rename hygiene:** remote points at `Ian2400/Gaia` (done); local
   folder rename is the user's step after this session.
2. **Phase 1 — The template:** one complete, hand-written temple (core seven
   roles, assembly line, laws/canonical/gifts/config structure, working
   Law-keeper gate) with placeholders where the interview and pantheon inject.
3. **Phase 2 — The generator:** the `/gaia` skill — terrain survey (with guide
   mode and the starter-kit catalog), interview, pantheon selection, forging,
   state/resume.
4. **Phase 3 — Shakedown:** raise a real work temple on this account; run a
   small feature through it end-to-end; tune the template from what breaks.
5. **Phase 4 — Second terrain:** raise a personal/entertainment temple (likely
   under a non-Greek pantheon, to prove the mapping) with the creative review
   surface; add Muse/Reveler templates.
6. **Phase 5 — Plugin polish:** marketplace metadata, upgrade path, docs,
   publish.
7. **v2 (later):** pr-blueprint-style learning loop (feedback → proposed law
   amendments), generated enforcement hooks.

## 9. Settled questions (log)

Resolved during spec review, recorded so they aren't re-litigated:

1. **Deity fits** — table blessed as amended: Roman Reviewer is Veritas;
   Durga, Muninn, Týr, and Loki stand.
2. **Guide-mode suggestions** — requirement kept, as live lookup rather than a
   bundled catalog. Only tool *categories* ship statically; best-in-class
   options are fetched at run time from Anthropic's curated MCP subregistry and
   the official registry API, cross-checked by web search against directories
   with quality signals (Glama, PulseMCP). Degrades gracefully to naming
   categories when offline. (§5.1)
3. **Usage-history survey** — best-effort, never required, no decisions from it
   without human approval. (§5.1)
4. **Temple-name collisions** — checked by a small bundled script at interview
   time, not an agent. (§5.2, §7)
