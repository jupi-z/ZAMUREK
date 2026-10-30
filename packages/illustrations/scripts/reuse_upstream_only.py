#!/usr/bin/env python3
"""Reuse existing IRA Design Gallery / Humaaans SVG, recolor hex strings only.
Forbidden: generating paths, SVG groups, poses, accessories or animations.
"""
import base64, colorsys, csv, gzip, hashlib, io, json, re, subprocess
from pathlib import Path
from xml.etree import ElementTree as ET
from collections import Counter

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
TEMP=Path("/tmp/zamurek-official-artwork")
REG=ROOT/"docs/design/illustrations/ZAMUREK_Illustrations_Registry_V1.json"
HEX=re.compile(r"#[0-9a-fA-F]{6}\b")
SKINS={"#B28B67","#D3AB8B","#A0616A","#FFB8B8"}
BG={"#F8F8FF","#F5F5FC","#E9EDFC","#E9EDFB","#E9EDFA","#E1E6FC","#E1E6FB","#BAC5F4","#BAC4F6","#BAC6F2","#B1C1F2","#FCFCFC","#F4F4F4"}
G={"#1F28CF","#2B44FF","#5C63AB","#2F3676","#8991DC","#69A1AC","#89C5CC"}
USES={
"BASE-EMPTY":[4,21,22],"BASE-SUCCESS":[23,24,28],"BASE-ERROR":[2,4,20],
"BASE-LOADING":[7,8,21],"BASE-DISCOVERY":[5,6,13,14],
"BASE-SEARCH":[3,21,22],"BASE-CHECKOUT":[3,4,5,6],
"BASE-TENDER":[3,4,29,30],"BASE-PROFILE":[1,2,29],
"BASE-STORE":[13,14,29,30],"BASE-CATALOG":[3,4,11,12],
"BASE-MERCHANT-ORDER":[7,8,13,14],"BASE-ANALYTICS":[27,28,3,4],
"BASE-POS":[29,30,3,4],"BASE-POS-TOOLS":[29,30,3],
"BASE-FOOD":[11,12,17,18],"BASE-BEAUTY":[9,10,15,16],
"BASE-REPAIR":[1,2,29,30],"BASE-FURNITURE":[9,10,11,12],
"BASE-PHARMACY":[11,12,29,30],"BASE-SERVICES":[1,2,23,24],
"BASE-WEIGHT":[11,12,29,30],"BASE-VENUE":[13,14,29,30],
"BASE-AI-SHOP":[3,4,21,22],"BASE-AI-MERCHANT":[1,2,29,30],
"BASE-AI-OPS":[27,28,3,4],"BASE-AI-CHAT":[23,24,5,6],
"BASE-TRUST":[21,22,27,28],"BASE-ONBOARDING":[5,6,29,30],
"BASE-NOTIFY":[7,8,23,24],"BASE-EDITORIAL":[13,14,21,22,29,30],
"BASE-OPERATOR":[27,28,29,30],"BASE-UTILITY":[1,2,11,12]}
HUMAN_BASE={"BASE-PROFILE","BASE-BEAUTY","BASE-SERVICES","BASE-REPAIR",
"BASE-AI-CHAT","BASE-AI-SHOP","BASE-AI-MERCHANT","BASE-ONBOARDING","BASE-EDITORIAL"}
CLOTH_LIGHT={"#1F28CF":"#005C45","#2B44FF":"#005C45","#5C63AB":"#10886B",
 "#2F3676":"#005C45","#8991DC":"#70C7A7","#69A1AC":"#10886B","#89C5CC":"#70C7A7"}
CLOTH_DARK={"#1F28CF":"#4BB99A","#2B44FF":"#4BB99A","#5C63AB":"#7ED8B7",
 "#2F3676":"#2C866D","#8991DC":"#9CE8C9","#69A1AC":"#7ED8B7","#89C5CC":"#9CE8C9"}
PAL_LIGHT={
 "green":("#005C45","#10886B","#70C7A7","#C2E7D7"),
 "orange":("#C35E06","#FF8A1E","#FFAF58","#FFE1BF"),
 "magenta":("#9B104C","#D21868","#EA6D9C","#F5BBD3"),
 "neutral":("#152F25","#71897C","#D8E9DF","#F6FAF7")}
