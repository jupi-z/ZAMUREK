# Zamurek — Illustrations System (préproduction V2)

**Production vectorielle réalisée, validation artistique encore requise.**

La bibliothèque répond aux **275 contextes d’usage** du backlog officiel via **33 compositions maîtresses réutilisables**. Les 3 pilotes initiaux ont été conservés, sans réécriture.

| Livrable | Nombre |
|---|---:|
| Familles de compositions | 33 |
| Variantes des masters (clair / sombre × fixe / animé) | 132 |
| Contextes couverts `ZIL-001` → `ZIL-275` | 275 |
| Variantes SVG des contextes | 1 100 |
| Nouveaux fichiers SVG des contextes | 1 088 |
| SVG pilotes conservés | 12 |
| Poses Humaaans conservées comme sources | 8 |
| Composants IRA Design conservés comme sources | 4 |

## Prévisualisation

**`ZAMUREK_ILLUSTRATIONS_STUDIO_33_FAMILLES.html`** est un fichier HTML autonome avec tous les SVG compressés et incorporés. Ouvrir dans un navigateur récent avec `DecompressionStream('gzip')` (Chrome, Edge, Firefox récents). Recherche par ID ou libellé, filtres famille/priorité, clair/sombre, statique/animé, réduction des mouvements, export individuel SVG et pagination.

Le HTML de la première vague de 3 pilotes reste disponible : `ZAMUREK_STUDIO_SVG_AUTONOME.html`.

## Structure

- `third_party/humaaans/` — SVG sources Humaaans importés.
- `third_party/ira/` — SVG sources IRA Design importés.
- `assets/masters/BASE-*/` — 33 masters × 4 déclinaisons.
- `assets/static/` — 275 × 2 SVG, fonds transparents.
- `assets/motion/` — 275 × 2 SVG, animations non infinies et option réduction de mouvement.
- `registry/illustrations.production.v2.json` et `.csv` — mapping précis des 275 cas et états de revue.
- `reports/illustrations-v2-production.json` et `illustrations-v2-qa.md` — résultats de fabrication.
- `scripts/build_full_library.py` — générateur déterministe, sans dépendances Python externes.
- `THIRD_PARTY_NOTICES.md` et `THIRD_PARTY_LICENSES.md` — provenance, obligations de licence.

## Régénération

Depuis la racine du dépôt :

```bash
python3 packages/illustrations/scripts/build_full_library.py
python3 scripts/validate_illustrations_pilots.py
```

La génération vérifie les SVG avec `ElementTree` : racine et géométrie, identifiants uniques et liens internes, absence de balise image ou script, syntaxe des couleurs. Les contrôles de production GitHub Actions sont définis dans `.github/workflows/illustrations-pilots.yml`.

## Limites et acceptation

Les visuels sont **en état `REVUE_VISUELLE_REQUISE`**, pas `Acceptée`. Les 275 demandes réutilisent les masters et des repères contextuels ; elles ne représentent pas 275 compositions totalement distinctes dessinées manuellement. Les contrôles automatiques ne remplacent pas l'évaluation graphique et mobile à 128 / 192 / 320 px, la validation des états métier, des contrastes, de la performance ou la revue juridique.

Pour les confirmations de paiement, la pharmacie, la caisse et les autorisations, l’application doit conditionner l’affichage au statut réel validé dans le système. Une illustration n'est jamais une source de vérité métier. Le registre officiel de planification `docs/design/illustrations/ZAMUREK_Illustrations_Registry_V1.json` reste intact.

Le travail réutilise Humaaans et IRA Design ; les dérivés ne doivent pas être présentés comme entièrement exclusifs.
