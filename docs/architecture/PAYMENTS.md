# Checkout et paiements — modèle 16 octobre 2026

## Prix et conversion
Chaque produit/variante et zone de livraison a un tarif **USD interne unique**. Le commerçant règle `usdToCdf` versionné. Le backend convertit tous les montants affichés/commandés en **CDF** pour les ventes en RDC selon politique territoriale ; montants en unités mineures, arrondis explicites, aucun calcul JavaScript faisant autorité.

## Devis et commande
GET/POST devis côté serveur avec taux versionné et TTL, vérification du prix/source USD, taux et état au checkout, changement avant confirmation = nouveau devis avec acceptation client. Snapshot immuable USD, CDF, taux, date et policy dans order et lignes. Idempotency-Key sur checkout, transaction dans DB du tenant, aucun panier cross-tenant.

## Encaissement V1
Direct commerçant, PAY_ON_DELIVERY et MANUAL_TRANSFER. Prix public, validation commande et preuve/facture en CDF. **Paiement effectivement remis en USD** : option future à activer seulement après validation du cadre RDC et une procédure de rapprochement explicite (devise reçue, taux utilisé, équivalent CDF, preuve), jamais un marquage PAID automatique.

## Annulation
Le client dépose une demande ; marchand accepte/refuse selon conditions. Déjà payé = traitement spécifique, ne pas prétendre rembourser automatiquement.

## Abonnement plateforme
Un seul plan BASIC 7 USD/mois. Conversion de présentation CDF pour clients RDC utilise **taux plateforme distinct** (pas le taux commerçant) ; contrats et TVA à vérifier. Aucune commission sur commandes.

## Risques
Référence taux 2360 fournie par le porteur n'est **pas un cours officiel** ; BCC publie ses propres cours. Les règles du droit de publicité des prix et facture locale conditionnent G4.

Voir [FX](FX-PRICING.md), [revue juridique](../legal/RDC-INITIAL-REVIEW.md).
