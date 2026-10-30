#!/usr/bin/env python3
"""Generate Zamurek SVG illustrations from locally pinned Humaaans + IRA Design vectors."""
import base64, csv, gzip, html, io, json, re, unicodedata
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
REG=REPO/"docs/design/illustrations/ZAMUREK_Illustrations_Registry_V1.json"
PALETTE={"G":"#005C45","O":"#FF8A1E","M":"#D21868","G2":"#14886B",
         "INK":"#142C25","W":"#FFFFFF","CREAM":"#FFF0DE"}
HUMANS=("standing-1","standing-4","standing-7","standing-11","standing-18","standing-23","sitting-2","sitting-5")
CHARACTER={
"DISCOVERY":"standing-23","SEARCH":"standing-1","CHECKOUT":"standing-18","TENDER":"standing-4",
"PROFILE":"standing-23","STORE":"standing-4","CATALOG":"standing-7",
"MERCHANT-ORDER":"standing-18","ANALYTICS":"sitting-5","POS":"sitting-2",
"POS-TOOLS":"standing-11","FOOD":"standing-4","BEAUTY":"standing-7",
"REPAIR":"standing-11","FURNITURE":"standing-18","PHARMACY":"standing-11",
"SERVICES":"standing-1","WEIGHT":"standing-4","VENUE":"standing-23",
"AI-SHOP":"standing-23","AI-MERCHANT":"standing-7","AI-OPS":"sitting-2",
"AI-CHAT":"standing-1","ONBOARDING":"standing-23","EDITORIAL":"standing-4",
"OPERATOR":"sitting-5"}
OBJECT={
"EMPTY":"basket","SUCCESS":"parcel","ERROR":"phone","LOADING":"sync",
"DISCOVERY":"phone","SEARCH":"search","CHECKOUT":"basket","TENDER":"cash",
"PROFILE":"profile","STORE":"store","CATALOG":"catalog",
"MERCHANT-ORDER":"parcel","ANALYTICS":"chart","POS":"register",
"POS-TOOLS":"scanner","FOOD":"food","BEAUTY":"beauty","REPAIR":"repair",
"FURNITURE":"furniture","PHARMACY":"shield","SERVICES":"toolkit",
"WEIGHT":"scale","VENUE":"venue","AI-SHOP":"ai","AI-MERCHANT":"catalog",
"AI-OPS":"chart","AI-CHAT":"chat","TRUST":"shield","ONBOARDING":"steps",
"NOTIFY":"bell","EDITORIAL":"store","OPERATOR":"chart","UTILITY":"printer"}
# Each object is genuine SVG geometry, constructed to form separate reusable masters.
SHAPES={
"basket":'<path d="M38 113h244l-34 141H73z" fill="$G" stroke="$INK" stroke-width="6"/><path d="M78 113Q80 37 160 37t82 76" stroke="$O" stroke-width="22" fill="none" stroke-linecap="round"/><path d="M108 150v75m53-75v75m53-75v75" stroke="$W" stroke-width="13" opacity=".66"/><path d="M41 113h239" stroke="$G2" stroke-width="15"/>',
"parcel":'<path d="M43 83l119-54 116 54v136l-116 57-119-57z" fill="$G"/><path d="M43 83l119 58 116-58M162 141v135" stroke="$W" stroke-width="8" fill="none"/><path d="M103 54l120 56v43" stroke="$O" stroke-width="19" fill="none"/>',
"phone":'<rect x="79" y="18" width="164" height="271" rx="30" fill="$INK"/><rect x="93" y="33" width="135" height="238" rx="16" fill="$W"/><rect x="109" y="62" width="103" height="28" rx="12" fill="$G2" opacity=".3"/><path d="M118 144h81M118 173h59M118 201h73" stroke="$G" stroke-width="13" stroke-linecap="round"/><circle cx="159" cy="251" r="8" fill="$O"/>',
"sync":'<circle cx="158" cy="153" r="104" stroke="$G" stroke-width="21" stroke-dasharray="420 232" fill="none"/><path d="M241 49l28 69-72-13" fill="$O"/><path d="M79 258l-26-68 69 11" fill="$M"/><circle cx="158" cy="153" r="21" fill="$G2"/>',
"search":'<circle cx="122" cy="126" r="82" stroke="$G" stroke-width="25" fill="none"/><path d="M181 187l76 77" stroke="$O" stroke-width="28" stroke-linecap="round"/><circle cx="122" cy="126" r="30" fill="$G2" opacity=".18"/>',
"cash":'<rect x="21" y="62" width="270" height="175" rx="22" fill="$G" transform="rotate(-7 152 150)"/><rect x="47" y="84" width="224" height="122" rx="15" fill="$W" transform="rotate(-7 152 150)"/><circle cx="155" cy="155" r="44" fill="$O"/><path d="M155 123v60m-22-43h43m-43 27h43" stroke="$G" stroke-width="8" stroke-linecap="round"/><rect x="89" y="211" width="195" height="57" rx="10" fill="$G2" opacity=".95"/>',
"profile":'<rect x="28" y="48" width="264" height="221" rx="27" fill="$G"/><circle cx="113" cy="129" r="44" fill="$O"/><path d="M49 237q0-69 64-69t64 69" fill="$W"/><path d="M193 111h68m-68 29h53m-53 29h45" stroke="$W" stroke-width="11" stroke-linecap="round"/>',
"store":'<path d="M50 129h218v132H50z" fill="$G"/><path d="M37 93h243l-25 65H62z" fill="$O"/><path d="M87 93v65m56-65v65m55-65v65" stroke="$W" stroke-width="10" opacity=".7"/><rect x="93" y="179" width="76" height="82" rx="5" fill="$W"/><rect x="192" y="186" width="42" height="44" rx="8" fill="$G2"/><path d="M33 265h255" stroke="$INK" stroke-width="8"/>',
"catalog":'<path d="M78 69l47-37q31 39 70 0l49 37 41 53-43 41-28-22v126H106V141l-28 22-43-41z" fill="$G" stroke="$G2" stroke-width="6"/><path d="M129 111h70" stroke="$W" stroke-width="8"/><path d="M204 189l77-1v68l-77 1z" fill="$O"/><circle cx="226" cy="208" r="8" fill="$W"/>',
"chart":'<rect x="21" y="27" width="278" height="250" rx="29" fill="$W" stroke="$G2" stroke-width="7"/><path d="M53 247h214" stroke="$G" stroke-width="9"/><rect x="61" y="172" width="46" height="74" rx="8" fill="$G"/><rect x="127" y="139" width="46" height="107" rx="8" fill="$O"/><rect x="193" y="85" width="46" height="161" rx="8" fill="$M"/><path d="M57 142l69-40 48 17 66-52" stroke="$INK" stroke-width="9" fill="none" stroke-linecap="round"/>',
"register":'<rect x="25" y="143" width="266" height="116" rx="20" fill="$G"/><rect x="54" y="32" width="188" height="142" rx="22" fill="$INK"/><rect x="70" y="48" width="155" height="105" rx="10" fill="$W"/><rect x="95" y="74" width="106" height="22" rx="10" fill="$G2"/><rect x="96" y="116" width="89" height="14" rx="7" fill="$O"/><path d="M62 208h186" stroke="$G2" stroke-width="12"/><rect x="257" y="14" width="42" height="121" rx="8" fill="$W" stroke="$G2" stroke-width="5"/><path d="M268 46h20m-20 21h20m-20 21h16" stroke="$G" stroke-width="5"/>',
"scanner":'<rect x="41" y="45" width="239" height="151" rx="23" fill="$W" stroke="$G" stroke-width="11"/><path d="M73 79v92m18-92v92m28-92v92m18-92v92m34-92v92m20-92v92m19-92v92" stroke="$G" stroke-width="8"/><path d="M15 204l289-20" stroke="$M" stroke-width="9"/><rect x="223" y="211" width="66" height="51" rx="9" fill="$O"/>',
"food":'<ellipse cx="158" cy="166" rx="146" ry="101" fill="$W" stroke="$G2" stroke-width="13"/><ellipse cx="158" cy="166" rx="123" ry="82" fill="$O"/><path d="M158 166L75 105q-36 71 24 117z" fill="$G2"/><path d="M158 166l91-61q33 75-34 122z" fill="$CREAM"/><circle cx="98" cy="141" r="15" fill="$M"/><circle cx="198" cy="186" r="15" fill="$M"/><circle cx="148" cy="210" r="11" fill="$M"/><path d="M101 41q-10-24 8-38m60 38q-10-24 8-38m50 41q-10-24 8-38" fill="none" stroke="$G2" stroke-width="9" stroke-linecap="round"/>',
"beauty":'<rect x="67" y="26" width="193" height="232" rx="96" fill="$O"/><rect x="82" y="41" width="162" height="200" rx="82" fill="$W"/><path d="M105 193q54-100 114-29" stroke="$G" stroke-width="18" fill="none"/><path d="M55 271h224" stroke="$G2" stroke-width="11" stroke-linecap="round"/><path d="M25 97l67 76m0-76l-67 76" stroke="$M" stroke-width="9"/><circle cx="41" cy="183" r="15" fill="none" stroke="$M" stroke-width="7"/><circle cx="91" cy="183" r="15" fill="none" stroke="$M" stroke-width="7"/>',
"repair":'<rect x="95" y="20" width="143" height="255" rx="25" fill="$INK"/><rect x="108" y="36" width="116" height="217" rx="15" fill="$W"/><path d="M141 90l53 60-53 59" stroke="$G" stroke-width="13" fill="none" stroke-linejoin="round"/><path d="M24 85l57 58m-42-70L24 85l-5 27m158 100l76 64" stroke="$O" stroke-width="14" stroke-linecap="round"/><circle cx="162" cy="227" r="9" fill="$M"/>',
"furniture":'<rect x="80" y="60" width="164" height="116" rx="44" fill="$G"/><rect x="55" y="150" width="220" height="73" rx="27" fill="$G2"/><rect x="43" y="115" width="40" height="116" rx="19" fill="$O"/><rect x="245" y="115" width="40" height="116" rx="19" fill="$O"/><path d="M91 214v53m152-53v53" stroke="$INK" stroke-width="14" stroke-linecap="round"/>',
"shield":'<path d="M158 20l122 54v74q0 103-122 147Q36 253 36 148V74z" fill="$G"/><path d="M158 51l92 38v62q0 78-92 111-92-36-92-111V89z" fill="$G2"/><path d="M117 150l27 29 61-61" stroke="$W" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
"toolkit":'<rect x="40" y="111" width="241" height="165" rx="26" fill="$G"/><path d="M105 111V72q0-29 55-29t55 29v39" fill="none" stroke="$O" stroke-width="18"/><rect x="42" y="149" width="237" height="42" fill="$G2"/><rect x="143" y="161" width="37" height="59" rx="8" fill="$W"/><circle cx="161" cy="192" r="5" fill="$M"/>',
"scale":'<rect x="39" y="143" width="249" height="126" rx="29" fill="$G"/><rect x="69" y="165" width="185" height="69" rx="15" fill="$W"/><path d="M158 206l44-30" stroke="$M" stroke-width="12"/><circle cx="158" cy="207" r="10" fill="$O"/><path d="M27 132h271" stroke="$O" stroke-width="19" stroke-linecap="round"/><path d="M138 124q-38-68 10-84 62-15 59 53-5 43-69 31z" fill="$G2"/>',
"venue":'<path d="M20 113h130v147H20z" fill="$G"/><path d="M13 90h143l-19 48H32z" fill="$O"/><rect x="52" y="171" width="61" height="89" rx="7" fill="$W"/><path d="M175 91h125v169H175z" fill="$G2"/><path d="M162 91l18-57h110l16 57" fill="$M"/><rect x="208" y="155" width="52" height="105" fill="$W"/><path d="M10 263h300" stroke="$INK" stroke-width="8"/>',
"ai":'<rect x="27" y="57" width="263" height="185" rx="44" fill="$G"/><path d="M88 242l-18 48 82-48" fill="$G"/><path d="M127 105l13 35 34 14-34 13-13 34-14-34-34-13 34-14z" fill="$O"/><path d="M230 96l10 21 20 10-20 10-10 20-10-20-19-10 19-10z" fill="$W"/><circle cx="212" cy="197" r="13" fill="$M"/>',
"chat":'<rect x="28" y="37" width="240" height="139" rx="33" fill="$G"/><path d="M86 176l-16 35 65-35" fill="$G"/><rect x="74" y="172" width="219" height="95" rx="32" fill="$O"/><path d="M222 267l27 22-9-22" fill="$O"/><path d="M61 95h169M61 129h127" stroke="$W" stroke-width="14" stroke-linecap="round"/><path d="M114 216h135" stroke="$G" stroke-width="12" stroke-linecap="round"/>',
"steps":'<rect x="75" y="13" width="177" height="275" rx="30" fill="$INK"/><rect x="89" y="30" width="148" height="243" rx="16" fill="$W"/><circle cx="123" cy="92" r="21" fill="$G"/><circle cx="123" cy="158" r="21" fill="$O"/><circle cx="123" cy="223" r="21" fill="$M"/><path d="M159 92h49M159 158h49M159 223h49" stroke="$G2" stroke-width="12" stroke-linecap="round"/>',
"bell":'<path d="M73 221h181l-28-39v-69q0-57-65-70V23h-25v20q-64 14-64 70v69z" fill="$G"/><path d="M131 246q8 37 41 21 14-6 17-21" stroke="$O" stroke-width="14" fill="none"/><circle cx="242" cy="73" r="38" fill="$M" stroke="$W" stroke-width="9"/>',
"printer":'<rect x="32" y="123" width="264" height="140" rx="26" fill="$G"/><rect x="76" y="26" width="176" height="118" rx="14" fill="$W" stroke="$G2" stroke-width="7"/><path d="M111 67h105m-105 30h81" stroke="$G2" stroke-width="11" stroke-linecap="round"/><path d="M58 168h213" stroke="$W" stroke-width="10" stroke-linecap="round"/><circle cx="244" cy="215" r="13" fill="$O"/>'
}
def norm(s):
    return "".join(c for c in unicodedata.normalize("NFKD",s.lower()) if not unicodedata.combining(c))
