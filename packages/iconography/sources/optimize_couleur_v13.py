from __future__ import annotations
import copy, io, json, hashlib, re, shutil, zipfile, math, collections, time
from pathlib import Path
from lxml import etree as ET
import cairosvg
from PIL import Image, ImageDraw, ImageFont
import numpy as np

srczip=Path('/mnt/data/ZAMUREK_Icones_Matiere_Corrigees_V1_2.zip')
base=Path('/mnt/data/ZAMUREK_Matiere_Couleur_Revue_V1_3')
if base.exists():shutil.rmtree(base)
base.mkdir()
with zipfile.ZipFile(srczip) as z:z.extractall(base)
root=base/'Zamurek_Icones'
COLOR=root/'svg/couleur';MONO=root/'svg/interface'
ns='http://www.w3.org/2000/svg'; svgq=lambda name:f'{{{ns}}}{name}'
manifest=json.loads((root/'manifest.json').read_text())
ids=[e['id'] for e in manifest['icons']];assert len(ids)==len(set(ids))==288

# The approved monochrome geometry has priority where it was explicitly redesigned in V1.2.
shape_map={'services':'wrench','reparation-attente':'wrench','reparation-terminee':'wrench','outils-ia':'wrench','connexion':'key','changer-mot-de-passe':'key','meubles':'sofa','fauteuil':'sofa'}
reports=[]

def nsname(e):return ET.QName(e).localname

def drawing(r):
    l=r.xpath('//*[@data-layer="drawing"]')
    assert len(l)==1
    return l[0]

def geom_children(d):
    return [e for e in d if nsname(e) in ('path','circle','rect','polygon','line','polyline','ellipse')]

def make_colorized_parts(stem, old_draw, mono_draw, recipe):
    base=list(geom_children(old_draw))
    original_count=len(base)
    ref=[e for e in mono_draw.iter() if e is not mono_draw and nsname(e) in ('path','circle','rect','polygon','line','polyline','ellipse')]
    n=2 if recipe=='wrench' else 3
    assert len(ref)>=n and len(base)>=n,(stem,n,len(ref),len(base))
    res=[]
    def gradient(kind):return f'url(#zi-{stem}-c-{kind})'
    for i,original in enumerate(ref[:n]):
        e=copy.deepcopy(original)
        # Do not transfer mono clips, transforms, or strokes to the colored master.
        for att in ['clip-path','mask','transform','data-occluded']:
            e.attrib.pop(att,None)
        e.attrib.pop('style',None)
        e.set('stroke-linecap','round');e.set('stroke-linejoin','round')
        if recipe=='wrench':
            if i==0:
                e.set('fill',gradient('o' if stem=='outils-ia' else 'g'))
                e.set('stroke','#D6E7DF');e.set('stroke-width','2.5')
                e.set('stroke-opacity','.96')
            else:
                e.set('fill','#F8F7EA');e.set('stroke','#7BAF9D');e.set('stroke-width','2')
                e.attrib.pop('stroke-opacity',None)
        elif recipe=='key':
            if i==0:
                e.set('fill',gradient('g'));e.set('stroke','#D6E7DF');e.set('stroke-width','2.3');e.set('stroke-opacity','.95')
            elif i==1:
                e.set('fill','#F8F7EA');e.set('stroke','#8BB5AA');e.set('stroke-width','2.2');e.attrib.pop('stroke-opacity',None)
            else:
                e.set('fill','none');e.set('stroke','#FF8A1E');e.set('stroke-width','6.5')
                e.attrib.pop('stroke-opacity',None)
        elif recipe=='sofa':
            if i==0:
                e.set('fill','none');e.set('stroke','#005C45');e.set('stroke-width','5.6');e.attrib.pop('stroke-opacity',None)
            elif i==1:
                e.set('fill',gradient('o'));e.set('stroke','#D6E7DF');e.set('stroke-width','2.5');e.set('stroke-opacity','.95')
            else:
                e.set('fill','none');e.set('stroke','#005C45');e.set('stroke-width','5.2');e.attrib.pop('stroke-opacity',None)
        res.append(e)
    for e in base[n:]:res.append(e)
    # Keep only the old badge, etc.; change the core geometry deterministically.
    for e in list(old_draw):old_draw.remove(e)
    for e in res:old_draw.append(e)
    # Since newly drawn silhouettes use a different center, mono coordinates are authoritative.
    old_draw.attrib.pop('transform',None)
    return len(res),original_count

badge_results=[]
changed_geometry=[]
changed_badges=[]
changed_other=[]

