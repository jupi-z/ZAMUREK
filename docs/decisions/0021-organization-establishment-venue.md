# ADR-0021 — Organization, Establishment et Venue indépendants

**Statut ADOPTÉ — 2026-10-22**

Une Organization exploite une DB commerciale PostgreSQL isolée, avec **plusieurs établissements et plusieurs activités**. `establishmentId` figure dans permissions et agrégats pertinents ; l'app merchant peut basculer entre établissements autorisés.

Le `Venue`/mall est une collection tierce d'emplacements et de vendeurs **opt-in**, avec projection publique minimale. Le gestionnaire venue **n'a pas** accès aux commandes ni à la clientèle des vendeurs du fait de l'inscription au centre. Transactions et paiements restent mono-vendeur, sans escrow ni multi-tenant SQL distributed transaction.

L'identité client globale s'authentifie une fois, puis chaque ressource requiert authz tenant/establishment/object. Une même organization peut avoir plusieurs établissements avec différents calendriers, menus, devis et taux si la politique décidée le permet ; **taux FX par commerçant/organisation** avec possibilité d'héritage et configuration établissement explicitement versionnée si ajout futur.

Voir [domain model](../v1/DOMAIN-MODEL.md) et [security](../v1/SECURITY-THREAT-MODEL.md).
