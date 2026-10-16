# Distribution clients installables et production API-only

## Clients
- Android acheteur white-label, React UI embarquée + Capacitor/Kotlin.
- Android marchand séparé, React UI embarquée + Capacitor/Kotlin.
- Windows opérateur EXE/MSI, React embarqué + Tauri/Rust, **VPN obligatoire** ; Windows marchand futur.
- Marketplace additionnelle Android, opt-in et non requise en V1.

## Serveur
API NestJS HTTPS avec ressources statiques **uniquement médias nécessaires** et payload JSON ; aucun HTML marchand/administrateur, Swagger UI, SPA, SSR ni PWA. Routes publiques limitées à catalogue CDF, identité email, commandes authentifiées ; merchant routes avec RBAC/MFA selon rôle, plateforme routes **réseau privé/VPN exclusivement**, sans authentification désactivée en interne. DB, metrics, secrets, stockage interne ne sont jamais exposés.

## DNS proposés et non configurés
`xshop-api-test.shuleops.com` pour staging et `xshop-api.shuleops.com` après mise en production éventuelle. Les sous-domaines doivent être vérifiés contre usages existants du domaine et recevoir TLS. Le nom xShop est provisoire, garder abstraction des URLs.

## Devise
Backend produit prix CDF public à partir du prix USD interne et de la version de taux. UI React n'effectue pas de conversion autoritative ; la commande capture le taux. Les utilisateurs peuvent exprimer une préférence monétaire pour territoires futurs, mais **pas affichage USD activé pour RDC sans validation réglementaire**.

## Identité
Pas de SMS, e-mail + mot de passe et vérification par SMTP ; comptes marchands/opérateurs TOTP. Aucun refresh token transféré au DOM.

## Livraison Windows
Tauri 2 supporte NSIS EXE et WiX MSI, builds/signature sur Windows. Source : https://v2.tauri.app/distribute/windows-installer/ .

Voir [réseau détaillé](NETWORK-EXPOSURE.md), [auth](AUTH-NO-SMS.md) et [revue juridique](../legal/RDC-INITIAL-REVIEW.md).
