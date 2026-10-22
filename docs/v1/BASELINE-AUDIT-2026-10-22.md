> **NOTE HISTORIQUE :** cette baseline précédait le contrôle final. La CI a ensuite été mise au vert et les défauts OpenAPI corrigés. Voir impérativement le [rapport final d'audit](FINAL-REPO-AUDIT-2026-10-22.md) et le [prompt Codex initial](CODEX-PHASE-0.1.0-PROMPT.md) pour l'état actuel.

# Audit de préparation à Codex — ZAMUREK, 22 octobre 2026

## Périmètre audité
Dépôt `jupi-z/ZAMUREK` (`main`) passé en **public** par son propriétaire. L'ancien xShop était un projet de cadrage boutique, non un backend/API implémenté. La refonte prépare un système propriétaire universel, sans réemploi de moteur commercial complet.

## Livrables créés et soumis à GitHub
- Charte V1 complète + matrice obligatoire de **38 capacités** ; parcours pour retail, poids, food, services, mobilier, réparations, pharmacie sous restrictions, venue/mall.
- Domaine et frontières organisation/établissement/venue avec DB isolée par entreprise.
- Contrats Agentic Fabric et Event Envelope, policy+approvals+scopes, 3 assistants exigés et fallback.
- Contrat OpenAPI ZAMUREK **DRAFT** de 69 opérations, l'ancien xShop reste archive.
- Manifeste JSON machine des capacités, template progression ponderée (9 checkpoints/100%, base 0) et fixtures synthétiques de 7 commerçants.
- Gates 0.0.0→1.0.0, recette P0/P1, sécurité, régulé et revue juridique initiale.
- CI documentation, manifeste V1, contrats agent/event et OpenAPI ; scripts ajoutés à `scripts`.
- README et index dirigés vers les sources normatives ; anciennes spécifications et placeholders signalés historiques.

## Conflits d'architecture résolus
- 1 prix source USD et taux FX marchand contrôlé versionné, pas deux tarifs indépendants.
- Auth client e-mail vérifié sans SMS, pas compte invité.
- Organization=DB métier isolée, establishment=sous-entité sécurisée, venue=agrégateur opt-in, pas partage implicite de clientèle/ventes.
- Distribution uniquement apps installables, production API-only, operator via VPN.
- Vente/médicaments soumis à réglementation **fail-closed**, aucune promesse de dispense.
- IA outil métier autonome sous permissions et validation humaine, pas un modèle autorité.

## Vérifications réellement faites dans l'édition
- Toutes les créations/mutations revendiquées ont retourné un commit GitHub.
- Audit statique de références `$ref`/IDs au moment de génération du nouveau contrat : 69 `operationId` et 63 chemins sans duplicat textuel ou `$ref` à composant absent.
- Manifest JSON construit par sérialisation, 38 objets P0/P1, template des poids somme=100, fixtures synthétiques.
- Relecture des chemins Markdown principaux ; schémas des liens canoniques examinés.

## Limitations : NE PAS qualifier de PASS sans preuve
- **CI GitHub Actions : exécution réussie NON CONSTATÉE** via les outils disponibles. Le workflow est écrit, mais le résultat runner et ses logs doivent être contrôlés.
- **OpenAPI : brouillon structurel, non validation normative complète**. Il contient des schemas initialement typés à affiner en G1. Les contraintes de domaine sont en docs/v1.
- **Licence transitive : scan non exécuté** ; aucun lockfile applicatif ni packages installés.
- **Applications : non implémentées**, aucun APK/EXE/MSI, test runtime, intégration DB, redteam IA ni benchmark.
- **Infrastructure / légal : non validés** (VPS, DNS, SMTP, fournisseurs modèles, contrat, professions réglementées, BCC/DGI).
- **Propriété intellectuelle** : dépôt public ; avant pousser le moteur métier propriétaire, revérifier stratégie de dépôt privé. Les Actions fonctionnent en privé sous les quotas du compte.

## Conditions de « prête pour Codex »
Les sources normatives, le protocole de travail et les premiers tests statiques sont en place. Codex commence par **faire passer réellement la CI** et corriger ses échecs, stabiliser les contrats, construire `0.1.0`, publier rapport/PROGRESS.json. Le statut **prêt pour développement** ne signifie pas **prêt pour commercialisation**.

## Autorité
[CODEX-HANDOFF](CODEX-HANDOFF.md), [RELEASE-GATES](RELEASE-GATES.md), [CAPABILITY-MATRIX](CAPABILITY-MATRIX.md).
