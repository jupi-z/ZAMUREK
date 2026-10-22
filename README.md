# ZAMUREK — plateforme commerciale universelle multi-tenant

**Statut : cadrage et architecture documentaire ; code métier et applications non implémentés.** Dépôt privé ; **ZAMUREK** est l'identité du produit, **xShop** son ancien nom de travail.

**Décision propriétaire du 22/10/2026 :** le cœur métier, l'API et les mécanismes agentiques sont développés spécialement pour ZAMUREK. **Mercur et les moteurs commerciaux prêts à l'emploi sont exclus**. Frameworks et bibliothèques open source à licences permissives peuvent être utilisés après contrôle de leurs licences directes et transitives. Voir [ADR-0019](docs/decisions/0019-proprietary-platform-permissive-oss.md) et [politique de dépendances](docs/governance/OPEN-SOURCE-POLICY.md).

## Décisions les plus récentes
[Arbitrages validés le 16 octobre 2026](docs/DECISIONS-VALIDATED-2026-10-16.md) **priment** sur ceux du [15 octobre](docs/DECISIONS-VALIDATED-2026-10-15.md) en cas de contradiction.

- Une API backend NestJS commune, registre central d'identité + **une base PostgreSQL métier par tenant**.
- Catalogue et frais livraison enregistrés **en USD uniquement** ; taux **USD→CDF configurable par marchand**, versionné ; backend calcule les montants et les fige dans la commande.
- Le taux **2360 CDF/USD** est un paramétrage de démonstration fourni, **pas le cours officiel BCC**.
- Pour le pilote à Kolwezi, prix **affichés/facturés en CDF**, par précaution selon l'arrêté RDC de 2025. L'option d'affichage USD en RDC **ne sera pas activée** sans validation juridique ; le stockage USD interne subsiste.
- **Compte client obligatoire, e-mail + mot de passe, vérification par e-mail, sans SMS** ; SMTP à confirmer avant commercialisation. MFA TOTP pour rôles sensibles.
- Android acheteur et Android marchand **applications distinctes** (React UI, Capacitor, Kotlin Core) ; admin opérateur Windows EXE/MSI (React embarqué, Tauri/Rust).
- Production **API-only**, services internes privés. Routes opérateur via VPN ; API minimale nécessaire aux APK distant accessible sous HTTPS/auth. Aucun web frontend, SPA, PWA ou Swagger UI hébergé.
- Sous-domaines **provisoires proposés** et non créés : `xshop-api-test.shuleops.com` (tests), `xshop-api.shuleops.com` (futur prod).
- Un seul abonnement SaaS **BASIC 7 USD/mois par boutique**, devise CDF de publicité/facturation RDC conforme à vérifier, sans commission ni frais d'installation V1.
- Commerce pilote fictif `xShop Atelier` (pagnes/bijoux/accessoires) pour jeux de test Kolwezi ; aucun commerçant réel validé ; marketplace ultérieure opt-in et sans casser les apps existantes.

## Répertoires
`apps/api`, `apps/storefront-android`, `apps/merchant-android`, `apps/platform-desktop`, `apps/merchant-desktop`, `apps/marketplace` (plus tard), `packages/contracts`, `docs`, `infrastructure`, `scripts`.

**Les dossiers apps sont des emplacements documentés, pas des projets exécutables.** Aucun APK/EXE ni backend déployé.

## Documentation
- [Index](docs/INDEX.md)
- [PRD](docs/product/PRD.md), [spécifications V1](docs/product/V1-FUNCTIONAL-SPEC.md)
- [Prix USD + FX CDF](docs/architecture/FX-PRICING.md)
- [Authentification sans SMS](docs/architecture/AUTH-NO-SMS.md)
- [Exposition minimale du réseau](docs/architecture/NETWORK-EXPOSURE.md)
- [Revue juridique initiale RDC](docs/legal/RDC-INITIAL-REVIEW.md)
- [Abonnement unique](docs/architecture/SUBSCRIPTIONS.md)
- [OpenAPI 3.1 draft](packages/contracts/openapi/xshop-v1.yaml)
- [Feuille de route](docs/ROADMAP.md), [prérequis externes](docs/OPEN-QUESTIONS.md), [ADRs](docs/decisions/README.md)

## Contrôles G0
```bash
python3 scripts/validate_docs.py
python3 -m pip install -r scripts/requirements-docs.txt
python3 scripts/validate_openapi.py
```
Ces scripts valident structure et références, pas un serveur opérationnel, conformité OpenAPI exhaustive ni sécurité. CI GitHub existante, exécution réussie non confirmée ici.

## Gouvernance
Aucun secret, clé d'installation, mot de passe ou données réelles dans Git. Contrôle strict des tenants, montants, authentification et versions. Le VPS et les domaines ne sont pas connectés dans cette conversation.
