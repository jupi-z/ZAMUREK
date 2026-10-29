# Zamurek Matière — Pack d’icônes 1.2

**288 identifiants canoniques, deux rendus par icône : 576 SVG séparés, plus deux sprites.** L’inventaire est organisé en 18 familles et couvre graphiquement les 43 capacités de la V1 documentée. Il contient 298 noms sémantiques au total, alias compris.

## Ouvrir le catalogue

Ouvrez `Zamurek_Icones_Catalogue.html` dans votre navigateur après téléchargement. Il est autonome et fonctionne hors ligne. Il permet de rechercher un nom, un alias ou une capacité (ex. FND-01), filtrer les familles, changer la taille, le fond et la palette, examiner le code, copier ou télécharger un SVG et exporter la sélection dans un ZIP. Le bouton de réinitialisation restaure la palette d’origine.

Les couleurs choisies dans le catalogue ne modifient pas les fichiers sources du ZIP. Téléchargez la sélection personnalisée pour conserver ces modifications. Le fond d’aperçu n’est pas exporté.

## Organisation du pack

- `svg/couleur/` : 288 icônes à dégradés et relief doux.
- `svg/interface/` : 288 rendus monochromes à traits, sans filtre.
- `sprites/` : un sprite par rendu, chacun avec 288 symboles.
- `manifest.json` : noms, identifiants, alias, familles, usages et couverture des capacités.
- `design-tokens.json` : palette, grille et paramètres graphiques.
- `docs/Analyse_Style_et_Perimetre.md` : étude des deux références et cadrage du système.
- `docs/Couverture_Capacites.csv` : correspondance avec les 43 capacités V1.
- `docs/Verification_*.json` : résultats des contrôles structurels, de rendu et d’interface.
- `docs/sources/` : instantanés des documents produit consultés.
- `sources/` : dessins géométriques, inventaire, générateurs et validation.

Chaque SVG est indépendant. Tous les objets, signes et détails sont dessinés en formes/tracés ; aucune image, police, bibliothèque d’icônes ou ressource distante n’est incorporée. Les effets de relief utilisent des dégradés et filtres SVG natifs. Le rendu interface utilise des masques vectoriels pour dégager les badges.

## Utilisation dans une interface

Grille commune : `viewBox="0 0 96 96"`. Le rendu couleur convient surtout aux présentations, catégories et navigations de marque à partir de 48 px. Le rendu interface est prévu pour des contrôles de 24 à 32 px ; pour un badge ou un objet complexe, privilégiez 32 px et un libellé visible. Les fichiers ont aussi été rendus à 24 px, sans conclure que tous les détails y sont également lisibles.

Les fichiers monochromes héritent de `currentColor` lorsqu’ils sont intégrés en SVG inline. Par exemple :

```html
<button type="button" aria-label="Rechercher" style="color:#005C45">
  <!-- Insérer ici le contenu du fichier svg/interface/rechercher.svg -->
</button>
```

Avec une balise `<img>`, la couleur CSS de la page ne traverse pas le fichier SVG externe. Utilisez le SVG inline, le sprite inline, ou un export auquel une couleur explicite a été appliquée depuis le catalogue.

Pour utiliser les sprites, insérez le contenu du sprite une fois dans le document, puis référencez un symbole. Les deux rendus possèdent des identifiants de symboles différents :

```html
<svg width="32" height="32" viewBox="0 0 96 96" role="img" aria-label="Accueil">
  <use href="#zamurek-interface-accueil"></use>
</svg>
```

Pour la variante couleur, l’identifiant est `zamurek-couleur-accueil`. Les identifiants internes des sprites sont préfixés pour ne pas entrer en collision avec les fichiers individuels. Si vous insérez plusieurs fois un même SVG individuel inline, préfixez ses identifiants par instance, ou utilisez le sprite. Dans un pictogramme décoratif accompagné d’un libellé, utilisez `aria-hidden="true"`. Pour une commande sans libellé visible, donnez un nom accessible au bouton. La couleur seule ne doit pas communiquer un état. Les compteurs variables (nombre de produits, notifications) appartiennent à l’interface ; ils ne sont pas figés dans les SVG.

