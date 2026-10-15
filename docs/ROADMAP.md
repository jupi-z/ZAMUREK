# Feuille de route xShop

Les jalons sont **conditionnés par leurs critères de sortie**, pas par des délais arbitraires. Aucun pourcentage d'avancement fictif.

| Jalon | Livrables | Gate |
|---|---|---|
| G0 — Fondation documentaire | Specs, ADR, contrat API, arborescence, check documentation | [G0](quality/ACCEPTANCE.md) |
| G1 — Backend & tenants exécutables | API NestJS, registre, 2 DB provisionnées, migrations, admin minimale | G1 |
| G2 — Commerce API | Produits, panier, commande, retrait/livraison, paiement manuel, suivi | G2 |
| G3 — Expérience client + marchand | Android React/Capacitor/Kotlin, console, build marque A et B | G3 |
| G4 — Pilote réel contrôlé | Tests, sécurité, sauvegardes, déploiement, distribution validée | G4 |
| G5 — Multiplication boutiques | Génération configurable, CI/CD, monitoring et maintenance multi-app | G5 |
| Après G5 — Marketplace | Catalogue central opt-in, discovery, commandes mono-boutique | Nouveau PRD/ADR |

## Ordre d'exécution proposé
1. G0 : stabiliser décisions, valider notre modèle de commande / paiement.
2. G1 : contrat API et modèle tenant avant UI sophistiquée.
3. G2 : backend commande atomique et admin simplifiée.
4. G3 : relier premier client Android, tester deux marques isolées.
5. G4/G5 : pilote et industrialisation, sans précipiter les PSP ni marketplace.

## Première tranche de tickets G1
- Repository setup, toolchain, CI.
- Registry DB schema + migrations.
- Tenant provisioning saga/steps and test fixture.
- Tenant resolver + membership guards.
- Tenant DB client manager with bounded connections.
- OpenAPI validation and generated type contracts.
- Android Vite/Capacitor skeleton and minimal Kotlin bridge.
- Basic back-office login & health dashboards.
- Isolation integration tests A/B.

