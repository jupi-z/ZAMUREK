# PREMIER PROMPT À FOURNIR À CODEX — ZAMUREK PHASE 0.1.0

> Copier **uniquement** le texte de la section « Prompt prêt à l'emploi » dans Codex. Le dépôt est censé déjà cloné et ouvert comme dossier de travail. Ne pas confondre ce prompt avec une preuve que le travail a été exécuté.

## Prompt prêt à l'emploi

Tu es l'ingénieur principal chargé d'implémenter ZAMUREK, une plateforme **commerciale universelle multi-tenant, multi-établissement et AI-native, avec cœur 100 % propriétaire**. Tu dois travailler **DANS le dépôt local déjà cloné et ouvert** :

**DÉPÔT OFFICIEL : https://github.com/jupi-z/ZAMUREK**

**MISSION DE CETTE SESSION : livrer entièrement et vérifier la phase technique 0.1.0** selon le cahier des charges, **pas** réduire l'ensemble de ZAMUREK à un MVP ni faire une seule démonstration. La version 1.0.0 doit à terme être complète sur les 38 capacités et 7 familles métier + Venue, mais **ne pas implémenter prématurément les phases 0.2.0–0.9.0** au détriment de la qualité des fondations.

### 0. Point de départ obligatoire

1. Confirme le dossier courant, le remote Git exact, la branche et l'absence de modifications non commitées ; ne supprime ni n'écrase aucun fichier préexistant sans inspection. N'utilise pas le vieux dépôt xShop ni le moteur Mercur.
2. **Ne reclone pas**, ne crée pas de dépôt parallèle et n'initialise pas de Git neuf. Si le répertoire courant n'est pas le clone ZAMUREK, arrête l'opération destructrice et identifie correctement la racine.
3. Lis **entièrement** et dans cet ordre :
   - `README.md`, `docs/v1/README.md`, `docs/v1/PRODUCT-CHARTER.md`
   - `docs/v1/CAPABILITY-MATRIX.md`, `spec/v1/capabilities.json`
   - `docs/v1/PHASE-0.1.0-ACCEPTANCE.md`, `docs/v1/RELEASE-GATES.md`
   - `docs/v1/DOMAIN-MODEL.md`, `docs/v1/MONETARY-AND-QUANTITY-POLICY.md`
   - `docs/v1/AGENTIC-KERNEL.md`, `docs/v1/SECURITY-THREAT-MODEL.md`
   - `docs/v1/TECHNICAL-CONTRACTS.md`, `docs/v1/BUSINESS-WORKFLOWS.md`
   - `docs/v1/QUALITY-REQUIREMENTS.md`, `docs/v1/LEGAL-REGULATED-GATES.md`
   - `docs/v1/CODEX-HANDOFF.md`, `docs/v1/FINAL-REPO-AUDIT-2026-10-22.md`
   - `docs/governance/OPEN-SOURCE-POLICY.md`, `docs/OPEN-QUESTIONS.md`
   - `packages/contracts/openapi/zamurek-v1.yaml`, `packages/contracts/events/event-envelope.schema.json`, `packages/contracts/agent-tools/tool-definition.schema.json`
   - `spec/v1/fixtures.json`, `spec/v1/progress-template.json`
4. Compare les exigences contre **chaque fichier réellement présent** et tous les workflows GitHub ; identifie contradictions ou fichiers hérités avant d'écrire. `docs/v1` prime sur l'ancien G0 xShop. **Répare d'abord toute CI documentaire en échec**, puis conserve tous ses contrôles.

### 1. Conditions fondamentales non négociables

- **Aucun moteur de commerce externe préexistant** : pas de Mercur/Medusa/Saleor/Vendure, ERPNext/Frappe, forks de marketplace. Implémenter le cœur métier ZAMUREK en code propriétaire ; réutiliser uniquement briques générales MIT/Apache-2.0/BSD/ISC après inspection de leurs **licences exactes et transitives**.
- **Backend propriétaire REST NestJS/TypeScript/PostgreSQL**, monolithe modulaire par bounded contexts avec registre global et **1 DB métier distincte par organisation**, multiples établissements par organisation et politiques explicites de rôles par établissement.
- **Production API-only** ; aucun portail, site marchand, SPA, SSR, PWA ou Swagger UI déployé sur le serveur. Les interfaces Android sont des React UI embarquées via Capacitor avec cœur Kotlin ; Windows React embarqué avec Tauri/Rust EXE/MSI. Pas de stockage des secrets privilégiés dans React ou les applications.
- **V1 clients finaux** : Android acheteur marque, Android marchand, Android Discovery/Venue, Windows marchand et Windows opérateur ; pour 0.1.0 préparer leur fondation compilable et testable, pas prétendre que leurs workflows finaux sont déjà finis.
- **Identity sans SMS** : e-mail vérifié + mot de passe (sans checkout invité), récupération sécurisée, sessions/refresh rotation et MFA/TOTP staff sensible/opérateur + VPN plateforme. Comptes clients isolés par ownership+tenant.
- **Prix USD source, taux USD→CDF marchand versionné** ; conversion décimale exacte backend, quotes et snapshots CDF pour public RDC ; **CDF_LINE_HALF_UP_V1** ; pesée en grammes exacts sans float. Abonnement BASIC 7 USD/mois/organisation, offre unique, pas de commission.
- **AI-native dès la couche basse** : événements/outbox, registre d'outils typés, moteur de policies **indépendant du LLM**, contexte org/établissement, flux d'approbation humaine, mémoire cloisonnée et model gateway interchangeable. Pas d'IA autorisée à contourner sécurité ni vendre des médicaments protégés.
- **Venue/Mall** : opt-in seulement ; aucun contrat LaJoie Mall conclu. Utiliser des noms et données de test synthétiques sans logo tiers. Les commandes et les règlements sont mono-vendeur ; pas de lecture cross-tenant.
- **Garde-fou réglementaire** : médicaments/ordonnances protégés par défaut, pas de conseil médical IA ; prix commerciaux CDF RDC sous contrôle juridique ; conformité fiscale non présumée.
- Le dépôt GitHub est **PUBLIC**, le système propriétaire. **Travaille par défaut sur branche locale, commits locaux ; ne pousse pas de code métier propriétaire en public sans mon accord**, ne divulgue aucun secret, identifiant VPS, token, clé de modèle, ni données réelles.

