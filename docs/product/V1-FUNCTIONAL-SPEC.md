# xShop — Spécifications fonctionnelles V1 (révisées)

**Statut : objectifs contractualisés, non encore implémentés.** [Arbitrages approuvés](../DECISIONS-VALIDATED-2026-10-15.md).

## Rôles
- Client **avec compte obligatoire** : création, connexion, vérification identité selon protocole retenu, panier, commande, suivi, demandes d'annulation.
- Owner marchand : produits, variantes, tarifs, commandes, versements manuels, zones, employés.
- Staff : permissions dédiées (lecture / gestion catalogue / préparation / confirmation paiement si expressément autorisé).
- Platform operator : création et gestion des tenants et des canaux, sans lecture de commandes sauf délégation sécurisée et audit.

## Comptes clients
Identité centrale réutilisable entre apps personnalisées ; profil commercial **local** par tenant sans partage implicite de commandes. Inscription, connexion, reset, rotation/révocation sessions, logout et confidentialité. Voir [auth](../architecture/AUTH-CUSTOMER.md). **Aucun checkout invité**, ni token de suivi invité dans la V1.

## Catalogue et disponibilités
Produits, catégories, images, variantes simples (taille/couleur éventuelle), DRAFT/ACTIVE/HIDDEN/UNAVAILABLE/ARCHIVED, sans stock quantifié. Seuls articles publiés/visibles apparaissent ; les indisponibles ne sont pas achetables. Publication exige un prix valide **en CDF et en USD**, par variante. Aucun change automatique.

## Panier
Panier mono-tenant et **mono-devise**, protégé par identité client ; produit/variante, quantité demandée, prix indicatif retourné par serveur. Le client choisit CDF ou USD, et tout changement de monnaie déclenche un recalcul **dans la devise cible**. Aucun secret de panier invité dans le parcours authentifié définitif. Panier expirant et serveur autoritaire sur montant.

## Remise
Retrait en boutique ou livraison dans zone autorisée ; **frais par zone et devise** configurés par marchand, affichage avant confirmation. Adresse/contact requis pour livraison, consentement et protection des données. Aucun suivi GPS des coursiers dans V1.

## Checkout
Authentification obligatoire, devises CDF/USD supportées, tarifs cohérents dans **une monnaie unique par commande**, confirmation côté serveur et capture immutable des lignes/frais/totaux/devise. Idempotency-Key obligatoire (retry réseau). Aucun paiement ou commande multi-tenant. Le client ne peut pas modifier le statut de paiement.

## Commandes
Statuts : PLACED, ACCEPTED, PREPARING, READY, OUT_FOR_DELIVERY, COMPLETED, CANCELLED, avec transitions spécifiques et auditées. Demande d'annulation acheteur adressée au marchand, qui décide selon politique applicable ; aucune annulation automatique côté client. Historique dans son application sur identité authentifiée ; interdiction IDOR.

## Paiement
PAY_ON_DELIVERY ou MANUAL_TRANSFER, **vers comptes du commerçant** dans la devise de commande, état PENDING / AWAITING_CONFIRMATION / PAID / FAILED / CANCELLED, sans remboursement automatique. Paiement vérifié par un employé habilité ; un message acheteur ne signifie pas PAID. Le cas d'un transfert en devise différente est traité hors parcours automatique V1.

## Application Android client
Accueil, liste/recherche/détail produit, inscription/connexion, panier/devises, livraison/retrait, checkout, confirmation, historique/suivi, demande d'annulation, profil, erreurs/offline. React uniquement affichage ; Kotlin réseau/cache/sessions natives.

## Application Android marchand indépendante
Connexion staff, boutique courante, catalogue et prix CDF/USD, upload images, disponible/indisponible, zones et frais CDF/USD, commandes/statuts/paiements manuels, paramètres de boutique et accès employés selon permissions, chargement/erreurs.

## Administration Windows
Opérateur : provisioning, états des tenants, canal Android, santé, migration, audit sans exposition data client. Marchand Windows : client additionnel installable selon priorité. UI React embarquée dans Tauri, cœur natif Rust. **Aucune admin web publiée**.

## Notifications
Historique et statuts récupérés à l'ouverture/rafraîchissement ; pas de SMS, push ou WhatsApp en V1 par défaut (OTP d'identité **distinct** d'une notification commerciale). Si l'app est fermée, aucune notification de commande temps réel garantie.

## Langue et visual
Français V1, i18n préparée, branding par tenant, UX tactile accessible, prix/devises toujours non ambigus.

## Recette bloquante
Deux tenants, deux devises, identité obligatoire, isolation par boutique, commandes réelles de bout en bout, Android acheteur/marchand, au moins une console opérateur installable, restauration et sécurité. Voir [gates](../quality/ACCEPTANCE.md).
