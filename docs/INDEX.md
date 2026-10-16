# xShop — index G0 actualisé (16 octobre 2026)

**Document prioritaire** : [arbitrages du 16 octobre](DECISIONS-VALIDATED-2026-10-16.md), puis [ceux du 15 octobre](DECISIONS-VALIDATED-2026-10-15.md) uniquement si compatibles.

## Produit
- [PRD actif](product/PRD.md)
- [Fonctionnalités V1](product/V1-FUNCTIONAL-SPEC.md)
- [Parcours](product/USER-JOURNEYS.md)

## Architecture
- [Système](architecture/SYSTEM.md), [tenancy](architecture/TENANCY.md), [données](architecture/DATA-MODEL.md)
- [Prix USD + FX CDF](architecture/FX-PRICING.md) ; [ancien modèle à deux prix, remplacé](architecture/CURRENCY-CDF-USD.md)
- [Authentification sans SMS](architecture/AUTH-NO-SMS.md), [Identity](architecture/IDENTITY.md), [ancienne proposition SMS remplacée](architecture/AUTH-CUSTOMER.md)
- [Clients installables](architecture/CLIENTS-DEPLOYMENT.md), [Android](architecture/ANDROID.md), [white-label](architecture/WHITE-LABEL.md)
- [Réseau / accès privés](architecture/NETWORK-EXPOSURE.md), [API](architecture/API.md), [contrat OpenAPI](../packages/contracts/openapi/xshop-v1.yaml)
- [Paiements](architecture/PAYMENTS.md), [abonnement 7 USD](architecture/SUBSCRIPTIONS.md)
- [Marketplace](architecture/MARKETPLACE.md), [événements](architecture/EVENTS.md)
- [Sécurité](architecture/SECURITY.md), [exploitation](architecture/OPERATIONS.md)

## Conformité, qualité et gouvernance
- [Revue juridique initiale RDC](legal/RDC-INITIAL-REVIEW.md)
- [Audit G0 historique](quality/AUDIT-G0-2026-10-15.md) ; [audit post-arbitrages 15/10 historique](quality/AUDIT-POST-DECISIONS-2026-10-15.md)
- [Tests](quality/TEST-STRATEGY.md), [critères d'acceptation](quality/ACCEPTANCE.md), [roadmap](ROADMAP.md), [questions/prérequis](OPEN-QUESTIONS.md), [ADR](decisions/README.md)

## Statuts
**Décidé** = arbitrage du propriétaire ; **recommandé** = décision technique à vérifier ; **réalisé** = code/test/artefact effectif ; **historique** = document remplacé. Aucun serveur ou APK/EXE n'est actuellement qualifié de réalisé.
