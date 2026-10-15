# Authentification acheteur obligatoire — xShop

**Décision validée : aucun checkout invité.** Compte client nécessaire pour toute commande et suivi.

## Architecture proposée
- Identité client globale dans un domaine central séparé des données métier propres aux boutiques ; association aux profils clients locaux sous permissions et consentement appropriés.
- Identifiant proposé : numéro de téléphone normalisé E.164 + mot de passe fort haché (Argon2id recommandé). Preuve de possession du téléphone par code OTP à durée limitée avant commande de production, sous réserve de validation d'un prestataire SMS.
- Connexion, inscription, vérification numéro, rafraîchissement/révocation de session, récupération d'accès et déconnexion. Anti brute force, limites de tentatives et audit.
- Client Android : accès réseau et stockage sûr par Kotlin, React UI uniquement. Aucun jeton durable de session exposé à JavaScript.
- Accès aux commandes vérifié par (identité authentifiée, tenant résolu côté serveur, propriété de commande) ; aucun tenant ne voit l'historique d'un autre.
- Pas de token de suivi invité ; liste des commandes du client et détail sécurisé.
- Mot de passe oublié requiert vérification indépendante ; faux OTP autorisé uniquement en tests isolés, jamais en production.

## API à cadrer
POST /auth/v1/register ; POST /auth/v1/verify-phone ; POST /auth/v1/login ; POST /auth/v1/refresh ; POST /auth/v1/logout ; POST /auth/v1/recovery/request ; POST /auth/v1/recovery/confirm ; GET /auth/v1/me ; GET /v1/orders ; GET /v1/orders/{id}.

La dépendance SMS est un **prérequis pour le lancement commercial** de la méthode d'authentification proposée, non un fournisseur engagé. Le développement de l'auth sur des tenants de test peut précéder ce choix.

Sources : https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html ; https://owasp.org/API-Security/
