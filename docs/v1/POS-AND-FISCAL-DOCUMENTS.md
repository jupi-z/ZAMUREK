# ZAMUREK V1 — ventes sur place, encaissements, caisses et documents

**Normatif pour V1 ; non implémenté.** Les services financiers et de numérotation résident **exclusivement dans Monarque Connect Core**. L'app ZAMUREK est une interface installée capable de piloter une imprimante locale. **La frontière normative du Core est fixée par Docs/114 (PR Monarque Connect #152). Les endpoints POS ne sont pas encore livrés.**

## Périmètre de vente physique
- Un commerce peut vendre physiquement en boutique, au restaurant, en salon, à un comptoir de réparation ou stand sans connexion de l'acheteur.
- Caissier/terminal authentifiés et autorisés dans `organizationId+establishmentId`, session de caisse ouverte et traçable; pas de compte client exigé en passage `WALK_IN`.
- Recherche catalogue/variante/code-barres ou saisie d'offre; produits PCS, 125 g de chocolat, pizza+supplément, prestation, pièce/reparation approuvée; devis/recalcul serveur; prix CDF affiché selon droit RDC et snapshots.
- Mêmes produits, devises contractuelles, disponibilités, commandes et flux financiers que le canal online, origine `POS`, `RESTAURANT` etc. Une suppression de catalogue n'efface pas l'historique commercial.

## Entités Core nouvelles / étendues
| Agrégat | Champs principaux / invariants |
|---|---|
| `PosTerminal` | id, org, establishment, alias, statut, device registration non-secret |
| `CashSession` | terminal, cashier, openedAt/closedAt, float initial par monnaie, statut, réconciliation |
| `PosSale` | salesOrderId canonique, terminal/session, client walk-in facultatif, idempotency, état |
| `SaleTender` | mode CASH/MANUAL_TRANSFER/OTHER_MANUAL_ALLOWED, reçu, montant accepté, monnaie due, monnaie rendue |
| `CashReconciliation` | attendu/compte par devise, écart, justification, superviseur, horodatage |
| `CommercialPrintJob` | document canonique/version/checksum, format, appareil local, état demande ; n'implique PAS fiscalisation |
| `DocumentFiscalization` | juridiction/statut PENDING/AUTHENTICATED/BLOCKED/NOT_APPLICABLE, fournisseur homologué/référence, preuve et journal |

## Vente comptoir atomique
**Règle V1 :** chaque vente POS encaissée s'appuie sur Invoice du Core afin de ne pas briser le contrat `PaymentRecord.invoiceId`. Ce document interne n'autorise pas à imprimer une facture fiscalement normalisée sans processus homologué. Une vente cash 5 900 CDF encaissée sur 10 000 CDF remis enregistre 4 100 CDF rendus et une entrée Cash **nette de 5 900 CDF**. Retry client/timeout ne double ni invoice, ni PaymentRecord, ni mouvement de caisse.

1. `OPEN_SESSION` avec fonds d'ouverture; validation RBAC et établissement.
2. `CREATE_QUOTE` prix serveur, poids exact, réductions/TVA selon profil, version FX et expiration.
3. `CONFIRM_POS_SALE` transaction unifiée pour SalesOrder, **Invoice canonique interne obligatoire**, PaymentRecord lié par `invoiceId` non nullable, CashMovement **net si espèces**, validation stock, audit, idempotency, Outbox ; le document fiscal légal reste distinct et bloqué jusqu'à preuve applicable. `amountTendered` ≥ `amountDue` cash, `change` = remis − dû ; monnaie rendue n'est **pas** du chiffre d'affaires.
4. `ISSUE_RECEIPT/INVOICE` via renderer Core; imprimer localement ticket 58/80 mm ou A4, QR uniquement si produit par fiscalisation légalement valable. Un reçu ordinaire ne doit **pas** être présenté comme facture normalisée DGI.
5. Clôture de caisse : total théorique, comptage physique, écarts, justification, supervisor approval si seuil ; rapprocher chaque paiement/mouvement, ne pas « effacer » une correction.

## Cas importants
- **Paiement mixte** cash + transfert manuel seulement après validation du processus et distinction montant dû/confirmé; preuve de transfert ≠ paiement confirmé. Rendu monnaie par devise et caisse configurées.
- Retours, remboursements cash, annulations et erreurs de caissier font transactions inverses auditables; jamais suppression silencieuse de SalesOrder/facture.
- Coupure réseau : écran signale transaction incertaine, recherche par `Idempotency-Key` et état serveur avant relance ; **pas de vente réputée confirmée hors-ligne en V1**.
- App locale doit découvrir ou configurer imprimantes supportées et gérer erreurs papier/connexion sans dupliquer la vente ni invalider une facture émise.
- Compte de caisse déjà présent dans Monarque Connect ; les sessions POS complètent Cash, pas nouveau ledger.
- Intégration fiscale RDC : modalités légales / certification à vérifier ; mise en vente bloquée si des pièces authentifiées sont légalement exigées et non disponibles.

## Recette minimale
Exiger aussi vérification de non-régression des anciens Sales/Invoice/PaymentRecord/Cash et KPI 10A, permissions POS dédiées (sans ADMIN/FINANCE général), paiement externe finalisé seulement après preuve signée, impression post-commit sans duplication et adaptateur de stockage réel testé. `TECH_PASS` ne vaut pas `COMMERCIAL_GO` tant que fiscalité/PSP/appariels ne sont pas prouvés.

E2E vente cash CDF à client de passage : quote→sale→paiement→cash movement→reçu/ticket 80 mm; retry/replay simultané = **1 commande, 1 paiement, 1 cash entry**. Échec impression ≠ double commande. Prix chocolat 125g à 20 USD/kg×2360=5900 CDF exact. Multi-caissiers/établissements, fermeture caisse, fonds insuffisants, remboursements, sale online parallèle et droit d'accès testés. Factures A4 et fiscales selon droit confirmé, sans simulation frauduleuse.

## Propriété et livraison
Backend Core privé Monarque Connect ; pont imprimante Android Kotlin/Windows Tauri Rust dans ZAMUREK. Contrats sécurité et DTO versionnés entre dépôts, docs d'exploitation, vidéos/captures d'impression sur matériel réel avant V1.
