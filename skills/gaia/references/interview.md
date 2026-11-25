# Phase B: The interview

Nine steps, in order, one topic at a time. After each step: draft the answer
into the exact text that will land in the temple's files, show the draft, let
the user revise, then save state. The user can pause after any step and resume
later. Steps that don't apply are skipped aloud ("no Muse rostered, so no
poetics step").

Drafting rules, all steps:

- Rules and entries get IDs, the user's reasoning in their own words, and a
  source date — the entry formats are in the template's `laws.md.tmpl`,
  `canonical.md.tmpl`, `gifts.md.tmpl`, `heraldry.md.tmpl`, `poetics.md.tmpl`.
- Ask one question at a time; prefer concrete multiple-choice with an open
  option over essay prompts; use the terrain report to make questions
  specific ("you have both psycopg2 and SQLAlchemy in play — which is
  canonical?"), never generic.
- Never invent an answer the user didn't give. An unanswered topic is left
  empty with a dated "not yet ruled" marker, not filled with best practice.

## Step 1 — Name & purpose

Purpose first, in the user's own words (free text, not a taxonomy — there are
no temple "types"). Then the name: propose 2-3 short slugs fitting the purpose
(the pantheon's mount name is a natural candidate). Run
`scripts/check_name.py <name>` on the chosen name; on collision, say what it
collides with and propose variants. The script sees only `~/.claude` — also
check the name against the terrain report's plugin and skill inventory
yourself, since plugin-provided skills live outside it. The slug must be filesystem- and
slash-command-safe: lowercase, hyphens, no spaces.

## Step 2 — Pantheon

Offer Greek (default), Roman, Norse, Hindu from `assets/pantheons.json` —
show each pantheon's full role → deity table, not just its name. A custom
pantheon is a user-supplied table over the same fourteen roles (validate
completeness for the roles being rostered; slugs must be unique within the
temple). Individual deity overrides are welcome at any point ("Greek, but call
the Reveler Pan"). Roles are fixed in v1; names are the user's.

## Step 3 — Divine gifts

Walk the terrain report's candidates, highest confidence first. Per gift:
confirm what it grants, which roles wield it, or decline it (declined →
Untouched list, binding on all gods). Guide-mode installs that happened in
Phase A are confirmed here like any other gift. Draft `gifts.md` entries live.

## Step 4 — The laws

The temple's constitution, four sections (standards / security & data /
conventions / noise), drafted as LAW entries. Seed questions from the terrain
("Purdue data classifications apply?" only if the terrain suggests it — never
assume an org). Explicitly ask for the **noise list**: "what do automated
reviewers flag that you never want to hear again?" Also surface canon
candidates noticed in the terrain (duplicate tools) for step 5. Few laws is a
fine answer; empty sections are allowed.

## Step 5 — Canon & roster

**Canon:** "one blessed way to do each thing" — draft CANON entries from the
gifts and laws discussion (which library, which pattern, which server).
**Roster:** core seven are proposed staffed; walk the reserve bench with
triggers from the terrain and purpose (databases in play → Deep-keeper;
creative work in scope → Muse; interactive experiences → Reveler; long-lived
project → Chronicler). The user may trim core roles too (a solo hobbyist may
drop the Herald); warn once about what a dropped role's stage loses, then
respect the choice.

## Step 6 — Heraldry

Commit format, PR sections, changelog policy, attribution/sign-offs — the
`heraldry.md` sections in order. Where the user has no opinion, offer one
plain default per section (conventional commits; Summary/Changes/Verification/
Risk & revert) and mark it as a default they can amend later.

## Step 7 — Review surface & autonomy

Which decision classes pause for the human: plan approval (default on),
per-task pause vs. whole-plan runs, creative output, risky code. Plus the WIP
limit (default 3). `merge` is always-human and not offered as a choice.
Frame it as "where do mistakes hurt most in this temple?" — the gates go
there.

## Step 8 — Cost tiers

Model per role, with a sensible proposal: strong where quality compounds
(Architect, Builder, Reviewer, Victor's declarations), mid where mechanical-
but-judged (Test hunter, Deep-keeper, Healer), economical where routine
(Law-keeper checks, Herald, Chronicler, Steward). Use the model names valid in
agent frontmatter at forge time; let the user adjust per role.

## Step 9 — Poetics (only when the Muse is rostered)

Voice & tone, visual direction, themes & boundaries — drafted into
`poetics.md`. The approved/rejected ledgers start empty; explain that gate
rulings will fill them. If the user can't define the creative direction yet,
that's fine: forge with "not yet ruled" markers and point at the temple
editor for when the work arrives.

## Closing

Show the complete picture: name, pantheon, roster with models, gate settings,
and every drafted file's contents. One last chance to amend anything. Then
Phase C (`forge.md`).
