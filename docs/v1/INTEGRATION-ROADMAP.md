# Roadmap de convergence : Monarque Connect 10A.5 ↔ ZAMUREK 0.0.0→1.0.0

**Statut vérifié le 28/10/2026 :** C0–C2 sont clôturés. Core main 2dff07eae662d8de186d6f23cf831dd72c1dfec9, CI post-fusion #170 [run 40635438412](https://github.com/jupi-z/Monarque-Connect/actions/runs/40635438412) réussie; preuves C1 [Docs/118](https://github.com/jupi-z/Monarque-Connect/blob/main/Docs/118_C1_CLOSURE_EVIDENCE.md) et C2 [Docs/121](https://github.com/jupi-z/Monarque-Connect/blob/main/Docs/121_C2_CLOSURE_EVIDENCE.md). C3 est autorisée (issue #171), mais le contrat est en préparation et aucun endpoint catalogue/pricing/FX n'est livré. Pas de runtime ZAMUREK ni de contrat Core allowlisté. Produit V1 complet, pas un MVP; les gates Core et produit restent distincts.

| Vague | Core Monarque Connect propriétaire | ZAMUREK (apps/specs) | Critère bloquant |
|---|---|---|---|
| P0 / Alignement | 10A.5 C0–C2 clôturés; C3.1 contrat en préparation, C3.2–C3.4 non commencés | ADR-0024, charte, catalogue des 43 capacités | Preuves C0–C2 liées depuis main; aucun runtime ni prix ZAMUREK activé |
| P1 / Core interface | Contrats C1/C2 internes; C3 catalogue/pricing seulement proposé | SDK/tests uniquement après stabilisation d'un contrat Core correspondant | Pas d'API C3 runtime ou allowlistée; version et SHA source requis avant intégration |
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
- ZAMUREK et Monarque Connect sont observés publics au 28/10/2026. N'y publier aucun secret, donnée ou code dont la confidentialité est requise ; la visibilité doit être décidée séparément par le propriétaire avant la publication d'éléments sensibles. Les Actions peuvent aussi fonctionner sur un dépôt privé selon plan et quotas.
- Compatibilité anciens clients Monarque Connect, pas de migration forcée de monnaie.
- Activation de ZAMUREK seule ne débloque pas modules Monarque Connect non inclus.

## Passage à Codex
**NE PAS utiliser** l'ancien prompt 0.1.0. Le prompt d'intégration suit D-09 : cadrage documentaire libre; SDK/tests après contrat Core stable et versionné; intégration réelle après livraison de l'opération Core. La PR #2 reste en draft; C3 n'est pas encore un contrat consommable. 10B, 11, 11.5 et 12 ne sont requis que par les capacités qui en dépendent.

## Condition commerciale
7 USD/mois/organization = **hypothèse non approuvée, inactive et non publiable comme prix**. Le nombre d'établissements, quotas, coûts IA/transactions, facturation CDF/taxes et fiscalisation doivent être évalués avant toute décision commerciale.
