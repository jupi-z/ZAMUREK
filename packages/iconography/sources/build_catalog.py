from pathlib import Path
import json
from catalog import GROUPS
root=Path(__file__).resolve().parents[1]
assets=json.loads((root/'sources/assets.json').read_text())
text=(root/'sources/catalog.template.html').read_text().replace('__ASSETS__',json.dumps(assets,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')).replace('__GROUPS__',json.dumps({k:v[0] for k,v in GROUPS.items()},ensure_ascii=False))
(root/'Zamurek_Icones_Catalogue.html').write_text(text)
print('Catalog assembled:',len(assets),'icons')
