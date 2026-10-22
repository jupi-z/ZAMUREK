# ZAMUREK — index documentaire normatif (révision du 22 octobre 2026)

**Décision principale :** [ADR-0024](decisions/0024-shared-monarque-core-zamurek.md) — ZAMUREK est une extension produit/clients omnicanal du **Core Monarque Connect**, pas un deuxième backend. Les archives xShop et les textes antérieurs contradictoires sont supplantés.

## Consulter d'abord
- [Centre de spécification](v1/README.md) et [charte V1](v1/PRODUCT-CHARTER.md)
- [Core partagé](v1/SHARED-CORE-INTEGRATION.md), [vente physique/POS/impression](v1/POS-AND-FISCAL-DOCUMENTS.md)
- [Matrice des 43 capacités](v1/CAPABILITY-MATRIX.md) et [manifest JSON](../spec/v1/capabilities.json)
- [Roadmap synchronisée Core 10A.5/ZAMUREK](v1/INTEGRATION-ROADMAP.md) et [gates de version](v1/RELEASE-GATES.md)
- [Conceptions métier](v1/BUSINESS-WORKFLOWS.md), [domaine](v1/DOMAIN-MODEL.md), [agent runtime partagé](v1/AGENTIC-KERNEL.md), [contrats API](v1/TECHNICAL-CONTRACTS.md)
- [Prix/poids CDF exact](v1/MONETARY-AND-QUANTITY-POLICY.md), [sécurité](v1/SECURITY-THREAT-MODEL.md), [legal RDC](v1/LEGAL-REGULATED-GATES.md), [qualité](v1/QUALITY-REQUIREMENTS.md)
- [Préparer Codex dans Core privé puis ZAMUREK](v1/CODEX-HANDOFF.md), [nouveau prompt](v1/CODEX-INTEGRATION-PROMPT.md), [recette 0.1.0](v1/PHASE-0.1.0-ACCEPTANCE.md)

## Gouvernance / CI
[Registre des ADR](decisions/README.md) · [dépendances open source](governance/OPEN-SOURCE-POLICY.md) · [pré-requis](OPEN-QUESTIONS.md) · [progression](../spec/v1/progress-template.json) · [fixtures](../spec/v1/fixtures.json).

**Pré-convergence / archives, non exécutables :** [ancien prompt 0.1.0](v1/CODEX-PHASE-0.1.0-PROMPT.md), [OpenAPI ZAMUREK brouillon non canonique](../packages/contracts/openapi/zamurek-v1.yaml), [OpenAPI historique xShop](../packages/contracts/openapi/xshop-v1.yaml), [spécifications xShop](product/PRD.md), [audit préalable devenu historique](v1/FINAL-REPO-AUDIT-2026-10-22.md). Ce dernier document décrivait l'état **avant** la convergence, il n'est pas une validation des nouvelles exigences.

Toute CI documentaire verte n'est **pas** une certification du backend Core, des agents ni des POS physiques.
