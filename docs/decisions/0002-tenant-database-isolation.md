# ADR-0002 — Base de données dédiée par tenant

**Statut : adopté pour conception | Date : 2026-10-15**

## Contexte
Les commerçants doivent conserver des données séparées tout en partageant backend et maintenance.

## Décision
Registre PostgreSQL central distinct ; chaque tenant possède une DB PostgreSQL indépendante, credentials au moindre privilège, migrations communes, suivi schemaVersion et sauvegarde/restauration sélective.

## Alternatives
Table unique avec tenant_id : mise en œuvre plus simple mais forte discipline de filtrage ; schéma par tenant : compromis mais limites de gestion au niveau schéma.

## Conséquences
Isolation logique accrue, migrations et gestion des pools plus coûteuses. Sur serveur partagé : isolation non physique. Tenant resolver doit refuser tout changement de contexte non autorisé.

## Révision
Coût d'exploitation et charge réelle mesurés ; toute évolution doit préserver confidentialité et plan de migration tenant.

