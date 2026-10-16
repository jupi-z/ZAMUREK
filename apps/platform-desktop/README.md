# Opérateur xShop — Windows Desktop, G0 non implémenté

React embarqué + Tauri 2/Rust, package EXE/MSI. L'opérateur accède **seulement via VPN** aux endpoints privés `/platform/v1`, avec MFA TOTP et audit. Actions : provisioning tenant et DB, applications/canaux, supervision, offre BASIC 7 USD/mois et statut abonnement, contrôle juridique de commercialisation, sécurité/rate limits.

Production n'héberge aucune UI. Aucun secret privilégié embarqué dans l'installateur. Domaines `shuleops.com` candidats et non créés.

Voir [réseau](../../docs/architecture/NETWORK-EXPOSURE.md), [abonnement](../../docs/architecture/SUBSCRIPTIONS.md).