PAL_DARK={
 "green":("#3FA889","#64CCAA","#9CE8C9","#285A49"),
 "orange":("#E97618","#FF9C48","#FFC17D","#684B31"),
 "magenta":("#C71B60","#E65D91","#F5A0C0","#60324A"),
 "neutral":("#DAEEE1","#AAC1B2","#405A4A","#111318")}
def run(*args):
    subprocess.run(args,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def git(url,dest):
    if not (dest/".git").is_dir():
        dest.parent.mkdir(parents=True,exist_ok=True)
        run("git","clone","--quiet","--depth=1",url,str(dest))
    return subprocess.check_output(["git","-C",str(dest),"rev-parse","HEAD"],text=True).strip()
def put(path,content):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(content,encoding="utf-8")
def hashit(s):return hashlib.sha256(s.encode()).hexdigest()
def clean_svg(data):
    start=data.find("<svg")
    end=data.rfind("</svg>")
    assert start>=0 and end>start
    s=data[start:end+6]
    ET.fromstring(s)
    assert not re.search(r"<(?:image|foreignObject|script)\b",s,re.I)
    return s
def recolor(source,dark,library):
    def color(m):
        val=m.group().upper()
        if library=="humaaans":
            return (CLOTH_DARK if dark else CLOTH_LIGHT).get(val,m.group())
        if val=="#FFFFFF":return m.group()
        if val in BG:
            if dark:return "#111318" if val in {"#F8F8FF","#F5F5FC","#FCFCFC","#F4F4F4"} else "#25372E"
            return "#FFFFFF" if val in {"#F8F8FF","#F5F5FC","#FCFCFC","#F4F4F4"} else "#EAF4EE"
        r,g,b=(int(val[i:i+2],16)/255 for i in (1,3,5))
        h,l,s=colorsys.rgb_to_hls(r,g,b)
        deg=h*360
        category=("neutral" if s<.15 else "green" if 165<=deg<310 or 95<=deg<165
                  else "magenta" if deg<22 or deg>=310 else "orange")
        band=0 if l<.37 else 1 if l<.63 else 2 if l<.82 else 3
        return (PAL_DARK if dark else PAL_LIGHT)[category][band]
    out=HEX.sub(color,source)
    assert HEX.sub("#RECOLORED",out)==HEX.sub("#RECOLORED",source),"Artwork geometry changed"
    ET.fromstring(out)
    return out
def html_studio(items,pool):
    data=base64.b64encode(gzip.compress(json.dumps(pool,separators=(",",":")).encode(),compresslevel=9,mtime=0)).decode()
    listing=json.dumps(items,ensure_ascii=False,separators=(",",":")).replace("</script","<\\/script")
    beginning='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zamurek — Originaux IRA Design et Humaaans, 257 usages</title>
<style>:root{--bg:white;--fg:#16251c;--muted:#657e70;--line:#d9e4dd;--stage:#f5f9f6;--green:#005c45;--orange:#ff8a1e}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.48 system-ui,-apple-system,Segoe UI,sans-serif}body.dark{--bg:#111318;--fg:#edf8f0;--muted:#abc1b3;--line:#3c5546;--stage:#202a24}
header{border-bottom:1px solid var(--line)}.wrap{max-width:1350px;padding:0 clamp(18px,4vw,60px);margin:auto}.head{padding:22px 0;display:flex;align-items:center;justify-content:space-between;gap:15px;flex-wrap:wrap}.logo{font-size:27px;font-weight:850;color:var(--green);letter-spacing:-1px}.logo b{color:var(--orange)}h1{font-size:clamp(26px,3vw,38px);margin:0;line-height:1.15;letter-spacing:-.04em}.intro{padding:30px 0}.intro p{max-width:780px;color:var(--muted)}
button,input,select{font:inherit}button,select,input{border:1px solid var(--line);border-radius:8px;padding:9px 12px;background:var(--bg);color:var(--fg)}button{cursor:pointer}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid var(--orange)}
.toolbar{border-block:1px solid var(--line);background:var(--bg);position:sticky;top:0;z-index:5}.tools{display:flex;gap:8px;flex-wrap:wrap;padding:12px 0}.search{min-width:180px;flex:1}.count{margin-left:auto;font-size:12px;color:var(--muted);align-self:center}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:15px;padding:23px 0}.card{border:1px solid var(--line);border-radius:12px;overflow:hidden}.art{height:250px;background:var(--stage)}.art iframe{width:100%;height:100%;border:0;pointer-events:none}.inside{padding:14px}.meta{font-size:11px;color:var(--muted)}h2{font-size:17px;margin:4px 0}.inside p{font-size:12px;color:var(--muted)}.actions{display:flex;gap:7px;flex-wrap:wrap}.actions button{font-size:12px;padding:7px}.pager{display:flex;align-items:center;justify-content:center;gap:12px;padding:15px 0 42px}footer{border-top:1px solid var(--line);padding:20px 0 34px;color:var(--muted);font-size:12px}
@media(max-width:600px){.toolbar{position:static}.search{flex-basis:100%}.count{width:100%;margin:0}}</style></head>
<body><header><div class="wrap head"><div class="logo">Zamu<b>r</b>ek</div><strong>62 SVG originaux · 257 cas</strong></div></header>
<div class="wrap intro"><h1>Illustrations réutilisées, sans nouveau dessin</h1><p>IRA Design Gallery et Humaaans : uniquement les SVG existants, recolorés pour Zamurek. Les 257 cas réutilisent 62 sources. Une correspondance graphique exacte avec chaque contexte n’est pas garantie.</p></div>
<div class="toolbar"><div class="wrap tools"><input id="search" class="search" placeholder="ID, usage, famille…" aria-label="Rechercher"><select id="family" aria-label="Famille"><option value="">Toutes familles</option></select><select id="source" aria-label="Bibliothèque"><option value="">Toutes bibliothèques</option><option value="ira-gallery">IRA Design</option><option value="humaaans">Humaaans</option></select><button id="theme">Fond obsidienne</button><span class="count" id="count"></span></div></div>
<main class="wrap"><div id="loading">Chargement local de la galerie…</div><div id="gallery" class="gallery"></div><div id="pager" class="pager"></div></main>
<footer><div class="wrap">Crédits : IRA Design, Creative Tim (MIT) ; Humaaans, Pablo Stanley (CC BY 4.0 selon le miroir). Aucun nouvel SVG dessiné, aucune animation créée. Revue du choix de chaque illustration requise.</div></footer>
<script id="index" type="application/json">'''
    middle='''</script><script id="bundle" type="application/octet-stream">'''
    last=r'''</script><script>
