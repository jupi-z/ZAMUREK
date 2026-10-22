# ZAMUREK Agentic Fabric — package propriétaire planifié

**G0 : contrats et conception seulement, aucun runtime d'agents.**

Dès `0.1.0`, introduire domaine et types `AgentDefinition, ModelGateway, ToolDefinition, ToolExecution, PolicyDecision, MemoryScope, Approval, AgentRun, RunCheckpoint`, intégrés aux événements métier et aux use cases plutôt qu'aux seules interfaces chat.

- API `ModelGateway` provider-neutral, pas de clés dans clients Android/Windows.
- Every action: actor, tenant, establishment, object-level permission, consentement et classification de données ; budget/timeout/retries.
- Approval humaine liée au hash exact payload/action/version et durée limitée pour changement prix, FX, paiements, annulations et publications.
- Les tools appellent handlers/domain services qui exécutent **leur propre** validation, pas d'accès SQL illimité.
- Les documents ou messages clients sont **données non fiables** : protéger contre instruction injection, data exfiltration, role spoofing.
- Journal outbox, audit, stockage mémoire isolé, rétention et suppression, anti-corruption entre tenants.
- Aucun logiciel commerce/agentique tiers ne dicte l'orchestration métier. Composants techniques permissifs revus et approuvés.

Contrats JSON Schema de départ : [tool-definition](../contracts/agent-tools/tool-definition.schema.json) et [event-envelope](../contracts/events/event-envelope.schema.json). Ils doivent être étendus/validés en G1 par des tests stricts, pas considérés implémentation.

Référence : [architecture agentique](../../docs/v1/AGENTIC-KERNEL.md), [security](../../docs/v1/SECURITY-THREAT-MODEL.md).
