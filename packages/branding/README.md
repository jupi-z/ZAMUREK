# ZAMUREK — identité de marque V1

> **Portée : assets et tokens uniquement.** Aucun backend, client Android/Windows, SDK, API ou paiement n'est introduit.

## Référence retenue

- Logotype : mot **Zamurek** épais, avec **Z/mure** vert, **a** orange et **k** magenta.
- Icône : silhouette exact du croquis approuvé (tête ronde, chevron, lobes gauche/droite, lobe inférieur). **Ne pas la réinterpréter.**
- Couleurs : vert forêt `#005C45`, orange `#FF8A1E`, magenta `#D21868`.
- Fonds dominants : blanc `#FFFFFF` (clair), obsidienne `#111318` (sombre).
- Direction : brandboard **Concept 01 — Essential Identity**, fond clair, interfaces plates, minimalistes, sans ombres inutiles.
- UI : **Poppins** est un candidat issu du brandboard, pas une police identifiée de façon certaine à partir du logotype raster. Le logo doit être utilisé sous forme d'artwork, jamais reconstitué avec une substitution de police.

## Fichiers versionnés

- `assets/` : **15 SVG** (horizontal / vertical / icône × couleur clair / couleur sombre / vert mono / blanc mono / noir mono).
- `tokens/zamurek.tokens.json` : couleurs de marque et couleurs sémantiques des deux thèmes.
- `styles/zamurek-theme.css` : variables CSS sans styles imposés sur les composants.
- `manifest.json` : inventaire pour les outils, les futures interfaces et Figma.

Les SVG sont de véritables tracés éditables des **contours** vectorisés depuis le raster fourni et approuvé par le propriétaire, empreinte SHA-256 :
`e4aac9d59f75a01e58cf6e46d70d323432bda5b5aa32bd54a625f484421bc546`.

**Limite explicite :** ce traçage simplifie les micro-dégradés, les reflets et des bords de l'original. Il ne remplace ni les PNG maîtres existants ni une reconstruction vectorielle manuelle validée. Les SVG de fond sombre éclaircissent le vert sans modifier les contours. Le logo source raster et les PNG 15 variantes existent dans le dossier de livraison créatif mais **ne sont pas inclus dans ce commit** : leur export binaire doit être importé et validé séparément avant production.

## Utilisation prévue

```html
<link rel="stylesheet" href="/branding/zamurek-theme.css">
<div data-zamurek-theme="light">
  <img src="/branding/assets/zamurek-horizontal-light.svg" alt="Zamurek">
</div>
<div data-zamurek-theme="dark">
  <img src="/branding/assets/zamurek-horizontal-dark.svg" alt="Zamurek">
</div>
```

- Conserver les proportions, espaces intérieurs et contreformes de l'icône et des glyphes.
- Sur les fonds clair et sombre, utiliser le traitement correspondant.
- Monochromes : vert sur blanc, blanc sur fond sombre, noir pour les techniques d'impression.
- Ne pas substituer une nouvelle police au mot-symbole approuvé.
- Pas de gradients inventés sur les éléments UI. Les accents orange/magenta sont réservés aux usages voulus.
- L'application effective de la charte aux écrans reste **à réaliser avec Figma** ; les tokens sémantiques de surface sont des valeurs initiales à confirmer par tests de contraste, notamment pour des tailles réduites.

## À terminer pour la production

1. Importer dans GitHub les **PNG approuvés** (et sauvegarder le raster original), contrôler leurs hashes et transparences ; conserver les fichiers originaux de référence.
2. Vectoriser **nativement et précisément** les dégradés du logo tricolore, avec revue visuelle stricte face au PNG.
3. Vérifier contraste, réduction 16–48 px, zones de protection, tailles minimales et tests sur écran/print.
4. Produire et vérifier de véritables ressources Android adaptive/maskable, iOS, PWA, favicon et impression.
5. Dans Figma : composants, grilles, typographie UI, écran clair/sombre, états interaction, design tokens et accessibilité.
6. Faire approuver la version finale avant diffusion sur supports physiques/commerciaux.

## Contrôle

```bash
python3 scripts/validate_branding.py
```
