# Identité, sessions et autorisations

## Trois domaines séparés
1. Acheteur invité : pas de compte obligatoire en V1 ; token de suivi aléatoire, limité et stocké haché serveur. Pour permettre un retry idempotent juste après checkout, un snapshot de réponse chiffré peut être conservé temporairement avec TTL court et accès limité à la même session ; il ne constitue pas le stockage durable du secret.
2. Employé commerçant : identité authentifiée et membership tenant avec rôle OWNER ou STAFF ; permissions granulaires sur les actions ; révocation active.
3. Opérateur plateforme : identité distincte, MFA recommandé et journal d'audit obligatoire pour toute intervention inter-tenant.

## Préparation multi-boutiques
Prévoir PlatformIdentity globale pour les clients **sans fusion automatique** des fiches clients tenant. Un acheteur peut posséder plusieurs profils locaux ; l'association à un compte global doit être explicite et justifiée. Ne pas faire d'une adresse ou d'un téléphone un ID global implicite.

## Contrôles par requête
- Résoudre le tenant via le canal enregistré ou le chemin encadré marketplace.
- Authentifier la session d'employé, puis vérifier membership active et permission dans ce tenant, objet par objet.
- Les jetons ne donnent pas à eux seuls accès à toutes les bases : vérifier état tenant et membership.
- Interdire l'usurpation de tenant en manipulant headers, appId, body, JWT claims ou IDs.
- Autoriser le support par élévation explicitement bornée, raison, durée, approbation si nécessaire, traces.

## Cycle de vie
Tokens courts, rotation et révocation des refresh tokens, protection contre bruteforce, réponses sans enumeration, capacité de déconnexion de toutes les sessions. Aucune clé d'API serveur embarquée dans React/Kotlin ou APK.

## Suivi invité
Secret généré côté serveur avec entropie suffisante, envoyé en retour uniquement au créateur ; serveur ne conserve qu'un hash. En cas de perte, pas de parcours de récupération non authentifié ; étape ultérieure par vérification de téléphone/email.

## Référence
OWASP API Security Top 10 : https://owasp.org/API-Security/

