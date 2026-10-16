# White label — applications xShop installables

Nom **xShop provisoire**, thème et nom des APK personnalisés par commerçant, tous bâtis depuis un code commun. Canaux via registry, package ID distinct, signatures isolées, build reproductible ; aucune clé serveur embarquée.

## Flux
Chaque app Android client React UI + Capacitor/Kotlin affiche les **prix commerciaux CDF** fournis par API en RDC, même si le catalogue source USD est commun et le taux marchand configurable. Pas de sélecteur USD public en RDC sans validation du droit applicable. Android marchand distinct, gestion prix USD / taux versionné.

## Distribution
APK interne pour tests puis, si approprié, chaque commerçant publie sous **son compte Google Play** ; règles sur apps répétitives à vérifier. Pas de fork backend, pas de portail web xShop. Clients Windows EXE/MSI pour rôles concernés, React embarqué + Tauri/Rust.

## Sécurité
AppId/channelId public jamais preuve d'autorisation ; session, permissions tenant et identité côté serveur. Aucune donnée DB, clef de signature et credential privillégié dans APK. Toutes les versions anciennes supportées par stratégie de dépréciation explicite.

Voir [clients installables](CLIENTS-DEPLOYMENT.md), [FX](FX-PRICING.md), [réseau](NETWORK-EXPOSURE.md).
