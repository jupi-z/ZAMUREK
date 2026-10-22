# ZAMUREK — domaine V1 adossé aux tables Monarque Connect

**Normatif :** [modèle complet](../v1/DOMAIN-MODEL.md) et [Core partagé](../v1/SHARED-CORE-INTEGRATION.md). Ce document ne fournit pas de migrations SQL.

Les tables **Organization, Establishment, Membership, Item, SalesOrder, Invoice, PaymentRecord, CashAccount, CashMovement, Subscription et EventOutbox** restent sous propriété du backend Monarque Connect. Elles existent dans PostgreSQL partagé avec `organizationId` et établissements autorisés, pas dans une DB marchande externe. Les nouvelles extensions `PosTerminal/CashSession/SaleTender/CommercialPrintJob`, `Menu/KitchenTicket`, `Appointment/Resources`, `RepairCase`, `VenueMembership` et `OfferingOptions` sont des modules spécialisés ajoutés au **Core privé**.

Les applications ZAMUREK ne sont propriétaires **ni des montants canonisés ni des événements métier**. Le calcul USD→CDF s'applique aux offres ZAMUREK via `PricingContext` Core sans imposer USD à toutes les entreprises existantes. Le taux/quote/document émis est versionné et figé ; prix/poids sans float. Vente cash : commande + paiement + CashMovement + outbox atomiques, aucune double écriture réseau.

Tests P0 : source unique des transactions, tenant T1/T2, établissements E1/E2, buyer C1/C2, vente walk-in caissier, FX immuable, no double booking et restauration logique. Aucun schéma imposant « 1 DB par org » ne peut être introduit dans V1.
