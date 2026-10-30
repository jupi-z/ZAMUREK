# ZAMUREK — Protocole de production « Illustrations System » V1

**Statut : plan d'exécution. Le backlog contient 275 besoins d'usage, pas 275 assets créés.**

## Raison d'être
Le système doit être visuellement propriétaire, expressif et identifiable comme Zamurek dans l'ensemble des parcours. **Ne pas imposer le flat design** ; choisir un rendu illustratif stylisé, clair, personnalisé, avec volume et relief si cela améliore les scènes. Personnages et objets autonomes, peu de décors, pas de paysages.

## Les 6 étapes
1. **Relevé** : lier chaque besoin à son ID `ZIL-001` à `ZIL-275`, contexte UX, taille d'usage, étiquette et gate réglementaire.
2. **Art direction** : trois illustrations pilotes de profils différents : `ZIL-001` panier vide, `ZIL-044` bienvenue acheteur, `ZIL-117` ouverture de caisse. Validation du style avant extension.
3. **Kit de pièces** : figures A/B/C, variations d'expressions/teintes/poses, bras et mains séparés, téléphones, sacs, paquets, tickets, outils, balance, mobilier, aliments, badges. Relever la provenance/licence de chaque pièce importée.
4. **Masters** : composer les 33 familles de bases référencées `BASE-*` en SVG multicouche avec groupes ID stables, fonds transparents et versions fixes.
5. **Dérivés** : composer les 275 besoins à partir des masters ; ne créer de nouvelles géométries qu'en cas de besoin réel. Animations uniquement justifiées par le parcours.
6. **Recette** : validation visuelle sur blanc et obsidienne, limites de taille, accessibilité, cohérence, performance, réduction de mouvement, tests SVG, gouvernance des licences et métadonnées.

## Nomenclature proposée
`packages/illustrations/registry/` : JSON et CSV. `assets/masters/<base>/` : sources multicouches. `assets/static/<id>-{light,dark}.svg` : variations. `assets/motion/<id>/` : éventuels CSS/JS/SVG animés. `reports/` : tests d'intégrité, licences et QA.

Ne pas confondre ce plan avec l'ajout des 275 fichiers finaux : leur contenu reste à dessiner, à adapter et à vérifier.

## Spécification de dessin
- Palette dominante `#005C45`, accents `#FF8A1E`, `#D21868`, blanc/obsidienne pour les fonds d'application ; préserver des couleurs humaines réalistes pour la peau et les cheveux.
- Silhouettes cohérentes mais pas obligatoirement plates ; aucune contrainte de texture uniforme. Éviter effets gratuits, ombres excessives, dégradés sans fonction et paysages décoratifs.
- Rythme : pas de boucle infinie pour les éléments statiques ; états d'attente seuls peuvent boucler doucement. Respect `prefers-reduced-motion`.
- Ne jamais dessiner un médicament soumis à ordonnance comme vendable, ni un paiement comme confirmé sans retour du Core, ni un achat transversal à plusieurs vendeurs comme une transaction unique.

## Licence
Humaaans (CC0 déclaré sur https://www.humaaans.com/) et IRA Design (MIT : https://github.com/ira-design/ira-illustrations/blob/master/LICENSE.md) sont des **pistes**, non des dépendances incorporées. Toute réutilisation nécessite une entrée traçable `upstream`, `version`, `url`, `licence`, `original`, `modifications`, `avis requis`, et la conservation des avis MIT applicables. Ne pas prétendre que tout dérivé est exclusif.

## Statuts et preuves
`À produire` → `En création` → `Revue visuelle` → `QA technique` → `Acceptée`. Le statut `Acceptée` exige les fichiers effectifs et les preuves. Jamais de pourcentage d'achèvement déduit de la seule présence du backlog.