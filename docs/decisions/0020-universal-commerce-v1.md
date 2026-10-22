# ADR-0020 — ZAMUREK V1 universelle, pas MVP

**Décision ADOPTÉE le 22 octobre 2026 — remplace les restrictions boutique seule des spécifications xShop.**

## Architecture
Un `Offering` universel typé couvrant produit unitaire, vente au poids, plat/menu préparé, prestation planifiée, bien sur devis, réparation et marchandise réglementée à restrictions. Les contextes spécialisés sont propriétaires, composables par établissement. Restaurant, salon, produits pondéraux, meubles et réparations possèdent parcours bout-en-bout réellement testés en V1 ; pharmacie autorisée non réglementée et contrôle fail-closed pour médicaments.

## Portée
Aucun MVP ni lancement partiel : **38 capacités normatives** doivent être réalisées/testées. Phases de développement progressives **0.0.0→1.0.0**, seule release commerciale 1.0.0 après gates. Les applications installables incluent acheteur, marchand, Discovery/venue, Windows marchand et opérateur. Aucun site web hébergé.

## Conséquences
Le contrat `packages/contracts/openapi/xshop-v1.yaml` devient historique ; `zamurek-v1.yaml` est le nouveau draft. La documentation canonique est `docs/v1`. Voir [charte](../v1/PRODUCT-CHARTER.md) et [gates](../v1/RELEASE-GATES.md).
