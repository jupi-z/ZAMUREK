# Compatibilité future avec une marketplace

**Hors V1.** L'objectif est la compatibilité architecturale, non sa livraison immédiate.

## Invariants dès V1
- Identifiants immuables de tenants, produits et commandes, avec tenant explicite dans les références cross-store.
- API versionnée indépendante du canal de présentation.
- Config public catalogue et visibilité ; réglages d'opt-in de découverte (non activés automatiquement).
- Identités globales préparées mais données clients locales isolées et accès soumis à consentement.
- Checkout mono-tenant obligatoire : aucune commande traverse plusieurs DB.

## Agrégation future
Indexer **uniquement le catalogue public opt-in** dans une projection centrale : tenantId, productId, title, category, image URL publique, prix indicatif, devise, visibilité, updatedAt, sourceVersion.
Source de vérité : base tenant. Répliquer via outbox / consommateur idempotent ; traiter suppressions, désinscriptions, retard d'index et reconstruction complète.

## Parcours marketplace conseillé
Découverte de produits de différents commerçants, fiches et paniers **par boutique**. Au premier lancement marketplace, demander un checkout indépendant pour chaque boutique : limite le risque financier, la coordination et l'annulation distribuée.

## Si panier multi-vendeur plus tard
Créer une intention globale non financière et des commandes enfants indépendantes, chacune dans sa DB. Gérer compensation et états partiels de façon explicite ; jamais prétendre à transaction ACID distribuée. Paiements fractionnés/reversement exigent choix PSP et conformité spécifique.

## Compatibilité ascendante
Les apps propriétaires continuent à parler directement au canal enregistré de leur tenant. Marketplace est un canal additionnel, non un remplacement. Tests contractuels croisés obligatoires.

## Dépendances
Architecture outbox et opt-in catalogue, matrice de consentement, index externe, choix des commissions et règles de service client. Voir [events](EVENTS.md) et [identity](IDENTITY.md).

