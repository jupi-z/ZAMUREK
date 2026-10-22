# ZAMUREK — venue V1 et marketplace future

**Ne pas confondre** :
- **Venue / centre commercial fédérateur est OBLIGATOIRE en V1** : découverte et répertoire opt-in d'entreprises indépendantes, produits/services publics, localisation des magasins/étages, entrée dans transactions d'un marchand.
- **Marketplace transactionnelle multi-vendeurs / encaissement collectif** n'est PAS en V1 et requiert architecture légale et financière spécifique.

Chaque entreprise/tenant possède sa propre base commerciale. Un gestionnaire d'un lieu n'a **aucun droit automatique** sur commandes, paiements, réservations ou clients de la boutique. Consentement explicite, index public asynchrone sans PII et opt-out avec invalidation cachée ; disponibilité et prix recalculés par API du marchand.

Le client Discovery/venue est un APK installable, pas un site web hébergé. Chaque commande, réservation et règlement appartient à **un seul marchand** ; paniers affichés par marchand. La venue ne collecte pas les fonds du vendeur.

Sources : [Charte V1](../v1/PRODUCT-CHARTER.md), [Parcours W8](../v1/BUSINESS-WORKFLOWS.md), [Tenancy](TENANCY.md).
