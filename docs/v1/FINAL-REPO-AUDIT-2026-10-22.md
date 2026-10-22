# ZAMUREK — audit intégral pré-Codex du 22 octobre 2026

**Statut : READY_FOR_CODEX_0.1.0, sous réserves techniques/externes documentées ; NOT_READY_FOR_PRODUCTION.**
**Dépôt** : https://github.com/jupi-z/ZAMUREK · branche `main` · dépôt **public** (décision du propriétaire).

## 1. Portée effectivement contrôlée

- Arbre GitHub REST `git/trees/main?recursive=1` non tronqué, **108 fichiers présents avant création de ce rapport** ; sources Markdown, scripts Python, JSON, YAML, package/workspace, configurations CI, applications placeholders, ADRs et archives xShop.
- Revue des docs actifs `README.md`, `docs/v1`, `docs/architecture`, `docs/product`, `docs/governance`, `docs/legal`, `docs/decisions`, `apps/*`, `infrastructure`, `packages/*`, `scripts/*`, `spec/v1/*` et du workflow.
- Différenciation explicite **normatif ZAMUREK V1** / archives xShop ; l'OpenAPI xShop reste archive non utilisée par la validation V1.
- Vérifications automatiques **exécutées sur GitHub Actions**, avec lecture des journaux runner, en plus de contrôles statiques via GitHub des identifiants d'opérations et références composants.

## 2. Défauts réels détectés et corrigés

| ID | Anomalie constatée | Correction |
|---|---|---|
| A-01 | CI de validation V1 rouge : détecteur pharmacie cherchait un mot français littéral, malgré un garde-fou réellement décrit sous un autre libellé | `scripts/validate_v1_scope.py` vérifie désormais catégories et blocage sémantique |
| A-02 | `zamurek-v1.yaml` mal formé à la jonction ancien contrat/nouvelles routes : retour à la ligne absent | séparation des chemins et contrôle CI |
| A-03 | Remplacement textuel en JavaScript avait interprété le jeton spécial `$'` dans une regex YAML, corrompant `DecimalExact` | schéma normalisé, regexp réparée |
| A-04 | Une **copie dupliquée entière des anciens schémas** après les nouveaux contrats causait `Duplicate YAML key: PhoneE164` | bloc dupliqué supprimé ; liste des schémas à noms uniques |
| A-05 | Anciennes mentions `xshop_platform` et stockage xshop dans `.env.example` | identifiants renommés ZAMUREK, secrets toujours fictifs |
| A-06 | Le modèle de données ancien ne documentait pas suffisamment `Organization→Establishment` | architecture active reformulée : DB par org, plusieurs établissements sous droits propres |
| A-07 | Le registre des ADR gardait un tarif de 7 USD **par boutique**, opposé au modèle V1 **par organisation** | ADR-0014/0018 alignés sur unité `Organization` V1 et contrat restant à valider |
| A-08 | Ancienne `marketplace future` pouvait masquer le module **Venue obligatoire en V1** | séparation nette venue/découverte opt-in en V1 vs marketplace transactionnelle hors V1 |
| A-09 | Documents historiques xShop se présentaient parfois comme prioritaires | notices de supersession + refonte data/events/operations/security/white-label/parcours |
| A-10 | Classification pharmaceutique fusionnait implicitement `OTC` et non-médicament | séparation des catégories, contrôle de licence/lot/péremption et blocage par défaut |
| A-11 | Aucun premier prompt Codex indépendant du contexte conversationnel | [prompt prêt à l'emploi](CODEX-PHASE-0.1.0-PROMPT.md) et [critères 0.1.0](PHASE-0.1.0-ACCEPTANCE.md) créés, référencés en index/README/CI |

## 3. Vérifications CI réellement passées

Le [workflow GitHub Actions `zamurek-specification-check`](https://github.com/jupi-z/ZAMUREK/actions/workflows/docs.yml) a été observé **SUCCESS** sur :
- [Run 231 — commit `1420d2e`](https://github.com/jupi-z/ZAMUREK/actions/runs/39801069381) ;
- [Run 235 — commit `95c54d9`](https://github.com/jupi-z/ZAMUREK/actions/runs/39801211581) ;
- [Run 236 — commit `40ae586`](https://github.com/jupi-z/ZAMUREK/actions/runs/39801605683).

Leurs étapes incluent, avec succès : `validate_docs.py` (liens/structure), `validate_v1_scope.py` (38 capacités + 8 catégories + progression pondérée + prix fixtures), `validate_agent_contracts.py` (enveloppes et outils IA) et `validate_openapi.py` (parser YAML, ids/refs, endpoints). Des runs ultérieurs peuvent être en attente/annulés à cause de la fréquence des commits : **ne jamais présenter un run encore en attente comme SUCCESS**.

**OpenAPI :** 69 `operationId` uniques ; 64 chemins après correction, 78 composants `schemas` aux noms uniques et références internes sans absents lors du contrôle. L'introspection via linter normatif et la vérification de contrats générés restent à faire pendant Codex 0.1.0.

## 4. Éléments qui restent volontairement non implémentés ou non vérifiés

- **Aucun backend/API Node/NestJS exécutable dans le dépôt**, aucun PostgreSQL réel, aucun APK, EXE/MSI, SDK Kotlin/Rust ni tests E2E métier pour l'instant : le dépôt est un **socle de spécifications**, et non un produit prêt.
- Contrat OpenAPI : premier draft **non complet** sur les CRUD, scopes, retours, transitions, validations métier et documentation des erreurs ; G1 doit le consolider et installer un validateur OpenAPI 3.1 reconnu.
- Sécurité runtime, permissions objet/établissement, agents IA et anti-prompt-injection non démontrés par des tests applicatifs.
- Phases 0.2.0–0.9.0 à développer ensuite, pas incluses dans le lancement de la phase 0.1.0.
- Réglementation RDC prix CDF/FX, commercialisation médicaments, factures, données personnelles, marque et engagements LaJoie Mall non validés juridiquement ; pharmacologie protégée **fail-closed**.
- VPS, DNS `shuleops.com`, SMTP réel, fournisseur LLM, signing/distribution Store, politique des contrats/taxes à vérifier avant essais réels/production.
- Le dépôt est **public** ; ne pas y pousser de secret, code confidentiel ou IP à garder secret sans arbitrage de confidentialité. Les GitHub Actions fonctionnent aussi dans des dépôts privés selon les quotas.

## 5. Verdict

**GO — autoriser Codex à commencer la phase 0.1.0 dans le clone local.** Les contradictions majeures de périmètre et de validation documentaire identifiées dans cet audit ont été corrigées ; les contrôles de conception ont été effectivement vus au vert. **NO-GO** pour prétendre à une certification, à la V1 fonctionnelle ou à une production prête.

Codex devra initialiser le projet réel, compléter OpenAPI et les migrations, exécuter tests unitaires, PostgreSQL réel et builds Android/Windows, mettre à jour progression à partir de **0 % vérifié**, et fournir preuves testées. Lire [premier prompt](CODEX-PHASE-0.1.0-PROMPT.md).

Cette validation est une revue pré-implémentation : la « perfection » ne peut pas être démontrée avant tests du logiciel construit.