def colorize(s,dark):
    c=dict(PALETTE)
    if dark:c.update(W="#E8F7EE",INK="#A8C7B5",PALE="#33453A",CARD="#233128",OUTLINE="#4B7660")
    else:c.update(PALE="#EAF4EE",CARD="#FFFDFB",OUTLINE="#BEDBCC")
    for k,v in sorted(c.items(),key=lambda kv:-len(kv[0])):s=s.replace("$"+k,v)
    return s
def svg_source(name,ident,x,y,w,h):
    folder="ira" if name in ("object","tshirt","hair","leggins") else "humaaans"
    src=(ROOT/"third_party"/folder/(name+".svg")).read_text(encoding="utf-8")
    body=re.sub(r"^[\s\S]*?<svg\b[^>]*>","",src,count=1)
    body=re.sub(r"</svg>\s*$","",body)
    body=re.sub(r"<!--[\s\S]*?-->","",body)
    mapping={}
    seen=set()
    def mk(m):
        old=m.group(1);new=ident+"-node-"+str(len(seen))
        while new in seen:new+="x"
        seen.add(new);mapping.setdefault(old,new)
        layer="head" if "Head" in old else "body" if "Body" in old else "legs" if "Bottom" in old else "part"
        return 'id="'+new+'" data-part="'+layer+'"'
    body=re.sub(r'\bid="([^"]+)"',mk,body)
    for old,new in mapping.items():
        body=body.replace("url(#"+old+")","url(#"+new+")").replace('href="#'+old+'"','href="#'+new+'"')
    for a,b in (("#1F28CF","#005C45"),("#2B44FF","#14886B"),("#5C63AB","#005C45"),
        ("#8991DC","#14886B"),("#69A1AC","#005C45"),("#89C5CC","#14886B"),
        ("#E87613","#FF8A1E"),("#FF9B21","#FF8A1E"),("#2F3676","#005C45"),
        ("#7f96df","#14886B"),("#8395cb","#14886B")):body=re.sub(re.escape(a),b,body,flags=re.I)
    box="0 0 48 48" if name=="object" else "0 0 64 64" if name in ("tshirt","leggins") else "0 0 30.59 21" if name=="hair" else "0 0 380 400" if name.startswith("sitting") else "0 0 380 480"
    origin="IRA Design" if folder=="ira" else "Humaaans"
    return '<g id="'+ident+'" data-upstream="'+origin+'" data-source="'+name+'.svg"><svg x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'" viewBox="'+box+'" overflow="visible">'+body+'</svg></g>'
