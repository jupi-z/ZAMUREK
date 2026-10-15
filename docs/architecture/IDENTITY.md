# Identité, rôles et autorisation

**Révision des décisions du 15 octobre 2026 : compte client obligatoire.** L'ancien suivi invité et ses tokens sont supprimés du contrat V1. Voir [authentification client](AUTH-CUSTOMER.md).

## Domaines séparés
- **Client global** : identité authentifiée depuis le domaine Identity xShop, stable pour plusieurs applications/boutiques, avec consentement explicite à toute association d'un profil marchand.
- **Client local tenant** : snapshot de contact/commande et profil commercial uniquement dans DB du commerçant. Aucune recherche transverse de commandes de l'utilisateur sans consentement et contrôle.
- **Marchand** : staff/owner avec membership actif pour une boutique, RBAC tenant + objet/permission, possibilité d'être staff de plusieurs boutiques explicitement.
- **Plateforme** : opérateurs avec permissions distinctes, MFA recommandé/obligatoire suivant sensibilité, audit d'interventions inter-tenant.

## Auth
Proposition technique de départ : téléphone E.164 + mot de passe hash Argon2id + vérification OTP avant première vente de production ; fournisseur SMS à sélectionner. Login, refresh rotation, logout/révocation, récupération de compte et protections anti-bruteforce.

## Contrôles
Un channelId identifie le magasin mais **n'authentifie personne**. Chaque route protégée vérifie jeton, état utilisateur, membership tenant, ownership objet, action et statut tenant. Identifiants arbitraires en request ne changent jamais tenant DB sans autorisation.

## Android / Windows
Kotlin ou Rust détient et protège les sessions, pas React/DOM. Jamais de credentials serveur, secrets DB, tokens opérateur embarqués, même dans un APK signé. Toute permission est revalidée serveur.

## Tests
Tentative commande sans compte = 401 ; token A pour commande B = 403/404 ; IDOR dans même tenant rejeté ; logout invalide refresh token ; suspension employé invalide permission ; OTP bruteforce limité.

Référence : https://owasp.org/API-Security/
