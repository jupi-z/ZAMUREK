# Prérequis externes restant — 16 octobre 2026

**Aucun nouvel arbitrage métier obligatoire pour démarrer G1 en local.** Les décisions du [16 octobre](DECISIONS-VALIDATED-2026-10-16.md) ont remplacé les hypothèses 15/10 incompatibles.

## Avant staging sur VPS
- **E01** : OS, vCPU, RAM, stockage, sauvegardes et accès réseau du VPS existant. Vérifier non-collision et cohabitation avec usages ShuleOps ; pas de credential dans Git/chat.
- **E02** : confirmer propriété DNS de `shuleops.com` et disponibilité réelle de `xshop-api-test.shuleops.com`. DNS/TLS pas créés.
- **E03** : installer un VPN ou segmentation équivalente pour opérateur, DB, métriques, workers et routes `/platform/v1`, isoler staging/prod, vérifier pare-feu.

## Avant ventes réelles en RDC
- **E04 (juridique, prioritaire)** : vérifier **arrêté 007/2025** (publicité des prix/factures en CDF), exceptions éventuelles, conditions de règlement USD, taux marchand autorisé et fiscalité. En attendant, prix/factures client en **CDF uniquement**.
- **E05 (e-mail)** : tester un SMTP réel pour inscription, validation et récupération de compte ; **pas de SMS**, aucune marque/fournisseur choisi d'avance.
- **E06 (commerce)** : commerçant réel volontaire, produits, taux USD→CDF confirmé par lui (taux 2360 seulement de démonstration), frais de livraison, coordonnées et moyens de transfert, conditions de vente/retour.
- **E07 (SaaS)** : contrat d'abonnement **BASIC 7 USD/mois** ; cycle, suspension, service, modalités de paiement, taux plateforme pour facturation CDF et taxes à confirmer.
- **E08 (données)** : obligations du Code du numérique, mentions confidentialité, responsabilités opérateur/commerçant, durée conservation et demandes d'accès/suppression.
- **E09 (ops)** : sauvegardes/restauration par tenant, tests isolation, mesures et support, signature APK et règle de publication Google Play par commerçant.

## Ne bloque pas G1
Nom public définitif (xShop provisoire), commerçant réel pilote, budget infrastructure chiffré (évaluer après inventaire), DNS final, fournisseur Mobile Money, activation affichage USD, nouvelle formule d'abonnement, futur marketplace.

## Blocages techniques internes G1
Completer le contrat OpenAPI (identité marchand/TOTP, CRUD media/settings, fx write, subscription), migrations, tests d'intégration A/B, outils de build. Tout cela relève de l'équipe technique sans question supplémentaire pour le porteur.

## Références
[Revue juridique RDC](legal/RDC-INITIAL-REVIEW.md), [réseau](architecture/NETWORK-EXPOSURE.md), [FX](architecture/FX-PRICING.md), [auth sans SMS](architecture/AUTH-NO-SMS.md).
