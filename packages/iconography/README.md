# ZAMUREK Matière — Bibliothèque iconographique officielle V1.3

**Approuvée par le propriétaire le 29 octobre 2026.** Cette bibliothèque complète le système de marque de `packages/branding/` et couvre les interfaces acheteur, marchand, POS Android/Windows et les modules métiers documentés.

## Inventaire

- **288 pictogrammes canoniques**, chacun en **2 traitements SVG** = **576 fichiers SVG indépendants**.
- `svg/couleur/<id>.svg` : rendu de marque à dégradés/relief doux, notamment pour catégories et découvertes.
- `svg/interface/<id>.svg` : rendu monochrome en `currentColor`, notamment pour commandes UI.
- `sprites/zamurek-couleur.svg` et `sprites/zamurek-interface.svg` : 288 symboles par sprite.
- `manifest.json` : identifiants, catégories, alias, usages, correspondance avec les 43 capacités V1.
- `design-tokens.json` : grille et teintes de référence ; palette officielle principale dans `../branding/tokens/`.
- `Zamurek_Icones_Catalogue.html` et `ZAMUREK_Atelier_Audit_Icones_V1_3.html` : catalogues/inspecteurs HTML.
- `sources/` et `docs/` : code de génération, audit et documentation de référence.

## Règles d'utilisation

1. **N'utiliser que les sources V1.3 approuvées**. Ne pas réintroduire des SVG V1.0–V1.2.
2. La grille native est **96 × 96**. Icônes couleur : taille recommandée ≥48 px selon le détail ; interfaces monochromes : 24–32 px et libellés accessibles selon le contexte.
3. Monochrome : `currentColor` suit les tokens clair/sombre du contexte. Ne pas forcer le vert forêt sombre sur une interface obsidienne si le contraste est insuffisant.
4. Les badges de statut ne suffisent pas à transmettre une information métier : ajouter un texte ou un état accessible.
5. Les symboles `id` du sprite utilisent `zamurek-interface-<id>` ou `zamurek-couleur-<id>`.
6. Les visuels sont des ressources UI : leur existence n'implique pas qu'une fonctionnalité du Core Monarque Connect soit implémentée ou autorisée.
7. L'iconographie V1.3 a été validée visuellement par le propriétaire ; la validation de rendu à petite taille, de contraste et l'accessibilité complète doivent encore être contrôlées **dans les interfaces finales**.

## Vérification automatisée

```bash
python3 scripts/validate_iconography.py
npm run iconography:check
```

Les contrôles vérifient la structure XML, le nombre de fichiers, l'intégrité des références internes, les sprites, les alias et la couverture des 43 capacités. Ils ne remplacent pas l'audit d'ergonomie de chaque écran.

## Figma

Les assets sont versionnés comme référence officielle sur GitHub. Leur importation dans Figma, ainsi que la création de composants Figma réutilisables, feront l'objet d'une prochaine étape ; **aucune synchronisation Figma n'est revendiquée dans cette PR**.

## Provenance

Archive validée : `ZAMUREK_Icones_Matiere_Corrigees_V1_3.zip`, fournie et approuvée dans la conversation, sans sources externes incorporées aux SVG. Références de génération et rapports conservés dans `sources/` et `docs/`.
