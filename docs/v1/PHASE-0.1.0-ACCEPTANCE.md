# ZAMUREK 0.1.0 — périmètre technique et recette obligatoire

**Statut : SPECIFICATION, pas implémenté.** La première phase exécutable du projet doit préparer les fondations **multi-tenant + multi-établissement + AI-native**, pas livrer une maquette. Les parcours métiers complets arriveront aux jalons suivants ; leur support dans les types/policies de domaine doit néanmoins être prévu **dès 0.1.0**. Aucun commerce ne sera ouvert en production à cette étape.

## Ce que Codex doit construire en 0.1.0

### 1. Repository et développement reproductible
- Monorepo pnpm correctement configuré avec lockfile, scripts `install/dev/build/lint/typecheck/test/test:integration/contract:check` utilisables et documentation exacte.
- Application API NestJS propriétaire exécutable et conteneur ou orchestration locale PostgreSQL, registre + **deux bases métiers isolées d'organisation**, établissement E1/E2 dans une seule des DB.
- Environnement local de capture e-mail sans SMS, secrets factices test/développement et validation de configuration stricte en prod ; `.env.example` sans secret.
- CI réelle : scripts statiques existants toujours verts, lint/typecheck/build, tests unitaires/intégration sur PostgreSQL service, migrations, tests de non-régression de la tenancy ; fail-closed si jamais de DB/SMTP modèle configuré en production.

### 2. Registry, tenancy, establishments, permissions
- Registry PostgreSQL central avec `Organization`, `EstablishmentReference`, `TenantProvisioningJob`, `Channel`, `Membership` et `Venue` **structurel mais pas encore parcours complet**.
- Provisioner idempotent : DB métier et rôle séparé par org, migrations versionnées, secrets refs (aucune injection client), activation après validation ; rollback/compensation sur échec ; persistance/concurrence testées.
- Contexte requête immutable `actorId, organizationId, establishmentId, channelId, territoryPolicy` ; résolution serveur channel→org, ownership objet, RBAC actions et scopes établis.
- Modèle des établissements avec plusieurs activités possibles (RETAIL, WEIGHTED, FOOD, SERVICES, FURNITURE, REPAIRS, PHARMACY) activées explicitement par policy, **pas de table EAV géante**.
- DB pools limités avec eviction et handles contrôlés ; pas de requête brute cross-tenant ; migration A ne modifie pas B.

### 3. Identité, MFA, sessions
- Identité acheteur globale par e-mail/mot de passe, vérification e-mail challenge one-time, reset sans enumeration, login, refresh rotation/révocation, logout; hash de mot de passe résistant, rate limit et audit sans PII.
- SMTP local-capture en dev ; **pas de SMS** ; vrai SMTP production non configuré = pas d'inscriptions réelles (fail closed).
- Staff merchant membership au bon établissement et TOTP pour fonctions sensibles, opérateurs plateforme MFA+VPN, scopes séparés. Le simple channel public ne prouve jamais les droits.
- API `/auth/v1` et `/merchant/v1` documentée, DTO validés, erreurs HTTP déterministes, credential stuffing/faux tokens interdits.

### 4. Agentic Fabric — fondation exécutable
- Structures et interfaces propriétaires opérationnelles : `AgentDefinition`, `ToolRegistry`, `ModelGateway`, `PolicyEngine`, `ToolExecutor`, `AgentRun`, `MemoryScope`, `Approval`, `AgentEventEnvelope`. Pas de chatbot factice exigé à 0.1, mais **mécanisme outil + policy réel et testable**.
- Outbox transactionnelle et enveloppe JSON Schema versionnée, ingestion idempotente et replay ; events tenant/establishment-scoped.
- Au moins 2 outils de démonstration synthétiques : lecture catalogue publique autorisée et tentative d'écriture sensible refusée sans approval. Politiques **autorisées côté backend, jamais calculées par LLM**.
- Processus d'approbation humaine lié à payloadHash/actor/tenant/TTL ; interdire relecture autre tenant, changements de prix et exfiltration ; kill-switch tenant et global.
- Adapter provider `disabled` et simulateur déterministe pour CI ; le commerce **reste disponible si IA désactivée**. Un vrai fournisseur LLM est planifié pour 0.7.0, pas requis en 0.1.

