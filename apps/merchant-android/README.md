> **ZAMUREK V1 :** App marchand multi-établissement, cuisine, caisse, réservations et agentique avec approval. La source de vérité est [Charte V1](../../docs/v1/PRODUCT-CHARTER.md) et [Parcours métiers](../../docs/v1/BUSINESS-WORKFLOWS.md). L'ancien descriptif xShop ci-dessous reste historique.

# Marchand Android xShop — G0 non implémenté

Application séparée de l'acheteur ; React UI + Capacitor/Kotlin pour réseau, persistance, OS et sessions. E-mail/mot de passe, MFA TOTP pour rôles sensibles.

Gestion : produits et variantes **prix source USD seul**, zones et frais de livraison source USD, **taux USD→CDF marchand configurable**, version/audit, disponibilité sans stock chiffré, commandes/snapshots CDF, paiement livraison/transfert manuel, demandes d'annulation, équipe selon membership.

Pas de double prix CDF autonome, pas de SMS, pas de console web hébergée, accès strict tenant et objet. Route plateforme opérateur hors de portée de cette app.

Voir [FX](../../docs/architecture/FX-PRICING.md), [NETWORK](../../docs/architecture/NETWORK-EXPOSURE.md).
