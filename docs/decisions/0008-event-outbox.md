# ADR-0008 — Outbox transactionnelle, activation progressive

**Statut : adopté comme pattern d'évolution | Date : 2026-10-15**

## Décision
Les événements métier destinés à quitter la DB tenant passent par une table outbox écrite dans la transaction locale. Consommateurs idempotents ; retry et replay explicites. Ni Kafka ni broker requis pour G0/G1.

## Alternatives
Publication réseau synchrone après commit (perte d'événements) ; transaction distribuée (complexité excessive).

## Conséquences
Cohérence éventuelle et gestion des doublons ; surveillance backlog nécessaire. Publication/rebuild du catalogue marketplace s'appuiera sur ce pattern.

## Révision
Besoins de débit, latence et ordre mesurés.

