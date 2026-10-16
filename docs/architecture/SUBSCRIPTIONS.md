# SaaS xShop — un seul abonnement à 7 USD/mois

**Décision utilisateur le 16 octobre 2026** : exactement **une formule unique BASIC, 7 USD/mois par boutique**, sans frais de lancement ni commission sur les ventes V1. Évolutions de prix/plans futures versionnées sans changer rétroactivement les contrats.

## Registry
`subscription_plan('BASIC', monthlyUsdMinor=700, billingPeriod='P1M', active=true)`, `merchant_subscription(tenantId, planId, status, start, renewAt, graceUntil, cancelAt)`, `subscription_invoice`, `subscription_payment`, audit/événements. Les paiements SaaS restent séparés des achats clients (tenant DB).

## Devise
7 USD est **montant interne de référence**. Les prix publiquement affichés / factures concernant des opérateurs en RDC doivent être CDF par politique conservatoire documentée [legal](../legal/RDC-INITIAL-REVIEW.md). Conversion avec **taux plateforme distinct du taux marchand**, snapshot à l'échéance et facture, aucune nouvelle facture recalculée après paiement.

## Cycle
ACTIVE → PAST_DUE → SUSPENDED ou CANCELLED, grace period et règles d'accès/rétention à définir contractuellement. Pas de suppression automatique de commandes à suspension. Facturation/encaissement de l'abonnement à configurer avant commercialisation ; aucune « preuve fiscale » garantie.

## Évolutions
Prêt à supporter nouveaux tarifs dans le futur mais **une seule offre commercialisée au départ**. Pas de création d'une marketplace financière. Cycle de renouvellement, gestion des périodes, relances non-SMS et procédure de réactivation à spécifier dans G3/G4.

## Sources
[Décisions 2026-10-16](../DECISIONS-VALIDATED-2026-10-16.md).
