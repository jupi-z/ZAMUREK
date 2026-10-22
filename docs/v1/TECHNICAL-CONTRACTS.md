# Contrats techniques V1 — décisions d'implémentation déléguées

## Principes
Le référentiel canonique des API démarre dans `packages/contracts/openapi/zamurek-v1.yaml` **en état DRAFT**. Il ne remplace ni tests E2E ni code. Versionnement `/v1` ; ne pas changer signatures/behaviors incompatibles sans schéma de migration + tests anciens clients. Le contrat legacy `xshop-v1.yaml` reste **historique** et n'est pas une source de vérité V1.

## Headers et contextes
- `X-Zamurek-Channel` : identifiant public de canal/venue ou commerçant, **jamais un secret** ; résolu serveur sur `organizationId, establishmentId?, territoryPolicy, channelPolicy`.
- `Authorization: Bearer` obligatoire pour toute mutation acheteur/vente/profil/booking ; merchant auth séparée dans scopes JWT/memberships avec MFA.
- `Idempotency-Key` exigée sur create/order/booking/approval/payment/status sensibles. Scope `organization+actor+method+route+fingerprint`, répétition identique retourne le même résultat ; payload différent = 409.
- `X-Correlation-Id` serveur généré/propagé et redaction PII dans logs.

## Domaines d'endpoint (draft évolutif, toutes surfaces V1 ont une API)
- `/auth/v1/*` register, verify e-mail, login, refresh, logout, recovery, me ; `/merchant/v1/*` staff login + MFA/memberships.
- `/v1/organizations/*`, `/v1/establishments/*`, `/v1/capabilities/*` gestion publique limitée, écriture staff.
- `/v1/catalog/*` produits/services/food/weighted/quotes ; `/v1/fx/*` lecture CDF public et taux USD source côté marchand.
- `/v1/carts/*`, `/v1/quotes/*`, `/v1/orders/*`, `/v1/payments/*`, `/v1/fulfillment/*`, `/v1/cancellations/*`.
- `/v1/appointments/*`, `/v1/resources/*`, `/v1/restaurant/*`, `/v1/table-reservations/*`.
- `/v1/merchant/quotes/*`, `/v1/repairs/*`, `/v1/merchant/pos/*`, `/v1/merchant/venues/*` ; route staff avec permissions.
- `/v1/venues/*` découverte lieux, tenants opt-in et projection publique ; aucun historique cross-tenant.
- `/v1/agents/*` modèles/outils/sessions/approbations sous scope ; aucun endpoint système ou secrets.
- `/platform/v1/*` provisioning, abonnement BASIC et opérateur accessible **VPN only**.
- Tous les documents publics prix RDC en **CDF** ; l'USD n'apparaît que dans des contextes de gestion autorisés. Les médias sont protégés par politiques.

## Contrat de commande par type
`CartItem` discriminé avec `kind`: PRODUCT(qtyPCS), WEIGHTED(qtyGramExact), FOOD(options/requiresPrep), SCHEDULED_SERVICE(appointmentId), QUOTED_GOOD(acceptedQuoteId), REPAIR_SERVICE(acceptedRepairEstimateId), REGULATED_GOOD(allowedFlag). Un panier mono-vendeur et une commande mono-vendeur ; pour des services planifiés, le lien `appointmentId` peut être obligatoire. Valider invariants par module avant quote/checkout. Aucune « vente médicament » sous type générique pour contourner classification.

## Modes de fulfilment
PICKUP, LOCAL_DELIVERY, ON_SITE, APPOINTMENT, SPECIAL_DELIVERY, REPAIR_HANDOVER ; associations offre×établissement validées. L'enregistrement de commande ne peut pas réserver indéfiniment une table, un staff ou une ressource. Réservations et holdings expirables, état facturation indépendant.

## Contrats Agentic Fabric
`AgentTool` déclaré en schéma JSON versionné ; événements domain EventEnvelope versionné ; `run(agentDefinitionId,tenantContext,userConsent)` non privilégié, `approve(actionHash)` réservé à rôle et timebox. Toute opération d'agent passe par le même handler métier que l'action humaine. Format logs limité à runId, toolId, actorId, authzOutcome, payloadHash, modelId, timings et correlation.

## États/erreurs
HTTP 200/201/202/204 ; 400 malformed, 401 unauth, 403 forbidden, 404 inaccessible/nonexistent, 409 version/concurrency, 422 invalid business, 429 throttled, 503 unavailable. Body `{code,message,correlationId,details?}` sans fuite d'existence d'un compte/commande. Heure UTC, timezone IANA établissement pour créneaux.

## Build/dist
APK acheteur par magasin/venue, Android marchand, Discover Android ; Windows Tauri 2/Rust marchand et opérateur EXE/MSI, le MSI à compiler sur Windows. API/worker PostgreSQL via déploiement documenté, pas d'UI html sur réseau de production.

## Choix secondaires Codex
Bibliothèque décimale, ORM, SDK mail, bibliothèque auth/TOTP, framework de tests : à choisir sur preuve licence permissive et bonnes pratiques ; ne pas inventer une obligation d'outil à partir d'un placeholder G0. Vérifier licence réelle du framework/app version exact avant ajout.
