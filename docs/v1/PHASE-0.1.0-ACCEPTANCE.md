# ZAMUREK 0.1.0 — fondations clientes / intégration Core

**NOUVELLE recette normative du 22/10/2026, remplace l'ancien plan de recréation du backend**. Statut : PLANNED, **0 % vérifié**. Lire [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [intégration](SHARED-CORE-INTEGRATION.md) et [POS](POS-AND-FISCAL-DOCUMENTS.md).

## Dépendance bloquante
- `Monarque-Connect` privé doit publier des contrats testables de **phase 10A.5 C0–C3/C6/C7** et CI succès, identifiant SHA de l'OpenAPI canonique. En attendant, travailler sur apps/layouts et clients synthétiques mais ne pas clôturer 0.1.0.
- C4–C5 seront nécessaires pour la recette complète POS/vente comptoir 0.2.0, pas pour compiler le shell Android initial.

## À réaliser **dans ZAMUREK**
1. Monorepo clients reproductible (pnpm/lockfile, scripts UI typecheck/lint/test/build). Aucune création `apps/api` NestJS transactionnelle ni Prisma registry ; les squelettes legacy restent archives ou sont réorientés vers adaptateurs clients.
2. `packages/contracts` contient uniquement **références vérifiables aux contrats versionnés du Core** et types clients générés; l'OpenAPI `zamurek-v1.yaml` précédent est marqué DRAFT/PRE-CONVERGENCE, pas autorité du runtime. Diff canonique client à chaque CI.
3. Android acheteur marque, Android marchand et Android discovery/venue : UI React/Capacitor embarquée, Kotlin sécurisé, session client e-mail, rôles employés séparés, affichage état de connexion; APK réellement compilés sur runner adéquat ou statut NOT_RUN.
4. Windows commerçant/caissier et Windows opérateur : Tauri 2/Rust, application installable; appels opérateur uniquement VPN+MFA, aucune interface web hébergée. Test d'installation sur runner Windows ou statut bloqué honnête.
5. Client API typé, navigation par établissement, catalogue public et découverte opt-in sur fixtures; simulation UI admise pour développement, **aucune fausse commande, règlement ou facture prétendue terminée**.
6. Tests d'intégration contre **vrai backend Core** de staging local synthétique : autorisation buyer vs staff, organisation A/B et établissements A1/A2, provenance des prix CDF, fidélité contrat API et erreurs. Pas de DB commerciale ZAMUREK.
7. Traces de sécurité/session : aucun secret de Core dans JS/React/installeurs, chiffrement stockage mobile/native, expiry/revoke, pas de contournement CORS/Channel.
8. Intégration contractuelle minimale de l'Agent Runtime commun en read-only ; aucun orchestrateur IA concurrent.
9. Maintenir documentation, `spec/v1/capabilities.json`, `spec/v1/progress-template.json`, CI et rapport evidence sans fake.

## Gates de sortie
- Applications squelettes compilables sur plateformes couvertes (Android/Windows), un chemin Core auth/tenant/catalogue testé réellement, contract diff exact, protections ownership négatives, CI de spécification et builds réels verts.
- Aucune marque partenaire LaJoie Mall présumée autorisée.
- Aucun POS/règlement/fiscalisation revendiqué comme complet avant implémentation Core C4/C5 et E2E réel.
- Rapport `docs/implementation/REPORT-0.1.0.md` avec commandes, versions, résultats et blocages, progression locale/globale vérifiable. NOT_RUN/BLOCKED ≠ PASS.

L'ancienne instruction 0.1.0 de démarrer un second NestJS/PostgreSQL/registry était incompatible et a été **annulée**.
