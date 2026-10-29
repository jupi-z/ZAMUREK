#!/usr/bin/env python3
"""Validate Zamurek Matière V1.3 native SVG assets without external packages."""
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "packages" / "iconography"
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
assert manifest["version"] == "1.3.0", "expected approved V1.3 manifest"
icons = manifest["icons"]
ids = [entry["id"] for entry in icons]
assert len(ids) == len(set(ids)) == 288, "expected 288 unique icons"
id_set = set(ids)
capabilities = manifest["capabilityMap"]
assert len(capabilities) == 43, "V1 must map 43 capabilities"
assert all(names and set(names) <= id_set for names in capabilities.values()), "broken capability icon mapping"
assert all(v in id_set for v in manifest["aliases"].values()), "bad alias target"
assert (ROOT / "design-tokens.json").is_file(), "missing design tokens"

for flavor in ("couleur", "interface"):
    folder = ROOT / "svg" / flavor
    files = sorted(folder.glob("*.svg"))
    assert len(files) == 288, (flavor, len(files))
    assert {p.stem for p in files} == id_set, "missing or extra icons"
    for path in files:
        source = path.read_text(encoding="utf-8")
        node = ET.fromstring(source)
        assert node.tag.endswith("svg")
        assert node.attrib.get("viewBox") == "0 0 96 96", path
        names = [e.attrib["id"] for e in node.iter() if "id" in e.attrib]
        assert len(names) == len(set(names)), f"duplicate SVG IDs in {path}"
        referenced = re.findall(r"url\(\s*['\"]?#([\w:.-]+)", source)
        assert set(referenced) <= set(names), f"unresolved SVG fill/mask in {path}"
        for element in node.iter():
            assert element.tag.split("}")[-1] not in ("script", "image", "foreignObject"), path
            for value in element.attrib.values():
                assert not re.search(r"https?://|data:image/", value, re.I), path
    sprite = ROOT / "sprites" / f"zamurek-{flavor}.svg"
    root = ET.parse(sprite).getroot()
    symbols = [e for e in root.iter() if e.tag.endswith("symbol")]
    assert len(symbols) == 288
    assert {e.get("id") for e in symbols} == {f"zamurek-{flavor}-{name}" for name in ids}
    allids = [e.attrib["id"] for e in root.iter() if "id" in e.attrib]
    assert len(allids) == len(set(allids)), f"duplicate sprite IDs: {sprite}"
    print(f"{flavor}: 288 SVG icons and 288 sprite symbols validated")

assert (ROOT / "ZAMUREK_Atelier_Audit_Icones_V1_3.html").is_file()
assert (ROOT / "Zamurek_Icones_Catalogue.html").is_file()
print("Zamurek Matière V1.3: 576 SVG, two sprites, 43 mapped capabilities, and two HTML inspectors OK")
