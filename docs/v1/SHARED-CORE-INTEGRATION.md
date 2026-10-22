# ZAMUREK V1 — architecture normative d'intégration à Monarque Connect

**Statut : spécification de convergence ; aucune connexion runtime livrée.** Le Core dans le dépôt privé `https://github.com/jupi-z/Monarque-Connect` possède déjà NestJS/Prisma/PostgreSQL et des modules Sales, Cash, Billing, Items, Tenancy, Event Fabric. ZAMUREK ne les duplique pas.

## Séparation des responsabilités
| Source canonique | Détient / modifie | Dépôt |
|---|---|---|
| Monarque Connect Core | Organization/Establishment, identity, scopes, FairScale multi-produits, Item, quotes/prices, SalesOrder, Invoice, PaymentRecord, CashMovement, taxes, FX context, fiscal documents, Event Fabric, AI Gateway/Agent Runtime | privé `Monarque-Connect` |
| Extensions ZAMUREK intégrées au Core | cuisine/table, rendez-vous/staff, poids/options, devis meubles, réparations, venue opt-in/index, POS terminal/session/tender | implémentation backend **dans Monarque Connect** avec modules isolés |
| ZAMUREK applications | Android acheteur/marchand/discovery, Windows caissier/marchand, thème marque et console opérateur autorisée, appareil imprimante (Kotlin/Rust), contrats client/protocoles de test | dépôt ZAMUREK, code privé si IP sensible |
| Contrats communs | OpenAPI canonique Core `/api/v1`, event schemas, identity/tenant/product scoping, tool schemas et versionning | **Core est source de vérité**, ZAMUREK consomme contrats versionnés/générés |

La même organisation peut détenir l'offre ZAMUREK seule, Monarque Connect seule ou les deux. **Une seule instance métier et un seul historique canonique**, sans réplication bidirectionnelle ventes/argent.

## Données et sécurité
- `organizationId` vérifié serveur ; `establishmentId` + actor + objectOwner et permissions à chaque commande ; shared PostgreSQL Core, pas de connexion tenant DB depuis client.
- Client web/app acheteur ZAMUREK s'authentifie par e-mail pour checkout, mais **ne devient pas staff/membership**. Vente POS `walk-in` ne requiert pas d'inscription acheteur ; identité obligatoire du caissier.
- `Venue` publie seulement données consenties, sans lecture finances/PII même pour gestionnaire du mall. Commandes **mono-vendeur**.
- Le public `X-Zamurek-Channel` est un routage de canal, pas une preuve d'autorisation ; backward compatibility de l'API existante requise.
- Aucun traitement d'ordonnance pharmaceutique non autorisée ; actes règlementés fail-closed.

## Transactions et événements
- Checkout online/POS passe par use cases canoniques : quote autorisée → commande avec `origin` → facture/reçu selon juridiction → tender PaymentRecord → CashMovement si cash → outbox. **Atomicité transactionnelle pour tous les effets financiers internes** ; aucun success client tant que commit cohérent non obtenu.
- `Item` demeure générique, `offering` et spécificités métiers = profils étendus, pas un deuxième catalogue autonome. Prix source USD uniquement sur politiques d'offres ZAMUREK, préserver devise Monarque Connect existante.
- Événements ZAMUREK suivent Event Fabric canonique de Monarque Connect avec tenant/scope/provenance, pas enveloppe concurrente. AI agents utilisent les tool handlers du Core.
- App POS connectée V1 ; hors-ligne transactionnel hors V1 (l'UI peut présenter dernier catalogue mais **ne confirme jamais une vente offline**).

## Conventions d'API
Les routes `/v1/*` du `packages/contracts/openapi/zamurek-v1.yaml` sont un brouillon pré-convergence. Pour runtime réel, adopter **`/api/v1` Monarque Connect** et éviter les conflits d'identité, de pricing et de permissions. Les fonctionnalités publiques ZAMUREK doivent être des endpoints distincts à droits réduits, jamais exposer directement l'API financière staff à des jetons acheteur. Les API/DTO historiques Monarque Connect sont rétrocompatibles.

## Phasage / dépendances
1. Monarque Connect 10A.5 C0→C3 et C6/C7 : interface/stabilité contractuelle.
2. ZAMUREK 0.1.0 : socle client installable, SDK/types contractuels, faux commerçants, tests d'intégration réels sur les endpoints disponibles, jamais duplicate Prisma service.
3. Monarque Connect 10A.5 C4/C5 : POS, cash atomique, documents print/fiscaux ; ZAMUREK réalise interface imprimeur et E2E.
4. 10B partagé → 11/11.5 → produits sectoriels complets → release 12/Core et ZAMUREK 1.0.0 sous gates séparés.

## Gate de développement
Aucun travail ne peut être déclaré terminé si non testé sur le vrai Core. Mock API n'est acceptable que pour UI provisoire, **pas** comme preuve de transaction financière ni de release. CI et tests Core devront fournir commit SHA, version du contrat, logs des cases multi-tenant et progression vérifiée.

Référence Core sur branche de planification : `planning/phase-10a5-zamurek-convergence` (tant qu'elle n'est pas fusionnée).