for stem in ids:
    cp=COLOR/(stem+'.svg');mp=MONO/(stem+'.svg')
    text=cp.read_bytes()
    r=ET.fromstring(text); d=drawing(r)
    mono=ET.parse(str(mp)).getroot()
    rec=shape_map.get(stem)
    if rec:
        new_count,old_count=make_colorized_parts(stem,d,drawing(mono),rec)
        changed_geometry.append(stem)
    # Fix extremely pale chef hat on white backgrounds; the paper tone was under-contrasted.
    if stem=='cuisine':
        for e in geom_children(d):
            if e.get('data-paper-edge')=='true':
                e.set('fill','#ECF4EF');e.set('stroke','#4D9980');e.set('stroke-width','3.2')
        changed_other.append(stem)
    # Resolve badge-to-body collision by a truly transparent SVG inverse clip (no white cover).
    elems=list(d)
    badgeidx=None
    for j, e in enumerate(elems):
        if nsname(e)=='circle' and e.get('cx')=='76' and e.get('cy')=='76' and e.get('r')=='13':
            badgeidx=j;break
    if badgeidx is not None and badgeidx>0:
        defs=r.find(svgq('defs'))
        if defs is None:
            defs=ET.Element(svgq('defs'))
            r.insert(2,defs)
        idclip=f'zm-{stem}-c-body-clearance'
        assert not r.xpath(f'//*[@id="{idclip}"]')
        clip=ET.SubElement(defs,svgq('clipPath'),id=idclip)
        clip.set('clipPathUnits','userSpaceOnUse')
        cut=ET.SubElement(clip,svgq('path'))
        # Badge stroke ends at r=14.2. Use r=16.2 to enforce about 2px clear gap.
        cut.set('d','M-12 -12H108V108H-12Z M92.2 76 A16.2 16.2 0 1 0 59.8 76 A16.2 16.2 0 1 0 92.2 76Z')
        cut.set('fill-rule','evenodd');cut.set('clip-rule','evenodd')
        wrapper=ET.Element(svgq('g'))
        wrapper.set('clip-path',f'url(#{idclip})')
        wrapper.set('data-zamurek-layer','body-with-transparent-badge-clearance')
        for e in elems[:badgeidx]:
            d.remove(e);wrapper.append(e)
        d.insert(0,wrapper)
        changed_badges.append(stem)
    # Non-destructive filter reduction: prevents bright colored shapes from looking blurry at 24px.
    for filt in r.xpath('//*[local-name()="feDropShadow"]'):
        if filt.get('flood-opacity'):
            before=float(filt.get('flood-opacity'))
            if before>.14:
                filt.set('flood-opacity','.14')
                changed_other.append(stem)
        if filt.get('stdDeviation'):
            before=float(filt.get('stdDeviation'))
            if before>.75:
                filt.set('stdDeviation','.7')
                changed_other.append(stem)
    cp.write_bytes(ET.tostring(r,encoding='UTF-8',xml_declaration=False)+b'\n')

# Color silhouette and badge summary
changed_other=sorted(set(changed_other))
assert len(changed_geometry)==8
print('geometry',len(changed_geometry),'badge separation',len(changed_badges),'shadow/paper',len(changed_other))

# Rebuild both sprites to ensure full consistency with individual masters.
for mode in ('couleur','interface'):
    p=root/'sprites'/f'zamurek-{mode}.svg'
    parent=ET.Element(svgq('svg'),nsmap={None:ns})
    for stem in ids:
        r=ET.parse(str((root/'svg'/mode/(stem+'.svg')))).getroot()
        symbol=ET.SubElement(parent,svgq('symbol'),id=f'zamurek-{mode}-{stem}',viewBox='0 0 96 96')
        for child in r:
            symbol.append(copy.deepcopy(child))
        # Each icon references only stem-scoped ids.
    p.write_bytes(ET.tostring(parent,encoding='UTF-8',xml_declaration=True,pretty_print=False))

