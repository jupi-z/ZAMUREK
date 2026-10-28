#!/usr/bin/env python3
"""Validate ZAMUREK brand assets without external dependencies."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parents[1] / "packages" / "branding"
manifest = json.loads((BASE / "manifest.json").read_text(encoding="utf-8"))
tokens = json.loads((BASE / "tokens" / "zamurek.tokens.json").read_text(encoding="utf-8"))
expected = {f"assets/zamurek-{comp}-{tone}.svg"
            for comp in ("horizontal", "vertical", "icon")
            for tone in ("light", "dark", "green", "white", "black")}
assert len(expected) == 15
assert set(manifest["logoVariants"]) == expected, "manifest != expected variants"
for asset in sorted(expected):
    root = ET.parse(BASE / asset).getroot()
    assert root.tag.endswith("svg"), asset
    assert "viewBox" in root.attrib and "aria-label" in root.attrib, asset
    paths = [el for el in root.iter() if el.tag.endswith("path")]
    assert len(paths) == 3, (asset, len(paths))
    assert all(el.get("d", "").startswith("M") for el in paths), asset
assert manifest["color"] == {
    "forest": "#005C45", "orange": "#FF8A1E", "magenta": "#D21868",
    "light": "#FFFFFF", "dark": "#111318"}, "palette drift"
assert tokens["brand"]["forest"]["$value"] == "#005C45"
assert tokens["semantic"]["light"]["background"]["$value"] == "#FFFFFF"
assert tokens["semantic"]["dark"]["background"]["$value"] == "#111318"
print("ZAMUREK branding validated: 15 SVG variants, tokens, palette and both backgrounds")
