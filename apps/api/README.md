# API xShop (prévu ; non implémenté)

Backend NestJS + TypeScript, PostgreSQL par tenant, registre et modules Commerce. Le serveur est source de vérité pour prix, accès, paniers et commandes.

**Modules envisagés** : platform, tenancy, identity, catalog, cart, checkout, fulfillment, payments, audit, outbox.

**Démarrage** : en G1, générer ici le projet NestJS et versionner sa configuration. Aucune commande npm de build ne fonctionne encore dans ce répertoire.

Voir [SYSTEM](../../docs/architecture/SYSTEM.md), [TENANCY](../../docs/architecture/TENANCY.md) et [OpenAPI](../../packages/contracts/openapi/xshop-v1.yaml).

