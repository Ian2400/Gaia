<!-- ENGINE FILE — replaced by Gaia upgrades. -->

# Stage: Repo calibration (first run per repository, or `recalibrate`)

A temple carries account-wide laws; this profile adapts it to one repository.
Cached at `calibrations/<repo-key>.md` where `<repo-key>` is
`<host>-<owner>-<name>` from the origin remote (or the directory name slug
when no remote exists).

## Survey (read-only, fast — minutes, not hours)

Detect and record:

1. **Stack** — languages, frameworks, package managers (from manifests, not
   guesses).
2. **Test runner** — command, config, where tests live, current pass state.
3. **Checks** — linters/formatters with configs in the repo; the CI pipeline's
   steps if CI config exists. Record the exact commands the Law-keeper will
   run.
4. **Conventions** — existing CLAUDE.md / CONTRIBUTING / style docs (the
   temple honors them; laws.md wins on direct conflict, and conflicts are
   listed in the profile for the human to see); branch naming; versioning
   scheme.
5. **Heraldry deviations** — compare the repo's own commit/PR/changelog
   conventions (CONTRIBUTING, PR templates, recent history) against the
   temple's `heraldry.md`. Record only the **differences**, as explicit
   overrides per codex section; where the repo has no stated convention,
   record nothing and the codex rules. This is the one place repo style is
   inferred — once, at calibration, with the human confirming — so the Herald
   never re-derives it per run.
6. **Shape** — top-level layout, entry points, where specs/docs belong.
7. **Protected ground** — default branch, anything that looks like generated
   code or vendored directories (never hand-edited).

## Confirm

Draft the profile as one page. Show the human; apply their corrections. Cache
it. Later invocations load the cache silently. `recalibrate` re-runs this
survey and shows the diff against the cached profile.

The profile is **cached data** — a Gaia upgrade never touches it, and deleting
it is always safe (the temple just recalibrates).
