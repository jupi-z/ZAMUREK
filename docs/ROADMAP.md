# Roadmap xShop après validation des arbitrages

Aucun délai garanti avant mesures, aucune fonctionnalité prétendue opérationnelle tant qu'elle n'a pas de tests.

| Phase | Livraison | Gate |
|---|---|---|
| G0 | Décisions validées, architecture API-only, PRD, ADR, OpenAPI draft, sécurité et parcours | Documentation enregistrée ; contrôle CI + audit statique encore à confirmer |
| G1 | Monorepo exécutable : API NestJS, registry, identity, 2 DB tenant, authentification client/staff, migrations, OpenAPI vérifié, socles Android Kotlin/Capacitor et Windows Tauri | Builds + migrations + tests isolation A/B |
| G2 | Commerce API : catégories, variantes **deux tarifs CDF/USD**, panier authentifié mono-devise, checkout, retrait/livraison, paiement manuel, commande client, traitement annulation | Tests E2E CDF ET USD dans deux tenants, idempotence |
| G3 | APK acheteur white-label, **APK marchand distinct**, console opérateur Windows installable, UX/catalogue/checkout réels | Parcours Android natifs + Windows, aucune UI production web |
| G4 | Pilote Kolwezi : audit sécurité, restauration tenant ciblée, signing, distribution APK, vérification OTP, obligations légales, support, disponibilité API | Autorisations externes B04-B10 + tests |
| G5 | Industrialisation des builds multi-marques, client marchand Windows additionnel, abonnement mensuel opérationnel, maintenance compatibilité | Builds reproductibles + contrats + traçabilité facturation |
| Futur | Marketplace Android opt-in, index catalogue et commandes mono-boutique | PRD séparé, consentement marchand |

## Stratégie de développement
1. Auth globale, registry et résolution sécurisée des tenants.
2. Deux tenants d'essai : pagnes/bijoux (xShop Atelier fictif) et boutique différente, pour prouver isolation.
3. Contrat OpenAPI complet, deux tarifs CDF/USD, ledger des transactions de commande et états payements.
4. Clients installables et supervision native, pas de backend d'UI SSR/SPA.
5. Mesures sur VPS **après inventaire**, sans mettre des données réelles dans le staging.

Voir [gates détaillés](quality/ACCEPTANCE.md) et [blocages externes](OPEN-QUESTIONS.md).
