# Parcours utilisateurs V1 — édition 16 octobre

## Acheteur
1. Ouvre APK marque et récupère config publique ; aucun identifiant canal n'est une preuve d'auth.
2. Crée compte par e-mail + mot de passe ; vérifie e-mail via challenge, **sans SMS**, puis se connecte.
3. Catalogue : prix **CDF** calculé côté backend depuis la base USD et le taux actif marchand.
4. Ajoute article à panier authentifié, choisit retrait/livraison.
5. Demande **devis CDF** au backend : taux/version, frais et expiration ; confirme total et paiement livraison/transfert manuel.
6. Checkout avec quoteId et Idempotency-Key, snapshots enregistrés ; suivi de commande depuis son compte.
7. Demande annulation à commerçant, sans annulation automatique ; paiement marqué reçu uniquement par marchand habilité.

## Marchand Android
1. Se connecte sous rôle approuvé (TOTP si rôle sensible), choisit boutique autorisée.
2. Définit prix **USD** variante et frais USD par zone ; configure taux USD→CDF tenant avec audit.
3. Gère disponibilité, clients/profils autorisés et commandes ; reçoit demandes d'annulation, confirme transferts après rapprochement.
4. Anciennes commandes conservent leurs snapshots même si taux change.

## Opérateur Windows
Se connecte via VPN, MFA, gère registry, bases tenant, canaux et abonnements BASIC 7 USD ; routes plateforme pas publiques. Aucun portail web hébergé.

## Erreurs
Compte non vérifié → commande impossible ; panne SMTP = inscription/récupération retardée et traitée explicitement. Taux modifié après devis → nouveau prix et reconfirmation ; pas de checkout validé hors réseau. IDOR client ou inter-tenant rejeté ; prix USD public en RDC rejeté par règle territoriale. VPS test isolé du réel.

## Marketplace ultérieure
Même API, profil global, consentement marchand et nouveaux canaux ; pas de migration obligatoire d'APK existante.
