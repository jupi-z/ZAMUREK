# Nouveau prompt Codex ZAMUREK — client/intégration, PAS nouveau backend

**Statut : document de démarrage conditionnel.** Toute la séquence technique Monarque Connect (10A.5, 10B, 11, 11.5 et 12) doit être clôturée avec ses gates et une CI post-fusion verte avant toute session de code dans ZAMUREK. D'ici là, les travaux restent dans le dépôt Monarque Connect et les seules activités permises côté ZAMUREK sont la documentation normative et la revue de contrats inter-dépôts. C0–C3/C6/C7 gelés sont nécessaires à l'intégration mais ne constituent pas une autorisation anticipée de coder. **Le Core doit en outre avoir revu et adopté ses frontières sur des PR approuvées ; aucun mock ne peut valider une transaction réelle.**

## Prompt à copier dans Codex (clone ZAMUREK ouvert)

```text
Tu es chargé de développer les applications et intégrations ZAMUREK du dépôt https://github.com/jupi-z/ZAMUREK déjà cloné et ouvert dans ton environnement.

IMPORTANT : ZAMUREK est un PRODUIT commercial omnicanal propriétaire dont le backend canonique est MONARQUE CONNECT, dépôt privé https://github.com/jupi-z/Monarque-Connect. Ne recrée PAS de second backend NestJS/Prisma, aucun registry, base PostgreSQL dédiée par commerçant, moteur indépendant Sales/Invoices/Payments/Cash/Billing ni second Agentic Fabric. Avant de travailler dans le dépôt ZAMUREK, vérifie que Monarque Connect a terminé 10A.5, 10B, 11, 11.5 et 12, avec SHA de clôture et CI post-fusion verte, puis confirme les contrats API canoniques. Avant cette preuve, ne réalise aucun code client; seules les mises à jour documentaires et la revue de contrats sont permises, et l'intégration reste BLOCKED.

Lis intégralement docs/decisions/0024-shared-monarque-core-zamurek.md, docs/v1/SHARED-CORE-INTEGRATION.md, docs/v1/POS-AND-FISCAL-DOCUMENTS.md, docs/v1/INTEGRATION-ROADMAP.md, docs/v1/PHASE-0.1.0-ACCEPTANCE.md, docs/v1/PRODUCT-CHARTER.md, docs/v1/CAPABILITY-MATRIX.md, docs/v1/RELEASE-GATES.md, docs/v1/AGENTIC-KERNEL.md, docs/v1/QUALITY-REQUIREMENTS.md, spec/v1/capabilities.json et spec/v1/progress-template.json.

Commence par l'inventaire Git/CI, compare chaque fichier hérité à la nouvelle décision, puis planifie une phase 0.1.0 de CLIENTS, SDK/contrats et connexions Core réelles sur scénarios synthétiques. Maintiens UI embarquées React/Capacitor Android avec Kotlin natif, Windows Tauri/Rust, aucun frontend web de production ni secrets serveur dans les clients. Les nouvelles spécialités commerce, restaurant, service, etc. devront ultérieurement utiliser commandes/API du Core, pas réinventer transactions.

POS V1 : terminal, caissier, session, vente walk-in sans e-mail client, cash, rendu monnaie, clôture/écarts, ticket thermique/A4 et fiscalisation réglementaire selon obligations prouvées, **backend dans Core**. Une vente cash confirme **SalesOrder+Invoice canonique+PaymentRecord(invoiceId obligatoire)+CashMovement net+Outbox et stock** une seule fois par commande idempotente. Un reçu ou ticket n'est pas une facture fiscale homologuée ; le stockage doit être durable, pas seulement mémoire. Ne simule pas fiscalisation DGI. N'attribue pas de rôle ADMIN/FINANCE général aux caissiers ; respecte permissions POS par action/établissement/session. Conserve le contrat identité métier lors de l'intégration future OIDC/Monarque Auth. `TECH_PASS` n'est pas une autorisation commerciale. Une venue opt-in ne voit jamais historique financier de ses magasins.

Crée docs/implementation/PROGRESS.json et rapport selon preuves vérifiées. Pour chaque tâche : planned/implemented/tested/accepted/blocked + % exact de la phase et progression totale pondérée, tests/exit codes/CI/commit et next action. Teste vraie identité/Core/tenancy à travers API; un mock UI n'est pas PASS financier. Aucun push de secrets/code métier propriétaire dans dépôt public ; PR, pas direct main ; pas de déploiement production ni utilisation marque LaJoie Mall sans accord.

Ne marque pas 0.1.0 ou 1.0.0 complete si APIs Core manquantes, SDK Android/Windows non compilés, sécurité et tests inconnus. Continue les tâches indépendantes, signale blocages externes avec preuve. Commence par l'audit du clone et la vérification des contrats Core disponibles.
```

**Référence de phase Core préalable** : `Docs/113_CODEX_PHASE_10A5_FIRST_PROMPT.md` du dépôt privé Monarque Connect. Aucun code/back-end privé ne doit être copié dans le dépôt public pour faciliter le handoff.
