# Provenance de l'iconographie V1.2

- Source de référence : `svg/interface/` et `svg/couleur/` ; catalogues et sprites ont été reconstruits avec les SVG maîtres V1.2.
- `sources/drawing.py` et `sources/build.py` restent les **générateurs historiques V1.0**, conservés comme archives techniques. **Ne pas les relancer sur les masters V1.2** ; cela effacerait les optimisations.
- `sources/optimize_interface_v12.py` contient le traitement de la série monochrome utilisé à partir d'un SVG V1.1. Il n'est pas idempotent.
- Les corrections communes utilisent des `clipPath` à règle pair-impair : les traits arrière cachés sont supprimés sans ajouter un fond blanc opaque, y compris sur obsidienne.
- Les 116 badges ont été reconstruits avec des traits intérieurs plus fins et une zone de dégagement circulaire.
- Les familles Services, Réparation, Outils IA, Connexion/clé et Fauteuil/Meubles possèdent des géométries monochromes revues.
- Les SVG couleur sont strictement ceux de la V1.1.
