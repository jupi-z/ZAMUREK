# Architecture Decision Records (ADR)

Les ADR actent une **direction architecturale**, pas une preuve de code implémenté. Toute modification structurante crée un nouvel ADR qui remplace ou amende la décision précédente.

| ADR | Décision | État |
|---|---|---|
| [0001](0001-monorepo-modular-monolith.md) | Monorepo + monolithe modulaire | Adoptée pour conception |
| [0002](0002-tenant-database-isolation.md) | Une DB PostgreSQL par tenant | Adoptée pour conception |
| [0003](0003-android-ui-web-core-native.md) | React UI et Kotlin Core | Adoptée |
| [0004](0004-white-label-channels.md) | Apps white-label à code partagé | Adoptée |
| [0005](0005-single-store-checkout.md) | Panier et commande mono-boutique | Adoptée pour V1 |
| [0006](0006-merchant-direct-payments.md) | Encaissement direct commerçant | Proposée, à valider |
| [0007](0007-guest-checkout-identity.md) | Guest checkout et identité future | Adoptée pour V1 |
| [0008](0008-event-outbox.md) | Outbox transactionnelle | Adoptée comme pattern d'évolution |
| [0009](0009-marketplace-compatibility.md) | Marketplace sans remplacement des apps | Adoptée |
| [0010](0010-api-compatibility.md) | Contrats API versionnés | Adoptée |

## Format
Problème, décision, alternatives écartées, conséquences positives/négatives, statut, déclencheur de révision. Les ADR « adoptées pour conception » pourront être revues à l'issue des prototypes / tests.

