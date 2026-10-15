# xShop — commerce multi-tenant, clients installables

**Statut G0 : cadrage validé par le porteur de projet le 15 octobre 2026 ; le backend et les applications ne sont PAS encore implémentés.**

> **Production = backend + API uniquement.** Aucune interface cliente ou d'administration hébergée : ni site marchand, ni PWA/SPA, ni portail, ni Swagger UI public.

## Vision
Un moteur commerce NestJS/PostgreSQL unique avec base **isolée par tenant**, plusieurs apps Android personnalisées et une future marketplace additive opt-in. Les anciennes apps continuent à fonctionner. xShop vend son logiciel par **abonnement mensuel**, tandis que chaque commerçant est vendeur et encaisse directement.

## Décisions métier V1
- Pilote interne **xShop Atelier** : pagnes, bijoux, accessoires à Kolwezi (RDC), sans usage d'une marque client réelle.
- **Compte client obligatoire**, identité globale réutilisable entre boutiques avec commandes/PII tenant isolées ; pas de checkout invité.
- **CDF et USD simultanément par boutique**, tarifs individuels et indépendants pour chaque devise ; aucun FX implicite.
- Disponibilité simple, sans quantités de stock ; livraison tarifée par zones dans les deux devises, ou retrait.
- Paiement à la livraison et transfert manuel (marchand confirme après vérification).
- Demande d'annulation au marchand ; suivi dans l'app et les clients de gestion (pas de push/SMS de commande par défaut).
- APK pilote puis éventuel Google Play **sous compte du commerçant** ; code propriétaire dans dépôt privé.

## Clients à construire
- `apps/storefront-android/` — app acheteur, React UI + Capacitor + **Kotlin** (réseau, stockage, sécurité).
- `apps/merchant-android/` — app marchand séparée, React UI + Capacitor + Kotlin.
- `apps/platform-desktop/` — console xShop Windows EXE/MSI, React UI embarquée + **Tauri/Rust**.
- `apps/merchant-desktop/` — client marchand Windows additionnel.
- `apps/marketplace/` — marketplace future, installable, non implémentée.

## Backend
- `apps/api/` — monolithe modulaire NestJS / TypeScript, PostgreSQL registry + une base tenant par marchand.
- `packages/contracts/openapi/xshop-v1.yaml` — contrat d'API **provisoire**.
- `packages/branding`, `packages/shared`, `infrastructure`, `scripts` et `.github` — structure réservée et outillage de documentation.
- Les médias peuvent être transmis en HTTPS via l'API ou du stockage objet contrôlé ; cela ne constitue pas une interface web.

## Documentation
1. [Arbitrages expressément validés](docs/DECISIONS-VALIDATED-2026-10-15.md)
2. [Index complet](docs/INDEX.md)
3. [PRD V1](docs/product/PRD.md) et [spécifications](docs/product/V1-FUNCTIONAL-SPEC.md)
4. [Authentification](docs/architecture/AUTH-CUSTOMER.md) et [CDF/USD](docs/architecture/CURRENCY-CDF-USD.md)
5. [Production API-only / clients](docs/architecture/CLIENTS-DEPLOYMENT.md)
6. [Isolation des tenants](docs/architecture/TENANCY.md)
7. [Contrat OpenAPI V1](packages/contracts/openapi/xshop-v1.yaml)
8. [Risques de l'audit initial](docs/quality/AUDIT-G0-2026-10-15.md)
9. [Décisions ouvertes](docs/OPEN-QUESTIONS.md), [jalons](docs/ROADMAP.md), [ADRs](docs/decisions/README.md)

## Contrôles documentaires G0
```bash
python3 scripts/validate_docs.py
python3 -m pip install -r scripts/requirements-docs.txt
python3 scripts/validate_openapi.py
```
Ces scripts ne vérifient **ni un serveur de production, ni la sécurité réelle, ni l'exécution Android/Windows**. Ils ne remplacent pas la validation OpenAPI normative à ajouter en G1.

## Gouvernance
Branches/PR, revue stricte auth/tenant/prix/paiements ; aucun secret ni clé de signature dans Git. Aucun calendrier fictif. **Code propriétaire, sans licence open source accordée.** Toutes les exigences de mise en production et légales sont à vérifier au stade G4.

Le VPS existant et des noms de domaine disponibles sont des candidats pour des essais techniques, pas une infrastructure de production déjà auditée.
