#!/usr/bin/env python3
"""Offline structural and local-Markdown-link validation; standard library only."""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "docs/INDEX.md", "docs/product/PRD.md",
    "docs/product/V1-FUNCTIONAL-SPEC.md", "docs/architecture/SYSTEM.md",
    "docs/architecture/TENANCY.md", "docs/architecture/ANDROID.md",
    "docs/architecture/SECURITY.md", "docs/architecture/MARKETPLACE.md",
    "docs/quality/ACCEPTANCE.md", "docs/ROADMAP.md",
    "docs/decisions/README.md", "packages/contracts/openapi/xshop-v1.yaml",
]
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
errors: list[str] = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"required file missing: {rel}")
for path in ROOT.rglob("*.md"):
    if any(part in {"node_modules", ".git", ".venv"} for part in path.parts):
        continue
    content = path.read_text(encoding="utf-8")
    for match in LINK.finditer(content):
        value = match.group(1).strip()
        if not value or value.startswith("#"):
            continue
        parsed = urlsplit(value)
        if parsed.scheme or value.startswith("//"):
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        if ROOT not in target.parents and target != ROOT:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repo: {value}")
        elif not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link: {value}")
if errors:
    print("Documentation validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print("Documentation structure and local links: OK")

