# Zamurek Illustrations — sources, licences et modifications

Ce lot est un **échantillon technique en cours de revue visuelle**, non une livraison acceptée des 33 familles ni des 275 besoins. Les SVG sont **100 % vectoriels** et ne contiennent pas de PNG, de liens externes ou de balises `image`.

## Humaaans (Pablo Stanley)

Source originale : https://humaaans.com/ (site officiel indiquant CC0).
Fichiers effectivement téléchargés depuis le miroir https://github.com/Calinou/humaaans à la révision `818f184343b884123e08e531ffd62c5b2f9ffef4`, dont le fichier LICENSE.md indique **CC BY 4.0**. Par prudence nous conservons l'attribution et suivons CC BY 4.0 pour ces fichiers du miroir.

- `ZIL-044` : `Flat Assets/Humaaans/standing-23.svg`, SHA Git blob 0ccadfd297ebcda0a34f8fe041dc3d7f39a03b03 ; modifications : recoloration du vêtement et des accents ; incorporation dans une nouvelle composition Zamurek.
- `ZIL-117` : `Flat Assets/Humaaans/sitting-2.svg`, SHA Git blob 728990e30f181c1a161c095ec7743c17e21e3dce ; modifications : recoloration du vêtement et des accents ; incorporation dans une composition POS.

**Attribution :** « Humaaans » © Pablo Stanley, https://humaaans.com/ ; changements : palette, compositions et transformations par Zamurek. La licence du miroir est consultable sur https://github.com/Calinou/humaaans/blob/master/LICENSE.md .

## IRA Design (Creative Tim)

Source : https://github.com/ira-design/ira-illustrations (MIT). Licence intégrale dans `THIRD_PARTY_LICENSES.md`.

- `ZIL-044` : `assets/img/object.svg` (icône de mobilier), SHA Git blob 1d112612844b7c8cd4fbb7fbee6c64c3aba4b11a ; modifications : remplissage vert, intégration dans la case mobilier de l'interface illustrative.

**Attribution :** IRA Design © 2013–2021 Creative Tim, https://www.creative-tim.com, licence MIT. Toutes les illustrations dérivées de ces éléments conservent les notices requises.

## Éléments créés spécifiquement pour Zamurek

Panier vide, caisse, terminal, éléments de recherche, sacs, formes d'accompagnement, structures de composition, règles CSS/animations et thèmes clair/sombre. `ZIL-001` est un asset vectoriel Zamurek original parce que ces bibliothèques ne fournissent pas de panier correspondant au besoin ; aucun faux emprunt de source n'est revendiqué.

## Contraintes de validation

- Statiques et animés possèdent chacun des variantes clair/sombre à fond transparent.
- Animations à durée finie (aucune boucle infinie), `prefers-reduced-motion` respecté.
- Les personnages et éléments métier restent dans des groupes nommés ; sources conservées comme vrais éléments SVG.
- Aucun succès financier ni confirmation de paiement n'est montré.
- Statut : **Revue visuelle requise**. La validité XML / le rendu navigateur doivent être vérifiés séparément avant acceptation.
