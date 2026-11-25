#!/usr/bin/env python3
"""Temple-name collision check (Gaia, spec SS5.2 / settled question 4).

Usage: python check_name.py <temple-slug> [--claude-dir PATH]

Checks a proposed temple slug against what already exists at the user level:
skills, agents (a temple's agents are named <temple>-<god>), and Gaia's own
temple registry. Prints findings and exits 0 (clear), 1 (collision), or
2 (invalid slug). A script rather than an agent, for consistency.
"""

import argparse
import json
import re
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]{1,39}$")

# Names that collide with Gaia itself or common built-in commands.
RESERVED = {
    "gaia", "help", "clear", "config", "init", "review", "plan", "build",
    "agents", "skills", "settings", "mcp", "memory", "plugin", "plugins",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--claude-dir", default=str(Path.home() / ".claude"))
    args = ap.parse_args()

    slug = args.slug
    claude = Path(args.claude_dir)
    problems = []

    if not SLUG_RE.match(slug):
        print(f"INVALID: '{slug}' — use 2-40 chars: lowercase letter first, "
              "then lowercase letters, digits, hyphens.")
        return 2
    if slug in RESERVED:
        print(f"COLLISION: '{slug}' is reserved (Gaia or a common command).")
        return 1

    skill_dir = claude / "skills" / slug
    if skill_dir.exists():
        problems.append(f"skill directory exists: {skill_dir}")

    agents = claude / "agents"
    if agents.is_dir():
        hits = sorted(p.name for p in agents.glob(f"{slug}-*.md"))
        if hits:
            problems.append(
                f"agent files already use the '{slug}-' prefix: {', '.join(hits)}")
        if (agents / f"{slug}.md").exists():
            problems.append(f"an agent is already named '{slug}'")

    registry = claude / "gaia" / "temples.json"
    if registry.is_file():
        try:
            temples = json.loads(registry.read_text(encoding="utf-8"))
            names = {t.get("name") for t in temples if isinstance(t, dict)}
            if slug in names:
                problems.append("a temple of this name is in Gaia's registry "
                                "(editing it is /gaia's editor flow)")
        except (json.JSONDecodeError, OSError) as e:
            print(f"NOTE: could not read registry ({e}); checked files only.")

    # Prefix ambiguity: an existing temple whose name is a prefix of this one
    # (or vice versa) makes agent files visually confusable, not broken. Warn.
    skills_root = claude / "skills"
    if skills_root.is_dir():
        for p in skills_root.iterdir():
            n = p.name
            if n != slug and (n.startswith(slug + "-") or slug.startswith(n + "-")):
                print(f"WARN: existing skill '{n}' shares a prefix with "
                      f"'{slug}' — allowed, but easy to confuse.")

    if problems:
        print("COLLISION:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(f"CLEAR: '{slug}' is available.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
