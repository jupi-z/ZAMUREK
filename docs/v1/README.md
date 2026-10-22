# ZAMUREK V1 — centre de spécification après convergence Monarque Connect

**Sources normatives :** [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [Core partagé](SHARED-CORE-INTEGRATION.md) et [charte V1](PRODUCT-CHARTER.md). La version 1.0.0 reste complète (pas un MVP) et nécessite les **43 capacités obligatoires**.

## Ordre de lecture
1. [Core Monarque Connect ↔ ZAMUREK](SHARED-CORE-INTEGRATION.md)
2. [POS physique, encaissements, impression/facturation](POS-AND-FISCAL-DOCUMENTS.md)
3. [Charte produit](PRODUCT-CHARTER.md) et [matrice fonctionnelle](CAPABILITY-MATRIX.md)
4. [Roadmap coordonnée](INTEGRATION-ROADMAP.md) et [release gates](RELEASE-GATES.md)
5. [Parcours multi-activités](BUSINESS-WORKFLOWS.md) et [modèle de domaine](DOMAIN-MODEL.md)
6. [Prix/FX/poids exact](MONETARY-AND-QUANTITY-POLICY.md), [contrats techniques](TECHNICAL-CONTRACTS.md)
7. [Runtime IA partagé](AGENTIC-KERNEL.md), [menaces et sécurité](SECURITY-THREAT-MODEL.md), [gates légaux](LEGAL-REGULATED-GATES.md)
8. [Qualité](QUALITY-REQUIREMENTS.md), [acceptation clients 0.1.0](PHASE-0.1.0-ACCEPTANCE.md)
9. [Handoff Codex](CODEX-HANDOFF.md) et [prompt intégration clients](CODEX-INTEGRATION-PROMPT.md)

## Contrats machine
[43 capacités JSON](../../spec/v1/capabilities.json) · [progression vérifiée](../../spec/v1/progress-template.json) · [fixtures synthétiques](../../spec/v1/fixtures.json) · [OpenAPI ZAMUREK DRAFT avant convergence](../../packages/contracts/openapi/zamurek-v1.yaml) · [contrats événements/outils DRAFT](../../packages/contracts/events/event-envelope.schema.json).

**Autorité OpenAPI runtime = Monarque Connect Core privé** versionné ; ne pas traiter `zamurek-v1.yaml` comme un serveur réel ou lancer l'ancien [prompt autonome](CODEX-PHASE-0.1.0-PROMPT.md).

## Dépendances
- La phase Core **10A.5 C0–C3/C6/C7** est requise avant la clôture de ZAMUREK 0.1.0; C4/C5 avant 0.2.0 POS/fiscal.
- Les applications ZAMUREK sont **non réalisées** dans le dépôt ; les tests CI YAML/Markdown ne démontrent pas la production.
- Monarque Connect est privé, ZAMUREK est public : aucun code backend Core, secrets, données client ou clés de modèle ne doit être publié ici.
- LaJoie Mall reste **partenariat hypothétique** ; médicaments réglementés restent bloqués jusqu'aux preuves juridiques.

## Vérifications de conception
```bash
python3 scripts/validate_docs.py
python3 scripts/validate_v1_scope.py
python3 scripts/validate_convergence.py
python3 scripts/validate_agent_contracts.py
python3 -m pip install -r scripts/requirements-docs.txt
python3 scripts/validate_openapi.py
```

Aucun `PASS` documentaire ne remplace un test PostgreSQL réel, une impression physique, une facture fiscalisée ou l'évaluation d'un agent IA.