def badge(name,base):
    s=norm(name)
    keys=[("erreur echec echoue refuse impossible annule expire indisponible", "warning"),
     ("paiement transfert especes remboursement encaissement cash","cash"),
     ("reservation calendrier rendez-vous rappel","steps"),
     ("commande colis livraison retrait expedition stock","parcel"),
     ("panier achat acheter","basket"),("favoris envie","heart"),
     ("recherche resultat filtre explorer","search"),("boutique marchand etablissement","store"),
     ("coiffure salon beaute","beauty"),("restaurant pizza repas menu","food"),
     ("meuble mobilier","furniture"),("pharmaci soin identite permission","shield"),
     ("reparation maintenance outil","repair"),("grammage poids balance","scale"),
     ("assistant intelligent suggestion automatique","ai"),("discussion message chat","chat"),
     ("notification alerte promotion","bell"),("scanner qr","scanner"),
     ("facture recu impression imprimer export","printer"),
     ("securise connexion compte protege mot-de-passe","shield"),
     ("tableau analyse statistiques vente croissance","chart"),
     ("synchronisation chargement attente","sync")]
    for words,k in keys:
        if any(w in s for w in words.split()):return k
    return OBJECT.get(base.removeprefix("BASE-"),"printer")
def badge_shape(kind):
    return {
      "warning":'<path d="M0-32l32 58h-64z" fill="$M"/><path d="M0-13v18m0 9v1" stroke="$W" stroke-width="6" stroke-linecap="round"/>',
      "heart":'<path d="M0 29C-25 11-34-4-22-22-13-35 0-17 0-17S17-38 28-20C38-5 24 12 0 29z" fill="$M"/>',
      "search":'<circle cx="-6" cy="-6" r="19" fill="none" stroke="$G" stroke-width="8"/><path d="M7 8l23 22" stroke="$O" stroke-width="8" stroke-linecap="round"/>',
      "shield":'<path d="M0-32l28 12v20Q27 18 0 32-27 18-28 0v-20z" fill="$G"/><path d="M-13-1l10 12 18-21" stroke="$W" stroke-width="5" fill="none"/>',
      "ai":'<path d="M0-32l12 20 20 12-20 12L0 32l-12-20-20-12 20-12z" fill="$O"/>',
      "bell":'<path d="M-22 17l7-10v-20q0-21 15-21 15 0 15 21V7l7 10z" fill="$G"/><path d="M-10 21q10 18 20 0" stroke="$O" stroke-width="5" fill="none"/>',
      "cash":'<rect x="-31" y="-20" width="62" height="40" rx="7" fill="$G"/><circle r="13" fill="$O"/>',
      "parcel":'<path d="M-28-17L0-32l28 15v32L0 32l-28-17z" fill="$G"/><path d="M-28-17L0 1l28-18M0 1v31" fill="none" stroke="$W" stroke-width="4"/>',
      "basket":'<path d="M-27-11h54l-8 38h-38z" fill="$G"/><path d="M-15-9Q-15-31 0-31T15-9" stroke="$O" stroke-width="8" fill="none"/>',
      "food":'<circle r="28" fill="none" stroke="$G" stroke-width="8"/><path d="M-9-17v34m18-34v34" stroke="$O" stroke-width="6"/>'
    }.get(kind, '<g transform="translate(-35 -35) scale(.22)">' + SHAPES.get(kind, SHAPES['printer']) + '</g>')
