# ADR-0012 — Deux prix indépendants par devise

**STATUT : REMPLACÉE par [ADR-0015](0015-usd-source-converted-cdf.md), depuis le 16 octobre 2026.**

## Ancienne proposition (historique seulement)
Chaque variante/zone possédait deux prix indépendants CDF et USD, sans taux de change. Cela **n'est plus le modèle xShop**.

## Décision actuelle
Un prix de base USD et un taux USD→CDF marchand configurable, versionné. Conversion **serveur** avec snapshots commande et affichage public CDF pilote RDC. Lire [FX-PRICING](../architecture/FX-PRICING.md). Ne pas réutiliser cette ancienne approche dans les migrations ou l'API.
