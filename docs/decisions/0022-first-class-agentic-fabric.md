# ADR-0022 — Agentic Fabric fondatrice et propriétaire

**Statut ADOPTÉ — 2026-10-22**

Dès `0.1.0`, intégrer les fondations : événements de domaine, registre d'outils typés, actor/context/tenant scopes, policy decision point indépendant du LLM, approbations, workflow checkpoints, modèle et mémoire tenant scellés. À `0.7.0`, délivrer runtime durable, interop modèles interchangeables, trois assistants réels et redteam. Le modèle n'est jamais autorité commerciale ou sécurité.

Règles : disponibilité commerce sans modèle, zéro accès inter-tenant, trace des actions, outils à schéma strict et approval sensible. Approvals hashées/expirantes non réutilisables sur autre payload. Aucune exécution médicale réglementée, aucune action financière autonome.

Réutiliser uniquement composants techniques permissifs audités ; orchestrateur et policies ZAMUREK propriétaires. Voir [noyau agentique](../v1/AGENTIC-KERNEL.md) et [policy OSS](../governance/OPEN-SOURCE-POLICY.md).
