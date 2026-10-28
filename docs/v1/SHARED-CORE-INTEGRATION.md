# ZAMUREK V1 — architecture normative d'intégration à Monarque Connect

**Statut : spécification de convergence; aucune connexion runtime ZAMUREK livrée.** Monarque Connect est le Core transactionnel NestJS/Prisma/PostgreSQL. C0–C2 sont clôturés sur main 2dff07eae662d8de186d6f23cf831dd72c1dfec9 (CI post-fusion #170 run 40635438412 réussie; preuves C2 Docs/121). C3 est autorisée, mais le contrat catalogue/pricing/FX reste en préparation; aucun endpoint ou contrat externe allowlisté n'est disponible.

## Séparation des responsabilités
| Source canonique | Détient / modifie | Dépôt |
|---|---|---|
| Monarque Connect Core | Organization/Establishment, identity, scopes, FairScale, Item historique, SalesOrder, Invoice, PaymentRecord, CashMovement et Event Fabric. Catalogue commercial multi-produit, pricing et FX sont au cadrage C3, non runtime. Fiscal documents partagés et AI Gateway/Agent Runtime restent des objectifs non livrés | dépôt propriétaire Monarque-Connect; visibilité GitHub publique |
| Extensions ZAMUREK intégrées au Core | cuisine/table, rendez-vous/staff, poids/options, devis meubles, réparations, venue opt-in/index, POS terminal/session/tender | implémentation backend **dans Monarque Connect** avec modules isolés |
| ZAMUREK applications | Android acheteur/marchand/discovery, Windows caissier/marchand, thème marque et console opérateur autorisée, appareil imprimante (Kotlin/Rust), contrats client/protocoles de test | dépôt ZAMUREK ; éviter d'y publier code ou données dont la confidentialité est requise |
| Contrats communs | OpenAPI canonique Core `/api/v1`, event schemas, identity/tenant/product scoping, tool schemas et versionning | **Core est source de vérité**, ZAMUREK consomme contrats versionnés/générés |

La même organisation peut détenir l'offre ZAMUREK seule, Monarque Connect seule ou les deux. **Une seule instance métier et un seul historique canonique**, sans réplication bidirectionnelle ventes/argent.

## Données et sécurité
- La fédération future d'authentification Monarque Auth/OIDC ne change pas l'identité métier interne et les droits Core ; distinguer principals BUYER/STAFF/AGENT, aucun rôle staff via e-mail/checkout. `X-Zamurek-Channel` et le choix produit ne constituent jamais une autorisation. Chaque staff POS possède action, établissement et terminal/session autorisés ; pas de rôle global FINANCE/ADMIN pour contourner la caisse.
- ZAMUREK-only et Monarque-Connect-only ont des souscriptions isolées par `productCode`. Une activation ZAMUREK n'ouvre aucun endpoint métier ERP hors ses commandes POS bornées, et la suspension d'un produit ne supprime pas l'autre.

- `organizationId` vérifié serveur ; `establishmentId` + actor + objectOwner et permissions à chaque commande ; shared PostgreSQL Core, pas de connexion tenant DB depuis client.
- Client web/app acheteur ZAMUREK s'authentifie par e-mail pour checkout, mais **ne devient pas staff/membership**. Vente POS `walk-in` ne requiert pas d'inscription acheteur ; identité obligatoire du caissier.
- `Venue` publie seulement données consenties, sans lecture finances/PII même pour gestionnaire du mall. Commandes **mono-vendeur**.
- Le public `X-Zamurek-Channel` est un routage de canal, pas une preuve d'autorisation ; backward compatibility de l'API existante requise.
- Aucun traitement d'ordonnance pharmaceutique non autorisée ; actes règlementés fail-closed.

## Transactions et événements
- Opérations PSP et impression **hors transaction SQL**, avec validation webhook signée/intent durable pour les fonds externes ; commande cash atomique interne et idempotente, stock et contrôle de caisse revalidés dans la transaction. L'adaptateur de documents doit être persistant/chiffré et audité avant toute exploitation POS réelle : le stockage mémoire du Core reste test-only.

- Checkout online/POS passe par use cases canoniques : quote autorisée → SalesOrder avec `origin` → **Invoice canonique interne** → PaymentRecord (lien Invoice obligatoire) → CashMovement **net** si espèces → Outbox ; reçu/tax invoice sont des documents distincts de la pièce interne selon fiscalité. **Atomicité transactionnelle pour tous les effets financiers internes** ; aucun success client tant que commit cohérent non obtenu.
- `Item` demeure l'entité canonique historique. Le catalogue commercial/pricing C3 doit le prolonger dans le Core, sans second catalogue; cette capacité est encore proposée et n'est pas runtime. Les prix USD ne pourront être employés que par une politique ZAMUREK explicitement approuvée; préserver la devise historique de chaque organisation.
- Événements ZAMUREK suivent Event Fabric canonique de Monarque Connect avec tenant/scope/provenance, pas enveloppe concurrente. AI agents utilisent les tool handlers du Core.
- App POS connectée V1 ; hors-ligne transactionnel hors V1 (l'UI peut présenter dernier catalogue mais **ne confirme jamais une vente offline**).

## Conventions d'API
Les routes `/v1/*` du `packages/contracts/openapi/zamurek-v1.yaml` sont un brouillon pré-convergence. Pour runtime réel, adopter **`/api/v1` Monarque Connect** et éviter les conflits d'identité, de pricing et de permissions. Les fonctionnalités publiques ZAMUREK doivent être des endpoints distincts à droits réduits, jamais exposer directement l'API financière staff à des jetons acheteur. Les API/DTO historiques Monarque Connect sont rétrocompatibles.

## Phasage / dépendances selon D-09
1. Avant contrats stables : cadrage fonctionnel, UX, maquettes et revue de frontières dans ZAMUREK.
2. Après stabilisation d'un contrat Core nécessaire (version, allowlist, SHA source, tests de compatibilité) : SDK, clients de base et tests contractuels correspondant à ce contrat peuvent avancer; les interfaces non disponibles restent explicitement en attente.
3. Après livraison et vérification d'une commande transactionnelle Core : l'intégration fonctionnelle réelle de ce parcours peut commencer. Les mocks ne prouvent jamais les transactions Core.
4. 10B, 11, 11.5 et 12 sont des dépendances par capacité (IA, administration, readiness agents, hardening/release), pas un verrou global sur des clients ou contrats indépendants. La commercialisation ZAMUREK attend l'ensemble des gates techniques et externes applicables.

## Gate de développement
Aucun travail ne peut être déclaré terminé si non testé sur le vrai Core. Mock API n'est acceptable que pour UI provisoire, **pas** comme preuve de transaction financière ni de release. CI et tests Core devront fournir commit SHA, version du contrat, logs des cases multi-tenant et progression vérifiée.

Référence Core sur branche de planification : `planning/phase-10a5-zamurek-convergence` (tant qu'elle n'est pas fusionnée).
