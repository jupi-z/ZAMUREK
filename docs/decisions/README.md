# ADR ZAMUREK — registre des décisions

**Règle** : pour l'implémentation 0.0.0→1.0.0, [ZAMUREK V1](../v1/README.md) et les ADR-0020→0023 priment sur les décisions historiques xShop. [Arbitrages monétaires antérieurs](../DECISIONS-VALIDATED-2026-10-16.md) restent applicables s'ils ne sont pas contradictoires.

| ADR | Statut |
|---|---|
| [0001 Monorepo/modulaire](0001-monorepo-modular-monolith.md) | adopté |
| [0002 Base par tenant](0002-tenant-database-isolation.md) | adopté |
| [0003 Android React + Kotlin](0003-android-ui-web-core-native.md) | adopté |
| [0004 Apps white label](0004-white-label-channels.md) | adopté |
| [0005 Checkout mono-boutique](0005-single-store-checkout.md) | adopté |
| [0006 Paiements directs marchand](0006-merchant-direct-payments.md) | adopté |
| [0007 Commande invitée](0007-guest-checkout-identity.md) | remplacé par 0011 |
| [0008 Outbox](0008-event-outbox.md) | pattern d'évolution |
| [0009 Marketplace additive](0009-marketplace-compatibility.md) | adopté |
| [0010 Contrats API versionnés](0010-api-compatibility.md) | adopté |
| [0011 Compte obligatoire](0011-mandatory-customer-accounts.md) | adopté, sans SMS selon 0016 |
| [0012 Deux prix indépendants](0012-dual-currency-cdf-usd.md) | **remplacé par 0015** |
| [0013 API-only / clients natifs](0013-api-only-and-native-clients.md) | adopté, resserré par 0017 |
| [0014 Abonnement/encaissement marchand](0014-monthly-saas-merchant-collection.md) | adopté, tarif et unité par 0018 et 0021 |
| [0015 USD source + FX CDF](0015-usd-source-converted-cdf.md) | **adopté 16/10** |
| [0016 Pas de SMS / e-mail auth](0016-no-sms-auth.md) | **adopté 16/10** |
| [0017 Exposition réseau minimale](0017-minimum-exposure.md) | **adopté 16/10** |
| [0018 Plan BASIC 7 USD mensuel](0018-basic-seven-usd.md) | **adopté, par organisation en V1** |

| [0019 Plateforme propriétaire, briques OSS permissives](0019-proprietary-platform-permissive-oss.md) | **adopté 22/10 — Mercur exclu** |

| [0020 V1 universelle et non MVP](0020-universal-commerce-v1.md) | **adopté 22/10** |
| [0021 Organisation, établissements et lieu](0021-organization-establishment-venue.md) | **adopté 22/10** |
| [0022 Agentic Fabric dès les fondations](0022-first-class-agentic-fabric.md) | **adopté 22/10** |
| [0023 Secteurs réglementés fail-closed](0023-regulated-commerce-fail-closed.md) | **adopté 22/10** |

| [0024 Core Monarque Connect partagé, ZAMUREK extension omnicanale](0024-shared-monarque-core-zamurek.md) | **adopté en principe 22/10, non implémenté** |

L'ADR est une décision de conception, non une preuve d'exécution.
