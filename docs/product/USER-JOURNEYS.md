# Parcours V1 et cas d'échec

## Visiteur → achat invité
1. L'application installée initialise son identifiant de canal et récupère la configuration publique de sa boutique.
2. Affichage produits paginés ; un produit indisponible n'est pas commandable.
3. Ajout produit au panier : validation serveur, retour de montants recalculés et de la devise.
4. Choix retrait/livraison ; choix zone, frais, coordonnées, remarques.
5. Dernière vérification serveur ; commande unique créée avec clé d'idempotence.
6. Affichage confirmation, numéro et jeton de suivi local sécurisé.
7. Consultation du statut avec preuve de possession du jeton.

## Marchand → exécution
1. Connexion propriétaire ou employé et contrôle RBAC propre au tenant.
2. Affichage commandes de sa boutique uniquement.
3. Acceptation, préparation, disponibilité/retrait ou expédition, complétion.
4. Vérification documentée d'un transfert manuel si utilisé.
5. Toute modification de statut enregistre acteur, origine, date et résultat.

## Plateforme → ouverture d'une boutique
1. Validation données de commerce et unicité de slug/app ID.
2. Création registre PROVISIONING, réservation des identifiants.
3. Génération credentials et base dédiés, migrations vérifiées, bucket/namespace médias.
4. Tests de connexion et d'isolation, publication de configuration canal.
5. Activation seulement quand les contrôles réussissent ; sinon FAILED et compensation.

## Échecs obligatoirement traités
- Produits devenus indisponibles au checkout : 409 + panier actualisé, sans créer la commande.
- Paiement manuel non confirmé : commande créée, paiement PENDING/AWAITING_CONFIRMATION.
- Réseau perdu pendant POST : retry avec **la même clé** d'idempotence ; lecture d'état ensuite.
- Tentative de lire tenant B via token tenant A : rejet, audit et test de non-divulgation.
- Tenant suspendu : catalogue public selon politique d'indisponibilité, checkout interdit.
- Nouvelle version de catalogue : pas de prix client pris pour autorité.
- Double webhook d'un prestataire futur : pas de double encaissement comptabilisé.
- Application ancienne : réponse d'incompatibilité contrôlée, version d'API maintenue selon politique de cycle de vie.

## Limites assumées
Pas de récupération du jeton invité sans canal de vérification, pas de traitement automatique des remboursements en V1, pas de promesse de fonctionnement complet hors connexion.

