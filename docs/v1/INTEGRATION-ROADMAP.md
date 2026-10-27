# Roadmap de convergence : Monarque Connect 10A.5 ↔ ZAMUREK 0.0.0→1.0.0

**Statut 27/10/2026 : cadrage produit, pas de connexion runtime livrée.** Produit V1 ZAMUREK **complet et non MVP** ; implémentation progressive par preuves. Les gates Core et produit restent distincts. La PR Core #152 est encore à fusionner; ses contrats et invariants Docs/114–116 sont prérequis aux interfaces qui les utilisent.

| Vague | Core Monarque Connect propriétaire | ZAMUREK (apps/specs) | Critère bloquant |
|---|---|---|---|
| P0 / Alignement | 10A.5 C0 – audit, ADR-039, contrats partagés | ADR-0024, charte, prompt invalidé, catalogue des 43 capacités | Documents cohérents; PR/CI des deux dépôts |
| P1 / Core interface | C1–C3 + C6/C7, selon leurs contrats effectivement stabilisés | Fondations client/SDK et tests contractuels uniquement pour les interfaces prouvées | OpenAPI allowlist versionnée, SHA source attesté, aucun code serveur dupliqué |
| P2 / Commerce & POS | 10A.5 C4/C5 – cash transactionnel, factures/reçus et printer contract | 0.2.0 : retail, poids, checkout public, POS Android/Windows, impression réelle | SalesOrder + Invoice + PaymentRecord + CashMovement net au besoin, stock et ticket ; fiscal gate |
| P3 / Verticaux | Core use cases conservés, backend domain extensions mutualisés | 0.3 restaurant, 0.4 salon, 0.5 meubles/réparations, 0.6 pharmacie autorisée/venue | 1 commande canonique, réservation anti collision, privacy venue |
| P4 / Intelligence | 10B AI gouvernée + 11.5 agents, 11 entitlements multi-produits | 0.7 : trois assistants IA utilisant le même gateway/runtime, 0.8 : apps complètes | Pas de double Agentic Fabric, tool permissions, coût, E2E apps |
| P5 / Release | 12 : hardening Core, CI, backup, sécurité et conformité | 0.9 : tests bout en bout; 1.0 : une seule ouverture commerciale complète | Tous les gates P0/P1, licences, accès, DGI/pharmacie, matériel, légaux |

## Dépendances explicites
- Facturation SaaS : souscriptions par `productCode`, anciennes API Monarque Connect préservées ; seuls les use cases POS bornés sont accessibles depuis une offre ZAMUREK-only.
- Caisse : staff POS scoped, aucun `ADMIN/FINANCE` de contournement ; Invoice canonique avant PaymentRecord, rendu de monnaie hors chiffre d'affaires, sortie de stock atomique.
- Identité : Monarque Auth/OIDC futur branché via contrat d'identité sans réécrire `userId` ni promouvoir un BUYER en membre staff.
- Documents : stockage durable en environnement réel, imprimante après commit, fiscalisation RDC uniquement avec preuve applicable ; IA indisponible ne bloque pas une vente.

- Aucun compte client acheteur ZAMUREK ne doit déclencher `OrganizationMembership` staff.
- Ventes POS sans compte d'acheteur, mais compte caissier authentifié.
- Factures SaaS FairScale indépendantes des factures commerçants, même plateforme Billing.
- Une DB partagée avec isolement logique, pas une DB par commerce avant V1.
- ZAMUREK et Monarque Connect sont observés publics au 27/10/2026. N'y publier aucun secret, donnée ou code dont la confidentialité est requise ; la visibilité doit être décidée séparément par le propriétaire avant la publication d'éléments sensibles. Les Actions peuvent aussi fonctionner sur un dépôt privé selon plan et quotas.
- Compatibilité anciens clients Monarque Connect, pas de migration forcée de monnaie.
- Activation de ZAMUREK seule ne débloque pas modules Monarque Connect non inclus.

## Passage à Codex
**NE PAS utiliser** l'ancien [prompt 0.1.0](CODEX-PHASE-0.1.0-PROMPT.md). Le [prompt d'intégration](CODEX-INTEGRATION-PROMPT.md) doit être appliqué par étapes : cadrage documentaire libre; SDK/tests seulement pour les contrats Core stabilisés; intégration runtime après les commandes Core correspondantes; commercialisation après gates complets. La PR #2 reste en draft tant que le contrat Core minimal/versionné et sa provenance SHA ne sont pas gelés. Les phases 10B, 11, 11.5 et 12 restent requises uniquement aux capacités qui en dépendent, pas comme attente globale automatique.

## Condition commerciale
7 USD/mois/organization = **hypothèse non approuvée, inactive et non publiable comme prix**. Le nombre d'établissements, quotas, coûts IA/transactions, facturation CDF/taxes et fiscalisation doivent être évalués avant toute décision commerciale.
