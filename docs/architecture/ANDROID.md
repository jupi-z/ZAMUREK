# ZAMUREK Android — trois catégories de clients V1

- **Acheteur marque (APK par commerçant)** : recherche, produits/services au poids, restaurant, réservations, devis/réparations, prix CDF RDC, compte e-mail vérifié, panier/devis/checkout/états.
- **Marchand (APK)** : gestion des établissements/capacités, prix source USD+taux FX, menus/cuisine, vente au poids, agenda, devis/réparation, caisse connectée, opt-in venue et suggestions IA avec approbation.
- **Discovery/Venue (APK)** : découverte commerces d'une ville et lieux partenaires (par ex. centre commercial éventuel), adhésions consenties, navigation multi commerçants et commandes **séparées par marchand**.

UI React/TypeScript/HTML/CSS compilée et **embarquée**, Capacitor bridge typé ; **Kotlin** HTTP, sessions, cache local, tâches système et OS. Le serveur calcule prix, disponibilité finale, verrouillage des créneaux, rôles et agents ; pas de secrets ou tokens long-terme dans DOM. Modules mobiles partagent lib de composants/fonctions natives, pas de duplication de règles métier.

Livraison APK signés, tests vrais émulateurs/appareils, UX offline en lecture avec impossibilité de confirmer vente/réservation sans succès serveur. Aucun frontend web/SSR/PWA hébergé.

Voir [client architecture](CLIENTS-DEPLOYMENT.md), [V1](../v1/PRODUCT-CHARTER.md).
