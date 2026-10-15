# Abonnement mensuel xShop — modèle commercial et technique

**Décision validée : xShop est facturé par abonnement mensuel uniquement. Aucun pourcentage ou commission sur les ventes des commerçants en V1.**

## Séparation financière
- **Abonnement xShop** : payé par le marchand au fournisseur du logiciel ; enregistré dans le domaine `platform-subscription` du registre central, sans mélanger les écritures commerciales tenant.
- **Paiements des achats** : acheteur → marchand directement (livraison ou transfert manuel) ; enregistrés dans **DB tenant**, pas dans la facturation SaaS.
- Les PSP de l'abonnement xShop et les moyens d'encaissement des ventes peuvent être totalement distincts.

## Entités de conception
subscription_plan(id, name, currency, monthlyAmountMinor, isActive, effectiveAt) ; merchant_subscription(id, tenantId, planId, status, cycleStart, cycleEnd, trialEndsAt?, canceledAt?) ; subscription_invoice(id, tenantId, cycle, amountMinor, currency, status) ; subscription_payment(id, subscriptionInvoiceId, method, verificationStatus, paidAt?) ; subscription_event/audit.

Montant, devise, frais de mise en route (interdits par décision « abonnement uniquement »), essai, taxes et règlement restent à arbitrer **avant vente**, non avant le prototype technique.

## Cycle proposé
DRAFT → ACTIVE → PAST_DUE → SUSPENDED / CANCELLED. Émission de facture d'abonnement du fournisseur logiciel distincte des documents de vente du commerçant. Une période de grâce éventuellement nécessaire sera fixée contractuellement.

## Préservation des données
La suspension d'un abonnement ne détruit pas automatiquement la DB tenant ni les commandes historiques ; accès/modes bloqués selon droits et contrat. Export, réactivation, résiliation, rétention et effacement documentés par contrat et règles applicables. Un marchand ne peut pas contourner les restrictions en changeant de canal APK.

## Portée par phase
G1 : modèles et statuts tenant prêts pour extensibilité, pas d'encaissement SaaS obligatoire. G4/G5 : abonnement réel, conditions contractuelles, facture/confirmation, suspension/réactivation testée avant commercialisation.

## Décisions externes en attente
Tarif, modalités de règlement, cycle de facturation, conditions de retard/réactivation, taxes, support inclus, politique de suppression/export. Pas de « conformité fiscale » supposée.

Voir [ADR-0014](../decisions/0014-monthly-saas-merchant-collection.md), [blocages](../OPEN-QUESTIONS.md).
