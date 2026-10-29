"""Portable structural validation; no network or browser required."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'manifest.json').read_text());icons=manifest['icons'];ids={e['id'] for e in icons};assert len(ids)==len(icons)==288
files=[]
for mode in ['couleur','interface']:
    for e in icons:
        p=ROOT/'svg'/mode/(e['id']+'.svg');data=p.read_bytes();s=data.decode();root=ET.fromstring(s)
        all_ids=[n.attrib['id'] for n in root.iter() if 'id' in n.attrib];assert len(all_ids)==len(set(all_ids)),p
        for ref in re.findall(r'url\(#([^)]+)\)',s):assert ref in all_ids,(p,ref)
        assert root.get('viewBox')=='0 0 96 96',p
        assert not re.search(r'data:|base64|NaN|Infinity|https?://(?!www.w3.org/2000/svg)',s),p
        tags={n.tag.split('}')[-1] for n in root.iter()};assert not tags&{'image','foreignObject','text','script','style'},p
        if mode=='interface':assert 'linearGradient' not in tags and 'filter' not in tags,p
        files.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
for mode in ['couleur','interface']:
    p=ROOT/'sprites'/('zamurek-'+mode+'.svg');root=ET.fromstring(p.read_bytes());all_ids=[n.attrib['id'] for n in root.iter() if 'id' in n.attrib];assert len(all_ids)==len(set(all_ids)),p
    assert len([n for n in root if n.tag.endswith('symbol')])==288
    for ref in re.findall(r'url\(#([^)]+)\)',p.read_text()):assert ref in all_ids,(p,ref)
cap_source=json.loads((ROOT/'docs/sources/capabilities.json').read_text());caps={c['id'] for c in cap_source['capabilities']};assert len(caps)==43 and set(manifest['capabilityMap'])==caps
for cap,mapped in manifest['capabilityMap'].items():assert mapped and set(mapped)<=ids,cap
for alias,target in manifest['aliases'].items():assert target in ids,alias
html=(ROOT/'Zamurek_Icones_Catalogue.html').read_text();assets=json.loads(re.search(r'<script id="assets" type="application/json">(.*?)</script>',html,re.S).group(1));assert len(assets)==288
for a in assets:
    for mode in ['couleur','interface']:assert a['svg'][mode]+'\n'==(ROOT/'svg'/mode/(a['id']+'.svg')).read_text()
assert not re.search(r'<(?:img|image|foreignObject|canvas)\b|<script[^>]+src=|<link[^>]+href=',html,re.I)
assert '__ASSETS__' not in html and '__GROUPS__' not in html
report={'canonicalIcons':288,'semanticNamesWithAliases':len(manifest['aliases']),'individualSvgFiles':576,'spriteFiles':2,'categories':len({a['category'] for a in icons}),'capabilitiesCovered':43,'capabilitiesTotal':43,'missingCapabilities':[],'svgXmlValid':True,'uniqueIds':True,'internalReferencesResolved':True,'htmlSvgMatchesFiles':True,'bitmapElements':0,'fontDependencies':0,'externalAssets':0,'htmlSha256':hashlib.sha256((ROOT/'Zamurek_Icones_Catalogue.html').read_bytes()).hexdigest(),'files':files}
(ROOT/'docs/Verification_Structure.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(files),'individual SVGs;',len(caps),'capabilities; sprites and catalog consistent; no bitmap or font dependency.')
