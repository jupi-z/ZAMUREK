# Revue post-arbitrage — xShop G0

> **HISTORIQUE (avant révision du 16 octobre 2026)** : voir les [décisions récentes](../DECISIONS-VALIDATED-2026-10-16.md). Les anciennes prescriptions sur deux tarifs indépendants CDF/USD, SMS ou affichage USD public RDC ne sont plus applicables.

**15 octobre 2026 — Audit documentaire de cohérence uniquement.** Ce fichier ne certifie pas la sécurité, la validité réglementaire ni des tests d'implémentation.

## Décisions vérifiées dans les spécifications
- Account checkout obligatoire ; parcours invité supprimé de la spécification active.
- Deux prix CDF et USD indépendants par variante et frais de livraison par devise ; panier et commande mono-devise.
- API backend centrale multi-tenant DB PostgreSQL isolée par commerçant + identity registry.
- Android acheteur et Android marchand **deux APK différents** ; React présentation, Kotlin Core.
- Admin opérateur Windows EXE/MSI, marchand Windows facultatif en canal additionnel ; Tauri 2/Rust.
- Serveur production **API-only**, aucune UI HTML ni Swagger UI public hébergés.
- Paiement livraison ou transfert manuel direct commerçant ; abonnement logiciel xShop mensuel.
- Future marketplace opt-in additive, sans forcer la migration des apps existantes.
- Dépôt GitHub **privé**, choix technique propriétaire sans licence open source accordée.

## Points à compléter dans G1 sans nouvel arbitrage du porteur
- Implémenter les projets NestJS, Capacitor Kotlin et Tauri Rust, actuellement dossiers de conception uniquement.
- Compléter OpenAPI : gestion staff/roles, profils marchands, médias upload, catégories, contrats administratifs et maintenance ; tests de contrat stricts.
- Définir et tester la rotation OTP/refresh et les permissions objet/tenant.
- Préciser stockage/pools/backup et environnement de staging à deux tenants.
- Vérifier sur appareils réels les performances WebView / bridge, CPU, mémoire et installateurs Windows.
- Organiser releases/signatures et mises à jour des clients sans frontend distant.

## Prérequis externes AVANT pilote commercial
VPS/DNS inventoriés, fournisseur OTP validé, commerçant réel avec modalités de remise et tarifs CDF/USD, exigences locales des ventes/protection des données/taxes, prix d'abonnement et contrat, identité éditeur Google Play, restauration/audit sécurité. Voir [registre de blocages](../OPEN-QUESTIONS.md).

## Statut honnête
- **Documentation** : décisions intégrées, mais audit à confirmer par CI et revue humaine finale.
- **Contrat OpenAPI** : draft enrichi, non validé comme norme complète.
- **Tests applicatifs** : non exécutés car code applicatif non implémenté.
- **Production** : interdit de prétendre prêt ; G1/G2/G3/G4 restent à réaliser.
