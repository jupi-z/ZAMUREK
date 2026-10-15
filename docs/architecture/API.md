# API xShop V1 — conventions

**Production : API JSON/HTTPS uniquement**, pas de site ni Swagger UI public. Schéma OpenAPI dans [contrat](../../packages/contracts/openapi/xshop-v1.yaml), versionné ; **draft en cours d'alignement**, non déployé.

## Domaines
- /auth/v1/* : register/verifyPhone/login/refresh/logout/recovery/me ; comptes acheteurs obligatoires.
- /v1/* : config boutique, catalogue, tarifs CDF/USD, choix devise, panier authentifié, zones/frais, checkout, historique commandes client, détail d'une commande et demande annulation.
- /v1/merchant/* : authentification staff, produits/tarifs/zone, commandes/états, validation paiement manuel, paramètres, employé.
- /platform/v1/* : provisioning/migrations/tenants/canaux, authentification opérateur et audit.

## Sécurité
X-Shop-Channel désigne le canal public, **jamais une preuve d'identité**. Bearer session exigé pour panier, checkout, commandes et administration. Route ouverte uniquement sur catalogue/configuration publique. Tenant et ownership contrôlés serveur ; endpoints platform protégés séparément.

## Montants
Prix des variantes et frais de zones en CDF et USD ; JSON `amountMinor` entier décimal chaîne. Monnaie dans contexte panier et commande ; **recalcul intégral côté serveur**, pas de conversion automatique.

## Robustesse
Version d'URL /v1 ; DTO explicites, timestamps UTC, erreurs code/message/correlationId, Idempotency-Key sur création de commandes, pagination, 401/403/404/409/422/429. Les applications déjà installées conservent compatibilité selon politique documentée.

## Statut
G1 doit valider un OpenAPI normatif complet, les schémas d'auth et de paiement et les clients générés avant d'en déclarer le contrat stable.