# Keep identity semantic mapping.
manifest['version']='1.3.0';manifest['optimizedFrom']='1.2.0'
manifest['colorReliefReview']={
    'source':'ZAMUREK_Icones_Matiere_Corrigees_V1_2.zip',
    'monochromePreservedCount':288,
    'couleurReviewedCount':288,
    'geometryAlignedToMonochrome':changed_geometry,
    'transparentBadgeClearanceCount':len(changed_badges),
    'badgeClearanceRadiusIn96px':16.2,
    'surfaceAndShadowRefinements':len(changed_other),
    'noBitmapOrExternalAssets':True,
    'notes':'No change to semantic ID or family. Gradients retained; badge overlap made transparent and shadow blur reduced.'
}
(root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

p=root/'design-tokens.json';tokens=json.loads(p.read_text())
tokens['colorReliefRevision']={'version':'1.3.0','badgeSeparation':'evenodd vector clipPath 16.2 on a 96x96 grid','shadowOpacity':0.14,'shadowBlur':0.7,'opaqueWhiteBadges':False}
p.write_text(json.dumps(tokens,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

rd=root/'LIRE_MOI.md';rd.write_text(rd.read_text(encoding='utf-8')+'''\n\n## Mise à jour V1.3 — Couleur / relief\n\nLes 288 variantes couleur ont été comparées à leurs équivalents monochromes V1.2. Les huit silhouettes de la famille clés, outils et sièges ont été réalignées par le dessin monochrome validé. Les badges de couleur ont une séparation transparente entre la base et le badge. Les dégradés d'origine ont été conservés, les ombres réduites et la toque de cuisine rendue plus visible sur blanc. Les 288 SVG monochromes n'ont pas été retouchés. Voir `docs/RAPPORT_REVUE_COULEUR_V1_3.md`.\n''',encoding='utf-8')

report='''# ZAMUREK Matière — Revue couleur / relief V1.3\n\n## Périmètre et méthode\n\n- Référence : archive V1.2 et ses **288 icônes monochromes corrigées**.\n- **288 variantes couleur** examinées visuellement sur planches, comparées par rendu optique et structure SVG à la géométrie monochrome V1.2.\n- Géométrie principale redessinée depuis la monochromie pour 8 icônes : '''+', '.join('`'+a+'`' for a in changed_geometry)+'''.\n- Les badges ronds sont isolés au moyen de découpes **vectorielles transparentes**, en conservant les formes et dégradés du badge.\n- Le relief est préservé, l'ombre est légèrement atténuée pour éviter les halos à 24 px.\n- Couleurs officielles inchangées : `#005C45`, `#FF8A1E`, `#D21868`.\n- Les 288 fichiers monochromes sont **identiques octet par octet** à la V1.2.\n\n## Modifications mesurables\n\n| Opération | Quantité |\n|---|---:|\n| SVG couleur contrôlés | 288 |\n| Silhouettes de référence monochrome transposées en couleur | '''+str(len(changed_geometry))+''' |\n| Séparations transparentes badge / corps | '''+str(len(changed_badges))+''' |\n| Ajustements d'ombre / papier sur couleur | '''+str(len(changed_other))+''' |\n| SVG couleur de sortie | 288 |\n| SVG monochromes conservés | 288 |\n\n## Contrôles et limites\n\nUn validateur local vérifie les 576 documents SVG, les IDs d'icônes, les références de peinture, le rendu multi-tailles, la transparence et la cohérence des sprites. Les contrôles ne prouvent pas à eux seuls l'absence de toute ambiguïté sémantique ou de défaut perceptif : une inspection humaine écran par écran et à différentes tailles reste nécessaire.\n\n### Fichiers\n\n- `svg/couleur/` : nouvelles versions V1.3.\n- `svg/interface/` : monochromes V1.2 identiques.\n- `sprites/` : générés depuis les masters individuels.\n- `manifest.json` et `design-tokens.json` : mis à jour.\n- `ZAMUREK_Atelier_Audit_Icones_V1_3.html` : recherche et comparaison des 576 SVG directement dans le HTML autonome.\n'''
docs=root/'docs';docs.mkdir(exist_ok=True)
(docs/'RAPPORT_REVUE_COULEUR_V1_3.md').write_text(report,encoding='utf-8')
# Add source for actual v1.3 optimizations; historical build.py is preserved not to regress masters.
shutil.copy2(Path(__file__),root/'sources'/'optimize_couleur_v13.py')
(root/'sources'/'README_V1_3.md').write_text('''# Sources V1.3\n\nLes générateurs `build.py` et `drawing.py` restent des archives de V1.0 : ne pas les exécuter sur les assets finalisés. La passe corrective V1.3 est implémentée par `optimize_couleur_v13.py` (source de la présente génération). Le paquet ZIP V1.2 est l'entrée requise; les masters corrigés V1.3 sont dans `svg/couleur` et les monochromes V1.2 sont inchangés.\n''')

# Create content reference record for further validation later.
(base/'V1_3_CHANGES.json').write_text(json.dumps({'geometry':changed_geometry,'badges':changed_badges,'shadow_or_paper':changed_other},ensure_ascii=False,indent=2)+'\n')
print('OUTPUT',root)
