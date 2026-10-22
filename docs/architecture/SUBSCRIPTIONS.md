# ZAMUREK — abonnement produit séparé dans FairScale Core

**Planifié ; pas d'abonnement réel ZAMUREK seedé/facturé à ce stade.** Le propriétaire a retenu une **cible à 7 USD/mois par organisation** et aucune commission sur les ventes, mais cela ne permet pas d'affirmer que **tous** les établissements/utilisateurs/canaux sont sans limite au même prix.

## Core Billing
Monarque Connect conserve son catalogue de plans et le moteur Billing/FairScale. Introduire `productCode=ZAMUREK`, `ZAMUREK_BASIC`, `planVersion`, `subscription`, `effectiveEntitlements` indépendants de `MONARQUE_CONNECT`. Une seule Organization peut détenir les deux produits et conserver ses commandes canoniques. Un marchand ZAMUREK seul ne peut ouvrir CRM, Achats, Projets ou modules Business/Enterprise.

## Quotas et fiscalité à valider
Avant facturer : nombre inclus d'établissements, terminaux, caissiers, offres, consommations IA, frais de support, stockage, sauvegarde, coût moyen par client, croissance et conditions de suspension. Les planchers/limites FairScale historiques ne sont pas automatiquement effacés. Factures SaaS **séparées** des factures de vente du marchand, prix commercial en CDF selon droit local et snapshot taux plateforme distinct du taux commerçant.

## Tests
ZAMUREK-only, MC-only, double abonnement même org, upgrade/downgrade, suspension sélective, changement quota établissement, aucun droit non entitled, pas de double prélèvement ni effacement de factures/commandes à la résiliation.

Références : [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [open questions](../OPEN-QUESTIONS.md).
