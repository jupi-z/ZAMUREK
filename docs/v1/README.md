# ZAMUREK V1 — centre de spécification

**Lecture obligatoire avant tout développement Codex.** Le dossier `docs/v1` et `spec/v1` est le corpus **normatif du produit 0.0.0 → 1.0.0**. Les anciens docs xShop sont archivés conceptuellement ; ils ne doivent pas guider la conception V1 en cas de conflit.

1. [Charte produit](PRODUCT-CHARTER.md) — identité et exigences incontournables.
2. [Matrice des 38 capacités](CAPABILITY-MATRIX.md) — engagements de la V1.
3. [Parcours métiers](BUSINESS-WORKFLOWS.md) — tous les types d'activité et venue.
4. [Modèle de domaine](DOMAIN-MODEL.md) — agrégats, multi-tenant, établissements.
5. [Politique prix, poids et arrondis exacts](MONETARY-AND-QUANTITY-POLICY.md) — règle CDF_LINE_HALF_UP_V1.
6. [Noyau agentique](AGENTIC-KERNEL.md) — sécurité, agents et outils IA dès la fondation.
7. [Contrats techniques](TECHNICAL-CONTRACTS.md) — API, clients, versionnement.
8. [Menaces/sécurité](SECURITY-THREAT-MODEL.md) — accès, privacy, anti-abus.
9. [Risques juridiques](LEGAL-REGULATED-GATES.md) — pharmacie, prix, données.
10. [Gates de qualité](QUALITY-REQUIREMENTS.md) — P0/P1, tests et preuves.
11. [Roadmap 0.0.0→1.0.0](RELEASE-GATES.md) — critères de sortie.
12. [Dossier opérationnel Codex](CODEX-HANDOFF.md) — protocole d'implémentation.

Les contrats machine : [capacités](../../spec/v1/capabilities.json), [progression](../../spec/v1/progress-template.json), [fixtures synthétiques](../../spec/v1/fixtures.json), [OpenAPI 3.1 V1](../../packages/contracts/openapi/zamurek-v1.yaml). **Attention : l'OpenAPI est un premier contrat de conception, non un backend prêt ou un schéma définitivement stabilisé.**

## Conditions à date
- Partenariat LaJoie Mall **envisagé mais non conclu**, aucune marque tierce présumée autorisée.
- Dépôt GitHub actuellement **public**, politique code propriétaire ; étudier la privatisation avant publication de cœur métier.
- Aucune exécution Android/Windows/backend, aucune CI de cette nouvelle version déclarée passée sans preuve.
- Les fonctions liées aux médicaments réglementés et les opérations juridiques non vérifiées restent fail-closed.

## Vérifications locales
```bash
python3 scripts/validate_docs.py
python3 scripts/validate_v1_scope.py
python3 scripts/validate_agent_contracts.py
python3 -m pip install -r scripts/requirements-docs.txt
python3 scripts/validate_openapi.py
```

Ces scripts garantissent des **invariants documentaires** seulement ; tests d'intégration, conformité juridique et validation runtime à réaliser pendant G1–G4.
