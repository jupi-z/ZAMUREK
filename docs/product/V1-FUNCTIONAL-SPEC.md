# xShop — Fonctionnel V1 actif au 16 octobre 2026

## Canal & identité
- App Android **acheteur** white-label et app Android **marchand** séparées ; console Windows opérateur EXE/MSI.
- Compte acheteur **obligatoire** : email + mot de passe et adresse vérifiée, aucun SMS. Récupération par email. Identité globale mais chaque objet commande/profil isolé DB tenant.
- Marchand/staff avec rôles/permissions tenant et TOTP ; plateforme accessible via console VPN.
- Aucun frontend hébergé sur le serveur production.

## Catalogue
Catégories, variantes, images, prix source **USD seul** par variante, publication disponibilité (ACTIVE/UNAVAILABLE/HIDDEN/DRAFT), pas de stock quantitatif. Taux USD→CDF **marchand** réglable via app marchand, audité/versionné ; défaut 2360 **en fixture de test seulement**. Frais livraison en USD par zone et convertis CDF à partir du taux du marchand.

## Affichage commercial Kolwezi
Public **CDF uniquement** par politique de prudence réglementaire. Les réponses API publiques sont converties côté backend ; l'utilisateur n'a pas un sélecteur de devise USD opérationnel en RDC avant avis juridique. Une préférence d'affichage est prévue techniquement pour territoires autorisés plus tard. Ne pas confondre affichage prix avec devise du règlement.

## Parcours client
Catalogue → panier authentifié → choix retrait ou zone de livraison → **devis CDF du backend** avec ID/taux/version/expiration → confirmation explicite du total → commande CDF idempotente avec snapshots immuables USD, taux et CDF. Si taux/prix/frais changent, quote expirée ou invalidée et confirmation exigée. Suivi dans app par propriétaire connecté.

## Modes de paiement
À livraison ou transfert manuel direct marchand. L'app affiche uniquement les instructions du commerçant ; le client ne peut pas s'auto-déclarer payé. Toute réception USD éventuelle est hors automatisation V1 et doit être validée légalement. La commande et preuve commerciale sont en CDF.

## Livraisons, annulations et suivi
Retrait ou zones de livraison, frais convertis depuis USD et affichés CDF ; adresse et téléphone destinataire si livraison. Demande d'annulation au marchand, aucune annulation automatique ; les paiements et états de commande sont des automates distincts.

## App marchand
Catalogue et prix USD, taux USD→CDF, zones et frais source USD, commandes/confirmations, disponibilité, personnel autorisé, boutique et médias. Aucune commande d'un autre tenant. Pas d'interface web marchand en production.

## Offre xShop
Plan unique BASIC **7 USD/mois/boutique**, facturation CDF sur marché RDC selon validation juridique, taux plateforme distinct du taux marchand. Service client final = commerçant ; support logiciel = xShop.

## Critères de recette
Tests auth sans SMS, quote stable, modifications taux/anciennes commandes, CDF public, cross-tenant + cross-customer, app Android acheteur/marchand distinctes, console Windows, réseau privé platform, restauration DB et conformité applicable. Voir [FX](../architecture/FX-PRICING.md), [Legal](../legal/RDC-INITIAL-REVIEW.md), [Tests](../quality/TEST-STRATEGY.md).