## Régénérer les fichiers

Les SVG et le HTML livrés ne nécessitent aucune installation. Pour modifier les générateurs : Python 3 et le paquet `lxml` sont utilisés. Depuis le dossier du pack :

```sh
python sources/build.py
python sources/build_catalog.py
python sources/validate.py
```

Modifiez les tracés dans `sources/drawing.py`, l’inventaire dans `sources/catalog.py`, et le catalogue dans `sources/catalog.template.html`. Conservez les identifiants existants ; ajoutez des alias si un terme métier change.

## Portée vérifiée

Les 43 capacités ont chacune au moins un repère dans la matrice. Cette couverture décrit le référentiel consulté, pas des fonctionnalités déjà opérationnelles ni de futurs écrans encore non spécifiés. Les éléments éditoriaux complémentaires portent le statut `complement` dans le manifest. Un pictogramme carte/portefeuille n’annonce pas un paiement automatisé ; un pictogramme pharmacie n’autorise aucune transaction réglementée ; les codes graphiques QR/barres ne contiennent pas de donnée transactionnelle.

Les contrôles portent sur le XML, les identifiants, les références internes, la correspondance HTML/fichiers, les sprites, les 576 rendus, la présence à petite taille, les débordements de la grille et le fonctionnement du catalogue sur ordinateur et mobile. Les planches ont été inspectées visuellement ; ce n’est pas un test utilisateur de compréhension de chaque symbole.


## Optimisations V1.1

Cette version a fait l’objet d’une revue visuelle finale et d’une normalisation optique des 576 SVG : recentrage lorsque nécessaire, agrandissement léger des pictogrammes trop petits dans leur boîte 96×96 et renforcement discret du trait pour certains signes très minimaux. Les tracés d’origine sont conservés ; les corrections sont appliquées par transformation vectorielle non destructive et ajustement léger des épaisseurs de trait sur les cas les plus fins.


## Révision 1.2 — correction du mode interface

La série couleur 1.1 a été conservée à l'identique. Les 288 SVG monochromes ont été reconstruits avec un masquage **vectoriel** des tracés arrière cachés par les formes superposées ; les formes restent indépendantes et modifiables. Les contours de la famille Services (outil), Connexion (clé) et Meubles/fauteuil ont été redessinés pour une reconnaissance plus immédiate. Les variantes à badge disposent de dégagements transparents et de glyphes internes affinés. Les icônes monochromes héritent toujours de `currentColor`. Les sprites et catalogues sont synchronisés.

Les corrections structurelles et l'absence d'échec de rendu sont testées automatiquement. Cela ne garantit pas que tous les signes soient parfaitement interprétables par chaque utilisateur : la revue humaine de compréhension à 24 et 32 px demeure nécessaire.

## Attention au rendu monochrome
Les découpes des zones cachées utilisent `clipPath` + règle `evenodd`, pas un masque de luminance. Les avatars, actions et badges restent transparents, y compris en mode sombre. La V1.2 est destinée à une revue ergonomique visuelle ; ne pas supposer que chaque icône de 16 px est lisible sans test réel.


## Mise à jour V1.3 — Couleur / relief

Les 288 variantes couleur ont été comparées à leurs équivalents monochromes V1.2. Les huit silhouettes de la famille clés, outils et sièges ont été réalignées par le dessin monochrome validé. Les badges de couleur ont une séparation transparente entre la base et le badge. Les dégradés d'origine ont été conservés, les ombres réduites et la toque de cuisine rendue plus visible sur blanc. Les 288 SVG monochromes n'ont pas été retouchés. Voir `docs/RAPPORT_REVUE_COULEUR_V1_3.md`.
