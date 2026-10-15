# Isolation multi-tenant xShop

**Décision validée : une base PostgreSQL métier par commerçant**, plus registre central. L'identité client globale est un service partagé **séparé**, pas une mise en commun des commandes.

## Registre
Tenant(id immuable, slug, legalName, status PROVISIONING/ACTIVE/SUSPENDED/FAILED, dbSecretRef, schemaVersion), channels client et marchand, comptes opérateurs/staff/memberships et **globalCustomerIdentity** (phoneE164, vérification, session). Les commandes, adresses, prix et profils locaux restent dans chaque DB tenant.

## Résolution et autorisation
- Un canal public permet d'identifier boutique et configuration ; ne prouve pas l'identité.
- Pour panier/checkout/commande, vérifier **identité authentifiée**, état vérifié si exigé, tenant et **ownership de l'objet**.
- Pour marchand, membership active et permission tenant ; pour opérateur, rôle plateforme et audit.
- Chaque client PostgreSQL est ouvert par références du registre et secrets distincts, jamais SQL/host arbitraire depuis des paramètres clients.
- Pools bornés, cycle de vie éviction, métriques des connexions tenant et protections contre le noisy neighbor. Même serveur PostgreSQL = séparation logique, **pas isolation physique**.

## Provisioning
Enregistrer tentatives idempotentes, créer DB + rôle, migrations + seeds minimales, namespace médias, tests de permissions et connexion, rendre ACTIVE seulement après vérification ; reprise/compensation en cas de panne.

## Évolutions
Versions schema migrées par cohortes, expand/contract et backups par DB. Un tenant ne doit jamais être pointé vers la DB d'un autre. Restoration tenant A sans modifier tenant B et indépendance du registre démontrées avant G4.

## Devises / données
Une DB contient variant_price CDF/USD et frais zones CDF/USD, commande mono-devise et contact client local, jamais partage inter-tenant. Identité globale permet reconnexion multi-app sans exfiltrer profils/commandes.

## Tests
Au moins tenants A/B et clients 1/2 du même tenant, opérations lecture/écriture, médias, achat, staff, récupérations, suspensions et restore. Une violation inter-tenant interdit production.

Référence : https://www.postgresql.org/docs/ ; https://owasp.org/API-Security/ .
