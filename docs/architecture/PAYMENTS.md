# Commandes, paiements et réconciliation

## Politique initiale
L'encaissement revient **directement à chaque commerçant** ; xShop fournit le logiciel, sans collecte ni reversement des fonds en V1. Ce choix est un défaut réversible à valider contractuellement (voir questions ouvertes).

## Modes V1
- PAY_ON_DELIVERY : commande enregistrée, paiement PENDING ; le commerçant marque PAID après encaissement réel, avec trace.
- MANUAL_TRANSFER : afficher instructions du commerçant et référence ; déclarer AWAITING_CONFIRMATION, jamais PAID sur seule déclaration de l'acheteur.

## États distincts
La commande suit son propre workflow ; le paiement possède des états PENDING / AWAITING_CONFIRMATION / PAID / FAILED / CANCELLED ; REFUNDED réservé aux opérations futures. Une commande COMPLETED peut nécessiter un contrôle de paiement suivant le mode et la politique tenant.

## Calcul
Unit price minor × quantity en précision entière ; addition des lignes, frais livraison, total. Pas de conversion multi-devise V1. Snapshot irréversible à la création ; changement de prix catalogue ne modifie pas une commande existante.

## Transaction checkout
- Vérifier tenant, disponibilité commerciale, variantes, devises, modes de remise, quantités demandées et coordonnées.
- Idempotency-Key scoped par tenant + session + endpoint + empreinte du contenu, TTL documenté à l'implémentation.
- Écrire commande, lignes, événement outbox et résultat de la clé dans une transaction tenant.
- Réémettre le même résultat au retry identique ; un payload divergent avec même clé renvoie 409.

## Intégration électronique future
Interface PaymentProvider : createIntent, verifyCallbackSignature, parseEvent, reconcile, refund (si supporté). Webhooks vérifiés, horodatage/nonce quand disponible, déduplication provider_event_id, comparaison montant/devise/tenant/commande avant mutation ; aucun callback du client n'authentifie une transaction financière.

## Comptabilité et responsabilités
xShop V1 ne remplace pas un ERP, une caisse fiscale, une preuve de paiement externe ni une comptabilité réglementaire. Factures fiscales, taxes, remboursements, litiges et conformité du PSP nécessitent spécification juridictionnelle et validation.

## Risques à traiter
Chargeback, faux SMS de transfert, paiement double, annulation alors que payé, indisponibilité PSP, réconciliation et webhook tardif ; blocages pour lancement électronique tant que non testé.

