# apps/api — EMPLACEMENT HISTORIQUE, backend séparé ABANDONNÉ

**Ne pas implémenter de NestJS/Prisma/backend commercial dans ce dossier.** Décision [ADR-0024](../../docs/decisions/0024-shared-monarque-core-zamurek.md) : Monarque Connect privé est l'unique API et Core transactionnel. Le dépôt ZAMUREK ne porte pas de second registre, DB par tenant, duplicata de SalesOrder/Invoice/PaymentRecord/CashMovement, Billing ni runtime agents.

Les extensions restaurant, appointment, repair, POS, venue qui nécessitent transaction/permissions s'implémentent en **modules dédiés dans le backend Monarque Connect privé**. Les adaptateurs clients/types OpenAPI et tests contractuels résident plutôt dans `packages/contracts` / clients ZAMUREK.

Ne pas lancer l'ancien prompt autonome G1. Lire [intégration](../../docs/v1/SHARED-CORE-INTEGRATION.md) et [nouveau prompt](../../docs/v1/CODEX-INTEGRATION-PROMPT.md). Conserver ce fichier comme trace explicite du pivot, puis supprimer ce placeholder seulement si ADR le permet.
