# ZAMUREK — Reconciliation Figma et SVG natifs V2

Date: 2026-10-29. Code source: packages/branding/assets/.
Le dépôt GitHub possède les quinze masters SVG natifs, mais la publication dans Figma est une opération distincte.

**État Figma (29/10/2026) :** le fichier Design Q5VQfVbvjmRaqFIhHGjVwQ existe et possède des variables, une planche de marque et des premiers composants. L'outil MCP Figma Starter a renvoyé `tool call limit` lors de la tentative d'accès visant à remplacer les anciens SVG. Aucune mutation Figma n'a été réalisée dans ce lot. Il faut actualiser le brandboard et les composants depuis les SVG GitHub quand le quota le permettra.

## Reprise contrôlée
1. Ouvrir https://www.figma.com/design/Q5VQfVbvjmRaqFIhHGjVwQ
2. Depuis `main/packages/branding/assets`, importer les six variantes tricolores `horizontal/vertical/icon × light/dark` en vecteurs éditables; utiliser les trois autres traitements pour les exemples monochromes.
3. Remplacer les anciens calques du board plutôt que de redessiner la silhouette. Vérifier la typographie et les dégradés visuellement à 100 % et à petite taille.
4. Garder les couleurs primitives / sémantiques déjà ajoutées, l'arrière-plan blanc pour clair et obsidienne pour sombre.
5. Mettre en place des composants de marque LogoLockup (orientation, thème) et IconMark (thème, monochrome), puis les employer par **instances** dans les futurs écrans.
6. Capturer et comparer un écran de jour et un écran sombre, et confirmer la synchronisation Figma avant de clore la tâche.

Cela ne modifie ni l'architecture de Monarque Connect ni les 43 capacités ZAMUREK V1.
