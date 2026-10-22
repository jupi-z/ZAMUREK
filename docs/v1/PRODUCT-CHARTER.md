# ZAMUREK V1 — charte normative du produit

**Version du cadrage : 2026-10-22 · Statut : NORMATIF pour l'implémentation 0.0.0 → 1.0.0 ; non réalisé.**
**Priorité :** cette charte et l'[ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md) prévalent sur l'ancienne architecture xShop/ZAMUREK indépendante. La source canonique des transactions est le Core Monarque Connect (privé), avec API et Event Fabric partagées. Aucun ancien dossier n'est une source normative pour les fonctionnalités V1.

## Mission
ZAMUREK est **une plateforme commerciale et de services propriétaire, multi-tenant, multi-établissement, multi-activité et AI-native**, indépendante de tout centre commercial. **LaJoie Mall n'est qu'un partenaire potentiel non conclu** ; aucun logo, contrat, nom de domaine ou droit d'usage de son identité n'est présumé.

Le lancement **1.0.0 n'est pas un MVP** : les parcours de bout en bout de chaque verticale déclarée V1 doivent être implémentés et validés avant la diffusion commerciale. Chaque tenant ne voit que les capacités qu'il active, sans dégrader les autres. On n'exige pas des fonctionnalités médicales illicites ou légalement non autorisées ; les fonctionnalités réglementées restent bloquées par défaut jusqu'à preuve d'habilitation.

## Hiérarchie
**Platform Core (Monarque Connect)** → **Organization** (entreprise, données dans PostgreSQL Core partagé sous isolation logique forte par `organizationId`) → **Establishment** (succursale, restaurant, salon, officine, kiosque) → **Business profile** (une ou plusieurs activités actives) → **Channels** (APK boutique, application de centre commercial / découverte, caisse installée, app marchand Android, Windows opérateur). Un tenant peut gérer plusieurs établissements et plusieurs types de commerce ; un *mall* est une **Collection/Venue** regroupant des entreprises **indépendantes opt-in**, jamais propriétaire automatique de leurs données.

## Invariants indérogeables
1. **Core Monarque Connect et modules spécialisés ZAMUREK entièrement propriétaires pour le métier, les API, le pricing, les transactions, l'intelligence et les données** ; aucune fondation Mercur/Medusa/Saleor/autre moteur du commerce. Briques techniques permissives seulement après contrôle licence/transitives et notices (ADR-0019).
2. **Production serveur = backend REST API Monarque Connect partagé + workers + PostgreSQL/stockage** ; aucune SPA, SSR, interface marchande ou plateforme hébergée. Tous les clients sont installables (APK, EXE/MSI). Les clients React embarquent leurs assets ; Kotlin/Rust gèrent les capacités système et la protection des secrets.
3. **Base PostgreSQL partagée du Core Monarque Connect**, isolation vérifiée par `organizationId`, `establishmentId`, `actor`, ownership et permissions dans toutes les transactions et projections, tests BOLA et restore/export ciblés. **Aucune DB commerciale ZAMUREK distincte** ni réplication des commandes/paiements ; dédiée possible uniquement en future architecture arbitrée séparément. Aucun transfert automatique des fonds des marchands par la venue.
4. **Identité acheteur obligatoire pour checkout en ligne**, e-mail vérifié/mot de passe, sans SMS V1 ; en **POS physique le client de passage est autorisé sans compte**, mais caissier et session authentifiés. Rôles staff/MFA, opérateurs MFA+VPN, propriété objets et scopes côté Core.
5. **Les offres ZAMUREK utilisent un prix source USD et taux USD→CDF marchand versionné**, sans changer la devise par défaut d'une organisation Monarque Connect existante. Conversion exacte et devis du **Core** côté API ; snapshot USD/taux/CDF à la confirmation. Sur territoire RDC, affichage public/facture **CDF par précaution juridique**, sous réserve de validation locale formelle. Ventes au poids = quantités décimales exactes en grammes/unité canonique, pas de calcul flottant.
6. **Règlement en espèces au comptoir (POS) obligatoire**, ainsi qu'à livraison/retrait ou par transfert manuel, preuve ≠ confirmation ; sessions et réconciliation caisse, monnaie rendue, tickets/factures imprimables A4/58/80 mm via renderer Core. **Facture normalisée DGI seulement sous dispositif légalement validé**. Offre cible **ZAMUREK BASIC à 7 USD/mois par organisation**, sans commission et **distincte des plans Monarque Connect** ; nombre d'établissements inclus/quotas, tarifs, marge, fiscalité doivent être validés avant encaissement réel (ne pas présumer illimité).
7. **Dès V1**, exposition discovery/venue = **opt-in par entreprise** ; référencement de seuls produits/services publiables, liens vers commandes **mono-vendeur**. La découverte est unifiée, mais un achat ne mélange jamais plusieurs organisations/contreparties sans protocole multi-commerçants explicitement conçu.
8. **Une Event Fabric, une AI Gateway et un Agent Runtime communs dans Monarque Connect** : ZAMUREK déclare ses outils métiers versionnés ; journal d'événements canonique, politiques, registre de capacités, contexte cloisonné et autorisations d'actions ; **toute transaction sensible reste contrôlée côté domaine avec approbation humaine si requise**. Le système fonctionne même si le fournisseur LLM est indisponible.
9. **Protection de la vie privée, conformité locale, sécurité et restauration** sont des gates de lancement et non des promesses marketing.
10. **Dépôt ZAMUREK public**, Core Monarque Connect privé ; aucune copie de code serveur financier, secrets ni données personnelles dans le dépôt public. Le code app sensible futur doit être protégé par dépôt privé ou changement de visibilité avant publication.

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
- Android vitrine marquée par marchand (même fondation personnalisable) ; Android marchand (gestion multi-activité, commandes, calendrier, **POS avec fonds/cash/ticket imprimé et client de passage**).
- Windows marchand **et caisse POS** installables EXE/MSI, impression thermique/A4 via Rust ; Windows opérateur installable EXE/MSI avec VPN, provisioning, tenant administration. Aucune interface publique de production web.
- Application venue/mall configurable depuis l'app Discovery ou build dédié sous identité autorisée et consentements explicites. Aucun contrat LaJoie Mall n'est acquis.

## Portée et exclusions
**Dans la V1** : toutes les capacités communes exploitées via Monarque Connect et verticales ci-dessus, y compris vente POS cash, rendu monnaie, clôture et documents imprimés, y compris le socle agentique + au moins trois assistants sûrs réellement fonctionnels et révocables (aide catalogue, FAQ catalogue, synthèse d'exploitation), toujours sans écritures critiques autonomes.
**Non engagé** : dispensation de médicaments soumis à ordonnance, diagnostics médicaux, encaissement/escrow marketplace, paiement carte/mobile money automatisé, fidélité avancée, GPS coursier temps réel, POS hors-ligne transactionnel, iOS. Les restrictions légales ou infrastructures non obtenues **ne seront jamais simulées comme des fonctionnalités prêtes**.

## Source of truth
[ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md) · [Contrat partagé](SHARED-CORE-INTEGRATION.md) · [POS & documents](POS-AND-FISCAL-DOCUMENTS.md) · [Matrix des capacités](CAPABILITY-MATRIX.md) · [Parcours métiers](BUSINESS-WORKFLOWS.md) · [Contextes/données](DOMAIN-MODEL.md) · [Noyau IA](AGENTIC-KERNEL.md) · [Gates](RELEASE-GATES.md) · [Pack Codex](CODEX-HANDOFF.md).
