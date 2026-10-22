# ZAMUREK — protocole Codex avec Core Monarque Connect partagé

**Statut : plan d'exécution, pas produit implémenté.** L'ancienne consigne de créer un backend ZAMUREK séparé est **REJETÉE** par [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md). Il faut **commencer dans le dépôt privé Monarque Connect**, phase [10A.5](https://github.com/jupi-z/Monarque-Connect/blob/planning/phase-10a5-zamurek-convergence/Docs/105_PHASE_10A5_CONVERGENCE_EXECUTION_SPEC.md), jusqu'au gel de contrats C0–C3/C6/C7 ; puis seulement démarrer ZAMUREK 0.1.0.

## Dossier obligatoire
[Charte](PRODUCT-CHARTER.md), [intégration](SHARED-CORE-INTEGRATION.md), [POS/fiscal](POS-AND-FISCAL-DOCUMENTS.md), [matrix 43](CAPABILITY-MATRIX.md), [parcours](BUSINESS-WORKFLOWS.md), [domaine](DOMAIN-MODEL.md), [IA](AGENTIC-KERNEL.md), [prix](MONETARY-AND-QUANTITY-POLICY.md), [contrat](TECHNICAL-CONTRACTS.md), [gates](RELEASE-GATES.md), [sécurité](SECURITY-THREAT-MODEL.md), [legal](LEGAL-REGULATED-GATES.md), [acceptation](PHASE-0.1.0-ACCEPTANCE.md), [manifest](../../spec/v1/capabilities.json), [progrès](../../spec/v1/progress-template.json), [nouveau prompt](CODEX-INTEGRATION-PROMPT.md).

## Règles absolues
- Core unique **Monarque Connect** : un moteur d'identité, organisations, établissements, Item, commandes SalesOrder, Invoice, PaymentRecord, CashAccount/CashMovement, abonnements et AI Gateway/Agent Runtime. **Ne pas reconstruire un monolithe NestJS/Prisma ZAMUREK ni DB par commerçant.**
- Implémentations backend spécialisées (POS, réservation, cuisine, venue, réparations) qui nécessitent transactions communes résident dans **Monarque Connect privé**. Dans ZAMUREK : APK et EXE/MSI, UX, bridges d'imprimantes Kotlin/Rust, contrats clients et tests E2E.
- **POS physique complet V1** : client walk-in sans compte/e-mail, caissier identifié, session/terminal, espèces, monnaie, clôture, tickets 58/80 et factures A4 ; toute vente produit order/payment/cash/outbox atomiques, fiscalisation authentique selon droit applicable, jamais faux QR DGI.
- Transaction online requiert buyer e-mail vérifié; tenant/establishment/ownership, idempotency et scopes produits vérifiés serveur. Venue/public ne lit aucun compte privé.
- Source USD des offres ZAMUREK, CDF publique RDC selon juridique, snapshots immuables ; préserver les autres devises Monarque Connect.
- Une seule infrastructure agentique Core avec tools ZAMUREK et approbation humaine des actes financiers. Modèle indisponible ≠ commerce indisponible.
- Offre ZAMUREK BASIC 7 USD/mois organisation **cible commerciale**, quota établissements/coûts et conformité à valider, jamais déblocage implicite de FairScale Business.
- Aucun Mercur/Medusa/Saleor/Vendure, ERPNext/Frappe ni fork commerce prêt à l'emploi ; briques techniques seulement licences permissives vérifiées.
- Dépôt ZAMUREK **public** : aucun code transactionnel Core privé, secret, PII, token, clé de signature ou donnée réelle. Production API-only pour ces apps, aucun frontend web hébergé.
- Aucune marque/partenariat LaJoie Mall présumés. Pharmacie réglementée fail-closed.

## Procédure et progression
1. Auditer le clone local, le statut Git, l'OpenAPI canonical Core (commit + version), les schémas JSON et tous les docs ; enregistrer les écarts de la V1.
2. Créer `docs/implementation/PROGRESS.json` depuis `spec/v1/progress-template.json` avec **43 IDs obligatoires** ; commencer à 0 pour toutes les activités non testées.
3. Développer des lots atomiques ; après chaque lot test+contrat+CI+scopes/FX/sécurité, corriger erreurs et re-tester.
4. Montrer progression par jalon et globale pondérée sur résultats prouvés; `PLANNED/IMPLEMENTED/NOT_RUN/BLOCKED` = pas PASS.
5. Reproduire dans un environnement synthétique : T1/T2, E1/E2, POS walk-in, imprimante, commerce online, venue opt-in, droits produits, 3 assistants. Aucun mock seul ne suffit pour déclarer un moteur commerce opérationnel.
6. Générer rapport par version avec tests, commandes, exit codes, environnement, artefacts, version contrat Core et SHA. Ne pas annoncer 1.0.0 sans tous les P0/P1 et validations externes réelles.
7. Développement par branche/PR; pas de push direct main, pas d'accès VPS/DNS/paiements réels sans approbation.

## Séquence Codex
**Premier prompt effectif : Monarque Connect privé `Docs/113_CODEX_PHASE_10A5_FIRST_PROMPT.md`.** Ensuite [prompt d'intégration ZAMUREK](CODEX-INTEGRATION-PROMPT.md) après preuve de contrats C0–C3/C6/C7. **Ne jamais exécuter** [ancien prompt autonome ZAMUREK 0.1.0](CODEX-PHASE-0.1.0-PROMPT.md).
