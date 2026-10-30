#!/usr/bin/env python3
"""Idempotently repair the generated Zamurek offline studio and its source template.
Prevent a strict-mode ReferenceError caused by a missing 'let' in card headings.
"""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
generator=root/"scripts"/"build_full_library.py"
gallery=root/"ZAMUREK_ILLUSTRATIONS_STUDIO_33_FAMILLES.html"
needle='content.className="content",h2=document.createElement("h2");'
replacement='content.className="content";let h2=document.createElement("h2");'
count=0
for path in (generator,gallery):
    if not path.exists():
        continue
    body=path.read_text(encoding="utf-8")
    if needle in body:
        path.write_text(body.replace(needle,replacement),encoding="utf-8")
        count+=1
    elif replacement not in body:
        raise RuntimeError("Unknown HTML source syntax: "+str(path))
print("Gallery strict-mode patch verified; files updated:",count)
