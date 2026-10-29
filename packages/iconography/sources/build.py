from pathlib import Path
import json,csv,io,copy,re
from lxml import etree as ET
from catalog import inventory,GROUPS
from drawing import render,PALETTE

ROOT=Path(__file__).resolve().parents[1]
rows,mapping,aliases=inventory()
caps=json.loads((ROOT/'docs/sources/capabilities.json').read_text())
assert set(mapping)=={c['id'] for c in caps['capabilities']}
assets=[]
for e in rows:
    pair={}
    for mode in ['couleur','interface']:
        svg=render(e,mode);p=ROOT/'svg'/mode/(e['id']+'.svg');p.write_text(svg+'\n');pair[mode]=svg
    assets.append({**e,'svg':pair})
(ROOT/'manifest.json').write_text(json.dumps({'name':'Zamurek Matière','version':'1.0.0','viewBox':[0,0,96,96],'icons':[{k:v for k,v in a.items() if k!='svg'} for a in assets],'aliases':aliases,'capabilityMap':mapping,'sourceCapabilitiesSha':'3dec6d5217987018a73a8ec5b6b21cb0ceddf2e6'},ensure_ascii=False,indent=2)+'\n')
(ROOT/'design-tokens.json').write_text(json.dumps({'brand':PALETTE,'grid':96,'safeArea':[8,8,88,88],'coloredStroke':2.4,'interfaceStroke':4,'lightDirection':'top-left','gradients':{'green':['#259F7C','#005C45','#003B2D'],'orange':['#FFBE67','#FF8A1E','#DA580C'],'magenta':['#F4599C','#D21868','#940B47']},'contours':{'surface':'#E3F0D9','paper':'#8BB5AA'},'interfaceColor':'currentColor','defaultExportSize':96},indent=2)+'\n')
s=io.StringIO();w=csv.writer(s);w.writerow(['capability_id','description','icon_ids','source'])
for cap in caps['capabilities']:w.writerow([cap['id'],cap['description'],' | '.join(mapping[cap['id']]),'https://github.com/jupi-z/ZAMUREK/blob/main/spec/v1/capabilities.json'])
(ROOT/'docs/Couverture_Capacites.csv').write_text(s.getvalue(),encoding='utf-8-sig')
for mode in ['couleur','interface']:
    root=ET.Element('{http://www.w3.org/2000/svg}svg',nsmap={None:'http://www.w3.org/2000/svg'})
    for a in assets:
        x=ET.fromstring(a['svg'][mode].encode())
        source_ids={node.get('id'):'sp-'+node.get('id') for node in x.xpath('//*[@id]')}
        for node in x.iter():
            if node.get('id'):node.set('id',source_ids[node.get('id')])
            for key,value in list(node.attrib.items()):
                if 'url(#' in value:node.set(key,re.sub(r'url\(#([^)]+)\)',lambda m:'url(#'+source_ids[m.group(1)]+')',value))
        sym=ET.SubElement(root,'{http://www.w3.org/2000/svg}symbol',id='zamurek-'+mode+'-'+a['id'],viewBox='0 0 96 96')
        for child in x:sym.append(copy.deepcopy(child))
    (ROOT/'sprites'/('zamurek-'+mode+'.svg')).write_bytes(ET.tostring(root,encoding='UTF-8',xml_declaration=True,pretty_print=True))
(ROOT/'sources/assets.json').write_text(json.dumps(assets,ensure_ascii=False,separators=(',',':')))
print(len(rows),'semantic icons;',len(rows)*2,'individual SVG files;',len(mapping),'capabilities;',len(aliases),'names/aliases.')
