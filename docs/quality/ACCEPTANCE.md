# Gates et Definition of Done — xShop

## Toute fonctionnalité
PR/commit revu, schéma API/documentation à jour, test automatique reproductible, contrôle des droits sur identité+tenant+objet, absence secrets/PII dans logs, montant/monnaie intacts, erreurs UI, migration si pertinente.

## G0 — cadrage
Arbitrages approuvés et documentés ; dépôt privé, PRD/API-only, double devise, identité obligatoire, clients installables, plan d'essais. **Une documentation seule n'est pas preuve d'un système prêt.**

## G1 — fondations exécutables
Builds vérifiés NestJS, React/Capacitor Android, Tauri/Rust Windows ; registry et **deux bases tenant**, tenant resolver, credentials séparés, auth/refresh/logout, validation OpenAPI normative, erreurs sécurisées. Tests isolation A/B exécutés en CI.

## G2 — cœur commerce
Catalogue et variantes avec prix CDF ET USD et frais par zone, panier/checkout client authentifié, commandes sans doublon, remise et paiement manuel, annulation sur demande marchand ; tests E2E dans les deux devises et tenants. Paiement non auto-certifié par l'acheteur.

## G3 — interfaces installables
APK acheteur, APK marchand différent, application opérateur Windows EXE/MSI en staging, signés selon politique, parcours complets avec Kotlin/Rust assurant réseau/sessions. **Aucune URL d'interface web hébergée en production.**

## G4 — pilote réel Kolwezi
Inventaire VPS/domaine, secrets, TLS, sauvegarde-restauration ciblée, auth vérifiée (provider OTP si retenu), tests sécurité, règles locales vente/fiscalité/PII, commerçant réel et comptes de paiement, support, APK pilote. Pas de production sans preuves.

## G5 — scale
White-label par canal, app marchand Windows additionnelle, abonnement mensuel contractuel et facturation xShop, gestion N DB / pools, tests compatibilité vieux clients et future marketplace opt-in.

## Bloquants immédiats
Fuite inter-tenant, commande anonyme, tarif unique masquant devise, devise non vérifiée, état de paiement payé par demande client, app à secrets embarqués, interface web en production, restauration non testée avant commercialisation.

Une preuve = tests/logs anonymisés/commit + critères de recette. Aucun résultat de test Android ou infra n'est actuellement revendiqué.
