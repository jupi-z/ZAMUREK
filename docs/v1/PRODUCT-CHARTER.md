# ZAMUREK V1 — charte normative du produit

**Version du cadrage : 2026-10-22 · Statut : NORMATIF pour l'implémentation 0.0.0 → 1.0.0 ; non réalisé.**
**Priorité :** ce document et les documents `docs/v1/*` prévalent sur les anciens textes xShop lorsqu'ils se contredisent. Aucun ancien dossier n'est une source normative pour les fonctionnalités V1.

## Mission
ZAMUREK est **une plateforme commerciale et de services propriétaire, multi-tenant, multi-établissement, multi-activité et AI-native**, indépendante de tout centre commercial. **LaJoie Mall n'est qu'un partenaire potentiel non conclu** ; aucun logo, contrat, nom de domaine ou droit d'usage de son identité n'est présumé.

Le lancement **1.0.0 n'est pas un MVP** : les parcours de bout en bout de chaque verticale déclarée V1 doivent être implémentés et validés avant la diffusion commerciale. Chaque tenant ne voit que les capacités qu'il active, sans dégrader les autres. On n'exige pas des fonctionnalités médicales illicites ou légalement non autorisées ; les fonctionnalités réglementées restent bloquées par défaut jusqu'à preuve d'habilitation.

## Hiérarchie
**Platform** (ZAMUREK) → **Organization** (entreprise + 1 DB commerciale isolée) → **Establishment** (succursale, restaurant, salon, officine, kiosque) → **Business profile** (une ou plusieurs activités actives) → **Channels** (APK boutique, application de centre commercial / découverte, caisse installée, app marchand Android, Windows opérateur). Un tenant peut gérer plusieurs établissements et plusieurs types de commerce ; un *mall* est une **Collection/Venue** regroupant des entreprises **indépendantes opt-in**, jamais propriétaire automatique des DB de celles-ci.

## Invariants indérogeables
1. **Propriétaire à 100 % pour le domaine métier, moteur de prix, orchestration, API, données et gouvernance agentique** ; aucune fondation Mercur/Medusa/Saleor/autre moteur du commerce. Briques techniques permissives seulement après contrôle licence/transitives et notices (ADR-0019).
2. **Production serveur = backend REST API + workers + DB + stockage média** ; aucune SPA, SSR, interface marchande ou plateforme hébergée. Tous les clients sont installables (APK, EXE/MSI). Les clients React embarquent leurs assets ; Kotlin/Rust gèrent les capacités système et la protection des secrets.
3. **Une base métier PostgreSQL par organization** + registry plateforme, avec séparation par establishmentId obligatoire dans les tables concernées. Chaque commerce reste responsable des ventes, de ses services, de sa clientèle et de ses paiements. Aucun transfert automatique de fonds via ZAMUREK.
4. **Une identité acheteur authentifiée obligatoire** : e-mail vérifié/mot de passe, sans SMS pour la première V1. Rôle marchand + MFA, opérateurs MFA+VPN, propriété des objets et tenant vérifiés backend.
5. **Prix source USD, taux USD→CDF configurable/versionné par marchand**, conversion exacte et devis côté API ; snapshot USD/taux/CDF à la confirmation. Sur territoire RDC, affichage public/facture **CDF par précaution juridique**, sous réserve de validation locale formelle. Ventes au poids = quantités décimales exactes en grammes/unité canonique, pas de calcul flottant.
6. Modes de règlement V1 : à la livraison/au retrait ou transfert manuel au marchand, preuve ≠ confirmation, rapprochement et remboursements non automatiques, sans intégrateur obligatoire. Abonnement plateforme **BASIC 7 USD/mois/organization** comme hypothèse métier héritée à clarifier contractuellement si plusieurs établissements ; **ce point doit être tranché avant facturation réelle**, sans bloquer G1.
7. Future exposition marketplace/venue = **opt-in par entreprise** ; référencement de seuls produits/services publiables, liens vers commandes **mono-vendeur**. La découverte est unifiée, mais un achat ne mélange jamais des DB/contreparties sans protocole multi-commerçants explicitement conçu.
8. IA au cœur de l'architecture : outil métier typé versionné, journal d'événements, moteur de politiques, registre de capacités, contexte cloisonné et autorisations d'actions ; **toute transaction sensible reste contrôlée côté domaine avec approbation humaine si requise**. Le système fonctionne même si le fournisseur LLM est indisponible.
9. **Protection de la vie privée, conformité locale, sécurité et restauration** sont des gates de lancement et non des promesses marketing.
10. **Le dépôt est public à la date de cette révision.** Code métier propriétaire non encore publié ; rendre le repo privé avant tout dépôt de code sensible ou choix explicite d'un dépôt privé séparé. Le public n'autorise aucune publication de secrets.

