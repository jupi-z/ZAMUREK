# Exploitation — serveur API-only

## Topologie
Serveur de production : backend NestJS API et worker(s), registry PostgreSQL, **une DB métier par tenant**, stockage médias contrôlé, TLS et supervision. **Aucun frontend hébergé**, admin Windows et apps Android livrées aux utilisateurs ; Swagger UI désactivé en production.

## Ressources disponibles (à vérifier)
Le porteur possède un VPS et des domaines libres, proposés provisoirement pour essais. **Capacité, OS, ports, sauvegardes, performances et disponibilité ne sont pas connus**. Ne pas les présenter comme audités ou déjà déployés.

## Environnements
Local → staging isolé (deux tenants fictifs) → production séparée. Ne pas réutiliser une DB de production pour démo ; secrets dans coffre sécurisé hors code. Domaines possibles: sous-domaine API uniquement, avec HTTPS/certificats et DNS gérés.

## Migrations et tenant
Provisioning idempotent, pool PostgreSQL borné/éviction, versionnage et migrations par cohortes, contrôle des dépendances registry→tenant et compensation échec. Backup et restauration d'un tenant sans perturber les autres ; registre sauvegardé indépendamment.

## Observabilité / incidents
Métriques de connexion et disponibilité API, latence, erreurs checkout/monnaie, santé DB, backlog outbox, crashes Android/Windows via mécanisme de télémétrie consenti et configuré. Journaux anonymisés. On-call/support et engagements RPO/RTO à définir après mesures et besoins commerciaux.

## Release
Artéfacts APK et EXE/MSI versionnés/signés par canaux appropriés ; signature et publication des apps Play sous compte marchand ; compatibilité API conservée. Pas de deploy d'interface HTML, même pour admin. Les schémas OpenAPI sont livrables internes (Git/CI), jamais page Swagger UI publique.

## Sécurité et conformité
Permissions tenant, HTTPS, secrets, SSH sécurisée, politique sauvegarde/restauration, contrôle de vulnérabilité, revue juridique RDC et contrats clients avant G4. L'accès au VPS n'a pas été fourni et n'est pas demandé en clair dans Git ou le chat.

Voir [clients](CLIENTS-DEPLOYMENT.md), [tenancy](TENANCY.md), [blocages](../OPEN-QUESTIONS.md).
