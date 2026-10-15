# Spécifications fonctionnelles — V1

**Statut : contrat produit initial ; aucune fonction ci-dessous n'est encore implémentée.**

## Rôles
- Visiteur : explorer les produits publics.
- Acheteur invité : créer panier et commande, consulter sa commande via preuve de possession (jeton non devinable).
- Merchant owner : gérer informations boutique, produits, commandes et utilisateurs.
- Merchant staff : gérer catalogue et commandes suivant permissions.
- Platform operator : créer / suspendre / inspecter état technique des tenants ; jamais lire les commandes sans justification, autorisation et audit.

## Catalogue
- Produit : ID opaque, titre, description, catégorie, images, prix en unités monétaires mineures, devise ISO, statut DRAFT/ACTIVE/HIDDEN/UNAVAILABLE/ARCHIVED, variantes facultatives (options et prix propres).
- Recherche texte simple, tri et pagination cursor/offset plafonnée ; aucune exposition des brouillons.
- Pas de quantité disponible / entrepôt V1. La quantité demandée dans le panier reste possible, mais n'est pas une quantité en stock.
- Validation serveur des montants, images, options, produit actif, catégorie et statut.

## Panier
- Panier rattaché à **une seule boutique** et à un appareil/session (non à un identifiant de tenant libre).
- Ajouter, modifier quantité et retirer ; limites configurables ; calcul côté serveur à chaque mutation.
- Le panier est temporaire ; il peut expirer ; aucune promesse de prix bloqué avant validation de commande.
- Le jeton secret du panier est délivré à la création puis conservé par Kotlin ; GET/PATCH ne renvoient pas à nouveau ce secret.

## Livraison
- Le commerçant configure RETRAIT / LIVRAISON et ses zones / frais.
- L'adresse et le téléphone sont requis pour livraison ; informations de contact adaptées au retrait.
- Les zones de livraison sont sélectionnées à partir de la configuration tenant et validées serveur.
- Aucune géolocalisation ni suivi GPS du livreur en V1.

## Commande
- Au checkout, le serveur revalide les produits, frais, mode de règlement et montants, puis crée une commande immuable quant aux prix et intitulés capturés.
- L'opération est idempotente via une clé client par tentative, avec portée tenant + canal + acteur.
- Numéro de commande visible propre au tenant ; ID interne global opaque.
- Statuts V1 : PLACED, ACCEPTED, PREPARING, READY, OUT_FOR_DELIVERY, COMPLETED, CANCELLED.
- Transitions autorisées explicites : PLACED→ACCEPTED/CANCELLED ; ACCEPTED→PREPARING/CANCELLED ; PREPARING→READY/CANCELLED (si autorisé) ; READY→OUT_FOR_DELIVERY ou COMPLETED ; OUT_FOR_DELIVERY→COMPLETED ; les transitions impossibles renvoient 409.
- Annulation côté client après commande : demande au marchand, non automatique en V1 ; politique configurable par boutique.
- Échec partiel ou double soumission : aucune création dupliquée ni double débit.

## Paiement
- Méthodes minimales : PAY_ON_DELIVERY et MANUAL_TRANSFER (si activées pour le tenant).
- États de paiement indépendants : PENDING, AWAITING_CONFIRMATION, PAID, FAILED, REFUNDED (réservé aux futures intégrations), CANCELLED.
- MANUAL_TRANSFER ne devient PAID qu'après vérification de marchand habilité ; l'acheteur ne peut pas auto-certifier son paiement.
- Les paiements électroniques utilisent plus tard une interface provider-agnostic avec webhooks signés et idempotents.

## Suivi acheteur
- Un jeton secret de suivi propre à la commande est retourné une seule fois à la création, stocké sous forme hachée serveur, sans données sensibles dans l'URL publique.
- Répéter la consultation nécessite cette preuve ; mécanisme futur de récupération par vérification d'identité.
- La réponse client masque les informations sensibles du personnel et de la plateforme.

## Administration boutique
- Catalogue CRUD, chargement média contrôlé, visibilité, suivi/statuts, validation de paiement manuel, paramètres livraison/contact, gestion d'employés suivant leurs rôles.
- Toutes les opérations sensibles produisent une entrée d'audit contextualisée.

## Administration plateforme
- Provisionner tenant, préparer credentials, appliquer migrations, configurer application + canaux, états PROVISIONING/ACTIVE/SUSPENDED/FAILED, vue de santé et audit.
- Support inter-tenant strictement motivé, contrôlé et journalisé.
- Suppression définitive : hors parcours self-service V1.

## Vues mobiles indispensables
Accueil, recherche/catalogue, détail produit, panier, mode de remise et contact, confirmation, suivi, erreurs réseau, vide, chargement, tenant désactivé, mise à jour incompatible.

## Accessibilité et localisation
FR V1, contraste lisible et tailles de cible tactiles adaptées ; devises affichées selon devise du tenant. Les formats ne doivent pas modifier les valeurs monétaires stockées.

## Critères de recette
Voir [acceptation](../quality/ACCEPTANCE.md). La spécification OpenAPI documente la surface prévue, non son implémentation.

