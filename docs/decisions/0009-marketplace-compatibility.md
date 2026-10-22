# ADR-0009 — Marketplace additive et opt-in

**Statut : adopté avec précision par [ADR-0021](0021-organization-establishment-venue.md) : découverte Venue OBLIGATOIRE en V1 ; marketplace de paiement collectif hors V1 | Date : 2026-10-22**

## Décision
Prévoir IDs globaux et contrats indépendants des canaux. La marketplace future consomme les mêmes API et un index public opt-in ; les apps white-label continuent à opérer. Checkouts mono-tenant jusqu'à décision spécifique.

## Alternatives
Fusionner DBs tenant ou migrer tous les clients vers une application unique.

## Conséquences
Source de vérité par boutique, coûts d'indexation eventual-consistency, consentement et versionnement indispensables. Aucune marketplace construite en V1.

## Révision
Tests d'index et exigences de parcours multi-commerçant.

