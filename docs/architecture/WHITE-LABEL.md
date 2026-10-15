# Distribution et personnalisation white-label

## App indépendante par boutique
Même code source, configurations et builds différents : channelId public, branding, appId/packageName, icônes et textes, signature, identifiant métier tenant. Aucune donnée de connexion DB ni clé d'administration dans APK.

## Distribution validée
APK pilote à Kolwezi, puis Google Play **au cas par cas**, sous **compte éditeur du commerçant**. Publication et propriété des marques vérifiées avec le titulaire ; politique Google Play contre contenus répétitifs : https://support.google.com/googleplay/android-developer/answer/9899034 .

## Apps de gestion
App marchand Android séparée du client ; la console plateforme et le client marchand Windows sont installables (EXE/MSI) et utilisent la même API. Aucune interface hébergée côté production.

## Pipeline
Création tenant (DB isolée) → canal lié → thème/build → tests de signature, autorisations et isolation → distribution autorisée → compatibilité contractuelle et release contrôlée. La génération des installateurs est un système à réaliser, pas une capacité déjà disponible.

## Marketplace
Canal ultérieur qui **s'ajoute** sans modifier l'association des apps propriétaires. Participation volontaire, pas de fusion des DB ni des commandes.

## Sécurité
Un channelId n'est pas un secret ; les droits sont prouvés par sessions et autorisations serveur. Protéger clés de signature dans un coffre, jamais Git.
