# Applications personnalisées (white label)

## Principe
**Un code source storefront commun, plusieurs artefacts signés et configurés**. Chaque commerçant possède son application de marque lorsque la distribution sur store est permise/pertinente ; pas de fork applicatif au cas par cas.

## Configuration de build / registre
channelId public (opaque), tenantId de référence non secret, applicationId/packageName unique, nom, icônes et splash, couleurs, polices autorisées, contenu marketing, deeplinks, domaines, paramètres features et endpoints API. Les secrets, JWT, credentials DB et clés de paiement privées restent hors client.

## Pipeline envisagé
1. Un opérateur crée tenant et canal.
2. Configuration validée et versionnée, assets vérifiés pour dimensions/droits.
3. Build Android Gradle par flavor / configuration générée ; signature gérée dans coffre de secrets CI sécurisé.
4. Tests automatiques et manuels sur artefact ; validation du canal en backend.
5. Publication par propriétaire autorisé ; maintenance via versions communes et stratégie de release.

## Compatibilité / cycle de vie
- Chaque application conserve son canal et tenant à travers les upgrades backend.
- Publication d'un nouveau canal n'affecte pas les applications existantes.
- Les contrats API possèdent une politique de support ; aucune suppression sans migration des clients encore supportés.
- Changement d'identité légale, de package Android ou transfert de propriété nécessitent parcours séparé.

## Variabilité autorisée
Couleurs, logos, informations boutique, pages marketing, catégories, modules activables. Les écrans fondamentaux et les protocoles ne se dupliquent pas.

## Publication Android
Google Play contrôle les applications répétitives : changer un logo ne garantit pas acceptation. Prévoir PWA/web dédié et une évaluation de la valeur spécifique de chaque appli avant soumission.
Politique : https://support.google.com/googleplay/android-developer/answer/9899034

## À ne pas faire
Aucune duplication de backend par client, aucune modification manuelle de 20 forks, aucune clé privilégiée incluse dans un APK, aucun « nom de DB » transmis par l'application pour piloter la connexion.

