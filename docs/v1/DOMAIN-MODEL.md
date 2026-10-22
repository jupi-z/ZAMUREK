# ZAMUREK — modèles spécialisés sur le Core commun Monarque Connect

**Normatif V1 après ADR-0024 (22/10/2026) ; modèles planifiés et non implémentés.** L'ancien « registry + 1 DB métier PostgreSQL par tenant » est **remplacé** par l'isolation logique PostgreSQL actuelle du Core Monarque Connect (organizationId + establishmentId + ownership). Lire [décision](../decisions/0024-shared-monarque-core-zamurek.md) et [architecture d'intégration](SHARED-CORE-INTEGRATION.md).

## Agrégats canoniques du Core (ne jamais dupliquer)
- Identity : `User`, buyer verified email, `Membership`, `Organization`, `Establishment`, `OrganizationEntitlement`, ProductPlan/Subscription, staff MFA.
- Commerce : `Item`, price policy, units, `SalesOrder`, `Invoice`, `PaymentRecord`, `CashAccount`, `CashMovement`, refund/reversal, document serialisation, tenant fiscal status.
- Intelligence : audit, `DomainEvent/Outbox`, `ModelGateway`, `ToolRegistry`, `AgentRun`, `Approval`, tenant-aware knowledge.
- L'instance Core contient les données canoniques des organisations utilisant Monarque Connect, ZAMUREK ou les deux. Pas de mirroring des commandes ni de second Prisma service financier ZAMUREK.

## Domaines supplémentaires (modules backend dédiés dans le Core privé)
| Module | Agrégats propres | Lien avec Core |
|---|---|---|
| Channels & Merchant Offerings | `SalesChannel`, `OfferingRevision`, variant/attribute/media, availability, `PriceQuoteVersion` | `Item`, org/establishment, sales order |
| POS | `PosTerminal`, `CashSession`, `CashierAssignment`, `SaleTender`, `CashReconciliation`, `CommercialPrintJob` | SalesOrder + PaymentRecord + CashMovement transaction unique |
| Weighted Commerce | `UnitDefinition`, `WeightPolicy`, `MeasuredQuantity`, tare/finalized weight | core price policy/quote version |
| Restaurant | `Menu`, `ModifierGroup`, `KitchenTicket`, `Table`, `TableReservation` | canonical Order and table slot locks |
| Service Booking | `StaffResource`, `WorkCalendar`, `Hold`, `Appointment`, `NoShow` | canonical order/quote, staff membership |
| Furniture | `CustomOption`, `MerchantEstimate`, `SpecialDelivery` | quote approved → canonical order |
| Repair | `RepairCase`, `DeviceRef`, `Consent`, `Diagnostic`, `WorkOrder`, `Handover` | quote/payment canonical, PII restricted |
| Regulated goods | legal `ProductClassification`, `MerchantLicenseStatus`, lot/expiration | catalog+checkout policy fail-closed |
| Venue | `Venue`, `Floor`, `Unit`, `VenueMembership`, public listing projection | opt-in org, no cross-tenant orders/PII |

## Monnaie, poids et devis
Prix source USD pour **les offres ZAMUREK**, version FX du marchand, monnaie documentaire publique CDF RDC sous revue légale ; laisser inchangées les organisations Monarque Connect existantes dont `defaultCurrency` diffère. Quote serveur snapshot `amountUsd/sourceRevision/rateVersion/taxPolicy/roundingPolicy/finalCdf/expiresAt`. La règle de calcul exacte est [CDF_LINE_HALF_UP_V1](MONETARY-AND-QUANTITY-POLICY.md), sans float. Quantités vente au poids exactes, 125 g de 20 USD/kg × 2360 = 5900 CDF.

## Transaction POS unique
`PlacePosOrder` valide caissier + terminal + session ouverte + entitlement + stock/disponibilité + quote → écrit **dans transaction DB Core** : `SalesOrder(origin=POS)`, `PaymentRecord` pour fonds effectivement reçus, `CashMovement` pour cash, marque idempotency, outbox. Échec de l'un = rollback de tous, retry identique = même résultat. L'impression peut échouer **après** validation de la vente : réimprimer document versionné sans nouveau paiement. `BusinessParty` du buyer n'est pas obligatoire pour `WALK_IN` ; pas de faux e-mail. Une vente online exige e-mail vérifié mais pas staff membership.

## Tenancy, partitions de droits et restauration
Chaque agrégat Core/external product est rattaché à `organizationId`; les données établissement ont `establishmentId` et les lignes sensibles nécessitent validation ownership. Implémentation centrale garde-fou, tests BOLA/T1→T2, E1→E2, customer C1→C2, venue→payment, agent→other tenant. PostgreSQL partagé = isolation logique testée ; backups/export/restauration ciblés par organisation demandent solutions explicites (ne pas supposer restauration physique simple).

## Event Fabric et Agentic Runtime
L'enveloppe Event Fabric et les tool policies sont **canoniques chez Monarque Connect**. Les documents JSON Schema locaux ZAMUREK sont des **brouillons de compatibilité** en attendant contrats partagés versions ; ne pas déployer un deuxième event bus ni un second agent runner. Les assistants public/merchant utilisent policy, approval et MemoryScope communs.

## Évolution du schéma
Migrations additives et compatible anciennes opérations Monarque Connect, changement de devise jamais rétroactif, contraintes de non-chevauchement booking et index lisibles venue sous consentement. Hors V1 : multi-merchant settlement, paiement automatisé marketplace, POS offline, prescription médicale non autorisée.
