# ADR-0012 — CDF et USD simultanément par boutique

**Statut : ADOPTÉ | 2026-10-15**

Chaque variante et zone de livraison commercialisée possède **deux montants indépendants**, CDF et USD, renseignés par le marchand ; aucun change automatique. Panier et commande sont **mono-devise**, sélectionnés par l'acheteur et confirmés côté backend. Frais et paiements liés à la même monnaie. Données financières en unités mineures entières, JSON chaîne.

Alternative écartée : une seule devise par boutique ou conversion FX implicite. Cette décision complète le modèle de données et le contrat OpenAPI.

Conséquences : validation stricte de publication et intégrité des totaux CDF/USD, tests de changement de devise et taxes/conformité à valider selon territoire.
