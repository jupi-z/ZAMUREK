# Android : React UI + Capacitor bridge + Kotlin Core

## Périmètre
Deux **APK distincts** :
- storefront client white-label (inscription/connexion obligatoire, catalogue, prix CDF/USD, panier, commande et suivi).
- app marchand (administration catalogue, prix CDF/USD, livraison, commandes et paiements manuels), staff/owner limités par tenant.

## Responsabilités strictes
React/TS/HTML/CSS = **interfaces et état éphémère**. Kotlin = HTTP, identité sécurisée, sessions, cache local Room/SQLite, tâches système, fichiers et communication avec le serveur. Bridge Capacitor typé, APIs en nombre limité. **Aucune logique prix autoritative en JS/Kotlin** : recalcul serveur.

## Exemple de contrats natifs
Auth.register / verifyPhone / login / refresh / logout ; Store.getBootstrap ; Catalog.listProducts({currency,query,limit}); Cart.create({currency}); Cart.updateItem; Checkout.placeOrder({cartId,method,details,idempotencyKey}); Orders.listMy; Merchant.listOrders/updateStatus/confirmManualPayment, Merchant.updatePricing.

Kotlin transmet au frontend seulement les DTO nécessaires ; ne pas exposer refresh tokens/mots de passe aux événements DOM ou logs. Éviter les appels bridge par frame de rendu ; les animations se font côté WebView.

## Dépendances de release
Android Lifecycle et WebView restrictive ; tests réseau instable, reprise, ancienne APK/nouvelle API, protection sessions, déconnexion, charge RAM, refus de permissions ; validation UX prix/monnaie explicite.

## Hors ligne
L'UI embarquée fonctionne sans réseau ; possibilité de montrer catalogue mis en cache avec avertissement. **Aucune commande acceptée hors ligne sans réponse positive du serveur.**

Voir [AUTH-CUSTOMER](AUTH-CUSTOMER.md), [CLIENTS-DEPLOYMENT](CLIENTS-DEPLOYMENT.md).
Sources : https://capacitorjs.com/docs/plugins/android ; https://developer.android.com/topic/architecture .
