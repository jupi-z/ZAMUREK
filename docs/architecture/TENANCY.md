# ZAMUREK — isolation multi-tenant et multi-établissement (V1)

**Document actif conforme à [DOMAIN-MODEL V1](../v1/DOMAIN-MODEL.md).**

## Hiérarchie
Platform Registry → Organization (tenant commerçant, **sa base PostgreSQL dédiée**) → Establishments (succursales/sites multi-activités dans la même DB), avec `organizationId` validé au routage DB et `establishmentId` validé sur chaque objet et action. Une personne peut avoir des memberships différents par établissement.

LaJoie Mall et tout centre commercial éventuel sont représentés comme `Venue` dans le registry avec ses propres niveaux/zones et adhésions **opt-in** ; ils ne deviennent jamais propriétaires de données des entreprises adhérentes.

## Registry
Organizations, DB secret references, établissements metadata minimales, channel app mappings, identity globale **e-mail vérifié, sans SMS**, staff sessions/MFA et venue consent/public discovery metadata. Commandes, rendez-vous, réparations, paiements et données confidentielles résident dans **DB métier de l'organisation**, jamais registry/venue.

## Résolution et permissions
- `X-Zamurek-Channel` identifie un canal, **ne prouve pas de droit**.
- Tenant résolu uniquement après contrôle serveur channel→organization, policy territoriale et actor; DB credentials sélectionnés depuis un registry privé, jamais URL/header client.
- Contrôle systématique `userId + organizationId + establishmentId + action + objectOwnership + businessCapability` ; clients, employés, agents et venues ne sautent jamais ces vérifications.
- Opérateur plateforme via VPN/MFA. Aucun outil Agentic Fabric n'accorde des privilèges implicites.
- SQL tenant credentials et pools séparés/limités ; une DB commune PostgreSQL par organisation est **isolation logique**, pas machine physique dédiée.

## Provisioning / migrations
Créer organization idempotente, DB role + DB, appliquer migrations et enregistrements initialisés, contrôle droits, activation seulement après validations. Migrations expand/contract par cohorts, rotation secrets, recovery ciblé et backup registry distinct. Le code supporte plusieurs établissements sous la même organization sans ouvrir une DB par succursale.

## Prix et poids
Catalogue offre/variant stocke **USD source** ; prix CDF dérivé backend via taux commerçant versionné. Aucun double tarif autonome CDF/USD ; *aucun float* pour montants ou grammes. Snapshots immuables commande, quote et établissement. Politique RDC CDF publique jusqu'à validation juridique.

## Tests P0
A→B cross-organization, E1→E2 cross-establishment dans une même org, deux clients d'E1, venue manager→order, agent d'une org→autre org, secret DB et migration, backup A/restauration A sans toucher B. La mise en production est bloquée à la moindre fuite.

Voir [DOMAIN-MODEL](../v1/DOMAIN-MODEL.md), [SECURITY](../v1/SECURITY-THREAT-MODEL.md), [NETWORK](NETWORK-EXPOSURE.md).
