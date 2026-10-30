#!/usr/bin/env python3
"""Validate native vector pilot assets (separate from the 275-item planning backlog)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "packages" / "illustrations"
SVG = "{http://www.w3.org/2000/svg}"
IDS = ("ZIL-001", "ZIL-044", "ZIL-117")
FORBIDDEN = {"image", "script", "foreignObject", "iframe", "animateMotion"}
REF = re.compile(r"url\(#([^\)]+)\)")
SVG_ID = re.compile(r"^[A-Za-z_][\w.:-]*$")


def check_one(path: Path, code: str, motion: bool, theme: str) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path}: missing file"]
    source = path.read_text(encoding="utf-8")
    if "<!DOCTYPE" in source.upper() or "<!ENTITY" in source.upper():
        errors.append("DTD/entities are not allowed")
    try:
        tree = ET.fromstring(source)
    except ET.ParseError as exc:
        return [f"{path}: invalid XML: {exc}"]
    if tree.tag != SVG + "svg":
        errors.append("not an SVG root")
    if tree.attrib.get("viewBox") != "0 0 800 600":
        errors.append("incorrect viewBox")
    if tree.attrib.get("data-zamurek-illustration") != code:
        errors.append("incorrect illustration ID")
    if tree.attrib.get("data-theme") != theme:
        errors.append("incorrect theme")
    if tree.attrib.get("data-motion") != ("on" if motion else "off"):
        errors.append("incorrect motion state")
    if not tree.find(SVG + "title") is not None or tree.find(SVG + "desc") is None:
        errors.append("accessible title or description missing")
    ids: set[str] = set()
    count_paths = 0
    all_refs: list[str] = []
    upstream: set[str] = set()
    for node in tree.iter():
        name = node.tag.rsplit("}", 1)[-1]
        if name in FORBIDDEN:
            errors.append(f"forbidden element {name}")
        if name == "path":
            count_paths += 1
        identifier = node.attrib.get("id")
        if identifier:
            if identifier in ids:
                errors.append(f"duplicate ID {identifier}")
            ids.add(identifier)
            if not SVG_ID.fullmatch(identifier):
                errors.append(f"invalid XML identifier {identifier}")
        if node.attrib.get("data-upstream"):
            upstream.add(node.attrib["data-upstream"])
        for key, value in node.attrib.items():
            all_refs += REF.findall(value)
            if key.rsplit("}", 1)[-1] == "href":
                if not value.startswith("#"):
                    errors.append(f"external reference {value}")
                else:
                    all_refs.append(value[1:])
            if re.search(r"(?:javascript:|data:|https?://)", value, re.I):
                errors.append(f"nonlocal source {key}={value[:35]}")
    for target in all_refs:
        if target not in ids:
            errors.append(f"unresolved fragment #{target}")
    if count_paths < 3:
        errors.append("illustration insufficiently vectorized")
    if motion and "prefers-reduced-motion" not in source:
        errors.append("missing reduced-motion fallback")
    if not motion and "@keyframes" in source:
        errors.append("static file contains CSS keyframes")
    if "infinite" in source:
        errors.append("unexpected infinite animation")
    if code == "ZIL-044" and upstream != {"Humaaans", "IRA Design"}:
        errors.append("upstream Humaaans / IRA Design not present")
    if code == "ZIL-117" and "Humaaans" not in upstream:
        errors.append("Humaaans character not present")
    return [f"{path}: {e}" for e in errors]


def main() -> int:
    manifest = json.loads((ROOT / "registry" / "pilot-manifest.json").read_text())
    if manifest.get("status") != "REVUE_VISUELLE_REQUISE":
        print("Unexpected pilot status: only visual review is claimed.")
        return 1
    findings: list[str] = []
    for code in IDS:
        for motion, part in ((False, "static"), (True, "motion")):
            for theme in ("light", "dark"):
                p = ROOT / "assets" / part / f"{code.lower()}-{theme}.svg"
                findings.extend(check_one(p, code, motion, theme))
    for filename in ("README.md", "THIRD_PARTY_NOTICES.md", "THIRD_PARTY_LICENSES.md", "preview.html"):
        if not (ROOT / filename).is_file():
            findings.append(f"Missing required documentation: {filename}")
    if findings:
        print("\n".join(findings))
        return 1
    print("PASS: 12 native SVG pilot variants; IDs, licensing documents, metadata and reduced motion checks.")
    print("NOTE: this validation does not replace visual, browser, performance or accessibility review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
