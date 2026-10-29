# ZAMUREK Matière — Revue couleur / relief V1.3

## Périmètre et méthode

- Référence : archive V1.2 et ses **288 icônes monochromes corrigées**.
- **288 variantes couleur** examinées visuellement sur planches, comparées par rendu optique et structure SVG à la géométrie monochrome V1.2.
- Géométrie principale redessinée depuis la monochromie pour 8 icônes : `services`, `fauteuil`, `meubles`, `reparation-attente`, `reparation-terminee`, `connexion`, `changer-mot-de-passe`, `outils-ia`.
- Les badges ronds sont isolés au moyen de découpes **vectorielles transparentes**, en conservant les formes et dégradés du badge.
- Le relief est préservé, l'ombre est légèrement atténuée pour éviter les halos à 24 px.
- Couleurs officielles inchangées : `#005C45`, `#FF8A1E`, `#D21868`.
- Les 288 fichiers monochromes sont **identiques octet par octet** à la V1.2.

## Modifications mesurables

| Opération | Quantité |
|---|---:|
| SVG couleur contrôlés | 288 |
| Silhouettes de référence monochrome transposées en couleur | 8 |
| Séparations transparentes badge / corps | 116 |
| Ajustements d'ombre / papier sur couleur | 288 |
| SVG couleur de sortie | 288 |
| SVG monochromes conservés | 288 |

## Contrôles et limites

**Contrôles exécutés :** 576 SVG parsables, 1728 rendus multi-tailles, 116 badges découplés ; sprites de 288 symboles chacun, 288 monochromes SHA-256 inchangés. Un validateur local vérifie les 576 documents SVG, les IDs d'icônes, les références de peinture, le rendu multi-tailles, la transparence et la cohérence des sprites. Les contrôles ne prouvent pas à eux seuls l'absence de toute ambiguïté sémantique ou de défaut perceptif : une inspection humaine écran par écran et à différentes tailles reste nécessaire.

### Fichiers

- `svg/couleur/` : nouvelles versions V1.3.
- `svg/interface/` : monochromes V1.2 identiques.
- `sprites/` : générés depuis les masters individuels.
- `manifest.json` et `design-tokens.json` : mis à jour.
- `ZAMUREK_Atelier_Audit_Icones_V1_3.html` : recherche et comparaison des 576 SVG directement dans le HTML autonome.
