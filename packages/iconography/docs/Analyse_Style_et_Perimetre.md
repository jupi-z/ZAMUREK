# Zamurek Matière — analyse et direction du système

## Références analysées

Deux images fournies : 189247.png et 189246.png. Elles servent de références stylistiques ; les dessins du pack sont construits en code, sans détourer leurs pixels ni reprendre une bibliothèque de pictogrammes.

La première planche privilégie les silhouettes pleines, les superpositions de matières, le vert dominant et des accents orange/magenta. La seconde ajoute des contours ivoire, des angles arrondis, des dégradés de volume plus marqués et une lumière venant du haut gauche. Les flous et halos du fond appartiennent à la mise en scène des planches : ils ne sont pas intégrés comme arrière-plans aux icônes.

## Direction retenue

Formes compactes et arrondies, objets vus de face ou avec une perspective très légère, lumière uniforme du haut gauche. Les contours ivoire structurent la matière sans devenir un trait blanc épais. Les pièces ivoire utilisent une arête vert grisé #8BB5AA pour rester visibles sur fond blanc. Le relief vient des dégradés et des plans superposés. Une ombre SVG discrète accompagne le rendu couleur ; aucun fond n’est incorporé.

Palette : vert forêt #005C45, orange #FF8A1E, magenta #D21868. Les nuances du système sont centralisées dans design-tokens.json. Vert pour la structure ; orange pour les transactions, objets et accents d’action ; magenta pour les liens affectifs, l’attention et certains états. Chaque état important possède aussi un symbole explicite : la couleur seule ne porte pas son sens.

Grille : viewBox 0 0 96 96. Cadrage optique régulier, coins arrondis et terminaisons de traits rondes. Deux rendus : couleur avec relief pour navigation, catégories et signes de marque ; interface à traits monochromes currentColor pour les commandes compactes. Aucun caractère de police n’est utilisé pour les signes ou les objets.

Les badges plus, moins, validation, annulation, délai et verrou reprennent une construction constante. Ils indiquent des opérations distinctes sur un même objet. Les formes génériques usuelles (loupe, cœur, panier) sont dessinées pour ce système.

## Analyse du produit

Sources consultées directement :
- [README](https://github.com/jupi-z/ZAMUREK/blob/main/README.md), contenu SHA bd7d08adc1e1adb76e956721a7cae830b17586b6.
- [Charte V1](https://github.com/jupi-z/ZAMUREK/blob/main/docs/v1/PRODUCT-CHARTER.md), contenu SHA b51c4e30448def9b5f8f7b40b2b56cb44ade4fac.
- [Manifest des capacités](https://github.com/jupi-z/ZAMUREK/blob/main/spec/v1/capabilities.json), contenu SHA 3dec6d5217987018a73a8ec5b6b21cb0ceddf2e6.
- [Parcours métiers](https://github.com/jupi-z/ZAMUREK/blob/main/docs/v1/BUSINESS-WORKFLOWS.md), contenu SHA 03f2f50330b6a199e205a898a75b0d543b2477b8.
- [Assistants IA](https://github.com/jupi-z/ZAMUREK/blob/main/docs/v1/AGENTIC-KERNEL.md), contenu SHA c6aebf2d63649a2c4ce117afd8fdb317f8021b37.

Ces sources décrivent une plateforme commerciale et de services omnicanale : retail, vente au poids, restauration, services planifiés, meubles, réparation, pharmacie autorisée et découverte de lieux. Les parcours concernent acheteurs, marchands, caissiers et opérateurs. La documentation précise que la V1 est spécifiée, non livrée : un pictogramme fourni n’atteste pas d’une fonctionnalité opérationnelle. Les extraits de référence sont conservés dans docs/sources.

L’inventaire couvre navigation, catalogue, panier, commandes, livraisons/retrait, verticales métiers, espèces et caisse, tickets/impression, comptes, isolation et permissions, assistants et approbations, exploitation, actions et états. La correspondance des 43 capacités est donnée dans Couverture_Capacites.csv et manifest.json. Une couverture signifie qu’un repère graphique pertinent existe ; elle ne prouve ni le fonctionnement ni l’exhaustivité de futurs écrans non spécifiés.

Les éléments éditoriaux complémentaires — cadeau, premium, avis, carte générique, portefeuille — portent le statut complement. Ils ne présument ni programme de fidélité, ni paiement carte automatisé, ni porte-monnaie de plateforme. Le marqueur pharmacie identifie une catégorie ; les icônes restriction/autorisation ne signifient pas qu’un médicament est vendable. Le mode hors ligne représente la connectivité, sans promettre un POS transactionnel hors ligne. Les QR et codes-barres sont des pictogrammes, pas des codes utilisables pour une transaction.

## Mise en œuvre

Chaque SVG est autonome : tracés, formes géométriques, dégradés et filtres SVG natifs. Aucune image incorporée, base64, police ou ressource externe. Les sources Python décrivent les tracés et l’inventaire ; elles sont livrées pour permettre l’extension et la maintenance. Les identifiants stables sont en minuscules avec tirets ; les libellés et descriptions sont en français.
