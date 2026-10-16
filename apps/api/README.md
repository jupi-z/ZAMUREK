# API xShop — monolithe NestJS, G0 non implémenté

Seul serveur applicatif prévu en production ; OpenAPI JSON/REST, registre global, base PostgreSQL **par tenant**. Pas d'interface hébergée. Routes publiques acheteur limitées au strict nécessaire ; marchand auth RBAC+TOTP selon droits ; opérateur `/platform/v1` accessible **VPN seulement**.

## Modules cibles
- Identity **e-mail + mot de passe et vérification e-mail (sans SMS)**.
- Tenants/roles/membership, catalogue **prix de base USD seulement**.
- FX marchand USD→CDF versionné et audité ; calcul quotes **CDF serveur** + snapshot sur commande ; pas de deux prix indépendants.
- Carts, idempotent checkout, orders, fulfillment, paiements manuels direct marchand, cancellation requests, BASIC 7 USD/mois SaaS.
- Outbox, audit, metrics non publics, sauvegarde par tenant.

## Infrastructure
Proposer `xshop-api-test.shuleops.com` pour staging ; `xshop-api.shuleops.com` plus tard. DNS/VPS non configurés ; tests locaux d'abord. Droit RDC affichage commercial CDF à vérifier avant lancement.

Voir [API](../../docs/architecture/API.md), [FX](../../docs/architecture/FX-PRICING.md), [réseau](../../docs/architecture/NETWORK-EXPOSURE.md).
