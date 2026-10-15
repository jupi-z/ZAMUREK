# Paiements, montants et commande — V1

**Décisions approuvées :** CDF/USD simultanément dans chaque boutique ; paiement à la livraison ou transfert manuel ; encaissement **direct marchand**, jamais xShop collecteur en V1.

## Prix par devise
- Chaque variante publiable possède prix distincts CDF et USD ; chaque zone de livraison possède frais distincts CDF et USD.
- Aucun taux de conversion ni valeur FX implicite. Le client sélectionne une monnaie avant checkout, le backend calcule tout dans cette monnaie, la capture est immuable.
- Int64 en unités mineures par devise ; sérialisation JSON chaîne décimale. Voir [currency](CURRENCY-CDF-USD.md).
- Aucun mélange de monnaies dans un panier, une commande, une transaction ou un montant affiché sans étiquette.

## Checkout
Bearer client obligatoire, vérification tenant + ownership panier + versions de prix/disponibilité. Idempotency-Key scoped tenant + client + endpoint + request fingerprint ; transaction tenant avec order/order_items/payment/outbox/idempotency record. Retry identique retourne résultat sans créer de doublon. Changement de montant au checkout explicite et reconfirmé côté client.

## Paiements
- PAY_ON_DELIVERY : commande PENDING, marchand confirme reçu réellement, journalisé.
- MANUAL_TRANSFER : instructions et coordonnées configurées par marchand **dans la monnaie de la commande** ; preuve fournie par client peut être enregistrée, mais PAS une confirmation. Seul marchand habilité après vérification rapprochement passe PAID.
- Paiement dans autre devise / partiel : cas exceptionnel traité manuellement hors automatisation V1, pas d'état PAID par défaut.
- Statut de paiement séparé du statut de préparation/livraison et transition contrôlée.

## Annulation
Client dépose demande ; marchand décide et journalise. Commande déjà payée ou livrée : ne pas faire transition naïve vers CANCELLED ni simuler remboursement ; workflow cas par cas et obligations légales à clarifier.

## Facturation
Aucune garantie fiscale DGI, aucune taxation calculée sans règles confirmées ; montant commande et preuve paiement ne valent pas facture fiscale homologuée. Vérifier responsabilités et modalités locales avant lancement.

## Extension future
PaymentProvider abstrait, webhooks signés, idempotents, capture/confirmation serveur, rapprochement, remboursements/chargebacks par prestataire autorisé ; pas d'engagement PSP électronique V1.
