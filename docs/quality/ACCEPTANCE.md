# Definition of Done et validation des jalons

## Done — toute fonctionnalité
Spécification et ADR cohérents, code review, migrations reproductibles, tests unitaires/intégration pertinents, erreurs/états UI, authz tenant, logs et audit sensible, documentation API/ops mise à jour, démonstration E2E, pas de secret commité.

## G0 — cadrage
- Monorepo documenté et arborescence réservée.
- PRD, fonctionnalités V1, schéma conceptuel, tenance, sécurité, bridge Android, marketplace, ADR et questions ouvertes.
- Contrat API initial consultable ; vérificateur documentaire disponible.
- Statut des composants honnête : non implémentés.

## G1 — fondation exécutable
- pnpm install + build API/admin + app React passent, projets natifs générés et build Android debug sur SDK documenté.
- PostgreSQL registry + provisioner + deux DB tenant migrés ; test d'isolation A/B en CI.
- Healthcheck tenant-scopé et création d'une boutique de test reproducible.

## G2 — backend commerce
- Produits/catégories, panier, checkout idempotent, livraison/retrait, paiements manuels, état commande, suivi invité et role merchant testés E2E.
- Test double soumission et capture de prix immuable.

## G3 — Android + administration
- App white-label pilotable de bout en bout, Kotlin réseau/cache/sécurité, UI React, marchand et plateforme administrables.
- Tests Android réel + tests de reprise réseau, permissions et deux builds à marques distinctes.

## G4 — pilote opérationnel
- Deux tenants distincts, restauration d'une seule DB vérifiée, monitoring, audit, configuration secrets, checklists Play Store / distribution, documentation support.
- Livraison électronique seulement si PSP et conformité validés.

## G5 — industrialisation
- Pipeline white-label reproductible, mise à jour sans casser l'ancien canal, migration N tenants, métriques/alertes et versionnement des clients.
- Pas de marketplace nécessaire pour atteindre G5.

## Preuve attendue
Un lien PR/commit, résultat CI ou test reproductible, traces anonymisées et checklist signée. Une simple présence de code n'est pas une preuve de Done.

