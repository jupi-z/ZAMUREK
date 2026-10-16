# Roadmap xShop — révisée le 16 octobre 2026

| Gate | Livraison | Validation |
|---|---|---|
| G0 | Arbitrages datés, PRD/specs/API/ADR, étude légal prix CDF et risques, noms DNS provisoires | cohérence documentaire/CI à vérifier |
| G1 | Backend NestJS initial, registry + deux DB tenant, identity **email sans SMS**, environnement de dev/staging, FX taux versionné et API segmentation | tests d'isolation/auth + builds squelettes |
| G2 | Produits prix **USD**, taux USD→CDF par commerçant, devis **CDF** calculés serveur, livraison zones, checkout idempotent, commande snapshot et règlement manuel | E2E prix/taux arrondis/changement taux/paiements |
| G3 | APK acheteur et marchand distincts, admin Windows Tauri/Rust, UI React embarquée, API-only | tests Android/Windows réels et réseau |
| G4 | pilote marchand réel Kolwezi sous politique CDF, vérification légale fiscale/TVA, SMTP réel, déploiement VPS/DNS/VPN, backups et support | check juridique, sécurité, sauvegarde, signature |
| G5 | white-label industrialisé, **abonnement BASIC 7 USD/mois** contractuel et facturation, monitoring et compat API | tests N tenants et release |
| Futur | marketplace app opt-in, nouveaux territoires/règles monétaires | ADR/PRD séparés |

Sans attendre E01 VPS ou commerçant réel pour le G1 local. Aucune date artificielle. Voir [gates](quality/ACCEPTANCE.md) et [prérequis](OPEN-QUESTIONS.md).
