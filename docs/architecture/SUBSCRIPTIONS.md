# ZAMUREK BASIC — une offre SaaS 7 USD/mois

**Décision de travail V1 :** une formule BASIC à **7 USD mensuels par Organization commerçante** (une organisation peut disposer de plusieurs établissements), sans frais d'installation ni commission sur ventes. Les modalités de limitation raisonnable, de facturation commerciale en CDF RDC, taxes et contrats doivent être documentées et acceptées avant encaissement réel.

## Registry
`subscription_plan(code='BASIC', monthlyUsdMinor=700, period='P1M')` ; `merchant_subscription(organizationId, planId, state, cycle, grace)`, `subscription_invoice`, `subscription_payment`, audit, entitlement(s). Aucune confusion avec les ventes dans DB tenant. Il n'existe qu'une offre commercialisée à la sortie V1, plan extensible sous nouvelles ADR.

## Cycle
ACTIVE → PAST_DUE → SUSPENDED / CANCELLED avec grace window, notification in-app/e-mail selon accord. Suspension ne supprime pas la DB, historiques, factures ou réservations sans procédure légale/contractuelle. Retours/export après résiliation selon contrat.

## Devise
Référence interne 700 cents USD ; documents commerciaux RDC affichés CDF **selon règlementation applicable**, avec taux **plateforme** distinct de la conversion des marchands. Historiser snapshot taux/date/montant lors de chaque facture ; pas de modification rétroactive.

## Gate vente réelle
CGV/contrat, taxes, capacité support, périmètre de compte et plusieurs établissements, limites d'usage, modalités de paiement, suspension/remboursement/rétention et notification légale doivent être formellement validés ; aucun logiciel de facturation fiscale certifié n'est présumé.

Voir [charte V1](../v1/PRODUCT-CHARTER.md) et [LEGAL](../v1/LEGAL-REGULATED-GATES.md).