### 5. Contrats, fixtures et modèles transversaux
- Lire et corriger le draft [OpenAPI ZAMUREK](../../packages/contracts/openapi/zamurek-v1.yaml) AVANT codegen : lint/validation normative, cohérence paths/parameters/security/schemas/erreurs et opérations nécessaires 0.1 ; conserver les opérations des autres verticales comme contrats futurs explicites.
- Stabiliser `EventEnvelope` et `ToolDefinition` JSON Schema, rejets stricts. Ajouter tests de structure et génération de types utiles Kotlin/Rust/TypeScript si outillage pertinent.
- USD source/FX merchant/règle `CDF_LINE_HALF_UP_V1`, quantité canonique gramme et unités doivent posséder **types/interfaces SQL et tests de calcul pur** dès 0.1, pas nécessaire d'implémenter checkout 0.2 avant les fondations.
- Les données de test [fixtures](../../spec/v1/fixtures.json) doivent être reproductibles, organisations synthétiques et établissement E1/E2, contenu pharmacie sensible BLOCKED.

### 6. Clients installables — squelette vérifiable
- Préparer apps Android acheteur, Android marchand, Android Discover/venue avec React UI **embarquée**, Capacitor et Kotlin core, et Windows marchand + opérateur avec Tauri/Rust ; il faut au moins vérifier compilation pour les cibles réellement disponibles, avec un pipeline Windows Android réel / CI appropriée.
- UI minimale de connexion/configuration/test tenant et état serveur ; **aucun écran de simulation prétendant finalisé**. Stockage session natif, aucun secret serveur dans UI.
- Aucun frontend web de production, aucun Swagger UI public et aucune application distante hébergée ; seules API et ressources médias nécessaires sont accessibles.

## Tests de sortie P0/P1 indispensables
```
- registry DB et tenant A/B physiquement séparés ; droits A ne lisent/modifient jamais B ;
- établissements E1/E2 du tenant A n'ont pas de fuite d'autorisations ;
- email vérifié obligatoire + reset, token replay invalide, logout/refresh révoqués ;
- staff marchand et opérateur hors scope refusés ; MFA/accès VPN platform contrôlés au serveur/proxy ;
- provisioning idempotent, migration puis réexécution sans perte/collision ;
- outbox commit atomique, retry/dedup et replay sans double effet ;
- agent tool READ_PUBLIC autorisé seulement scope explicitement validé ;
- tool SENSITIVE_WRITE refusé sans approval ; changement du payload après approval refusé ;
- modèle indisponible, commerce/API registry continuent ;
- prix USD exact et 125g × 20 USD/kg × 2360 = 5900 CDF dans les tests de calcul ;
- deux familles d'applications Android et Windows préparent builds, erreur sans outil de build reportée honnêtement ;
- configuration production refuse valeurs CHANGEME/dev/test et exposition publique des routes platform ;
- toutes validations documentaires + contrats AI + manifest V1 PASS réellement.
```

## Definition of Done **0.1.0**
- API réellement démarrable localement et tests PostgreSQL réels exécutés ; builds applicables compilés ; pas de mocks pour prouver l'isolation SQL.
- Evidence test avec `command`, `exit_code`, `environment`, `commit`, `timestamp` dans `docs/implementation/REPORT-0.1.0.md`.
- `docs/implementation/PROGRESS.json` avec 38 capability IDs, jalons pondérés et calcul expliqué ; `NOT_RUN`, `SKIPPED` ou `BLOCKED` ≠ accepté.
- Révision de `docs/v1/RELEASE-GATES.md` si contrainte démontrée, ADR sur toute décision structurante, API/fixtures à jour.
- Si la CI ne peut pas vérifier Windows/Android (runner/outils), blocage de jalon documenté, **pas de mensonge « 0.1.0 100 % »**.
- **Ne pas déployer**, changer les DNS, pousser des secrets ou publier du code sensible sur dépôt public sans autorisation explicite.
