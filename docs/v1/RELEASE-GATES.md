# Trajectoire immuable 0.0.0 → 1.0.0 — ZAMUREK

**V1 = lancement commercial complet des 43 capacités obligatoires, pas MVP.** Phase Core préalable = Monarque Connect **10A.5**, voir [roadmap intégration](INTEGRATION-ROADMAP.md) et [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md). Chaque jalon livre un incrément réel testé ; les branches non terminées ne sont pas présentées comme « V1 ». Versions sont des checkpoints internes, non des autorisations de commercialisation. **Les invariants Core Docs/114 ont été acceptés avec C0 après fusion de la PR #152; C1 est livré sur `main@8546236d2afa849c16ab1c2d6a953934212d08d8`. C1 ne publie ni API transactionnelle ZAMUREK ni offre commerciale. Un gate bloqué juridiquement ne devient pas PASS technique fictif.**

| Version cible | Workstream et livrable | Critère de sortie bloquant |
|---|---|---|
| **0.0.0** | Convergence ADR-0024; C0 et C1 internes du Core acceptés/livrés; cadrage des contrats externes requis pour ZAMUREK; migration du cahier des charges et retrait de l'ancien prompt | Documentation cohérente; APIs nécessaires allowlistées/versionnées avec SHA Core seulement quand elles sont stabilisées; aucun runtime ou prix ZAMUREK déclaré livré |
| **0.1.0** | Après stabilisation des contrats Core requis pour chaque fonction : clients Android/Windows compilables, SDK généré/validé contre les contrats disponibles, tests contractuels; seules les intégrations réelles dont les opérations Core sont livrées sont activées | Builds Android/Windows réels, version/SHA du contrat Core, tests scopes A/B E1/E2 contre APIs existantes, aucun backend autonome |
| **0.2.0** | Core 10A.5 C4/C5 : POS cash/fonds/session/rendu monnaie et documents ; apps ZAMUREK retail/poids/checkout online + POS Android/Windows | vente POS walk-in sans e-mail client, 1 ordre+1 Invoice canonique+1 payment lié+1 mouvement cash net, A4/58/80mm imprimés, FX 125g exact, fiscale fail-closed |
| **0.3.0** | Restaurant/pizzeria : menu/options, capacité, timing, tickets de cuisine, commandes, réservation de table | E2E prise commande + modificateurs + préparation et réservation sans doublon |
| **0.4.0** | Prestations, ressources/staff/calendriers, salon, reports/no-show | E2E réservation + concurrents/ressource, fermeture/créneaux |
| **0.5.0** | Devis meubles et livraison volumineuse, service réparation/diagnostic/consentement | E2E devis→accord→commande ; réparation→accord→restitution |
| **0.6.0** | Module pharmacie fail-closed & vérification légale, groupes Venue/mall, discovery opt-in, révocation et cache | produits interdits rejetés ; deux commerçants indépendants et opt-out effectif |
| **0.7.0** | Utilisation du **Runtime IA commun** MC 10B/11.5, outils métiers ZAMUREK et 3 assistants V1 | un seul gateway/runs/mémoire/policies; provider réel évalué, désactivation sûre, PII/Red Team et actions A3 humaines |
| **0.8.0** | Android acheteur, Android marchand, Android Discover/venue, Windows marchand, Windows opérateur, builds white-label | APK(s) et EXE/MSI exécutés sur devices/Windows, aucun web admin déployé |
| **0.9.0** | Qualification conjointe Core et ZAMUREK : isolation logique A/B, rollback/restauration sélective, multi-produit FairScale, POS+imprimante, privacy, performance, sauvegardes et fiscalité | Core phase 12 et produits testés séparément et ensemble ; licences, conformité, appareils, zéro risque critique ouvert |
| **1.0.0** | Publication commerciale unique, avec capacités obligatoires testées, docs opérateur et engagements support | Go/no-go formel signé, **100% des gates P0/P1**, preuves CI/build/E2E/juridique, pas de fonctionnalité V1 laissée pour plus tard |

**Dépendance normative :** seules les interfaces Core stabilisées autorisent les SDK/tests correspondants; les opérations transactionnelles doivent être livrées avant intégration réelle; C4/C5 sont requis avant vente/encaissement et impression 0.2.0. 10B/11/11.5/12 s'appliquent aux fonctions qui en dépendent et au lancement final, sans verrou global automatique sur 0.1.0. La visibilité publique du Core est intentionnelle et n'accorde aucun droit de réutilisation. ZAMUREK ne possède aucun registry, DB par marchand ni Agent Runtime indépendant. Les gates commerciaux restent séparés.

## Méthodologie de clôture
- Décisions distinctes : **Core techniquement accepté**, **Monarque Connect commercialement autorisé**, **ZAMUREK commercialement autorisé**. Les preuves légales (facture normalisée, PSP, licence) sont `EXTERNAL_PENDING` tant que non obtenues ; sans elles, aucun lancement concerné même si les tests logiciels réussissent.
- Aucune vente POS réelle sans Invoice canonique + PaymentRecord lié, stock cohérent, sessions caissier, documents persistants et test matériel ; aucun déblocage des modules ERP par un abonnement ZAMUREK BASIC.

- Un checkpoint n'est clos que si ses critères **tous** `PASS` avec preuves réelles (commit, test logs, captures de test, artefacts et environnement). `NOT_RUN`, `BLOCKED`, `SKIPPED` ≠ PASS.
- Les spécifications normatives définissent le `what`; le dépôt/CI et les tests démontrent le `done`. Ne jamais utiliser le seul nombre de fichiers/commits comme mesure de fonctionnalité terminée.
- Des dépendances externes (SMS exclu, SMTP, DNS, VPS, juriste, éditeurs Play, paiement vendeur) peuvent bloquer **publication**, mais n'autorisent pas à supprimer silencieusement une verticale V1.
- Les besoins explicitement hors V1 (ordonnances médicales non autorisées, encaissement marketplace central, iOS, transaction hors ligne) restent documentés comme `EXCLUDED`, non des « écarts de livraison ».
- Certaines obligations de Play Store sont externes : un build APK validé peut être commercialisable hors Play seulement si légal et autorisé ; ne pas prétendre une app approuvée sans examen Google.

## Métriques d'avancement exigées
- Un fichier `docs/implementation/PROGRESS.json` (créé à G1, voir squelette `spec/v1/progress-template.json`) contient workstreams pondérés, unités atomiques et preuves. `overallPercent = Σ(weight × ratioVerified) / Σ(weights)`, sans arrondi >100 et sans avancement sur tâches non testées.
- Pour chaque étape : planned, in_progress, implemented, tested, blocked, accepted ; pourcentage, dépendances, définition de « done », liens commits/tests. Communiquer progression **globale et par jalon**.
- Impossible de clore 1.0.0 par simple compte de tâches si n'importe quel `P0/P1` non accepté.

## Contraintes de Codex
Ne pas modifier décisions en silence ; enregistrer tout changement dans ADR/PRD, exécuter tests et revoir la matrice après chaque lot. Résoudre les erreurs itérativement ; ne demander intervention utilisateur que pour blocage réel externe ou conflit de décisions, sans inventer de preuves. Ne pas déployer ni distribuer à des clients sans autorisation explicite.

Référence : [critères de release](QUALITY-REQUIREMENTS.md), [handoff Codex](CODEX-HANDOFF.md).
