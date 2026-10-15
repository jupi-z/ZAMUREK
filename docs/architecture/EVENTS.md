# Outbox et événements métier — proposition d'extension maîtrisée

## Motivation
Synchroniser un jour catalogue marketplace, notifications, recherche, audit externe, sans coupler la transaction commande à des services distants.

## Pattern
Écrire une ligne outbox **dans la même transaction PostgreSQL tenant** que la modification métier. Worker lit par lot, publie vers destination, marque traité, retry/backoff ; DLQ logique ou statut terminal avec alertes. Les consommateurs doivent être **idempotents**.

## Événements candidats
product.published.v1, product.hidden.v1, product.updated.v1, order.placed.v1, order.status_changed.v1, payment.confirmed.v1, tenant.activated.v1 (registre central).

## Envelope
eventId UUID, eventType, schemaVersion, tenantId, aggregateId, occurredAt, correlationId, payload public/minimal. Éviter PII dans événements de catalogue ; jamais tokens, mots de passe, coordonnées de paiement.

## Précautions
At-least-once par défaut ; ordre garanti seulement là où conçu (clé aggregate, version) ; doublons et retards autorisés ; reprise et replay contrôlés. Pas d'infrastructure broker à déployer tant que le besoin n'est pas réel. Les writes métier n'attendent pas les consommateurs.

## Tests
Retry, publication deux fois, crash worker, événement obsolète, changement de version, suppression boutique et rattrapage de projection ; aucune fuite multi-tenant.

