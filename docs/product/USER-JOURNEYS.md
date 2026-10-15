# Parcours V1 après décisions

## Client Android : inscription → achat
1. L'application récupère la configuration publique du canal, sans présumer de permission.
2. L'utilisateur s'inscrit / se connecte ; contrôle d'identité (vérification téléphone prévue pour commercialisation).
3. Il consulte le catalogue, choisit **CDF ou USD** ; toutes les lignes et frais affichés dans cette monnaie.
4. Il ajoute produit/quantité au panier **lié au compte, au tenant et à la devise**.
5. Livraison en zone tarifée CDF/USD ou retrait ; téléphone/contact et adresse de livraison, si nécessaire.
6. Le serveur revalide session, accès tenant, prix, devise, disponibilité, frais, puis crée commande idempotente.
7. Confirmation authentifiée, historique/états dans l'app ; demande d'annulation transmise au marchand.

## Marchand Android : préparation
1. Connexion staff + membership tenant ; aucun accès croisé entre tenants.
2. Catalogue/variantes, **saisie séparée de prix CDF et USD**, disponibilité sans stock, zones/frais par monnaie.
3. Accepter, préparer, remettre/livrer commande ; confirmer **manuellement** transfert ou paiement livraison après preuve.
4. Demande d'annulation traitée selon politique, pas de changement d'état non autorisé ; journal d'audit.

## Plateforme Windows : cycle tenant
Opérateur autorisé s'authentifie, crée tenant, provisionne DB/secret/migration, contrôle deux tests d'isolation, associe canal et app ; active, suspend, supervise. Aucune interface web distante.

## Échecs
Utilisateur non connecté au checkout = 401 ; token d'un autre client/tenant = refus ; produit sans un des deux tarifs = non publiable ; devise changée = panier recalculé ; réseau coupé durant POST = retry même clé ; faux paiement déclaré = reste non payé ; tenant suspendu = checkout refusé.

## Prolongement
Future marketplace Android en canal supplémentaire ; participation du commerçant explicitement consentie ; aucun achat multi-tenant transactionnel en V1.
