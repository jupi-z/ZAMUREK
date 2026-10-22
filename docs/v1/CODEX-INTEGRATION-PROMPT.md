# Nouveau prompt Codex ZAMUREK — client/intégration, PAS nouveau backend

**Statut : document de démarrage conditionnel.** La **première session de développement** doit se dérouler **dans Monarque Connect privé pour la phase 10A.5**, pas dans ZAMUREK. Ce prompt devient applicable **après** stabilisation/test des contrats C0–C3/C6/C7 du Core.

## Prompt à copier dans Codex (clone ZAMUREK ouvert)

```text
Tu es chargé de développer les applications et intégrations ZAMUREK du dépôt https://github.com/jupi-z/ZAMUREK déjà cloné et ouvert dans ton environnement.

IMPORTANT : ZAMUREK est un PRODUIT commercial omnicanal propriétaire dont le backend canonique est MONARQUE CONNECT, dépôt privé https://github.com/jupi-z/Monarque-Connect. Ne recrée PAS de second backend NestJS/Prisma, aucun registry, base PostgreSQL dédiée par commerçant, moteur indépendant Sales/Invoices/Payments/Cash/Billing ni second Agentic Fabric. Avant de travailler, vérifie que le Core phase 10A.5 a stabilisé C0–C3/C6/C7, donne les SHA des contrats API; à défaut, réalise seulement les parties clients/contrats synthétiques sans prétendre que les ventes fonctionnent et marque l'intégration BLOCKED.

Lis intégralement docs/decisions/0024-shared-monarque-core-zamurek.md, docs/v1/SHARED-CORE-INTEGRATION.md, docs/v1/POS-AND-FISCAL-DOCUMENTS.md, docs/v1/INTEGRATION-ROADMAP.md, docs/v1/PHASE-0.1.0-ACCEPTANCE.md, docs/v1/PRODUCT-CHARTER.md, docs/v1/CAPABILITY-MATRIX.md, docs/v1/RELEASE-GATES.md, docs/v1/AGENTIC-KERNEL.md, docs/v1/QUALITY-REQUIREMENTS.md, spec/v1/capabilities.json et spec/v1/progress-template.json.

Commence par l'inventaire Git/CI, compare chaque fichier hérité à la nouvelle décision, puis planifie une phase 0.1.0 de CLIENTS, SDK/contrats et connexions Core réelles sur scénarios synthétiques. Maintiens UI embarquées React/Capacitor Android avec Kotlin natif, Windows Tauri/Rust, aucun frontend web de production ni secrets serveur dans les clients. Les nouvelles spécialités commerce, restaurant, service, etc. devront ultérieurement utiliser commandes/API du Core, pas réinventer transactions.

POS V1 : terminal, caissier, session, vente walk-in sans e-mail client, cash, rendu monnaie, clôture/écarts, ticket thermique/A4 et fiscalisation réglementaire selon obligations prouvées, **backend dans Core**. Une vente cash confirme commande+payment+cash movement+outbox une seule fois. Ne simule pas fiscalisation DGI. Une venue opt-in ne voit jamais historique financier de ses magasins.

Crée docs/implementation/PROGRESS.json et rapport selon preuves vérifiées. Pour chaque tâche : planned/implemented/tested/accepted/blocked + % exact de la phase et progression totale pondérée, tests/exit codes/CI/commit et next action. Teste vraie identité/Core/tenancy à travers API; un mock UI n'est pas PASS financier. Aucun push de secrets/code métier propriétaire dans dépôt public ; PR, pas direct main ; pas de déploiement production ni utilisation marque LaJoie Mall sans accord.

Ne marque pas 0.1.0 ou 1.0.0 complete si APIs Core manquantes, SDK Android/Windows non compilés, sécurité et tests inconnus. Continue les tâches indépendantes, signale blocages externes avec preuve. Commence par l'audit du clone et la vérification des contrats Core disponibles.
```

**Référence de phase Core préalable** : `Docs/113_CODEX_PHASE_10A5_FIRST_PROMPT.md` du dépôt privé Monarque Connect. Aucun code/back-end privé ne doit être copié dans le dépôt public pour faciliter le handoff.
