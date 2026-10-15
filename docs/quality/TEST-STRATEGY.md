# Stratégie qualité et tests

## Niveaux
1. Unitaires : pricing minor-unit, état commande/paiement, authz, clés d'idempotence, validations.
2. Intégration : PostgreSQL registry + deux DB tenant, migrations, repository, transaction checkout/outbox, médias.
3. Contrat : OpenAPI, stabilité des DTO, ancien APK/SDK face nouvelle API, statut erreurs.
4. E2E : deux apps mono-boutiques, commandes invitées, admin, livraison/retrait, suivi.
5. Android réel : rendu/lifecycle, clavier, permissions refusées, WebView bridge, réseau instable, process kill, mémoire et fluidité.
6. Sécurité : matrice A/B lecture/écriture, IDOR, session expirée, brute force, secrets, URLs média.
7. Exploitation : provisioning idempotent, migration multi-bases, backup et restore isolés, worker retry.

## Matrice minimale d'isolation
AppA→produitB privé = refus ; ownerA→orderB = refus ; clientA→suiviB sans secret = refus ; mediaA→mediaB privée = refus ; channelId modifié → aucune autorisation administrative ; opérateur non habilité → refus.

## Critères de blocage
- Une fuite inter-tenant, double commande après retry identique, faux paiement PAID, commande à prix fourni par appareil, absence de restauration testée ou credentials DB embarqués bloque release.
- Un build qui ne compile pas, un schéma cassé ou un contrat API non validé bloque fin de jalon.

## CI proposée
PR : liens/docs, lint, typecheck, tests métier, vérification OpenAPI et schema, secrets scan. Après implémentation : Android Gradle test et assemblage de debug, intégration Postgres jetable. Aujourd'hui seule validation de documentation est disponible.

## Jeux de test
Tenant A (pagne/bijoux) et Tenant B (téléphones) avec produits et permissions propres, scénarios devise/zone distincts. Données synthétiques exclusivement. Chaque test écrit sa DB transactionnelle/réinitialisée.

