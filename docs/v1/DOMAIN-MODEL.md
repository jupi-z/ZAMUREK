# Domaine et frontières transactionnelles — ZAMUREK V1

## Bounded contexts propriétaires
| Contexte | Agrégat racine / invariants |
|---|---|
| Platform Registry | Organization, EstablishmentReference, Channel, VenueMembership, Subscription, FeaturePolicy ; registry **sans commandes tenant** |
| Global Identity | CustomerIdentity, VerifiedEmail, Session, StaffIdentity, MFA, TenantMembership, Operator ; suppression/rétention sous règles |
| Tenant Commerce | Establishment, Offering, Variant, Media, Category, UnitDefinition, PriceBasis, ModifierGroup, AvailabilityPolicy |
| Catalog & FX | USDBasePrice, TenantFxRateVersion, PriceQuote, CdfRoundingPolicy, TerritoryCurrencyPolicy |
| Ordering | Cart, Order, OrderLine, StatusHistory, Fulfillment, PaymentRecord, CancellationRequest, RefundRequest |
| Booking | Resource, StaffCalendar, Table, ServiceSlot, Appointment, Hold, Reschedule, NoShow |
| Restaurant | Menu, MenuItem, ChoiceSet, PreparationTicket, Station, DiningService |
| Quotes & Repair | Quote, QuoteLine, QuoteAcceptance, RepairCase, Diagnostic, Consent, DeviceRef, WorkOrder, Handover |
| Venue Discovery | Venue, Floor, Unit, TenantOptIn, PublicOfferingProjection, Revocation/IndexSync |
| AI Fabric | AgentProfile, ModelAdapter, ToolRegistry, ContextGrant, Run, Step, Approval, MemoryScope, Audit |
| Platform Ops | Provisioning, DBMigration, LicenseEntitlement, BillingCycle, Health, BackupRestoreJob |

## Data ownership
- **Registry DB** : organizations, venues, établissement metadata minimales, mappings tenant DB, app channel, memberships/auth global, abonnements. Venue public listing index minimal et consent flags. Aucun historique commercial personnel sauf éventuelle référence opaque d'agrégation consentie.
- **Une DB PostgreSQL métier par Organization** : établissements, catalogues, horaires, devis, commandes, réservations, paiements, services et journal métier. `establishmentId` partout où une donnée appartient à un établissement ; données partagées explicitement reliées à une organisation.
- Même organisation peut gérer plusieurs établissements, mais `tenantId` ne se substitue **jamais** au contrôle `establishmentId`, au rôle, ou à l'ownership acheteur. Deux personnes du même tenant n'ont pas nécessairement les mêmes droits.
- Multi-tenant marketplace : lecture de projections **publiques opt-in** contrôlées ; aucun join SQL à travers DB tenant en direct. Opérations clients toujours routées après contrôles ownership.

## Entités et identifiants
UUID/ULID non signifiante, numéro commercial local spécifique tenant/établissement ; aucune adresse/nom client dans events publics. `Offering.kind = PRODUCT | WEIGHTED_PRODUCT | PREPARED_FOOD | SCHEDULED_SERVICE | QUOTED_GOOD | REPAIR_SERVICE | REGULATED_GOOD`. `offeringCapability` non déduite naïvement de `kind` : validation module et droits pour chaque action.

## Inventaire et prix
**Ne pas confondre quantités vendues et stock physique**. `availability=AVAILABLE|UNAVAILABLE` est la source de commande V1 ; booking/table/capacité peut réserver une ressource/slot avec prévention de double booking. Définir `UnitDefinition` G, KG, PCS, HOUR, MINUTE, SERVICE, etc. via unité canonique et fraction exacte. **Pas de float monétaire ni masse** ; quantité interne en decimal exact (scale borné) ou entier de plus petite unité métier avec contrôle de précision. Variantes & prix de base USD (centimes), précisions par offre ; taxe/FX appliqués backend sur quote.
- Prix au poids `priceBaseUsdMinorPerUnit` + `unitBasis`, quantité mesurée exacte et taux FX → sous-total; arrondi final par étape documentée.
- `PriceQuote` inclut `fxRateVersion`, `currencyPolicyVersion`, `taxPolicyVersion`, `offeringRevisionIds`, `feeRevision`, `expiresAt` et empreinte de contenu ; **checkout refuse devis périmé**.
- Transactions doivent stocker snapshots de prix et des clauses en vigueur, non des pointeurs recalculés par le taux courant.

## Réservations et ressources
Stocker ressources et slots avec contraintes concurrency/DB uniques/exclusion applicables par établissement (ressource, intervalle temporel, statut bloquant), timezone locale IANA et timestamps UTC. Reprogrammer = transaction de libération/acquisition avec contrôle anti-chevauchement. Horaires exceptionnels, pauses, congés, staff habilités et capacité restaurant.

## Transactions et fiabilité
- Achat mono-merchant : transaction DB tenant entre ordre, lignes, paiement en attente, idempotency record, outbox et snapshot. Registry DB **n'intervient pas en transaction distribuée** au checkout.
- Booking : hold limité, expiration, confirmation atomique ressource/slot, annulation et compensations si ordre échoue.
- Vente en caisse : sale POS est une commande sous `origin=POS` ; prix serveur et synchro en ligne requise, pas de paiement automatique de la caisse sans preuve.
- Rapprochement de paiements/reçus dans tenant DB ; SaaS subscription séparé dans registry.
- Outbox/per-tenant, events versionnés, consumers idempotents et retry/backoff/dead letter.
- Migration tenant progressive, pool borné/éviction, backups en DB cohérentes, restore ciblé sans cross-tenant.

## Gouvernance métier
État `DRAFT/ACTIVE/SUSPENDED` par capability ; les modules *pharmacy regulated* sont OFF par défaut et ne deviennent pas activables par marchand sans privilège + preuve légale vérifiée. Médicaments réglementés non proposés aux transactions tant que non autorisés. Venue manager ne reçoit pas les commandes des commerces par sa seule qualité de gestionnaire du centre.

## Évolution
Éviter table EAV sans schéma ; noyau `Offering` stable + tables spécifiques par verticale, modules NestJS à frontières strictes, aucun monolithe God Service. Aucun moteur ERP ou commerce tiers en fondation.
