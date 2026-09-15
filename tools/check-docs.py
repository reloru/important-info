#!/usr/bin/env python3
"""Structural checks for this documentation repo.

Stdlib only, no dependencies, no network. Run from the repo root:

    python3 tools/check-docs.py

Checks:
  links    every relative Markdown link resolves to a file that exists
  anchors  every "#fragment" in a relative link matches a heading in the target
  orphans  every content page is linked from at least one other page
  fences   code fences are balanced
  tables   table rows have the same column count as their header

Exits non-zero if any check fails, so CI can gate on it.

Intentionally NOT checked:
  - Pseudo-links containing "[" are skipped. docs/templates/*.md deliberately
    ship "[BRACKETED]" placeholders, including inside link targets, e.g.
    "[Cookie Policy]([COOKIE POLICY URL])". Those are features, not defects.
  - External (http/https/mailto/tel) links are not fetched.
"""

import os
import re
import sys

SKIP_DIRS = {".git", "node_modules", "_site", ".site", "dist", "build"}
EXTERNAL = ("http://", "https://", "mailto:", "tel:")
# Pages that legitimately need no inbound link.
ORPHAN_EXEMPT = {"README.md", "CLAUDE.md", "CONTRIBUTING.md"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def markdown_files(root="."):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                out.append(os.path.normpath(os.path.join(dirpath, name)))
    return sorted(out)


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def slugify(text):
    """Approximate GitHub's heading-anchor algorithm."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    text = text.lower()
    # Non-breaking hyphen behaves like a hyphen; en/em dashes are dropped.
    text = text.replace("‑", "-").replace("–", "").replace("—", "")
    text = "".join(c for c in text if c.isalnum() or c in " -_")
    return re.sub(r"-+", "-", text.strip().replace(" ", "-"))


def headings(path):
    found = set()
    in_fence = False
    for line in read(path).split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            found.add(slugify(match.group(2)))
    return found


def relative_links(path):
    """Yield (target, fragment) for each in-repo link, skipping placeholders."""
    base = os.path.dirname(path)
    for match in LINK_RE.finditer(read(path)):
        target = match.group(1).strip()
        if target.startswith(EXTERNAL) or "[" in target:
            continue
        if target.startswith("#"):
            yield path, target[1:]
            continue
        file_part, _, fragment = target.partition("#")
        if not file_part:
            continue
        yield os.path.normpath(os.path.join(base, file_part)), fragment


def main():
    files = markdown_files()
    known = set(files)
    failures = []
    link_count = 0
    linked_to = set()

    heading_cache = {}

    for path in files:
        for target, fragment in relative_links(path):
            link_count += 1
            linked_to.add(target)
            if target not in known and not os.path.exists(target):
                failures.append(f"{path}: broken link -> {target}")
                continue
            if fragment:
                if target not in heading_cache:
                    heading_cache[target] = headings(target)
                if fragment not in heading_cache[target]:
                    failures.append(f"{path}: no such anchor -> {target}#{fragment}")

    orphans = [p for p in files
               if p not in linked_to and os.path.basename(p) not in ORPHAN_EXEMPT]
    failures.extend(f"{p}: orphan (no page links to it)" for p in orphans)

    for path in files:
        lines = read(path).split("\n")
        if sum(1 for line in lines if line.lstrip().startswith("```")) % 2:
            failures.append(f"{path}: unbalanced code fence")

        in_fence = False
        for i, line in enumerate(lines):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if not (re.match(r"^\s*\|?[\s:|-]*\|[\s:|-]*$", line)
                    and "-" in line and "|" in line):
                continue
            header = lines[i - 1] if i else ""
            if "|" not in header:
                continue
            width = header.count("|")
            if line.count("|") != width:
                failures.append(f"{path}:{i + 1}: table separator width mismatch")
            j = i + 1
            while j < len(lines) and lines[j].strip() and "|" in lines[j]:
                if lines[j].count("|") != width:
                    failures.append(f"{path}:{j + 1}: table row width mismatch")
                j += 1

    print(f"{len(files)} Markdown files, {link_count} in-repo links checked")
    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
