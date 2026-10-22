# packages/agentic — contrats clients des tools ZAMUREK

**Le Runtime IA est partagé et propriétaire de Monarque Connect**, pas implémenté ici. Les événements, modèle gateway, quotas, mémoires, 정책/permissions, approvals et agent runs réels appartiennent au backend Core privé.

Ce package ZAMUREK n'a vocation qu'à contenir des **types clients générés** depuis les contrats Core, fixtures de tests et définitions d'outils sectoriels sans privilèges (catalogue, FAQ, planning, rapports), versionnés avec le SHA contractuel de Monarque Connect. Ne pas créer de `ToolExecutor`, `ModelGateway`, outbox ou stockage mémoire indépendant.

Les contrats locaux dans `packages/contracts/agent-tools` et `events` sont **PRE-CONVERGENCE DRAFT**, à aligner/générer depuis le Core. Toute opération financière, publication, changement de prix ou mouvement caisse suit A3 approval/permissions et commands métier Core.

Voir [Agentique commune](../../docs/v1/AGENTIC-KERNEL.md) et [ADR-0024](../../docs/decisions/0024-shared-monarque-core-zamurek.md).
