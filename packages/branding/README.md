# ZAMUREK — système de marque, masters vectoriels V2

**Référence officielle :** 15 masters SVG natifs (3 compositions × 5 traitements), en fonds transparents. Depuis le 29 octobre 2026, ces fichiers remplacent les tracés provisoires.
Le logo conserve le symbole approuvé par le propriétaire et le mot-symbole épais **Zamurek**.

## Charte

- Vert forêt principal : `#005C45`
- Orange secondaire : `#FF8A1E`
- Magenta accent : `#D21868`
- Fond clair majoritaire : `#FFFFFF`
- Fond sombre majoritaire : `#111318` (obsidienne)
- Style UI plat, peu d'effets, aucun réinterprétation du symbole. Référence brandboard : Concept 01.

## Organisation des ressources

- `assets/zamurek-{horizontal,vertical,icon}-{light,dark,green,white,black}.svg` : **15 sources SVG natives**.
- `tokens/zamurek.tokens.json` : primitives/sémantiques.
- `styles/zamurek-theme.css` : variables CSS réutilisables.
- `manifest.json` : correspondance entre 15 fichiers, origine et traitements.
- `scripts/validate_branding.py` : XML, intégrité des tracés, palette, contraste vert/blanc/obsidienne.

Les modes `light` et `dark` correspondent aux **fichiers tricolores destinés aux fonds respectifs**. Ils ne contiennent pas de fond incorporé ; le fond est fourni par l'application. Les gradations du vert sont des traitements du vert de marque, sans changer les chemins. Le vert plus clair du logo sombre n'est pas une nouvelle couleur principale de l'identité.

## Fidélité et provenance

Les 15 SVG proviennent de l'archive utilisateur `Zamurek_Collection_Full_SVG.zip`, déposée le 29 octobre 2026. Tous les tracés et `viewBox` sont conservés. Pour les six versions tricolores, les arrêts des gradients verts ont été recalibrés afin de garantir une meilleure cohérence sur blanc et une meilleure lisibilité sur obsidienne. Les formes des caractères et de l'icône **ne sont pas réinventées**.
L'archive originale reste une référence d'entrée du travail créatif ; elle n'est pas distribuée automatiquement avec ce dépôt.

## Fichiers à utiliser

| Usage | Fichier |
|---|---|
| Header sur blanc | `assets/zamurek-horizontal-light.svg` |
| Header sur obsidienne | `assets/zamurek-horizontal-dark.svg` |
| Signature verticale claire | `assets/zamurek-vertical-light.svg` |
| Signature verticale sombre | `assets/zamurek-vertical-dark.svg` |
| Icône claire | `assets/zamurek-icon-light.svg` |
| Icône sombre | `assets/zamurek-icon-dark.svg` |
| Impresssion monochrome | `assets/zamurek-*-green.svg`, `*-white.svg`, `*-black.svg` |

`light`/`dark` ne sont pas interchangeables sur les fonds opposés. L'icône de petite taille demande un contrôle de reconnaissance et une exportation adaptée à chaque plateforme (PWA/Android/iOS), avant publication. La vectorisation native ne remplace pas ces exports.

## Figma

Fichier de travail : https://www.figma.com/design/Q5VQfVbvjmRaqFIhHGjVwQ

L'import direct des nouveaux masters dans Figma est nécessaire pour remplacer les anciens contours présents dans le premier brandboard. Ne pas présenter les maquettes Figma existantes comme synchronisées avec cette V2 avant confirmation par capture.

## Contrôle

```bash
python3 scripts/validate_branding.py
```

Les animations, interfaces et flux commerciaux ne sont pas livrés par ce changement de branding.
