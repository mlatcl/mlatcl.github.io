#!/usr/bin/env python3
"""Generate stub pages in _supervisorprojects/ for every person who
supervises at least one entry in _availableprojects/.

Each stub is a tiny Jekyll collection document whose layout
(`supervisor-projects`, defined in the mlatcl/jekyll-theme repo) filters
`site.availableprojects` by `page.person_slug` at build time. This script
does not touch Jekyll's build process -- it only keeps the set of stub
files in sync with the `supervisors:` fields used across
`_availableprojects/*.md`, since GitHub Pages' "legacy" build does not run
custom generator plugins.

Usage:
    python3 scripts/generate_supervisor_pages.py [--dry-run]

Re-run this script whenever a project's `supervisors:` list changes (new
project added, supervisor added/removed, or a person's name changes).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AVAILABLE_PROJECTS_DIR = ROOT / "_availableprojects"
PEOPLE_DIR = ROOT / "_people"
OUTPUT_DIR = ROOT / "_supervisorprojects"


def read_front_matter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    return parts[1]


def extract_list_field(front_matter: str, field: str) -> list[str]:
    """Extract a simple YAML list field, e.g.:

    supervisors:
      - neil-d-lawrence
      - christian-cabrera
    """
    lines = front_matter.splitlines()
    values: list[str] = []
    capturing = False
    for line in lines:
        if re.match(rf"^{re.escape(field)}:\s*$", line):
            capturing = True
            continue
        if capturing:
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m:
                values.append(m.group(1).strip().strip('"').strip("'"))
                continue
            if line.strip() == "" or line.startswith(" "):
                # blank line inside the list block; keep scanning
                if line.strip() == "":
                    continue
            # non-indented, non-list line ends the block
            capturing = False
    return values


def extract_scalar_field(front_matter: str, field: str) -> str | None:
    for line in front_matter.splitlines():
        m = re.match(rf"^{re.escape(field)}:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def person_display_name(slug: str) -> str | None:
    person_path = PEOPLE_DIR / f"{slug}.md"
    if not person_path.exists():
        return None
    fm = read_front_matter(person_path)
    given = extract_scalar_field(fm, "given") or ""
    family = extract_scalar_field(fm, "family") or ""
    name = f"{given} {family}".strip()
    return name or None


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    supervisor_slugs: set[str] = set()
    for project_path in sorted(AVAILABLE_PROJECTS_DIR.glob("*.md")):
        fm = read_front_matter(project_path)
        for slug in extract_list_field(fm, "supervisors"):
            supervisor_slugs.add(slug)

    OUTPUT_DIR.mkdir(exist_ok=True)

    created, updated, skipped = [], [], []
    for slug in sorted(supervisor_slugs):
        name = person_display_name(slug)
        if name is None:
            skipped.append(slug)
            continue

        stub_path = OUTPUT_DIR / f"{slug}.md"
        content = (
            "---\n"
            "layout: supervisor-projects\n"
            f"title: \"{name} \u2014 Projects to Supervise\"\n"
            f"person_slug: {slug}\n"
            "---\n"
        )

        existed = stub_path.exists()
        if not dry_run:
            stub_path.write_text(content, encoding="utf-8")
        (updated if existed else created).append(slug)

    print(f"Created {len(created)} stub page(s): {created}")
    print(f"Updated {len(updated)} stub page(s): {updated}")
    if skipped:
        print(
            f"Skipped {len(skipped)} slug(s) with no matching _people/*.md "
            f"file: {skipped}"
        )
    if dry_run:
        print("(dry run -- no files written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
