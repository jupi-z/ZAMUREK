# Isolation multi-tenant et provisionnement

## Choix
Une **base PostgreSQL métier par boutique** + **registre central**. Même modèle logique / migrations de tenant pour tous, versions potentiellement décalées durant un déploiement progressif.

## Registre central
Tenant(id UUID immuable, slug unique, legal_name, display_name, status, db_locator_ref, schema_version, created_at), StorefrontChannel(id, tenant_id, kind, app_id/package_id/domain, public_config_version, status), PlatformIdentity et memberships selon [IDENTITY](IDENTITY.md), opérations de provisioning et audit plateforme.

Le registre contient une **référence de secret**, jamais le mot de passe de base en clair. Les identifiants de connexion, clés et secrets sont fournis par un secret manager externe au dépôt.

## Isolation
- Credentials SQL distincts par tenant, privilèges minimaux sur leur propre DB uniquement.
- Paramétrage pool/client par base, limite totale de connexions, éviction des clients inactifs et instrumentation.
- Chaque requête reçoit un TenantContext côté serveur **après** résolution du canal et vérification des permissions.
- Pour les routes publiques mono-boutique, le canal enregistré identifie le tenant (une valeur app_id publique n'est pas une preuve d'identité ni un secret).
- Pour les écritures marchand : membership et rôle vérifiés côté serveur contre le tenant résolu et l'action.
- Pour marketplace : tenant cible explicitement sélectionné puis vérifié par le service ; aucune traversée implicite.
- Aucun SQL interpolant un nom de base fourni directement par la requête.

## Provisioning idempotent
1. Créer entrée PROVISIONING avec une clé de tentative et identifiants réservés.
2. Planifier une tâche autorisée en back-office (jamais par client public).
3. Créer DB, rôle et secret uniques ; appliquer migrations et données essentielles.
4. Créer zone média / politique d'accès ; vérifier santé et permissions négatives.
5. Enregistrer version du schéma et rendre ACTIVE.
6. Échec : FAILED, audit et procédure de reprise/compensation ; ne pas annoncer ACTIVE avant succès.

## Migrations
- Migration du modèle tenant versionnée, répétable ou idempotente selon outil ; aucune manipulation manuelle non suivie.
- Installer changements expand/contract compatibles entre API et anciennes bases ; migration par cohortes avec progression/rollback métier documenté.
- Suspendre les actions incompatibles pendant migrations, sans faire pointer le tenant sur une autre DB par accident.
- Restaurer un tenant isolément et valider l'intégrité après restauration.

## Politique de données
- Métier et PII du client local exclusivement dans DB tenant, sauf identités globales explicitement consenties.
- Pas d'agrégation de commandes commerciales au registre.
- Logs masquent adresses, secrets, tokens et données personnelles.
- Médias tenant-scopés avec URLs temporaires pour contenu non public.

## Tests impératifs
Tenants A/B : lecture croisée, modifications, médias, panier, commande, employés, audit, accès opérateur, et restauration. Pour chaque test B sous contexte A, réponse non révélatrice (403/404) et zéro fuite.

## Risques techniques
Pool exhaustion quand beaucoup de tenants actifs ; migrations N bases ; support et backups complexes. Mesurer les pics et ajuster le nombre de connexions, le placement des DBs, le cycle des clients et les ressources. Référence : https://www.prisma.io/docs/orm/v7/prisma-client/setup-and-configuration/databases-connections.

