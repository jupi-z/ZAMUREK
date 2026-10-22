# ZAMUREK — outbox et événements métier

**En vigueur pour la V1 dès 0.1.0**, et non une option reportée à une version ultérieure. Voir [noyau agentique](../v1/AGENTIC-KERNEL.md) et [event envelope](../../packages/contracts/events/event-envelope.schema.json).

Un événement est écrit dans la **même transaction PostgreSQL tenant** que la mutation métier ; les workers récupèrent/outbox avec backoff, circuit-breaker, dead-letter et consommateurs idempotents. Aucune promesse exactly-once inter-systèmes ; rejouabilité/versionnement et trace d'audit contrôlés.

Envelope : eventId, eventType et schemaVersion, organizationId, establishmentId éventuel, correlationId/causationId, occurredAt, classification, payloadRef. Payload tenant protégé par ACL ; aucun envoi d'informations privées au gestionnaire d'un centre commercial, à un autre tenant ou à un modèle IA non approuvé.

Événements V1 : `catalog.item.changed.v1`, `fx.rate.changed.v1`, `order.placed.v1`, `appointment.booked.v1`, `restaurant.kitchen.updated.v1`, `repair.case.updated.v1`, `venue.optin.revoked.v1`, `agent.run.requested.v1`, `agent.tool.approval.v1`. Un changement FX invalide les quotes non confirmées et régénère les projections publiques CDF, mais **ne modifie pas les commandes historiques**.

Tests obligatoires : transaction/outbox atomique, duplicate event delivery, replay, périmètre tenant, fusion de versions, crash worker et opt-out venue.
