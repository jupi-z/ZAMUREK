> **RÈGLE V1 APRÈS CONVERGENCE :** [Contrats d'intégration](../v1/TECHNICAL-CONTRACTS.md) et [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md) font autorité. Le contrat **canonique runtime provient de Monarque Connect** (`/api/v1`). Les fichiers OpenAPI `zamurek-v1.yaml` et `xshop-v1.yaml` sont des **brouillons historiques non exécutables**, ne pas générer un second backend depuis eux.

# Contrats API historiques xShop V1 — 16 octobre 2026

## Base
**Historique uniquement** : les anciens schémas xShop et ZAMUREK pré-convergence ne sont plus les sources du runtime. Utiliser [Shared Core](../v1/SHARED-CORE-INTEGRATION.md).

Version `/v1`, OpenAPI 3.1 [draft archivé](../../packages/contracts/openapi/xshop-v1.yaml) ; REST JSON HTTPS exclusivement, aucun Swagger UI public / frontend en prod. Préfixe identité `/auth/v1`, opérateur `/platform/v1` protégé par VPN et MFA.

## Surface
- `/auth/v1/register`, `verify-email`, login/refresh/logout/recovery et me : **aucun SMS**.
- `/v1/storefront/config`, catégories, produits → prix publics CDF calculés serveur.
- `/v1/carts`, `/v1/carts/{id}/quote`, `/v1/checkouts` → commandes liées au compte, CDF, taux versionné et quoteId, idem key.
- `/v1/orders` et détail, demande annulation.
- `/v1/merchant/products` : seul tarif source USD ; `/v1/merchant/fx-rate` : taux audit/versions (GET draft ; écriture PUT et auth marchande à détailler avant G1 Done).
- `/platform/v1/tenants` : provisioning privé/VPN.

## Sécurité
ChannelId public = découverte boutique, **jamais auth**. Les droits viennent du bearer/membership/ownership/tenant server. Pas de prix ou taux soumis par client comme autorité. Rate limiting, réponses erreur, idempotence, checks brossés G1.

## Devise
USD en DB catalogue, CDF API commerciale publique RDC, taux merchant décimal versionné. Snapshots USD/taux/CDF. Autres devises/territoires via politique après étude, sans promettre sélecteur USD aux clients RDC.

## Statut draft
Endpoints manquants : CRUD catégories/médias/settings, auth marchand + TOTP, écriture taux, abonnement, politiques de règlement. À définir et valider de manière normative en G1, pas de faux SDK « prêt ».
