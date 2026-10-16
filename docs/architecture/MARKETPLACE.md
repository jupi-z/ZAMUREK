# Marketplace future xShop — client installable et opt-in

**Hors V1.** Réutilise identité globale, contrats API, canal additionnel, sans remplacer les APK individuelles ni fusionner les DB de commerçants.

## Catalogue
L'index de découverte recopie **seulement les informations de vente publiques opt-in** de chaque marchand, sous sa politique territoriale. Chaque prix source reste stocké **en USD dans DB tenant**, avec taux USD→CDF actif versionné par marchand ; l'index RDC publie **prix CDF converti** et date/identifiant de version, rafraîchi via outbox. Prix final toujours recalculé/confirmé par la source tenant au checkout.

## Commande
Acheteur compte e-mail vérifié, panier mono-boutique, devis/commande en CDF RDC, modalités propres à chaque marchand. Pas de paiement split ni transfert entre DB V1 ; jamais de transaction cross-tenant.

## Compatibilité
Apps marque restent actives ; vendeur peut activer/désactiver opt-in ; les anciennes commandes gardent snapshot FX. Aucune interface web hébergée pour marketplace.

Voir [FX](FX-PRICING.md), [règles légales](../legal/RDC-INITIAL-REVIEW.md), [EVENTS](EVENTS.md).
