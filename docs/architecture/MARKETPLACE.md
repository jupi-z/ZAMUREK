# Marketplace future : canal installable additionnel

**Hors V1, compatibilité anticipée.** Le commerçant active **volontairement** l'exposition de son catalogue public dans la marketplace, avec possibilité de retrait.

## Contrat d'intégration
Référence produits (tenantId, productId, variantId) et disponibilité, tarifs **CDF et USD** distincts, aucun FX automatique. Projection centrale de catalogue opt-in consommant événements outbox, mais bases tenant restent sources de vérité ; respecter retrait et données privées.

## Identité et commandes
Identité acheteur **globale obligatoire** introduite dès V1 ; profils et commandes locaux tenant isolés. Une application marketplace Android future consomme les API versionnées, avec paniers et checkouts **mono-boutique** et monnaie sélectionnée par commande. Ni paiement fractionné ni panier inter-vendeur V1.

## Compatibilité
Les APK personnalisées continuent à fonctionner indépendamment. Aucune migration forcée de bases/identités/apps, pas de portail web marketplace. Les contrats API restent compatibles ou dépréciés avec période de support documentée.

Voir [IDENTITY](IDENTITY.md), [CURRENCY](CURRENCY-CDF-USD.md), [EVENTS](EVENTS.md).
