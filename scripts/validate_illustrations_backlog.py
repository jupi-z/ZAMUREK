#!/usr/bin/env python3
"""Validate ZAMUREK illustration plan, not the existence of illustrations."""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "docs" / "design" / "illustrations"
reg = json.loads((ROOT / "ZAMUREK_Illustrations_Registry_V1.json").read_text(encoding="utf-8"))
scope = json.loads((REPO / "spec" / "v1" / "capabilities.json").read_text(encoding="utf-8"))
expected_cap = {x["id"] for x in scope["capabilities"]}
items = reg["items"]
assert reg["status"] == "PLANNING_NOT_PRODUCED"
assert reg["assetCount"] == 0, "Do not present a backlog as created artwork"
assert reg["itemCount"] == len(items) == 275
assert reg["masterCount"] == 33
assert [x["id"] for x in items] == [f"ZIL-{x:03d}" for x in range(1, 276)]
assert len({x["id"] for x in items}) == 275
assert len({x["base"] for x in items}) == 33
assert set(x["priority"] for x in items) == {"P0","P1","P2","P3"}
assert sum(x["priority"] == "P0" for x in items) == 36
assert all(x["status"] == "À produire" for x in items)
for x in items:
    assert x["name"].strip() and x["scope"].strip()
    assert set(x["capabilities"]) <= expected_cap, x["id"]
for number in (113,190,200,246):
    x = items[number - 1]
    assert x["priority"] == "P3" and x["scope"].startswith("Hors V1"), x["id"]
assert (ROOT / "ZAMUREK_ILLUSTRATIONS_MASTER_BACKLOG_V1.md").is_file()
assert (ROOT / "ZAMUREK_ILLUSTRATIONS_PRODUCTION_GUIDE_V1.md").is_file()
print("ZAMUREK illustrations: 275 needs; 33 master compositions; 36 P0; none produced")
