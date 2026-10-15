# API et cycle de vie des contrats

## Versionnement
Préfixe /v1 pour les API métier, OpenAPI 3.1 dans [packages/contracts](../../packages/contracts/openapi/xshop-v1.yaml). Il s'agit d'un **premier squelette de contrat**, pas d'une description complète de services déjà construits.

## Canaux
- Application mono-boutique : en-tête X-Shop-Channel contenant un identifiant public enregistré ; tenant résolu serveur. N'est **pas** un mécanisme d'authentification.
- Merchant Admin : canal + token Bearer ; membership et rôle tenant vérifiés.
- Platform Admin : préfixe /platform/v1, token opérateur et autorisation plateforme séparée.
- Marketplace future : contexte tenant explicite sur les opérations mono-boutique, avec lookup autorisé.

## Types d'opération V1
GET /v1/storefront/config, GET /v1/categories, GET /v1/products, GET /v1/products/{id}, GET /v1/fulfillment/options, POST /v1/carts, PATCH /v1/carts/{id}/items, POST /v1/checkouts, GET /v1/orders/{id}/tracking (jeton invité), PUT /v1/merchant/products/{id} et PATCH /v1/merchant/orders/{id}/status ; routes plateforme de provisioning.

## Conventions
- JSON UTF-8 ; dates UTC ISO 8601 ; prix minor-unit en chaînes décimales.
- Error envelope standard : code, message public, correlationId, details facultatifs non sensibles.
- Pagination bornée, tri explicite, contrôle d'entrée strict.
- Clé Idempotency-Key obligatoire sur POST checkout et sur provisioning.
- X-Request-ID/correlationId émis ou renvoyé, propagé dans logs sans PII.
- 401 = non authentifié ; 403 = interdit ; 404 peut masquer ressource inter-tenant ; 409 = état/conflit ; 422 = validation ; 429 = rate limiting.
- Limite de compatibilité fixée par politique de dépréciation annoncée ; pas de suppression brutale d'un endpoint utilisé par une ancienne app publiée.

**Jetons panier :** POST /v1/carts renvoie CartCreated (secret délivré à la création) ; GET/PATCH renvoient Cart sans secret. Les appels sur un panier exigent X-Cart-Token.

**Limite actuelle :** routes authentification employé, administration catégories, images, boutique et employés non encore exhaustivement décrites. Compléter les contrats en G1 avant leur implémentation.

## Choix contractuels non finalisés
Authentification marchand exacte, modèles exhaustifs, limites API et versions du schéma HTTP seront consolidés lors de G1. Aucun SDK généré n'est déclaré disponible.

## Gestion des évolutions
Contrat reviewed en PR avant implémentation, tests de conformité OpenAPI, tests de compatibilité ascendante, snapshots JSON versionnés, notes de changement. Préférer l'ajout compatible à la modification destructive.

