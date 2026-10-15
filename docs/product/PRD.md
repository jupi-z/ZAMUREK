# xShop — PRD V1 (arbitrages validés le 15 octobre 2026)

**Statut : cadrage produit approuvé ; code applicatif non implémenté.** Document prioritaire : [décisions validées](../DECISIONS-VALIDATED-2026-10-15.md).

## Produit
Plateforme commerce multi-tenant : backend commercial mutualisé NestJS, registry central et **base PostgreSQL dédiée par boutique**, applications clients distinctes et personnalisables. Marketplace future additionnelle, aucune migration forcée des anciennes apps.

## Première utilisation
**xShop Atelier**, commerce pilote fictif de pagnes, bijoux et accessoires pour Kolwezi (RDC). Ce nom sert aux jeux de données et ne doit pas être publié comme identité d'un commerçant réel.

## Canaux V1
1. **Android acheteur** : APK React UI + Capacitor + Kotlin Core, boutique white-label.
2. **Android marchand séparé** : APK gestion catalogue, tarifs CDF/USD, commandes, disponibilité, livraison, validation de paiement manuel et gestion des permissions.
3. **Console opérateur installable Windows** : EXE/MSI (React embarqué + Tauri/Rust), provisioning et gestion des tenants.
4. **Client marchand Windows installable** : canal additionnel, réutilisant les services métiers, priorisation selon gates.
**AUCUNE UI hébergée en production**, aucune console web/SPA/PWA/SSR/Swagger UI. Seul backend/API et infrastructure non visuelle tournent côté serveur.

## Profils
- Acheteur **authentifié obligatoirement** pour commander et suivre ses commandes ; pas de guest checkout.
- Propriétaire et employé boutique avec rôles limités à leurs tenants.
- Opérateur plateforme avec droits distincts et journalisation forte.

## Périmètre commercial
Catalogue/catégories/images, variantes simples, disponibilité sans inventaire quantifié, recherche et panier, **prix affichables CDF et USD pour chaque boutique**, monnaie sélectionnée par client et montants recalculés par serveur. Livraison par zones tarifées en CDF/USD et retrait. Commandes mono-boutique, paiement à livraison/transfert manuel au commerçant, suivi authentifié et demande d'annulation au marchand. Notifications limitées à l'actualisation dans les clients installés et la console marchand.

## Responsabilités / offre
Vendeur = commerçant ; xShop = logiciel et support technique, contrat à vérifier juridiquement. **Abonnement mensuel uniquement**, prix non fixés. Encaissement des ventes directement par le marchand, pas de prélèvement/redistribution plateforme.

## Distribution
APK pilote, puis Google Play au cas par cas sous le compte éditeur du commerçant, sous réserve des règles anti-applications répétitives. Windows EXE/MSI distribués de façon sécurisée et signés selon politique de release. GitHub **privé / code propriétaire**, sans redistribution de source.

## Hors V1
Marketplace, panier multi-commerçants, comptes invités, site web/PWA, back-office hébergé, gestion de stock quantitatif, change automatique/FX, paiement électronique intégré, reversement plateforme, programme fidélité, facturation fiscale garantie, moteur promotions avancé, IA, iOS.

## Indicateurs sans valeurs inventées
Proportion commandes terminées, taux d'échec checkout, pannes réseau, incidents d'accès tenant, restauration ciblée, latence API/pont natif, mémoire Android, nombre de tenants actifs. Les SLO et la capacité du VPS restent à mesurer.

## Gates
Une V1 n'est pas opérationnelle sans authentification client, test de 2 bases séparées, commande CDF et USD, client Android acheteur et marchand distincts, console opérateur installable, sauvegarde/restauration, validation légale et distribution, fournisseur SMS si OTP retenu.

Voir [spécifications fonctionnelles](V1-FUNCTIONAL-SPEC.md), [clients et déploiement](../architecture/CLIENTS-DEPLOYMENT.md), [devises](../architecture/CURRENCY-CDF-USD.md).
