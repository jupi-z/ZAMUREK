# Architecture logique — xShop

## Vue d'ensemble
Clients : (a) Android white-label React/Capacitor/Kotlin ; (b) Merchant Admin web ; (c) Platform Admin web ; (d) future marketplace.

Côté serveur : reverse proxy TLS, API NestJS modulaire, contrôle identités/permissions, Tenant Registry, Tenant Resolver, Commerce Modules, repositories PostgreSQL, stockage objet et worker d'événements (lorsqu'il sera implémenté).

### Modules backend
- **Platform** : tenant registry, provisioning, canaux, santé.
- **Identity** : identités opérateurs, staff/memberships, sessions et jetons.
- **Catalog** : catégories, produits, variantes, médias et visibilité.
- **Cart** : paniers mono-boutique, prix serveur, expiration.
- **Checkout/Orders** : validation transactionnelle, idempotence, snapshots, statuts.
- **Fulfillment** : zones, frais et modalités de remise.
- **Payments** : intentions de paiement et rapprochement manuel, futur adaptateur PSP.
- **Audit** : enregistrements sensibles et corrélation.
- **Events** : outbox transactionnelle et diffusion à terme.
- **Discovery (future)** : index public multi-tenant.

## Frontières et responsabilités
- React Android est **presentation only**. Il n'envoie pas de HTTP métier directement. Kotlin gère le réseau, les tokens, cache, synchronisation et appels de services ; il livre au pont des DTO minimaux.
- La logique native optimise l'expérience locale, mais **le serveur conserve l'autorité** sur les tarifs, permissions, commande et règlement.
- Merchant Admin web utilise directement l'API protégée : la contrainte « réseau en Kotlin » concerne l'application Android, pas un navigateur web.
- Les modules métier n'ouvrent pas eux-mêmes des connexions arbitraires : la couche TenantDB impose contexte et cycle de vie.
- Un tenant ne peut jamais être résolu à partir d'un seul paramètre fourni par un utilisateur non autorisé.

## Topologie de lancement
Monolithe modulaire, un déploiement serveur central, une base registry et plusieurs bases tenant sur une ou plusieurs instances PostgreSQL ; CDN non obligatoire, médias via stockage objet compatible S3, HTTPS partout.

Pas de microservice, Kafka, moteur de recherche dédié ni Redis obligatoire en G0. Les dépendances seront introduites sur besoin mesuré, pas par anticipation.

## Transaction et cohérence
- Transaction PostgreSQL par commande dans sa base tenant.
- Outbox écrite dans la **même transaction** que la mutation métier.
- Événements inter-bases asynchrones ; pas de transaction ACID distribuée entre registres, tenants et discovery.
- Pas de garantie d'« exactly once » entre services ; consommateurs idempotents et réconciliation.

## Sources primaires
NestJS modules : https://docs.nestjs.com/modules
Prisma v7 PostgreSQL : https://www.prisma.io/docs/orm/v7/core-concepts/supported-databases/postgresql
Voir [tenancy](TENANCY.md), [events](EVENTS.md), [android](ANDROID.md).

