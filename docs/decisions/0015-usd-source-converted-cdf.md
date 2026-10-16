# ADR-0015 — Tarif de référence USD et conversion CDF versionnée

**Statut : ADOPTÉ — 2026-10-16 ; REMPLACE ADR-0012**

Prix unique USD par variante/zone ; taux USD→CDF configurable par commerçant, version/horodatage/auteur, historique immuable. Conversion déterministe **sur backend** en décimal exact et arrondi documenté. Snapshot en CDF de la commande, du taux et USD source. Le taux de démonstration **2360** n'est pas un cours officiel. Pour vente RDC, l'affichage public en CDF seulement est appliqué conservatoirement suivant arrêté 007/2025, avant vérification juridique d'éventuelles exceptions.

Alternative écartée : deux tarifs indépendants CDF et USD, ou conversion uniquement UI. Tests de changement de taux, prix, precision, devis expiré, anciennes commandes et fraude requis.

Voir [FX-PRICING](../architecture/FX-PRICING.md).
