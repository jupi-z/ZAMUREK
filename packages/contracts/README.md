# ZAMUREK — contrats clients consommateurs du Core Monarque Connect

**Nouveau contrat canonique du runtime : celui de Monarque Connect** (repo privé, `openapi/`, `contracts/`) versionné pendant sa phase 10A.5. Ce dossier ZAMUREK publie uniquement les **SDK/types clients générés, suites de tests d'intégration et métadonnées de compatibilité** `coreCommitSha + coreContractVersion`.

- [zamurek-v1.yaml](openapi/zamurek-v1.yaml) : **DRAFT AVANT CONVERGENCE**, 69 opérations fictives de cadrage, **NON** un backend réellement disponible. Ne l'utiliser ni pour codegen runtime définitif ni pour reconstruire un Core.
- [xshop-v1.yaml](openapi/xshop-v1.yaml) : **ARCHIVE HISTORIQUE**, ne pas utiliser.
- [agent-tools/tool-definition.schema.json](agent-tools/tool-definition.schema.json) et [events/event-envelope.schema.json](events/event-envelope.schema.json) : brouillons de validation à harmoniser avec les schémas canoniques Monarque Connect et classes A0–A4.
- Contrats nécessaires au futur Core : buyer versus staff identities, POS walk-in/terminal/cash session/tenders/print jobs, commerce mono-vendeur, invoices/FX, Agent tools, entitlements par produit.

Le pipeline doit détecter toute divergence de version et les breaking changes pour les APK/EXE installés. Le Swagger/console web n'est pas hébergé en production.

Voir [contrats normatifs](../../docs/v1/TECHNICAL-CONTRACTS.md), [POS](../../docs/v1/POS-AND-FISCAL-DOCUMENTS.md) et [ADR](../../docs/decisions/0024-shared-monarque-core-zamurek.md).
