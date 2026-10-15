# Registre des ADR — xShop

**L'ADR nouvelle prévaut sur une ADR remplacée ; arbitrages métier validés dans [décisions du 15 octobre](../DECISIONS-VALIDATED-2026-10-15.md).**

| ADR | Statut / portée |
|---|---|
| [0001 Monorepo, monolithe modulaire](0001-monorepo-modular-monolith.md) | Adoptée |
| [0002 DB isolée par tenant](0002-tenant-database-isolation.md) | Adoptée |
| [0003 React UI + Kotlin Android](0003-android-ui-web-core-native.md) | Adoptée |
| [0004 Canaux white-label](0004-white-label-channels.md) | Adoptée |
| [0005 Panier mono-boutique](0005-single-store-checkout.md) | Adoptée |
| [0006 Encaissement direct marchand](0006-merchant-direct-payments.md) | Confirmée par ADR-0014 |
| [0007 Checkout invité](0007-guest-checkout-identity.md) | **REMPLACÉE par ADR-0011** |
| [0008 Outbox](0008-event-outbox.md) | Design de référence |
| [0009 Marketplace additive](0009-marketplace-compatibility.md) | Adoptée |
| [0010 Compatibilité API](0010-api-compatibility.md) | Adoptée |
| [0011 Compte client obligatoire](0011-mandatory-customer-accounts.md) | **Adoptée ; remplace 0007** |
| [0012 CDF/USD dans chaque boutique](0012-dual-currency-cdf-usd.md) | **Adoptée** |
| [0013 API-only / clients installables](0013-api-only-and-native-clients.md) | **Adoptée ; écarte les admins web** |
| [0014 Abonnement et encaissement](0014-monthly-saas-merchant-collection.md) | **Adoptée** |

L'état ADR représente une décision de conception, pas un code prêt. Une modification future est documentée par un nouvel ADR.
