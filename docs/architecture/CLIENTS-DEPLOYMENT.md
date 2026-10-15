# Clients installables et serveur API-only

**Décision validée : production = backend/API uniquement, jamais d'interfaces HTML hébergées.**

## Clients V1
- **Acheteur Android** : `apps/storefront-android`, APK React + Capacitor + Kotlin.
- **Marchand Android** : `apps/merchant-android`, APK distinct, React UI + Capacitor + Kotlin, permissions magasin.
- **Administration plateforme Windows** : `apps/platform-desktop`, programme React UI embarquée + Tauri 2/Rust natif, installé en EXE ou MSI.
- **Marchand Windows** : `apps/merchant-desktop`, client Windows additionnel installable, même principe Tauri 2/Rust. L'ordre de livraison de cette variante reste dépendant des gates de recette.
- **Future marketplace** : client Android indépendant, non hébergé en tant que site web.

## Windows
Tauri 2 prend en charge l'installation Windows NSIS .exe et WiX .msi ; MSI nécessite un build sur Windows. Documentation officielle : https://v2.tauri.app/distribute/windows-installer/ . Ressources React incluses dans le programme, réseau/persistance/permissions dans le code Rust, aucun frontend remote. IPC Rust strictement typé, pas de commandes arbitraires.

## Production serveur
Un service NestJS API, workers, registry et bases tenant, stockage médias nécessaires et reverse proxy HTTPS ; le backend peut servir des réponses JSON et des flux médias, **pas de SPA/SSR/PWA, portail navigateur, serveur de frontend ou Swagger UI**. OpenAPI versionné dans Git / artefacts CI ; spécification JSON de production exposée seulement si besoin et sous contrôle d'accès. Pas de /docs public.

Le VPS existant et certains domaines sont des candidats **provisoires de test**. Aucune information d'accès n'est présente dans Git. Vérifier OS/RAM/CPU/espace disque/versions/sauvegardes et config DNS avant usage. Staging et production doivent rester séparés ; données client réelles interdites sur environnement de test.

## Distribution
APK pilote direct, puis chaque marchand publie depuis son propre compte éditeur Google Play après vérification des règles et de la valeur distinctive de l'app. Signature/versions sous comptes autorisés ; livrables Windows signés et contrôlés, mises à jour sans serveur frontend. Toutes les applications clientes sont publiques au sens technique et ne peuvent contenir de secrets DB.

## Invariants
- Aucune interface accessible depuis navigateur en production xShop, même administration.
- React : affichage/interaction visuelle ; Kotlin et Rust : HTTP métier, persistance, services OS, traitement local. Le serveur reste autoritaire pour les règles commerciales.
- Les API sont accessibles en HTTPS aux clients authentifiés ; absence de CORS n'est pas une barrière de sécurité.
- Anciennes APK/MSI restent compatibles avec API versionnée.