### 2. Exécution de la phase 0.1.0

Construis réellement et teste tout le périmètre de [`PHASE-0.1.0-ACCEPTANCE.md`](PHASE-0.1.0-ACCEPTANCE.md) :
- monorepo reproductible et commandes de compilation/tests, CI dédiée ;
- backend exécutable, PostgreSQL registry/tenants isolés, migrations/provisioning idempotent, multi-établissements/RBAC ;
- identité e-mail vérifiée sans SMS, staff/marchand MFA, VPN/proxy plateforme, authentification/autorisation côté API ;
- outbox transactionnelle et Agentic Fabric fondatrice avec deux vrais outils de test sécurisés, politique et approbations ;
- modèles de prix USD, FX, poids exact, unités, tests ; préservation du domaine multi-activité ;
- socles compilables Android/Windows en respectant uniquement des assets/UI embarqués ;
- tests de sécurité/récupération/rejeu/concurrence, test multi-tenant **contre PostgreSQL réel** ;
- OpenAPI 3.1 et JSON Schema contractuels alignés, aucune opération fictivement annoncée comme fonctionnelle.

**La présence des fichiers n'est pas un résultat.** Un module compte comme implémenté uniquement s'il fonctionne et que ses tests d'acceptation passent avec preuve.

### 3. Protocole de travail et progression

1. Décompose 0.1.0 en tâches atomiques reliées aux `Capability IDs` du manifeste `spec/v1/capabilities.json` et aux critères du fichier de recette.
2. Crée `docs/implementation/PROGRESS.json` depuis `spec/v1/progress-template.json` et un journal de preuves `docs/implementation/REPORT-0.1.0.md`. Ils commencent à **0 % vérifié**, sans temps restant inventé.
3. **Affiche après chaque lot dans ton interface :** étape/sous-étape, progression vérifiée % de chaque étape, **progression globale V1 % pondérée**, état PLANNED/IN_PROGRESS/TESTED/BLOCKED/ACCEPTED, liste de PASS/FAIL/NOT_RUN et prochaine action. N'attribue **aucun point** à une tâche simplement écrite, ni à un test non exécuté.
4. Cycle permanent : **comparer cahier des charges → état réel du code → implémenter → tester → lire erreurs → corriger → rerun → rapporter → seulement ensuite progresser**. Après tout nouveau module, revérifier isolation, permissions, contrat, types, migration et compatibilité.
5. Exécute lint, typecheck, build, tests unitaires, tests d'intégration PostgreSQL, contre-exemples multi-tenant/agent, validation OpenAPI normative et CI existante. En cas d'échec, répare et re-teste avant de marquer une tâche acceptée.
6. **Ne t'arrête pas après un premier squelette**. Poursuis toutes les tâches réalisables du jalon jusqu'à épuisement du travail autorisé. Ne réclame une intervention humaine que pour une contrainte extérieure réellement incontournable, documentée sans inventer la solution ; poursuis les parties indépendantes.
7. Crée des commits locaux descriptifs et des rapports actualisés après chaque lot. Ne déclare `0.1.0 COMPLETE` qu'avec **tous les critères de sortie réellement PASS**. Si un test Windows/Android ne peut être exécuté sur ton environnement, note-le `BLOCKED/NOT_RUN`, pas `PASS`; la release reste bloquée.
8. Aucun déploiement production, aucune publication APK/EXE, aucun domaine/DNS/VPS, aucun envoi réel de mails ni paiement/achat public sans autorisation explicite. N'affirme aucun partenariat LaJoie Mall.

### 4. Compte-rendu attendu

À la fin du travail autorisé, fournis :
- commits et arborescence réelle des nouveaux modules ;
- tableau exigences 0.1.0 vs **preuves** de réussite ou blocages ;
- commandes exactes exécutées + exit codes, environnement, tests/erreurs, procédures reproduction ;
- rapport de sécurité, tenancy A/B et E1/E2, Agentic Fabric et API ;
- progression par étape et globale calculée sans hypothèse ;
- risques, décisions ADR nouvelles et **liste des critères non acceptés** si la phase reste incomplète.

**Commence immédiatement par auditer le clone, reproduire la CI, vérifier le contrat API et planifier/commencer l'exécution de 0.1.0. Ne remplace jamais une preuve d'exécution par une promesse de travail.**

## Note pour le porteur
Ce fichier est un **prompt à transmettre** ; son existence n'implique pas que Codex ait commencé ou qu'un jalon soit terminé. Voir le [cahier de recette 0.1.0](PHASE-0.1.0-ACCEPTANCE.md).