## Verticales V1 — parcours intégral obligatoire
- **Retail** : articles, variantes, disponibilité, commandes, retrait/livraison, caisse installée.
- **Weighted retail** : chocolats et aliments vendus au gramme/kg, mesure exacte, bornes, décimales, conversions et pesée saisie manuellement.
- **Food & beverage** : restaurant/pizzeria, carte, variantes, suppléments/options, commandes programmées, préparation cuisine, retrait/livraison, tables/réservations.
- **Scheduled services** : salons/coiffure, catalogue de prestations, collaborateurs, calendriers, disponibilités, réservation, annulation/report, dépôt de réservation si activé sans paiement électronique automatique.
- **Furniture / bulky goods** : dimensions/options, demandes de devis, livraison spéciale et approbation par marchand.
- **Electronics / repair** : produits + services, devis/diagnostic, consentement du client, réparation et restitution, informations de série restreintes.
- **Pharmacy** : **parcours d'inventaire/catalogue et vente de marchandises non réglementées autorisées uniquement** en configuration par défaut ; médicaments/prescriptions/dispensation **désactivés et hors transaction** jusqu'à validation juridique, autorisations et protocole professionnel. Le système gère les statuts d'autorisation et affiche explicitement les restrictions, sans ordonnances traitées par IA.

## Applications au 1.0.0
- Android consommateur générique (Discovery/ZAMUREK) avec vues entreprises, services, paniers individuels, commandes/rendez-vous et historique.
- Android vitrine marquée par marchand (même fondation personnalisable) ; Android marchand (gestion multi-activité, commandes, calendrier, caisse).
- Windows marchand installable EXE/MSI ; Windows opérateur installable EXE/MSI avec VPN, provisioning, tenant administration. Aucune interface publique de production web.
- Application venue/mall configurable depuis l'app Discovery ou build dédié sous identité autorisée et consentements explicites. Aucun contrat LaJoie Mall n'est acquis.

## Portée et exclusions
**Dans la V1** : toutes les capacités core et verticales ci-dessus, y compris le socle agentique + au moins trois assistants sûrs réellement fonctionnels et révocables (aide catalogue, FAQ catalogue, synthèse d'exploitation), toujours sans écritures critiques autonomes.
**Non engagé** : dispensation de médicaments soumis à ordonnance, diagnostics médicaux, encaissement/escrow marketplace, paiement carte/mobile money automatisé, fidélité avancée, GPS coursier temps réel, POS hors-ligne transactionnel, iOS. Les restrictions légales ou infrastructures non obtenues **ne seront jamais simulées comme des fonctionnalités prêtes**.

## Source of truth
[Matrix des capacités](CAPABILITY-MATRIX.md) · [Parcours métiers](BUSINESS-WORKFLOWS.md) · [Contextes/données](DOMAIN-MODEL.md) · [Noyau IA](AGENTIC-KERNEL.md) · [Gates](RELEASE-GATES.md) · [Pack Codex](CODEX-HANDOFF.md).
