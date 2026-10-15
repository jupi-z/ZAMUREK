# Stratégie qualité et tests (après arbitrages)

## Niveaux
- Unitaires : prix **CDF et USD indépendants**, frais livraison 2 devises, format minor-unit, aucun FX implicite, état paiement/commande, règles d'annulation.
- Intégration : registry + DB tenants A/B avec privilèges distincts, migrations, pools bornés, transactions et idempotence, stockage objet.
- API contract : OpenAPI normatif, identité / refresh / récupération, routes marchands/provisioning, contrats rétrocompatibles.
- E2E : inscription/connexion vérifiée, client authentifié commande CDF puis USD, refus checkout anonyme, suivi par identité, marchand Android accepte et marque transfert vérifié, Windows opérateur provisionne B.
- Android réel : deux APK distincts, Capacitor bridge vers Kotlin, suspension, récupération réseau, rotation, clavier, vieille APK/new API, empreinte mémoire/jank.
- Windows réel : EXE/MSI Tauri/Rust, stockage sûr tokens, UI embarquée fonctionnant sans frontend distant.
- Sécurité : deux clients différents dans même boutique et deux boutiques A/B, injections, IDOR, élévation staff/opérateur, aucun secret APK/EXE.
- Exploitation : VPS de staging, backup/restore uniquement A, perte réseau, panne de connexion DB, redémarrage et retries.

## Cas de refus obligatoires
- Sans token : POST panier/checkout et GET commandes → 401.
- Client A → commande client B, même magasin → 403/404, pas de fuite.
- Client tenant A → commandes/produits privés tenant B → 403/404.
- Variantes sans prix CDF ou USD → publication rejetée.
- Livraison frais manquants dans devise de commande → erreur explicite.
- Switch devise → nouveau calcul à partir du tableau tarifs, jamais taux de change.
- Double checkout même clé → même commande, changement payload même clé → 409.
- Paiement manuel déclaré par client → PAID refusé.
- Production contient SPA/SSR/Swagger UI → release rejetée.

## CI G0
scripts validate_docs et validate_openapi : contrôles de structure uniquement, **pas validation de conformité OpenAPI exhaustive ni code d'application**. Ajouter linter/schéma normatif en G1.

## États
Jeux d'essai synthétiques à Kolwezi, « xShop Atelier » fictif, minimum deux tenants. Les environnements de test ne contiennent aucune donnée réelle de clients.
