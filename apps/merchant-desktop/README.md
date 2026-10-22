> **ZAMUREK V1 :** Client marchand Windows EXE/MSI est désormais **REQUIRED pour 1.0.0** (et non une extension facultative). Lire [Distribution](../../docs/architecture/CLIENTS-DEPLOYMENT.md) et [Gates](../../docs/v1/RELEASE-GATES.md). L'ancienne description est historique.

# Marchand Windows — client additionnel planifié (pas de code)

React UI embarquée + Tauri/Rust, EXE/MSI. Fonctionnalités analogues app marchand Android : produits **USD source unique**, taux marchand USD→CDF versionné, ventes CDF RDC et commandes tenant, direct payments. Aucune UI déployée sur serveur et pas de credentials DB embarqués. MFA/TOTP pour rôles sensibles.

Voir [FX](../../docs/architecture/FX-PRICING.md), [clients](../../docs/architecture/CLIENTS-DEPLOYMENT.md).
