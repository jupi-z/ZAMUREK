# Index documentaire ZAMUREK — 22 octobre 2026

**Corpus normatif pour la V1 : [docs/v1/README](v1/README.md).** Le cadrage xShop ancien est historique et ne pilote plus le développement. Le statut du code applicatif reste `NOT_IMPLEMENTED`.

## Référence produit, architecture et recette
- [Charte produit](v1/PRODUCT-CHARTER.md)
- [Matrice des fonctionnalités](v1/CAPABILITY-MATRIX.md)
- [Parcours commerce / services](v1/BUSINESS-WORKFLOWS.md)
- [Prix/poids/arrondi CDF exact](v1/MONETARY-AND-QUANTITY-POLICY.md)
- [Domaine et isolation multi-établissements](v1/DOMAIN-MODEL.md)
- [Architecture agentique native](v1/AGENTIC-KERNEL.md)
- [Contrats techniques et sécurité API](v1/TECHNICAL-CONTRACTS.md)
- [Menaces et défense](v1/SECURITY-THREAT-MODEL.md)
- [Légal RDC et activités réglementées](v1/LEGAL-REGULATED-GATES.md)
- [Qualité / release gates](v1/QUALITY-REQUIREMENTS.md), [Versions 0.0.0 → 1.0.0](v1/RELEASE-GATES.md)
- [Passage à Codex](v1/CODEX-HANDOFF.md)

## Données machine
- [Manifeste 38 capacités](../spec/v1/capabilities.json)
- [Template de progression](../spec/v1/progress-template.json)
- [Données synthétiques de test](../spec/v1/fixtures.json)
- [OpenAPI ZAMUREK draft](../packages/contracts/openapi/zamurek-v1.yaml)

## Gouvernance
- [Décision propriété du moteur](decisions/0019-proprietary-platform-permissive-oss.md)
- [Politique licences permissives](governance/OPEN-SOURCE-POLICY.md)
- [Revue juridique RDC existante](legal/RDC-INITIAL-REVIEW.md)
- [Registre des ADR](decisions/README.md)
- [Pré-requis encore ouverts](OPEN-QUESTIONS.md)

## Archives xShop
- [Arbitrages du 16/10](DECISIONS-VALIDATED-2026-10-16.md)
- [PRD historique](product/PRD.md), [spécifications historiques](product/V1-FUNCTIONAL-SPEC.md)
- [Contrat historique xShop](../packages/contracts/openapi/xshop-v1.yaml)

En cas de divergence, appliquer le corpus ZAMUREK `docs/v1`, inscrire une ADR, corriger les anciens liens actifs. La documentation n'est pas un produit fonctionnel.