"use strict";
(async function(){
const docs=JSON.parse(document.getElementById("index").textContent);
if(typeof DecompressionStream==="undefined"){document.getElementById("loading").textContent="Navigateur trop ancien (DecompressionStream absent).";return}
const blob=Uint8Array.from(atob(document.getElementById("bundle").textContent.trim()),x=>x.charCodeAt(0));
const stream=new Blob([blob]).stream().pipeThrough(new DecompressionStream("gzip"));
const svgs=JSON.parse(await new Response(stream).text());
const state={q:"",family:"",source:"",theme:"light",page:0},families=[...new Set(docs.map(x=>x.base))].sort();
for(let name of families){let option=document.createElement("option");option.value=name;option.textContent=name;document.getElementById("family").appendChild(option)}
function key(item){return item.sourceSlug+"-"+state.theme}
function frame(item){let f=document.createElement("iframe");f.title="Illustration "+item.sourceSlug;f.loading="lazy";f.setAttribute("sandbox","");f.srcdoc='<!doctype html><html><head><meta charset="utf-8"><style>html,body{height:100%;width:100%;margin:0;overflow:hidden}body{display:flex;align-items:center;justify-content:center}svg{height:100%;width:100%;object-fit:contain}</style></head><body>'+svgs[key(item)]+"</body></html>";return f}
function button(label,click){let b=document.createElement("button");b.textContent=label;b.onclick=click;return b}
function save(item){let k=key(item),url=URL.createObjectURL(new Blob([svgs[k]],{type:"image/svg+xml;charset=utf-8"}));let a=document.createElement("a");a.href=url;a.download=item.id.toLowerCase()+"-"+state.theme+".svg";document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),700)}
function render(){
document.body.classList.toggle("dark",state.theme==="dark");document.getElementById("theme").textContent=state.theme==="light"?"Fond obsidienne":"Fond blanc";
let list=docs.filter(x=>(!state.family||x.base===state.family)&&(!state.source||x.library===state.source)&&(!state.q||(x.id+" "+x.name+" "+x.base+" "+x.sourceSlug).toLowerCase().includes(state.q)));
document.getElementById("count").textContent=list.length+" / 257";
let pages=Math.max(1,Math.ceil(list.length/15));state.page=Math.min(state.page,pages-1);
let gallery=document.getElementById("gallery");gallery.replaceChildren();
for(let item of list.slice(state.page*15,(state.page+1)*15)){let card=document.createElement("article");card.className="card";let pic=document.createElement("div");pic.className="art";pic.appendChild(frame(item));let body=document.createElement("div");body.className="inside";let meta=document.createElement("div");meta.className="meta";meta.textContent=item.id+" · "+item.library+" · "+item.sourceSlug;let h=document.createElement("h2");h.textContent=item.name;let p=document.createElement("p");p.textContent=item.base+" · Source existante réutilisée";let actions=document.createElement("div");actions.className="actions";actions.append(button("Télécharger SVG",()=>save(item)));body.append(meta,h,p,actions);card.append(pic,body);gallery.appendChild(card)}
let pager=document.getElementById("pager");pager.replaceChildren();if(pages>1){let prev=button("Précédent",()=>{state.page--;render();window.scrollTo(0,0)});prev.disabled=state.page===0;let next=button("Suivant",()=>{state.page++;render();window.scrollTo(0,0)});next.disabled=state.page===pages-1;pager.append(prev,"Page "+(state.page+1)+"/"+pages,next)}
document.getElementById("loading").textContent="";
}
document.getElementById("search").oninput=e=>{state.q=e.target.value.toLowerCase().trim();state.page=0;render()};
document.getElementById("family").onchange=e=>{state.family=e.target.value;state.page=0;render()};
document.getElementById("source").onchange=e=>{state.source=e.target.value;state.page=0;render()};
document.getElementById("theme").onclick=()=>{state.theme=state.theme==="light"?"dark":"light";render()};render();
})();
</script></body></html>'''
    put(BASE/"ZAMUREK_VISUALISATION_SOURCES_257.html",beginning+listing+middle+data+last)
def main():
    items=[x for x in json.loads(REG.read_text(encoding="utf-8"))["items"] if x["no"]<=257]
    assert len(items)==257 and len(set(x["id"] for x in items))==257 and len(USES)==33
    ira=TEMP/"ira";hum=TEMP/"hum";mit=TEMP/"mit"
    versions={"ira":git("https://github.com/ira-design/ira-design.github.io.git",ira),
              "hum":git("https://github.com/Calinou/humaaans.git",hum),
              "mit":git("https://github.com/ira-design/ira-illustrations.git",mit)}
    put(BASE/"licenses/IRA_MIT.md",(mit/"LICENSE.md").read_text(encoding="utf-8"))
    put(BASE/"licenses/HUMAAANS_CC_BY_4.md",(hum/"LICENSE.md").read_text(encoding="utf-8"))
    originals={};sources={}
    for n in range(1,31):
        slug="gallery-"+str(n).zfill(2);p="_includes/examples/svg/svg"+str(n)+".html"
        source=clean_svg((ira/p).read_text(encoding="utf-8"));originals[slug]=source
        put(BASE/"sources/original/ira-gallery"/(slug+".svg"),source)
        sources[slug]={"library":"ira-gallery","upstreamRepo":"ira-design/ira-design.github.io","upstreamCommit":versions["ira"],"upstreamPath":p,"svgSha256":hashit(source),"license":"IRA Design MIT"}
    for kind,maximum in (("standing",24),("sitting",8)):
        for n in range(1,maximum+1):
            slug=kind+"-"+str(n).zfill(2);p="Flat Assets/Humaaans/"+kind+"-"+str(n)+".svg"
            source=clean_svg((hum/p).read_text(encoding="utf-8"));originals[slug]=source
            put(BASE/"sources/original/humaaans"/(slug+".svg"),source)
            sources[slug]={"library":"humaaans","upstreamRepo":"Calinou/humaaans","upstreamCommit":versions["hum"],"upstreamPath":p,"svgSha256":hashit(source),"license":"CC BY 4.0 (mirror)"}
    assert len(originals)==62
    themes={}
    for slug,svg in originals.items():
        library="ira-gallery" if slug.startswith("gallery-") else "humaaans"
        for name,dark in (("light",False),("dark",True)):
            out=recolor(svg,dark,library);themes[slug+"-"+name]=out
            put(BASE/"assets/themes"/(slug+"-"+name+".svg"),out)
    index=[]
    for item in items:
        # Preserve whole upstream illustrations: never compose or edit geometry.
        candidates=["gallery-"+str(x).zfill(2) for x in USES[item["base"]]]
        if item["base"] in HUMAN_BASE and item["no"]%4==0:
            poses=(["sitting-01","sitting-02","sitting-03","sitting-04","sitting-05","sitting-06","sitting-07","sitting-08"]
                   if item["base"] in {"BASE-POS","BASE-ANALYTICS","BASE-AI-OPS","BASE-OPERATOR"} else
                   ["standing-"+str(n).zfill(2) for n in range(1,25)])
            candidates=poses
        slug=candidates[(item["no"]-1)%len(candidates)]
        library="ira-gallery" if slug.startswith("gallery-") else "humaaans"
        variants={}
        for mode in ("light","dark"):
            content=themes[slug+"-"+mode];dest=BASE/"assets/cases"/(item["id"].lower()+"-"+mode+".svg")
            put(dest,content)
            variants[mode]={"path":str(dest.relative_to(BASE)),"sha256":hashit(content)}
        index.append({"id":item["id"],"name":item["name"],"base":item["base"],"priority":item["priority"],
           "library":library,"sourceSlug":slug,"source":sources[slug],"variants":variants,
           "status":"REUSABLE_SOURCE_REQUIRES_CONTEXT_REVIEW"})
    assert len(index)==257 and len(list((BASE/"assets/cases").glob("*.svg")))==514
    html_studio(index,themes)
    manifest={"schemaVersion":"3.0-source-only","processedCases":257,"backlogCases":275,
       "notProcessed":["ZIL-"+str(i).zfill(3) for i in range(258,276)],
       "uniqueOriginals":62,"themeVariants":124,"caseVariants":514,
       "newSvgGeometry":0,"newAnimations":0,"sourceCommits":versions,
       "status":"SOURCE_REUSE_REVIEW_REQUIRED","cases":index}
    put(BASE/"registry/257-source-mapping.json",json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    buf=io.StringIO();writer=csv.writer(buf);writer.writerow(["id","name","base","library","sourceSlug","upstreamPath","lightPath","darkPath","quality"])
    for x in index:writer.writerow([x["id"],x["name"],x["base"],x["library"],x["sourceSlug"],x["source"]["upstreamPath"],x["variants"]["light"]["path"],x["variants"]["dark"]["path"],x["status"]])
    put(BASE/"registry/257-source-mapping.csv",buf.getvalue())
    put(BASE/"registry/upstream-sources.json",json.dumps(sources,ensure_ascii=False,indent=2)+"\n")
    put(BASE/"README.md","# Zamurek — uniquement les originaux SVG IRA Design et Humaaans\n\n"
        "**Aucune géométrie SVG nouvelle. Aucun objet SVG inventé. Aucune animation ajoutée.**\n\n"
        "Le traitement couvre **257 cas ZIL-001 à ZIL-257**, sur les 275 du registre historique. Les cas ZIL-258 à ZIL-275 sont volontairement exclus.\n\n"
        "Les 62 illustrations sources (30 scènes originales IRA Design Gallery + 32 personnages Humaaans) sont copiées dans sources/original.\n\n"
        "Les 514 fichiers thématiques (clair/sombre par cas) sont des copies réutilisées avec uniquement des substitutions hexadécimales de couleurs. Les 124 variantes de la bibliothèque de sources sont accessibles sous assets/themes.\n\n"
        "Le fichier HTML ZAMUREK_VISUALISATION_SOURCES_257.html est autonome et incorpore les 124 SVG de sources. Les 257 cas réutilisent ces sources, donc ne représentent pas 257 dessins indépendants.\n\n"
        "Chaque lien vers les originaux et SHA-256 se trouve dans registry/257-source-mapping.json et registry/upstream-sources.json.\n\n"
        "IMPORTANT : le choix des illustrations par cas est une association générique à revoir. Aucune correspondance métier précise n'est affirmée. Les thèmes conservent les formes exactes des SVG tiers. \n\n"
        "Licences dans licenses/ : IRA Design (MIT, Creative Tim), Humaaans (CC BY 4.0 d'après le miroir Calinou). La branche ne contient ni les anciens dessins géométriques Zamurek, ni les anciens générateurs.\n")
    print(json.dumps({"result":"PASS","cases":257,"upstreamSvgs":62,"modeVariants":124,"caseSvgs":514,"htmlBytes":(BASE/"ZAMUREK_VISUALISATION_SOURCES_257.html").stat().st_size}))
if __name__=="__main__":main()
