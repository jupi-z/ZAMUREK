# Exploitation xShop — API-only et segmentation

## Réseau
API HTTPS 443 publique limitée aux besoins réels des clients ; route plateforme `/platform/v1` **VPN privé et MFA**, DB PostgreSQL, objets privés, métriques, backups, secret manager et port SSH **pas accessibles publiquement**. Pare-feu DENY par défaut, reverse proxy strict, rate limits sur auth et endpoints commande.

## Sous-domaines de test
Proposer `xshop-api-test.shuleops.com` pour staging, `xshop-api.shuleops.com` pour production éventuelle, **sans prétendre que DNS / TLS existent**. Éviter collisions avec projets ShuleOps existants.

## VPS
Utilisateur possède VPS et domaines ; **aucune configuration ou accès connu**. Inventaire OS/RAM/CPU/disque et pare-feu obligatoire avant déploiement. Respecter isolation staging/prod ; pas de vraies données en tests.

## Données et sauvegardes
Registry et une DB par tenant ; pools bornés, migrations versionnées, creds séparés et rotations. Backups chiffrés vérifiables, restauration tenant A sans B, tests d'auth email et commerce, audits des taux USD→CDF.

## Traçabilité
Taux marchand modifié = nouveau numéro de version + acteur + date ; commande et facture conservent prix USD source, taux, total CDF. Les taux BCC peuvent être consultés informativement sans substitution automatique au taux du commerçant ; taux commerçant à vérifier légalement avant exploitation.

## Service et abonnements
Un seul plan BASIC 7 USD/mois et par boutique ; modèle des paiements d'abonnement isolé des commandes clients, conversion CDF selon politique RDC distincte des taux marchands.

## Release
API seulement, aucun Swagger UI/portail. Clients APK/EXE/MSI signés distribués via canaux appropriés ; SMTP de vérification e-mail à tester avant ventes réelles, aucun SMS.

Voir [réseau](NETWORK-EXPOSURE.md), [FX](FX-PRICING.md), [legal](../legal/RDC-INITIAL-REVIEW.md).
