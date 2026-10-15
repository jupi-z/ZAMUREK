# Modèle de sécurité initial

## Actifs protégés
Bases tenant, informations client, adresses/téléphones, tokens de suivi, comptes employés, mots de passe et clés opérateur, webhook payments, médias non publics, configuration de connexion et signature Android.

## Menaces prioritaires
- Broken object-level authorization / traversée inter-tenant.
- IDOR sur commandes/paniers et opérations d'administration.
- Injection SQL, corruption de paramètres de connexion, mass assignment.
- Usurpation de webhook ou simulation de paiement.
- Vol de jeton d'accès invité, accès non autorisé aux médias.
- Secrets embarqués dans APK ou dans Git.
- WebView chargée depuis origine non maîtrisée, bridge trop permissif.
- DDoS et épuisement pools PostgreSQL / stockage.

## Contrôles indispensables
- AuthN/AuthZ serveur pour toute action protégée, permission per object et per tenant ; ne pas traiter channelId comme secret.
- TLS, validation entrées DTO, limites upload, taille requêtes, pagination et rate limits.
- Jetons courts et révocables ; sessions sensibles journalières et MFA opérateurs ; mesures contre bruteforce.
- Secrets dans secret manager, rotation, privilèges SQL minimaux, sauvegardes chiffrées et restaurations testées.
- Logs structurés sans PII, corrélation, audit immuable ou protégé des opérations sensibles.
- CSP et WebView restrictive, uniquement ressources nécessaires ; pas de fonction générique d'exécution ou de navigation arbitraire sur le pont natif.
- Gestion dépendances, analyse statique, revue d'accès, politique de divulgation et processus de correction.
- Vérification de signature/timing des callbacks PSP ; idempotence et relecture du statut depuis prestataire le cas échéant.

## Exigences de confidentialité
Rétention et suppression à décider suivant obligations des pays opérés ; pas de publication des commandes d'une boutique dans la marketplace ; anonymisation/effacement sur base légale, contrôle d'accès support.

## Critère bloquant
Un échec d'isolation A/B, un endpoint marchand sans membership validée ou un mode de paiement qui se déclare PAID depuis le client bloque la mise en production.

## Source
https://owasp.org/API-Security/editions/2023/en/0x11-t10/

