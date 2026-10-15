# Architecture Android — React UI / Kotlin Core / Capacitor bridge

## Convention ferme
React + TypeScript + HTML/CSS = **rendu, navigation visuelle et état éphémère uniquement**. Toute connexion HTTP métier, logique de vente, persistance durable, gestion sécurisée des sessions, accès caméra/fichiers/système et travail en arrière-plan est en Kotlin.

## Couches
- Web UI : écrans et composants, design tokens, accessibilité, states loading/error/empty ; aucune clé privée.
- TypeScript bridge : interface strictement typée et minimale, adaptation des DTO, flux événementiel à granularité raisonnable.
- Capacitor plugin local : validation paramètres d'entrée, dispatch Kotlin suspend/coroutines, gestion de lifecycle.
- Kotlin domain/data : use cases, repositories, client HTTP (Retrofit/OkHttp ou équivalent évalué), Room, gestion de synchronisation, Android Keystore pour matériel cryptographique applicable.
- Backend : validation autoritative d'identité, prix, permissions, commande et paiement.

## Exemple de contrat (conceptuel)
- Storefront.getBootstrap() → StorefrontConfig
- Catalog.listProducts({cursor,limit,query}) → paginated products
- Cart.changeItem({variantId,quantity}) → CartSummary
- Checkout.placeOrder({form,idempotencyKey}) → OrderConfirmation
- Order.track({orderId,trackingToken}) → OrderTracking
- Events : connectivityChanged, cartChanged, orderUpdated

Aucune API prenant une URL arbitraire, commande SQL brute, path de fichier non validé, code à exécuter ou secret de connexion backend.

## Performances
- Ne pas faire traverser le bridge à chaque frame / keypress / pixel défilé ; batching, debounce et réponses sérialisées.
- Garder le scroll, animations et interactions purement visuelles côté WebView ; Kotlin ne rend pas le DOM.
- Paginer produits ; images redimensionnées, cache adapté ; mesurer cold start, frames saccadées, mémoire, consommation réseau et latence bridge.
- Ne pas prétendre qu'une WebView est un moteur d'UI natif ou que Kotlin élimine ses coûts de rendu.

## Hors ligne
L'interface embarquée démarre sans réseau. Cache catalogue facultatif et explicitement daté ; panier local possible mais checkout **nécessite** confirmation serveur. Interdire l'affichage de fausse confirmation hors ligne. Gestion des opérations différées idempotentes.

## Sécurité WebView
Contenu HTML/CSS/JS empaqueté ; navigation externe filtrée, HTTPS, origins contrôlées, pas d'injection de scripts distants, liens extérieurs traités par navigateur sûr, réduction des permissions WebView. Valider toutes les commandes reçues du bridge. Ne jamais considérer JavaScript comme environnement de confiance.

## Test indispensable
Instrumentation réelle Android, appels faux natifs sur simulateur web de développement uniquement, gestion rotation/suspension, process death, sans réseau, vieux APK face à API récente, permissions refusées, changement d'horloge et reprise.

## Références
Capacitor Android plugins : https://capacitorjs.com/docs/plugins/android
Android App Architecture : https://developer.android.com/topic/architecture

