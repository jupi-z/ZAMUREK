# xShop Storefront Android — socle client installable

**Prévu ; non implémenté.** React/Vite/TypeScript pour les écrans uniquement ; Capacitor bridge ; Kotlin pour réseau, sessions sécurisées, Room/cache et accès système.

Fonctionnalités de V1 : **compte client obligatoire** (identité globale), catalogue produits pagnes/bijoux/accessoires, prix CDF/USD parallèles, panier client dans une devise, livraison par zones ou retrait, paiement manuel/à la livraison, checkout authentifié, historique suivi et demande d'annulation. Pas de guest checkout.

Canaux et thèmes par commerçant, même cœur applicatif, plusieurs APK personnalisées et ultérieurement app marketplace distincte. APK pilote puis Google Play sous compte commerçant si admissible.

Aucune page HTML hébergée, aucune clé privée backend embarquée. Les DTO React viennent d'un plugin Kotlin. Le checkout requiert une réponse serveur.

Voir [Android](../../docs/architecture/ANDROID.md), [clients/déploiement](../../docs/architecture/CLIENTS-DEPLOYMENT.md).
