# ADR-0006 — Encaissement direct par les commerçants

**Statut : PROPOSÉ (non validé commercialement) | Date : 2026-10-15**

## Décision proposée
Chaque marchand encaisse sur ses propres moyens de paiement ; xShop ne collecte pas et ne répartit pas les fonds en V1. Modes PAY_ON_DELIVERY / MANUAL_TRANSFER prévus avant PSP électronique.

## Alternatives
Plateforme encaisse et reverse ; impose besoins de conformité, comptabilité, litiges et intégration PSP différents.

## Conséquences
Moins de complexité de flux financier dans le logiciel, mais les marchands doivent gérer leur encaissement et ses preuves. Les responsabilités légales et les contrats PSP restent à vérifier localement.

## Validation requise
Acceptation du modèle commercial, évaluation des PSP accessibles aux commerçants visés, politiques de remboursement et de rapprochement.