def render(base,name,code,dark,motion,master=False):
    short=base.removeprefix("BASE-")
    pose=CHARACTER.get(short)
    if pose and code.startswith("ZIL-") and int(code[-3:])%5==0 and short not in ("PHARMACY","POS"):
        pose=HUMANS[(int(code[-3:])//5)%6]
    person=svg_source(pose,code.lower()+"-person",9,89,355,445 if pose and pose.startswith("standing") else 405) if pose else ""
    center=407 if pose else 238
    symbol=OBJECT[short]
    geom=SHAPES[symbol]
    if short == "SUCCESS":
        geom += '<circle cx="257" cy="244" r="43" fill="$G" stroke="$W" stroke-width="9"/><path d="M235 244l15 15 30-33" fill="none" stroke="$W" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    elif short == "ERROR":
        geom += '<path d="M250 200l47 81h-94z" fill="$M" stroke="$W" stroke-width="7"/><path d="M250 229v25m0 10v1" stroke="$W" stroke-width="8" stroke-linecap="round"/>'
    # Use IRA vector components as nested layer, not as merely named references.
    accessory=({"CATALOG":"tshirt","FURNITURE":"object","BEAUTY":"hair",
       "EDITORIAL":"leggins","DISCOVERY":"object"}).get(short)
    imported=svg_source(accessory,code.lower()+"-ira",center+238,392,66,66) if accessory else ""
    icon=badge_shape(badge(name,base)) if not master else '<circle r="13" fill="$O"/>'
    theme="dark" if dark else "light"
    title=(short.replace("-"," ").title()+" — master") if master else name
    gate=("true" if any(w in norm(name) for w in ("paiement","transfert","encaissement","remboursement","pharmaci","prescription","ordonnance","autorisation","validation","commande confirmee")) and not master else "false")
    styles=""
    if motion:
        low=code.lower()
        styles=('<style><![CDATA['
            '#'+low+'-seal{transform-box:fill-box;transform-origin:center;animation:'+low+'-hint 2s ease-in-out 1}'
            '#'+low+'-device{transform-box:fill-box;transform-origin:center;animation:'+low+'-float 2.8s ease-in-out 1}'
            '@keyframes '+low+'-hint{0%,100%{scale:1;opacity:1}50%{scale:1.1;opacity:.72}}'
            '@keyframes '+low+'-float{0%,100%{translate:0 0}50%{translate:0 -6px}}'
            '@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}'
            ']]></style>')
    xml=(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="800" height="600" viewBox="0 0 800 600" role="img" aria-labelledby="{code.lower()}-title {code.lower()}-desc" data-illustration="{code}" data-base="{base}" data-theme="{theme}" data-motion="{"on" if motion else "off"}" data-requires-business-state="{gate}" data-status="REVUE_VISUELLE_REQUISE">
<title id="{code.lower()}-title">{html.escape(title)}</title><desc id="{code.lower()}-desc">Illustration Zamurek. Géométrie vectorielle native. Famille {base}. Sources Humaaans / IRA Design lorsque présentes. Pas de preuve transactionnelle.</desc>
{styles}
<g id="{code.lower()}-background" data-layer="decor">
<circle cx="{center+151}" cy="300" r="192" fill="$PALE" opacity=".81"/>
<ellipse cx="{center+159}" cy="496" rx="171" ry="14" fill="$G2" opacity=".12"/>
<circle cx="{center+300}" cy="137" r="32" fill="$O" opacity=".17"/>
<path d="M{center+294} 218l10 16 16 10-16 10-10 16-10-16-16-10 16-10z" fill="$M" opacity=".25"/></g>
{person}
<g id="{code.lower()}-device" data-layer="object" transform="translate({center} 153)">
<rect x="0" y="0" width="324" height="329" rx="51" fill="$CARD" stroke="$OUTLINE" stroke-width="4"/>
<g id="{code.lower()}-object-geometry" transform="translate(1 16)">{geom}</g>
</g>
{imported}
<g id="{code.lower()}-seal" data-layer="contextual-accessory" transform="translate({center+300} 126)">
<circle r="48" fill="$CARD" stroke="$OUTLINE" stroke-width="4"/>
<g id="{code.lower()}-context-symbol">{icon}</g></g>
</svg>''')
    return colorize(xml,dark)
def validate(src,label):
    if any(x in src for x in ("<image","<script","<foreignObject","data:image","<iframe")):raise ValueError("unsafe "+label)
    for cm in re.finditer(r'#[0-9a-fA-F]{1,9}\b',src):
        if len(cm.group(0)) not in (4,5,7,9):
            raise ValueError("invalid hexadecimal color "+cm.group(0)+" in "+label)
    root=ET.fromstring(src)
    ids=[e.get("id") for e in root.iter() if e.get("id")]
    if len(ids)!=len(set(ids)):raise ValueError("duplicate id "+label)
    for m in re.finditer(r'url\(#([^)]+)\)|(?:xlink:href|href)="#([^"]+)"',src):
        if (m.group(1) or m.group(2)) not in ids:raise ValueError("unresolved SVG ref "+label)
def save(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(data,encoding="utf-8")
def make_studio(data,items,masters):
    # All actual generated SVGs are embedded in a gzip/base64 archive, read locally via DecompressionStream.
    pack=base64.b64encode(gzip.compress(json.dumps(data,ensure_ascii=False,separators=(",",":")).encode(),compresslevel=9,mtime=0)).decode()
    catalog=json.dumps({"items":[{"id":i["id"],"name":i["name"],"base":i["base"],"priority":i["priority"],"scope":i["scope"]} for i in items],"masters":masters},ensure_ascii=False).replace("</script","<\\/script")
    prefix='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zamurek — 33 familles, 275 illustrations</title>
<style>:root{--g:#005c45;--o:#ff8a1e;--m:#d21868;--bg:#fff;--panel:#f5f9f6;--fg:#1d2b22;--muted:#667a6d;--line:#dce8df}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}body.dark{--bg:#111318;--panel:#202a24;--fg:#eef8f1;--muted:#aec2b5;--line:#3b5144}header{border-bottom:1px solid var(--line)}.wrap{max-width:1360px;margin:auto;padding:0 clamp(18px,4vw,62px)}.top{padding:22px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:18px}.logo{font-size:26px;font-weight:850;letter-spacing:-1.5px;color:var(--g)}.logo span{color:var(--o)}.kicker{font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted)}h1{font-size:clamp(27px,3.8vw,43px);letter-spacing:-.05em;line-height:1.13;margin:0}h2{font-size:17px;letter-spacing:-.025em;margin:0}.intro{padding:26px 0}.intro p{color:var(--muted);max-width:900px}button,select,input{font:inherit}button,select{background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:7px;padding:9px 12px;cursor:pointer}button[aria-pressed=true]{background:var(--g);color:#fff}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid var(--o);outline-offset:2px}.toolbar{border-block:1px solid var(--line);position:sticky;top:0;z-index:15;background:var(--bg)}.tools{padding:12px 0;display:flex;align-items:center;gap:8px;flex-wrap:wrap}.search{background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:7px;padding:9px;flex:1;min-width:220px}.count{margin-left:auto;font-size:12px;color:var(--muted)}main{padding-top:22px;padding-bottom:56px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:15px}.card{border:1px solid var(--line);border-radius:12px;overflow:hidden}.card-head{display:flex;justify-content:space-between;padding:12px 14px 0;font-size:11px;color:var(--g);font-weight:750}.preview{height:240px;background:var(--panel)}.preview iframe{border:0;width:100%;height:100%;pointer-events:none}.content{padding:14px}.content p{font-size:12px;color:var(--muted);min-height:36px;margin:5px 0 13px}.actions{display:flex;gap:8px;flex-wrap:wrap}.actions button{font-size:12px;padding:7px 9px}.pager{display:flex;justify-content:center;align-items:center;gap:12px;margin-top:30px}.muted{color:var(--muted)}footer{border-top:1px solid var(--line);padding:22px 0 35px;color:var(--muted);font-size:12px}@media(max-width:640px){.toolbar{position:static}.search{flex-basis:100%}.preview{height:270px}.count{width:100%;margin:0}}@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}</style></head><body>
<header><div class="wrap top"><div><div class="logo">Zamu<span>r</span>ek</div><div class="kicker">Studio des illustrations · Fichier HTML autonome</div></div><strong>33 familles · 275 cas · 1 100 SVG</strong></div></header>
<section class="wrap intro"><div class="kicker">Collection complète · revue graphique en cours</div><h1>Illustrations Zamurek</h1><p>Bibliothèque SVG réutilisable basée sur les sources vectorielles Humaaans et IRA Design. Tous les contenus SVG sont embarqués dans ce fichier, sans ressource réseau. Une illustration seule n'atteste jamais un paiement ou une opération réussie.</p></section>
<div class="toolbar"><div class="wrap tools"><input class="search" id="search" type="search" placeholder="Rechercher un usage, un ID…" aria-label="Rechercher"><select id="family" aria-label="Famille"><option value="">Toutes familles</option></select><select id="priority" aria-label="Priorité"><option value="">Priorités</option><option>P0</option><option>P1</option><option>P2</option><option>P3</option></select><button id="theme" aria-pressed="false">Obsidienne</button><button id="motion" aria-pressed="false">Animé</button><button id="reduce" aria-pressed="false">Mouvements réduits</button><span class="count" id="count"></span></div></div><main class="wrap"><div id="message" class="muted">Chargement de la collection SVG intégrée…</div><div id="gallery" class="grid"></div><nav id="pager" class="pager" aria-label="Pages de la collection"></nav></main>
<footer><div class="wrap">Attribution : Humaaans (Pablo Stanley, miroir CC BY 4.0) ; IRA Design (Creative Tim, MIT). Modification et composition : Zamurek. Les 275 compositions vectorielles sont disponibles pour revue, mais la qualité visuelle, la compatibilité Android et les états métier nécessitent encore une validation.</div></footer>
<script id="catalog" type="application/json">'''
    middle='''</script><script id="packed" type="application/octet-stream">'''
    suffix='''</script><script>
"use strict";
(async function(){
let catalog=JSON.parse(document.getElementById("catalog").textContent);
let packed=Uint8Array.from(atob(document.getElementById("packed").textContent.trim()),x=>x.charCodeAt(0));
if(typeof DecompressionStream==="undefined"){document.getElementById("message").textContent="Navigateur incompatible avec DecompressionStream. Utilisez Chrome ou Firefox récent.";return}
try{
let stream=new Blob([packed]).stream().pipeThrough(new DecompressionStream("gzip"));
let all=JSON.parse(await new Response(stream).text());packed=null;
let state={theme:"light",motion:"static",reduced:false,search:"",family:"",priority:"",page:0};
const gallery=document.getElementById("gallery"),pager=document.getElementById("pager"),family=document.getElementById("family");
for(let name of catalog.masters){let opt=document.createElement("option");opt.value=name;opt.textContent=name;family.appendChild(opt)}
function key(item){return item.id+"-"+state.motion+"-"+state.theme}
function makeFrame(k){let frame=document.createElement("iframe");frame.setAttribute("sandbox","");frame.setAttribute("referrerpolicy","no-referrer");frame.loading="lazy";frame.title="Illustration SVG "+k;let src=all[k];let rule=state.reduced?"<style>svg *{animation:none!important;transition:none!important}</style>":"";frame.srcdoc='<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;width:100%;height:100%;overflow:hidden}body{display:flex;align-items:center;justify-content:center}svg{width:100%;height:100%;object-fit:contain}</style></head><body>'+rule+src.replace('<?xml version="1.0" encoding="UTF-8"?>',"")+"</body></html>";return frame}
function download(k){let url=URL.createObjectURL(new Blob([all[k]],{type:"image/svg+xml;charset=utf-8"}));let a=document.createElement("a");a.href=url;a.download=k.toLowerCase()+".svg";document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1200)}
function btn(text,handler){let b=document.createElement("button");b.textContent=text;b.onclick=handler;return b}
function draw(){
document.getElementById("message").textContent="";document.body.classList.toggle("dark",state.theme==="dark");
document.getElementById("theme").textContent=state.theme==="light"?"Obsidienne":"Blanc";document.getElementById("theme").setAttribute("aria-pressed",state.theme==="dark");
document.getElementById("motion").textContent=state.motion==="static"?"Animé":"Fixe";document.getElementById("motion").setAttribute("aria-pressed",state.motion==="motion");document.getElementById("reduce").setAttribute("aria-pressed",state.reduced);
let list=catalog.items.filter(x=>(!state.family||x.base===state.family)&&(!state.priority||x.priority===state.priority)&&(!state.search||(x.id+" "+x.name+" "+x.base).toLowerCase().includes(state.search)));
document.getElementById("count").textContent=list.length+" / 275";let pages=Math.max(1,Math.ceil(list.length/18));state.page=Math.min(state.page,pages-1);gallery.replaceChildren();
for(let item of list.slice(state.page*18,(state.page+1)*18)){
let k=key(item),card=document.createElement("article");card.className="card";
let head=document.createElement("div");head.className="card-head";head.textContent=item.id+" · "+item.priority;
let preview=document.createElement("div");preview.className="preview";preview.appendChild(makeFrame(k));
let content=document.createElement("div");content.className="content";let h2=document.createElement("h2");h2.textContent=item.name;
let p=document.createElement("p");p.textContent=item.base+" · "+item.scope;
let actions=document.createElement("div");actions.className="actions";actions.append(btn("Télécharger SVG",()=>download(k)),btn("Relancer",()=>preview.replaceChildren(makeFrame(k))));
content.append(h2,p,actions);card.append(head,preview,content);gallery.appendChild(card)}
pager.replaceChildren();if(pages>1){let prev=btn("← Précédent",()=>{state.page--;draw();scrollTo(0,0)});prev.disabled=state.page===0;let next=btn("Suivant →",()=>{state.page++;draw();scrollTo(0,0)});next.disabled=state.page>=pages-1;let label=document.createElement("span");label.textContent="Page "+(state.page+1)+" / "+pages;pager.append(prev,label,next)}}
document.getElementById("search").oninput=e=>{state.search=e.target.value.toLowerCase().trim();state.page=0;draw()};
family.onchange=e=>{state.family=e.target.value;state.page=0;draw()};document.getElementById("priority").onchange=e=>{state.priority=e.target.value;state.page=0;draw()};
document.getElementById("theme").onclick=()=>{state.theme=state.theme==="light"?"dark":"light";draw()};
document.getElementById("motion").onclick=()=>{state.motion=state.motion==="static"?"motion":"static";draw()};
document.getElementById("reduce").onclick=()=>{state.reduced=!state.reduced;draw()};draw();
}catch(e){document.getElementById("message").textContent="Échec de lecture de la collection : "+e.message;throw e}
})();
</script></body></html>'''
    save(ROOT/"ZAMUREK_ILLUSTRATIONS_STUDIO_33_FAMILLES.html",prefix+catalog+middle+pack+suffix)
def main():
    registry=json.loads(REG.read_text(encoding="utf-8"))
    items=registry["items"];bases=sorted({x["base"] for x in items})
    assert len(items)==275 and len(bases)==33
    masters={}
    for base in bases:
        for theme in ("light","dark"):
            for mode in ("static","motion"):
                code=base.lower();svg=render(base,base,code,theme=="dark",mode=="motion",True)
                validate(svg,code)
                save(ROOT/"assets/masters"/base/(code+"-"+mode+"-"+theme+".svg"),svg)
    live={};production=[]
    pilots={"ZIL-001","ZIL-044","ZIL-117"}
    for item in items:
        code=item["id"];paths=[]
        for theme in ("light","dark"):
            for mode in ("static","motion"):
                file=ROOT/"assets"/mode/(code.lower()+"-"+theme+".svg")
                if code in pilots:
                    assert file.is_file(),file
                    svg=file.read_text(encoding="utf-8")
                else:
                    svg=render(item["base"],item["name"],code,theme=="dark",mode=="motion")
                    validate(svg,code)
                    save(file,svg)
                live[code+"-"+mode+"-"+theme]=svg
                paths.append(str(file.relative_to(ROOT)))
        production.append({**item,"status":"REVUE_VISUELLE_REQUISE","production_status":"GENERATED_VECTOR_PENDING_QA",
          "requires_business_state":any(w in norm(item["name"]) for w in ("paiement","encaissement","remboursement","transfert","pharmaci","autorisation","validation","commande confirmee","reussie")),
          "pilot_preserved":code in pilots,"paths":paths})
    assert len(live)==1100
    make_studio(live,items,bases)
    out={"schemaVersion":"2.0","status":"VECTORS_GENERATED_QA_PENDING","visualAccepted":False,"mobileValidated":False,
      "countCases":275,"countMasters":33,"countVariants":1100,"newCaseFiles":1088,"masterVariants":132,
      "sourceRegistry":"docs/design/illustrations/ZAMUREK_Illustrations_Registry_V1.json",
      "sources":"8 pinned Humaaans vectors + 4 pinned IRA Design SVG components", "items":production}
    save(ROOT/"registry/illustrations.production.v2.json",json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    buf=io.StringIO();writer=csv.writer(buf);writer.writerow(["id","name","base","priority","status","requires_business_state","static_light","motion_light","static_dark","motion_dark"])
    for row in production:writer.writerow([row["id"],row["name"],row["base"],row["priority"],row["status"],row["requires_business_state"]]+row["paths"])
    save(ROOT/"registry/illustrations.production.v2.csv",buf.getvalue())
    report={"cases":275,"masters":33,"case_variants":1100,"new_case_variants":1088,
            "master_variants":132,"preserved_pilots":sorted(pilots),
            "countsByFamily":dict(Counter(x["base"] for x in items)),
            "qa":"SVG structure programmatically validated; visual and mobile QA pending."}
    save(ROOT/"reports/illustrations-v2-production.json",json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    save(ROOT/"reports/illustrations-v2-qa.md",
       "# Production vectorielle Zamurek — 33 familles / 275 contextes\n\n"
       "132 variantes de master, 1100 variantes de cas (dont 12 fichiers pilotes conservés), 1088 nouvelles variantes SVG générées.\n\n"
       "Chaque fichier est vectoriel, avec structure modulaire, accessibilité, transparence et animations courtes respectant la préférence de mouvement réduit.\n\n"
       "Statut : REVUE_VISUELLE_REQUISE. Les tests XML ne prouvent ni la qualité esthétique, ni le contraste, ni la performance Android. "
       "Des contrôles de conformité métier et de licence sont toujours requis. Le backlog normatif d'origine est inchangé.\n")
    print(json.dumps({"status":"PASS_GENERATION","cases":275,"masters":33,"variants":1100,"newVariants":1088,
                      "studioBytes":(ROOT/"ZAMUREK_ILLUSTRATIONS_STUDIO_33_FAMILLES.html").stat().st_size},ensure_ascii=False))
if __name__=="__main__":main()
