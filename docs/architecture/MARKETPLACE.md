# ZAMUREK — venue opt-in et découverte V1

Le **venue/mall est requis en V1** pour découverte multi-entreprises, emplacements, étages, regroupements volontaires et visibilité publique consentie. Une marketplace transactionnelle multivendeur avec paiements collectifs/escrow est **hors V1**.

**Toutes les organisations partagent l'infrastructure PostgreSQL Core Monarque Connect, pas des bases individuelles**, mais restent isolées par `organizationId/establishmentId/ownership`. Le gestionnaire d'un centre n'a aucun accès automatique à commandes, clients, réservations, paiements, factures, caisses ou données agents des magasins. Opt-out supprime listing et projection/cache sans effacer les données privées du marchand.

Une application Discover peut naviguer parmi les entreprises, mais chaque panier/checkout/commande et règlement appartient à un vendeur unique, exécuté par Sales/Cash Core. Les identités et marques LaJoie Mall ne sont pas autorisées sans contrat explicite.

Voir [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [Core](../v1/SHARED-CORE-INTEGRATION.md), [parcours W8](../v1/BUSINESS-WORKFLOWS.md).
