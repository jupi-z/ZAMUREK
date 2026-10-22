# Politique de composants tiers — ZAMUREK

**Règle : produit et cœur métier propriétaires, briques techniques permissives réutilisables.** Cette politique s'applique au backend, aux applications Android et Windows, à l'outillage IA et aux composants embarqués/distribués.

## Autorisé par défaut
MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, uniquement après vérification de la **licence effective de la version exacte** et des dépendances transitives. Sont adaptés comme catégories : framework serveur, ORM, driver DB, moteur de templates, UI, sérialisation, tests, cryptographie reconnue, observabilité, files d'attente et SDK standard.

## Non retenu par défaut
Mercur/Mercure et tout autre **moteur commercial complet comme socle**. Dépendances à licences copyleft (GPL/AGPL/LGPL/MPL/EPL), source-available non permissives (SSPL/BUSL, etc.), licences commerciales restrictives ou inconnues : bloquer jusqu'à décision écrite, revue des conditions et possibilité réelle d'utilisation.

## Critères de choix
- Fonction technique circonscrite, API/documentation stables et maintenues.
- Pas d'obligation de remplacer le code métier propriétaire par celui du fournisseur.
- Analyse des vulnérabilités, des composants transitifs, de la redistribution embarquée APK/EXE/MSI et de l'éventuel usage de services distants.
- Tests, maintenabilité et possibilité de remplacer la brique sans migration totale de la plateforme.
- Ne pas déduire de la licence de **un** paquet la licence de tout son écosystème.

## Pipeline de gouvernance
1. Déclarer dépendance + version + finalité + URL source + SPDX identifier.
2. Scanner les dépendances directes et transitives à chaque PR et release ; fail closed sur licence inconnue/interdite.
3. Produire SBOM versionnée pour API et artefacts distribués ; archiver notices/licences des tiers.
4. Réévaluer les versions majeures et les doubles licences, vérifier brevets/notices et droits de distribution.
5. Exiger approbation explicite de toute exception et consigner sa justification dans un ADR avant merge.

## IP / contributions
Les contributions au cœur ZAMUREK doivent être couvertes par un accord et une chaîne de titularité permettant l'exploitation propriétaire. Le dépôt est privé, sans licence open source générale. Garder les notices de tiers là où elles sont requises.

## Agentique
Privilégier les interfaces abstraites de modèle, outils et mémoire ; domaines métier de ZAMUREK contrôlent toujours les transactions. Une bibliothèque open source agentique peut implémenter une opération technique isolée, mais l'autorisation d'une action sensible demeure la responsabilité du système propriétaire.

Ceci est une politique interne d'ingénierie, non un avis juridique individualisé.
