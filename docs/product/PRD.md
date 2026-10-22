> **ARCHIVE HISTORIQUE — ancien xShop.** Ce PRD n'est plus actif pour la nouvelle V1 multi-industries ZAMUREK. Appliquer [Charte produit V1](../v1/PRODUCT-CHARTER.md), [matrice complète](../v1/CAPABILITY-MATRIX.md), [parcours métiers](../v1/BUSINESS-WORKFLOWS.md). Les points contradictoires ci-dessous sont remplacés depuis le 22/10/2026.

# PRD xShop — édition 16 octobre 2026

## Produit
xShop est un **nom provisoire** pour la plateforme logicielle de boutiques simples. Une API NestJS, registry partagé, **base PostgreSQL par commerçant**, et plusieurs clients installés (Android acheteur, Android marchand, Windows opérateur). Marketplace future facultative/opt-in et additive.

## Première clientèle
Commerces physiques pagnes, bijoux, accessoires à **Kolwezi**, pilote fictif `xShop Atelier`. Chaque marchand vend à ses clients, les encaisse directement, gère remise et relation commerciale.

## Offre
**Un seul abonnement BASIC à 7 USD par mois et par boutique**, sans commission V1, sans frais d'installation. Affichage/facturation en CDF sur marché RDC selon règle vérifiée provisoirement, taxe/contrat à valider. Les clients APK ne doivent pas contenir de secrets de la plateforme.

## Catalogue et devises
Un **prix de base USD** par variante et un **coût de livraison USD** par zone. Taux de conversion **USD→CDF par marchand**, avec historique, contrôles et snapshot de commande. Le backend seul calcule les montants CDF commerçants qui engagent une vente. Le taux 2360 est une **illustration de configuration, non cours officiel**. Éviter toute double grille de prix indépendants. Aucune conversion monétaire autoritative dans React.

La préférence de devise d'affichage utilisateur est préparée, mais **CDF uniquement sur surfaces publiques RDC** tant que le droit en vigueur et ses exceptions n'ont pas été confirmés. Le paiement USD est un dossier différent et ne doit pas être supposé autorisé.

## Compte client
Obligatoire ; **e-mail + mot de passe et vérification e-mail, pas de SMS**, récupération sécurisée, session globale entre apps et propriété des commandes isolée tenant. Rôles marchands/opérateurs avec TOTP.

## V1
Produits + catégories + images, disponibilité simple sans stock chiffré, panier/quote checkout authentifié, livraison zones/retrait, paiements à la livraison ou transfert manuel au commerçant, historique et demande d'annulation au marchand. Suivi en app, pas de notifications commerciales payantes.

## Distribution / production
**API HTTPS backend seulement** : aucune UI web hébergée. Android client+marchand en deux APK, Windows opérateur EXE/MSI ; futurs autres clients ajoutés sans dupliquer le backend. Proposer `xshop-api-test.shuleops.com` pour staging après validation DNS. API publique minimale, plateforme via VPN.

## Hors V1
E-commerce web, checkout invité, stock chiffré, marketplace, panier multi-tenant, prestataires de paiement intégrés, change automatique au cours BCC, SMS, reversement plateforme, fiscalité garantie, iOS.

## Gates
Conformité juridique/affichage CDF, vraie délivrance e-mail, budget VPS, contrats et backup avant pilote commercial. [Spécifications](V1-FUNCTIONAL-SPEC.md) ; [arbitrages](../DECISIONS-VALIDATED-2026-10-16.md).
