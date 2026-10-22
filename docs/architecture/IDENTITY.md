> **V1 après ADR-0024 :** l'identité et les memberships sont ceux du Core Monarque Connect, pas une autre base ZAMUREK. Acheteur online = e-mail vérifié sans StaffMembership ; **POS physique = walk-in sans compte** avec caissier/terminal/session auth. Voir [Shared Core](../v1/SHARED-CORE-INTEGRATION.md).

# Identité et habilitations — 16 octobre 2026

## Client
Compte obligatoire **e-mail vérifié + mot de passe** ; numéro de téléphone utilisé comme information de contact de livraison, pas comme identifiant de connexion en V1. **Aucun SMS**. Vérification e-mail à usage unique et récupération sûre ; SMTP configurable et dépendance réelle avant lancement commercial. Voir [AUTH-NO-SMS](AUTH-NO-SMS.md).

## Modèle global/tenant
Identité globale xShop stockée séparément des bases commerciales ; une identité peut commander dans plusieurs boutiques sans partager commandes ou profils. Chaque commande appartient à un `globalCustomerId` et un tenant. AuthN + ownership vérifiés serveur.

## Marchand et opérateur
Employés/propriétaires : identités avec memberships tenant, permissions spécifiques, TOTP pour rôles sensibles. Opérateurs : rôle plateforme, TOTP obligatoire, console Windows via VPN seulement, audit. Aucune approbation de transfert de fonds par déclarations clients.

## Appareil
Kotlin Android, Rust Windows gèrent le transport et la protection des sessions ; React reste UI. Révocation des refresh tokens, anti-énumération, rate limits, blocage après abus, aucune clé serveur dans APK/EXE.

## Tests
Refus panier/checkout sans auth ou e-mail non validé, cross-tenant IDOR, cross-client IDOR, attaques reset, replay token, brute force, step-up TOTP opérateur/marchand.
