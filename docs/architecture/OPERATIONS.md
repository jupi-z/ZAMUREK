# Exploitation, migrations, sauvegardes et observabilité

## Environnements
Local/dev, staging avec au moins 2 tenants factices, production. Ne jamais utiliser vraies données clients dans CI ou environnements de tests.

## Provisioning / migrations
Tenant Registry conserve statut, emplacement de DB et version de schéma. Worker orchestration idempotent ; supervision du nombre de bases/connexions. Migrations expand/contract par lot, canary tenant, compatibilité version API.

## Sauvegardes et restauration
- Sauvegardes **par base tenant** + registre séparé + objets médias avec inventaire.
- Fréquence, rétention, RPO et RTO **non décidés** : documenter et tester avant ouverture publique.
- Exercices de restauration d'un tenant A sans toucher B et de registre avec reconstruction vérifiée du mapping.
- Sauvegardes chiffrées, accès strict, preuves d'exécution et alertes d'échec.

## Observabilité
Metrics : requêtes/latences/erreurs par route et tenant pseudonymisé, santé DB/pools, provisioning et migrations, échecs checkout, outbox backlog, santé médias, uptime. Traces corrélées ; ne pas logger téléphone/adresse ni secret.

## Procédure incident
Détecter → qualifier impact tenant(s) → contenir → diagnostiquer corrélation → corriger → restaurer si besoin → documenter. Suspensions contrôlées pour empêcher nouvelles commandes pendant incident.

## Rotation secrets
Credentials tenant séparés, rotation graduelle, procédure de rollback. Aucun accès SQL privilégié depuis applications clientes.

## Mise à l'échelle
Budget de connexions par instance et tenant ; backpressure à forte charge ; tests nombre de tenants, failover, déplacement des DBs entre hosts. Pas de promesse SLO tant qu'aucune mesure en staging/pilote.

## Checklist pré-lancement
Secrets, certificats HTTPS, tests A/B, migrations et downgrade plan, backup/restore, quotas, logs/audit, sécurité admin, procédures de support et paiements validés.

