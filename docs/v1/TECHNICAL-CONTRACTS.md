# ZAMUREK — contrats d'intégration Core (V1)

**Statut : SPECIFICATION non implémentée.** Monarque Connect est la **seule autorité pour l'API transactionnelle** ; son contrat OpenAPI existe dans le dépôt privé et évolue via la phase 10A.5. Le fichier local `packages/contracts/openapi/zamurek-v1.yaml` est **PRE-CONVERGENCE DRAFT** : ses routes `/v1/*` ne sont pas des endpoints prouvés et ne doivent PAS être utilisées pour générer un backend ZAMUREK autonome. Voir [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [intégration](SHARED-CORE-INTEGRATION.md).

## Politique d'API
- Préfixe canonique serveur Monarque Connect `/api/v1/`. Le module ZAMUREK peut exposer une façade spécifique `/api/v1/zamurek/*` et/ou endpoints Core enrichis, sous contrats OpenAPI publics et privés séparés.
- Toute mutation requiert actor/identity valable, `organizationId` autorisé, `establishmentId`, entitlement par produit, ownership, idempotence; un channel public `X-Zamurek-Channel` ne donne aucun privilège.
- Achat *online* : buyer e-mail vérifié et propriétaire de la commande ; achat **POS walk-in** : buyer non enregistré mais caissier autorisé avec session ouverte. Pas de compte fictif/staff membership pour acheteurs.
- Transactions dans Core : quote pricing versionnée → SalesOrder `origin` → PaymentRecord → CashMovement si cash → outbox, atomique et idempotente.
- Détails API POS : [POS et impression](POS-AND-FISCAL-DOCUMENTS.md). Full CRUD, erreurs et security OpenAPI **à créer et tester pendant 10A.5**, pas s'appuyer sur esquisse actuelle.

## Transports / codes
REST 200/201/202/204, erreurs 400/401/403/404/409/422/429/503 sans révéler existence d'autres ressources. `Idempotency-Key` tenant/actor/operation/payload-hash obligatoire sur mutations critiques. Heure UTC + timezone IANA établissement, quantité `DecimalExact` string, prix serveur, politique CDF territoriale sans float.

## Produits, versions et entitlements
`productCode = MONARQUE_CONNECT|ZAMUREK` ; `ZAMUREK_BASIC` à 7 USD/mois cible, droits aux modules commerciaux nécessaires uniquement. Un org peut souscrire l'un, l'autre ou les deux sans duplication des commandes. Le serveur contrôle la séparation, pas React/Capacitor.

## API spécialisées à définir dans le Core (exigées V1)
- Discovery public opt-in, listings et disponibilités par venue (lecture filtrée).
- Catalogue typé, produits pondéraux, menus/options, devis, heures et slots.
- Checkout public mono-vendeur, order status et annulations sous ownership.
- POS caissier, sessions, tender/cash, cash reconciliation, PDF/ticket/rendu fiscal.
- Réservation services/tables avec contrainte concurrence, cuisines, devis/repairs.
- Agents via gateway partagé, aucune route arbitrant argent hors policy.
- Console opérateur via réseau privé VPN/MFA.

## Contrats sous contrôle de version
Core maintient schémas OpenAPI et événements canoniques, CI génère/adapte SDK TS/Kotlin/Rust pour ZAMUREK et vérifie compatibilité clients APK/EXE. Le client ZAMUREK consomme un artefact versionné identifié par `coreCommitSha + contractVersion`. Aucun schéma manuel divergant ne peut être déclaré `runtime ready`.

## Réalisation
La phase Core 10A.5 est préalable aux contrats financiers. Le jalon ZAMUREK 0.1.0 teste sessions/permissions et SDK contre vrais endpoints Core **dès qu'ils sont disponibles**. POS et fiscalisation attendent 10A.5 C4–C5; ne jamais produire une fausse facture DGI ni un succès mock de paiement.
