# Reusable corrective implementation. Pass a baseline original V1.1 SVG to modify(path).
# Do not reprocess files already marked with zm-clip IDs: the operation is not idempotent.
from pathlib import Path
from lxml import etree as ET
import copy, re, io
import cairosvg
from PIL import Image, ImageDraw, ImageFont

BASE=Path('/mnt/data/Zamurek_Icones_Full_SVG_Optimized_V2/Zamurek_Icones')
NS='http://www.w3.org/2000/svg'
def q(tag):return '{'+NS+'}'+tag

# The closed geometries have an occluding interior: avoid drawing hidden strokes of shapes behind them.
def opaque(elem):
    tag=ET.QName(elem).localname
    if tag in {'rect','circle','ellipse','polygon'} and elem.get('stroke-opacity') is not None:return True
    if tag=='path' and elem.get('stroke-opacity') is not None and 'Z' in (elem.get('d') or '').upper():return True
    return False

def hole_for(el, clearance=1.8):
    """A vector cutout path: exact for most geometry; closed Beziers preserve their silhouette."""
    typ=ET.QName(el).localname
    if typ=='circle':
        x=float(el.get('cx'));y=float(el.get('cy'));r=float(el.get('r'))+clearance
        return f'M{x+r:.2f} {y:.2f} A{r:.2f} {r:.2f} 0 1 0 {x-r:.2f} {y:.2f} A{r:.2f} {r:.2f} 0 1 0 {x+r:.2f} {y:.2f}Z'
    if typ=='ellipse':
        x=float(el.get('cx'));y=float(el.get('cy'));rx=float(el.get('rx'))+clearance;ry=float(el.get('ry'))+clearance
        return f'M{x+rx:.2f} {y:.2f} A{rx:.2f} {ry:.2f} 0 1 0 {x-rx:.2f} {y:.2f} A{rx:.2f} {ry:.2f} 0 1 0 {x+rx:.2f} {y:.2f}Z'
    if typ=='rect':
        x=float(el.get('x'))-clearance;y=float(el.get('y'))-clearance
        w=float(el.get('width'))+clearance*2;h=float(el.get('height'))+clearance*2
        return f'M{x:.2f} {y:.2f}h{w:.2f}v{h:.2f}h{-w:.2f}Z'
    if typ=='path':return el.get('d','')
    return ''

def add_clip(defs, uid, cut):
    clip=ET.SubElement(defs,q('clipPath'),id=uid,clipPathUnits='userSpaceOnUse')
    p=ET.SubElement(clip,q('path'))
    # Even-odd inverse; all clip silhouettes remain geometry, independent of background color.
    p.set('d','M0 0H96V96H0Z '+cut)
    p.set('clip-rule','evenodd');p.set('fill-rule','evenodd')


def group_optimize(root,uid):
    drawing=root.xpath('//*[@data-layer="drawing"]')[0]
    base=drawing[0] if len(drawing)>0 and ET.QName(drawing[0]).localname=='g' and drawing[0].get('mask') else drawing
    children=list(base)
    defs=root.find(q('defs'))
    if defs is None:defs=ET.Element(q('defs'));root.insert(2,defs)
    changes=0
    # Correct V1.1's unsupported luminance SVG mask by a true transparent vector cut-out.
    if base is not drawing and base.get('mask'):
        base.attrib.pop('mask',None)
        stem=uid+'-badge-hole'
        add_clip(defs,stem,hole_for(ET.Element(q('circle'),cx='76',cy='76',r='16'),0))
        base.set('clip-path','url(#'+stem+')')
        changes+=1
    # For every rear geometry, clip portions hidden by each later foreground silhouette.
    for index,node in enumerate(children):
        if node.get('data-occluded')=='true':continue
        later=[el for el in children[index+1:] if opaque(el)]
        if not later:continue
        loc=base.index(node);base.remove(node)
        outer=None;cursor=None
        for mindex,layer in enumerate(later):
            cut=hole_for(layer)
            if not cut: continue
            id_=uid+f'-clip-{index}-{mindex}'
            add_clip(defs,id_,cut)
            wrapper=ET.Element(q('g'))
            wrapper.set('clip-path','url(#'+id_+')')
            if outer is None:outer=wrapper
            else:cursor.append(wrapper)
            cursor=wrapper
        if outer is not None:
            cursor.append(node);base.insert(loc,outer);changes+=1
        else:base.insert(loc,node)
    return changes

# Rebuild the wrench using one continuous outer contour and a small handle eyelet.
WRENCH=[
  ('path',{'d':'M59 11C48 14 42 24 46 37L16 68Q10 75 17 82Q24 89 32 82L62 52C75 56 86 44 83 30L70 42L57 30L70 17Q65 13 59 11Z'}),
  ('circle',{'cx':'24','cy':'75','r':'3.5'})
]
SOFA=[
  ('path', {'d':'M24 53V35Q24 17 41 17H57Q74 17 74 35V53'}),
  ('path', {'d':'M22 44Q14 44 14 52V72Q14 80 23 80H74Q83 80 83 72V52Q83 44 75 44Q68 44 68 52V62H29V52Q29 44 22 44Z'}),
  ('path', {'d':'M23 80V86M74 80V86'})
]
KEY=[
  ('circle',{'cx':'27','cy':'40','r':'18'}),
  ('circle',{'cx':'27','cy':'40','r':'6.5'}),
  ('path',{'d':'M45 40H83M65 40V52M77 40V48'})
]

def replace_geometries(root,recipe):
    drawing=root.xpath('//*[@data-layer="drawing"]')[0]
    base=drawing[0] if len(drawing)>0 and ET.QName(drawing[0]).localname=='g' and drawing[0].get('mask') else drawing
    for child in list(base):base.remove(child)
    data=WRENCH if recipe=='wrench' else (SOFA if recipe=='sofa' else KEY)
    for typ,atts in data:
        el=ET.SubElement(base,q(typ),**atts)
        el.attrib.update({'fill':'none','stroke':'currentColor','stroke-width':'4.5' if recipe in ('wrench','sofa') else '4.3','stroke-linecap':'round','stroke-linejoin':'round','stroke-opacity':'1'})
    # original optical translations were measured against the old, incorrect drawing
    drawing.attrib.pop('transform',None)


def modify(fp):
    root=ET.parse(str(fp)).getroot();stem=fp.stem
    rec='wrench' if stem in {'services','reparation-attente','reparation-terminee','outils-ia'} else ('key' if stem in {'connexion','changer-mot-de-passe'} else ('sofa' if stem in {'meubles','fauteuil'} else None))
    if rec:replace_geometries(root,rec)
    n=group_optimize(root, 'zm-'+stem)
    return ET.tostring(root,encoding='utf-8',xml_declaration=False),n
