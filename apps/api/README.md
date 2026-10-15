# xShop API — application backend seule en production

**Prévue, non implémentée.** NestJS + TypeScript, monolithe modulaire, registry/identity, bases PostgreSQL métier **par tenant**, couche de connexion bornée et secrets externes.

Domaines V1 : identity client obligatoire (auth téléphone/mot de passe/OTP proposé), memberships personnel, catalogue variantes **prix CDF/USD**, panier/auth et monnaie sélectionnée, checkout idempotent, commandes, livraison/retrait et double frais CDF/USD, paiement manuel direct marchand, demandes d'annulation, audit et provisioning.

Déploiement : API REST JSON HTTPS, workers et infrastructures nécessaires seulement ; **pas de frontend, SPA/SSR/PWA, portail admin ou Swagger UI**. OpenAPI dans Git/CI.

Voir [contrat](../../packages/contracts/openapi/xshop-v1.yaml), [système](../../docs/architecture/SYSTEM.md), [tenancy](../../docs/architecture/TENANCY.md).
