# Roadmap de convergence : Monarque Connect 10A.5 ↔ ZAMUREK 0.0.0→1.0.0

**Statut 22/10/2026 : planifié, pas livré.** Produit V1 ZAMUREK **complet et non MVP** ; implémentation progressive par preuves. Les gates Core et produit restent distincts.

| Vague | Core Monarque Connect propriétaire | ZAMUREK (apps/specs) | Critère bloquant |
|---|---|---|---|
| P0 / Alignement | 10A.5 C0 – audit, ADR-039, contrats partagés | ADR-0024, charte, ancien prompt invalidé, catalogue capabilities révisé | Documents/contrats compatibles et CI des deux dépôts |
| P1 / Core interface | 10A.5 C1-C3 + C6/C7 – identity/tenancy/entitlement/pricing/events/API seam | 0.1.0 : fondations clients/SDK/contrats/maquettes avec tests sur Core | Pas de deuxième Core, 2 organisations/2 établissements sécurisés, contracts versionnés |
| P2 / Commerce & POS | 10A.5 C4/C5 – cash transactionnel, factures/reçus et printer contract | 0.2.0 : retail, poids, checkout public, POS Android/Windows, impression réelle | Commande unique cash/online, PDF/ticket validé, fiscal gate |
| P3 / Verticaux | Core use cases conservés, backend domain extensions mutualisés | 0.3 restaurant, 0.4 salon, 0.5 meubles/réparations, 0.6 pharmacie autorisée/venue | 1 commande canonique, réservation anti collision, privacy venue |
| P4 / Intelligence | 10B AI gouvernée + 11.5 agents, 11 entitlements multi-produits | 0.7 : trois assistants IA utilisant le même gateway/runtime, 0.8 : apps complètes | Pas de double Agentic Fabric, tool permissions, coût, E2E apps |
| P5 / Release | 12 : hardening Core, CI, backup, sécurité et conformité | 0.9 : tests bout en bout; 1.0 : une seule ouverture commerciale complète | Tous les gates P0/P1, licences, accès, DGI/pharmacie, matériel, légaux |

## Dépendances explicites
- Aucun compte client acheteur ZAMUREK ne doit déclencher `OrganizationMembership` staff.
- Ventes POS sans compte d'acheteur, mais compte caissier authentifié.
- Factures SaaS FairScale indépendantes des factures commerçants, même plateforme Billing.
- Une DB partagée avec isolement logique, pas une DB par commerce avant V1.
- ZAMUREK public n'héberge ni secrets ni code backend transactionnel propriétaire ; à rendre privé avant code applicatif sensible, Actions disponibles aussi en privé.
- Compatibilité anciens clients Monarque Connect, pas de migration forcée de monnaie.
- Activation de ZAMUREK seule ne débloque pas modules Monarque Connect non inclus.

## Passage à Codex
**NE PAS utiliser** l'ancien [prompt 0.1.0](CODEX-PHASE-0.1.0-PROMPT.md) : remplacé par [nouvelle session d'intégration ZAMUREK](CODEX-INTEGRATION-PROMPT.md) après C0–C3/C6/C7 Core. **Avant cela**, Codex doit travailler dans le dépôt **privé** Monarque Connect pour la phase 10A.5 : instructions dans `Docs/113_CODEX_PHASE_10A5_FIRST_PROMPT.md`.

## Condition commerciale
7 USD/mois/organization = **cible**, pas marge garantie. Doivent être décidés le nombre d'établissements inclus, quotas et coûts d'IA/transactions, règles de facturation CDF/taxes, et le fournisseur ou procédure de fiscalisation requise.
