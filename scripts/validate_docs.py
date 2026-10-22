#!/usr/bin/env python3
"""Offline structural and local-Markdown-link validation; standard library only."""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "SECURITY.md", "PROPRIETARY-NOTICE.md",
    "docs/INDEX.md", "docs/ROADMAP.md", "docs/v1/README.md",
    "docs/v1/PRODUCT-CHARTER.md", "docs/v1/CAPABILITY-MATRIX.md",
    "docs/v1/BUSINESS-WORKFLOWS.md", "docs/v1/DOMAIN-MODEL.md",
    "docs/v1/AGENTIC-KERNEL.md", "docs/v1/TECHNICAL-CONTRACTS.md",
    "docs/v1/SECURITY-THREAT-MODEL.md", "docs/v1/LEGAL-REGULATED-GATES.md",
    "docs/v1/QUALITY-REQUIREMENTS.md", "docs/v1/RELEASE-GATES.md",
    "docs/v1/CODEX-HANDOFF.md", "docs/architecture/TENANCY.md",
    "docs/decisions/0019-proprietary-platform-permissive-oss.md",
    "docs/governance/OPEN-SOURCE-POLICY.md",
    "spec/v1/capabilities.json", "spec/v1/progress-template.json",
    "spec/v1/fixtures.json",
    "packages/contracts/events/event-envelope.schema.json",
    "packages/contracts/agent-tools/tool-definition.schema.json",
    "packages/contracts/openapi/zamurek-v1.yaml",
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

