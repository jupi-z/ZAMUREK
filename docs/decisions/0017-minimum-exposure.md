# ADR-0017 — Exposition réseau minimale de l'API

**Statut : ADOPTÉ — 2026-10-16**

Production backend/API seulement. API de catalogue/identité/commande exposée en HTTPS avec authz et rate limiting selon besoin apps clientes ; routes marchand protégées (auth forte), routes plateforme **VPN only** ; base/métriques/SSH/backups privé. Pas de frontend web ni Swagger UI, pas d'exposition des secrets.

Domaines provisoires proposés : xshop-api-test.shuleops.com (staging), xshop-api.shuleops.com (future production) ; **aucun DNS déployé** et collision à vérifier. VPS existant inventaire requis.

Référence : [NETWORK-EXPOSURE](../architecture/NETWORK-EXPOSURE.md).
