# Arbitrages approuvés — xShop V1

> **Document historique.** Sur les devises, l'authentification et le périmètre réseau, la [décision du 16 octobre](DECISIONS-VALIDATED-2026-10-16.md) prime. Les règles de prix indépendants et OTP SMS ne sont plus applicables.

**Date : 2026-10-15. Statut : décisions produit validées par le porteur du projet.**

Ce document **primait sur les hypothèses de G0 à sa date** ; il est aujourd'hui **historique et remplacé par [ZAMUREK V1](v1/README.md)** pour tout choix incompatible. Les documents PRD, architecture et OpenAPI doivent s'y conformer. Les recommandations techniques ci-dessous restent proposées et sont révisables par ADR ; elles ne remplacent pas une validation réglementaire ou d'un prestataire.

## Décisions expressément validées

| Sujet | Décision |
|---|---|
| Première boutique | Boutique de démonstration **xShop Atelier** (nom interne provisoire, non une marque client) : pagnes, bijoux, accessoires |
| Territoire pilote | Kolwezi (RDC) d'abord |
| Plateformes V1 | App Android acheteur ; app **Android marchand séparée** ; consoles de gestion installables selon besoin, **aucune interface web hébergée** |
| Langues | Français V1, i18n préparée |
| Monnaies | **CDF et USD simultanément dans une même boutique** ; client choisit la monnaie de commande |
| Identité acheteur | **Compte client obligatoire**, plus de checkout invité |
| Disponibilité | Disponible/indisponible sans décompte de stock |
| Remise | Livraison par zones tarifées et retrait en boutique |
| Paiements | Paiement à la livraison + transfert manuel V1, commerçant encaisse directement |
| Annulation | Demande au commerçant ; pas d'annulation automatique acheteur |
| Notifications | Suivi dans l'app client et dans l'app marchand ; pas de SMS/push imposé en V1 |
| Distribution Android | APK pilote, Google Play au cas par cas, **compte éditeur de chaque commerçant** |
| Future marketplace | Participation **opt-in**, consentement explicite du commerçant |
| Commercialisation xShop | **Abonnement mensuel uniquement** ; tarifs et collecte abonnements à définir avant vente |
| Code source | **Propriétaire et dépôt GitHub privé**, aucun licensing open source |
| Responsabilités | Chaque marchand vend/facture/assure le SAV commercial ; xShop fournit logiciel et support technique ; clauses exactes soumises à validation juridique |
| Infrastructure | VPS existant et domaines disponibles comme ressources candidates de test, **aucun accès/secret communiqué**, validation des capacités avant déploiement |
| Production serveur | **Backend et API uniquement.** Pas de site public, portail admin hébergé, SPA, SSR, PWA, Swagger UI public, ni interface client accessible en navigateur |
| Ordinateur | Applications installables **EXE/MSI Windows**, sans dépendance à un frontend web distant ; le serveur ne livre que des API |

## Implications obligatoires

1. Supprimer l'ancien parcours de commande invitée de la V1 ; fournir inscription, vérification d'identité si applicable, connexion, renouvellement de session, déconnexion et récupération sécurisée.
2. Mettre les comptes clients globaux sous un domaine d'identité central **sans centraliser les commandes** ni partager les profils boutique sans autorisation. Toute commande contient customerIdentityId contrôlé et snapshot local.
3. Prix par **paire (produit/variante, monnaie)**, frais de livraison par (zone, monnaie), panier et commande strictement **mono-monnaie**. Aucun taux de change implicite.
4. Garder le serveur comme autorité pour prix, taxes légalement applicables, identité, commandes et statuts.
5. Fournir un socle commun UI React natif embarqué, des ponts sécurisés Android Kotlin et Windows Rust ; aucune logique commerciale critique dans JS.
6. Aucun artefact d'interface client ne sera hébergé sur le VPS de production ; seul le logiciel serveur y sera déployé. Documentation OpenAPI dans le dépôt / CI ; exposition production désactivée par défaut.
7. La future marketplace restera un **client installable** des mêmes API, opt-in catalogue et checkout initialement mono-boutique.

## Recommandations techniques déléguées (non-décisions commerciales)

- **Windows** : React pour la présentation, Tauri 2 + Rust pour le réseau, coffre sécurisé OS et accès système. Builds Windows signés, paquets NSIS .exe et WiX .msi après tests sur Windows. Source : https://v2.tauri.app/distribute/windows-installer/
- **Identity** : identités globales de clients en registry isolé, liaisons explicitement autorisées aux profils par tenant ; pour la RDC, **téléphone + mot de passe fort** et validation de possession du numéro par OTP avant première commande de production. Un prestataire SMS est nécessaire avant release commerciale ; aucun OTP simulé en production.
- **Multi-monnaie** : deux tarifs indépendants saisis par le marchand, pas de conversion automatique ; toutes les sommes en unités mineures entières et devise explicite.
- **Projet / tests** : version initiale sur un VPS de test candidat, aucun engagement de capacité ou sécurité tant que CPU/RAM/disque/OS, isolation staging et sauvegardes ne sont pas vérifiés.
- **Documentation d'API** : schéma OpenAPI conservé versionné dans Git ; endpoint brut en production facultatif, derrière autorisation si besoin. Pas de Swagger UI en production.

## Ce qui nécessite encore une validation externe

Capacité du VPS et droits de gestion ; signature/compte Google Play par marchand ; fournisseur SMS pour vérification de téléphone ; exigences fiscales et consommation RDC ; canaux de paiement électronique futurs ; contrat d'abonnement, conditions commerciales, protection des données ; hébergement public des fichiers médias sous accès HTTP/API contrôlés (ce n'est pas une interface web).

Voir [audit G0](quality/AUDIT-G0-2026-10-15.md), [dernier registre de blocages](OPEN-QUESTIONS.md).
