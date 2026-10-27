# Roadmap officielle ZAMUREK — dépendante du Core Monarque Connect

**État Core au 27/10/2026 :** C0 accepté et clos; C1.1–C1.4 sont livrés sur `main@8546236d2afa849c16ab1c2d6a953934212d08d8` ([preuves C1](https://github.com/jupi-z/Monarque-Connect/blob/main/Docs/118_C1_CLOSURE_EVIDENCE.md)). C1 fournit le registre et les entitlements internes multi-produits; aucun endpoint transactionnel ZAMUREK ni contrat externe allowlisté n'est encore livré.

**Séquence 0.1.0 selon D-09 :** cadrage produit avant stabilisation; SDK et tests contractuels après stabilisation des contrats Core nécessaires; intégration réelle des parcours uniquement après livraison de leurs opérations Core. Voir [calendrier croisé](v1/INTEGRATION-ROADMAP.md), [ADR-0024](decisions/0024-shared-monarque-core-zamurek.md). Aucun prix ZAMUREK n'est activé par cette roadmap.

- **0.1.0** Clients Android/Windows, SDK/contrats Core, identité/tenant/établissement, intégration prouvée (PAS nouveau backend).
- **0.2.0** Catalogues produits/poids, prix USD/CDF Core, commandes en ligne et POS physique : cash, monnaie, session, reçus/factures imprimés (requiert Core C4/C5).
- **0.3.0** Restaurant/pizzeria, cuisine, tables et commandes sur place/à distance.
- **0.4.0** Prestations et rendez-vous salon, ressources, staff et concurrence.
- **0.5.0** Mobilier/devis et réparations avec consentement.
- **0.6.0** Produits pharmaceutiques autorisés/fail-closed et venue/mall opt-in.
- **0.7.0** Trois assistants IA via AI Gateway/Agent Runtime commun **Monarque Connect 10B/11.5**.
- **0.8.0** Tous les clients installables Android/Windows, marque, tests périphériques.
- **0.9.0** Tests inter-produits, sécurité, licences, restauration logique, fiscalité, performances.
- **1.0.0** Une seule ouverture commerciale **V1 complète**, 43 capacités et P0/P1 prouvées, aucune dépendance juridique fictivement validée.

Voir [gates détaillés](v1/RELEASE-GATES.md), [matrix](v1/CAPABILITY-MATRIX.md) et [nouveau prompt Codex](v1/CODEX-INTEGRATION-PROMPT.md). Aucun stade n'est considéré implémenté par la présence de documents.
