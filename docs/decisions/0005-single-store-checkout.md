# ADR-0005 — Panier et commande mono-boutique

**Statut : adopté V1 | Date : 2026-10-15**

## Décision
Un panier appartient à une seule boutique ; le checkout crée une commande et son paiement dans une transaction de la base de cette boutique. Idempotency-Key obligatoire.

## Alternatives
Panier et paiement global multi-vendeur dès le départ, nécessitant compensation entre DB et PSP.

## Conséquences
Simplicité et fiabilité V1 ; dans marketplace initiale, paniers/commandes indépendants par boutique. Migration vers panier multi-vendeur exige nouveau contrat.

## Révision
Après validation opérationnelle d'une marketplace mono-boutique et définition des PSP.

