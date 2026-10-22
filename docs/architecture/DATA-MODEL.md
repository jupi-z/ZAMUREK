# ZAMUREK — schéma de données, résumé architectural actif

**Source normative : [DOMAIN-MODEL](../v1/DOMAIN-MODEL.md), [TECHNICAL-CONTRACTS](../v1/TECHNICAL-CONTRACTS.md) et [AGENTIC-KERNEL](../v1/AGENTIC-KERNEL.md).** Cet aperçu n'est pas une migration SQL exécutable.

## Registry global
`Organization` (une DB PostgreSQL métier), `EstablishmentReference`, `Venue`, `VenueMembership` opt-in, `Channel`, `Staff/CustomerIdentity` e-mail vérifié, `Session`, `RoleMembership`, `PlatformOperator`, `SubscriptionBASIC`, `ProvisioningJob`. Conserver un minimum de métadonnées communes, **jamais** commandes/rendez-vous/réparations privées dans le registry.

## DB commerciale séparée par organisation
`Establishment` (sous-division sécurisée) → `CapabilityProfile`, `Offering`, `Variant`, `Category`, `Media`, `UnitDefinition` (PCS/G/KG), `PriceBasis`, `ModifierGroup`, `MerchantFxRateVersion`, `TerritoryPricePolicy`.

Par établissement : `Resource`, `StaffCalendar`, `Table`, `ReservationHold`, `Appointment`, `RestaurantMenu`, `KitchenTicket`, `Quote`, `QuoteAcceptance`, `RepairCase`, `Consent`, `WorkOrder`, `Cart`, `PriceQuote`, `Order`, `OrderLine`, `PaymentRecord`, `RefundRequest`, `Fulfillment`, `OutboxEvent`, `AuditEvent`.

**Prix catalogue de base USD uniquement**, taux du commerçant USD→CDF versionné, devis et montants CDF figés côté serveur pour les ventes publiques RDC. Masse/prix décimaux exacts selon [règle d'arrondi](../v1/MONETARY-AND-QUANTITY-POLICY.md).

## Agentic Fabric — fondatrice dès 0.1.0
`AgentDefinition`, `ToolDefinition`, `PolicyDecision`, `Run`, `Checkpoint`, `Approval`, `MemoryScope` et traces d'événements avec organization/establishment/actor. Un agent ne peut interroger directement les bases commerciales sans handler et autorisation.

## Invariants SQL
- organization DB isolation; `establishmentId` et ownership sur toutes les données concernées.
- PostgreSQL exclusion/unique constraints contre doubles réservations.
- Checkout transactionnel idempotent, quote versionnée/snapshot ; pas de paiement confirmé par client.
- Pharmacie : classification règlementaire `BLOCKED` par défaut et vérification des preuves/autorisations avant toute transaction réglementée.
- Index venue ne stocke que projections publiques consenties, révocation et purge contrôlées.

Pas de double grille CDF/USD, pas d'authentification par SMS et pas de DB par simple boutique/établissement. Les anciennes spécifications xShop sont archivées par [INDEX](../INDEX.md).
