#!/usr/bin/env python3
"""Validate the native ZAMUREK SVG masters and theme colors (no external packages)."""
from pathlib import Path
import json, re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]/"packages"/"branding"
data=json.loads((ROOT/"manifest.json").read_text(encoding="utf-8"))
assert data["version"]=="2.0.0"
base={"forest":"#005C45","orange":"#FF8A1E","magenta":"#D21868","light":"#FFFFFF","dark":"#111318"}
assert data["color"]==base
comps={"horizontal":(11,16),"vertical":(11,16),"icon":(5,10)}
tones=("light","dark","green","white","black")
expected={f"assets/zamurek-{c}-{t}.svg" for c in comps for t in tones}
assert set(data["logoVariants"])==expected and len(expected)==15
def luminance(hexcode):
 c=[int(hexcode[i:i+2],16)/255 for i in (1,3,5)]
 k=lambda v:v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4
 return sum(x*y for x,y in zip((0.2126,0.7152,0.0722),map(k,c)))
def ratio(a,b):
 l1,l2=sorted((luminance(a),luminance(b)),reverse=True)
 return (l1+.05)/(l2+.05)
for comp,(mono,tri) in comps.items():
 for tone in tones:
  rel=f"assets/zamurek-{comp}-{tone}.svg"
  txt=(ROOT/rel).read_text(encoding="utf-8")
  node=ET.fromstring(txt)
  assert node.tag.endswith("svg") and "viewBox" in node.attrib
  assert not re.search(r"<(?:image|foreignObject|script|text|use)\b|data:image/|href=[\"\']https?://",txt,re.I), rel
  shapes=[n for n in node.iter() if n.tag.endswith("path")]
  stops=[n for n in node.iter() if n.tag.endswith("stop")]
  assert len(shapes)==(tri if tone in ("light","dark") else mono), (rel,len(shapes))
  assert all(s.get("d") for s in shapes), rel
  if tone in ("light","dark"):
   assert len(stops)>=100 and any(s.get("data-tone")=="primary" for s in stops),rel
   bg="#FFFFFF" if tone=="light" else "#111318"
   greens=[s.get("stop-color") for s in stops if s.get("data-tone")=="primary"]
   assert greens and min(ratio(v,bg) for v in greens)>=5.0,rel
  else:
   assert not stops,rel
   col={"green":"#005c45","white":"#ffffff","black":"#000000"}[tone]
   assert all(s.get("fill","").lower()==col for s in shapes),rel
assert (ROOT/"tokens"/"zamurek.tokens.json").is_file()
tokens=json.loads((ROOT/"tokens"/"zamurek.tokens.json").read_text(encoding="utf-8"))
assert tokens["brand"]["forest"]["$value"]=="#005C45"
assert tokens["semantic"]["light"]["background"]["$value"]=="#FFFFFF"
assert tokens["semantic"]["dark"]["background"]["$value"]=="#111318"
print("ZAMUREK SVG V2 verified: 15 native SVGs, geometry layers, controlled greens and themes")
