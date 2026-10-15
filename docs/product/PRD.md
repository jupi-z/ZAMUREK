# Product Requirements Document — xShop

**Version : 0.1 | 15 octobre 2026 | Statut : spécification de référence initiale**

## Problème
De petites boutiques ont besoin d'un canal de vente simple (application personnalisée, éventuellement site web), sans coût de construction d'une plateforme indépendante par commerçant. L'opérateur xShop veut centraliser le logiciel, isoler les données de chaque boutique, et pouvoir agréger plus tard les catalogues dans une marketplace unique.

## Proposition de valeur
- Commerçant : marque personnelle, catalogue, commandes et suivi, console de gestion limitée à sa boutique.
- Acheteur : découvrir les produits, choisir livraison ou retrait, commander sans création de compte obligatoire, suivre la commande.
- Opérateur : activer/suspendre une boutique, générer des configurations d'application, maintenir une seule API.
- Futur acheteur marketplace : découvrir plusieurs commerces sans perdre leurs applications d'origine.

## Personas
1. Visiteur / acheteur invité ; éventuellement client authentifié ultérieurement.
2. Propriétaire commerçant et personnel de boutique.
3. Opérateur plateforme et support habilité, avec actions auditées.

## Principes non négociables
- Une base commerciale PostgreSQL par tenant ; registre central dédié.
- Tout acte commercial est autorisé et valorisé par le serveur ; aucune confiance dans les prix ou droits envoyés par le client.
- Une commande V1 ne traverse jamais plusieurs boutiques.
- Aucun compte marchand ou moyen de paiement n'est commun à deux boutiques sans consentement/configuration spécifique.
- Le client Android est du React/HTML/CSS pour la présentation ; opérations API, cache, sécurité et traitements système en Kotlin.
- Les anciennes applications personnalisées gardent leur accès après l'arrivée de la marketplace.
- Le service reste utilisable sans paiements électroniques en V1, via un mode manuel / paiement à la remise configuré.
- Une boutique désactivée ou supprimée n'est pas effacée silencieusement ; archivage et conservation encadrés.

## Objectif V1
Réaliser et administrer une commande mono-boutique, depuis un téléphone Android, de manière traçable, pour au moins **deux tenants d'essai isolés**. Une première boutique peut être utilisée pour le pilote.

## Inclus V1
Identité et personnalisation simple, produit à prix fixe ou variantes simples, catégories, recherche basique, panier, livraison/retrait, adresse et téléphone, commande invitée, paiement manuel/à la livraison, suivi avec secret de consultation, gestion des commandes, rôles simples, supervision/creation de tenant, journal d'audit critique, tests d'isolation et restauration.

## Hors V1
Stock quantifié, réservation de stock, promotions avancées, programme de fidélité, panier multi-vendeur, paiement fractionné, commissions marketplace, reversement automatisé, messagerie, IA, livraison optimisée, ERP, comptabilité générale, facturation fiscale garantie, arbitrage de litige, iOS et web public complet. Extensions sur décision.

## Principes UX
Interface mobile accessible, lisible sans animations obligatoires ; français comme langue initiale ; états chargement/vide/erreur/hors-ligne définis. Catalogue et thèmes par tenant ; aucune duplication du cœur métier.

## Modèle économique (à décider)
Abonnement, frais de mise en service, frais de maintenance ou commission commerciale : non arbitrés. Ne pas coder de facturation SaaS ni de pourcentage implicite.

## Indicateurs à mesurer (sans seuil inventé)
Taux de conversion visite→commande, taux d'échec API, temps d'ouverture de l'app, durée commande, commandes par boutique, commandes annulées, incidents d'isolation, restauration testée. Les cibles SLO seront fixées après mesures pilote.

## Hypothèses à valider
Fournisseurs Mobile Money, responsabilités légales par pays, zone(s) de livraison, choix d'identité client, stratégie de publication de nombreuses applications sur Google Play, quantité de tenants initiale, infrastructure et budget.

Voir [spécification V1](V1-FUNCTIONAL-SPEC.md) et [questions ouvertes](../OPEN-QUESTIONS.md).

