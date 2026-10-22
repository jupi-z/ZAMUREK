# Règles numériques exactes — monnaie, poids, arrondis et devis V1

**Statut : politique de calcul déterministe de référence à tester en G1/G2 ; soumise aux ajustements imposés par avis réglementaire avant commercialisation.**

## Unités canonique et formats
- `MoneyUSD` : entier signé 64 bits **en cents USD** (`amountMinor`) ou, pour calcul intermédiaire proportionnel, décimal de précision adéquate non arrondi. Toujours préciser `currency=USD`. Aucun JS `Number` ou float SQL dans les opérations d'argent.
- `MoneyCDF` : entier signé 64 bits en **centimes CDF** ; montant commercial de vente/affichage V1 RDC arrondi au **franc entier** (`100` centimes). Pour d'autres territoires, stratégie par politique versionnée, **pas** de conversion implicite vers USD.
- `Quantity` : quantité exacte encodée en chaîne décimale et unité canonique explicite (`G`, `KG`, `PCS`, `SERVICE`). G et KG sont liés par **1000 g = 1 kg**. Le type et la granularité sont fixés par `UnitDefinition` et validés serveur ; interdire NaN, Infinity, notation flottante non déclarée, négatifs, zéro au checkout.
- `FX Rate` : représentation rationnelle ou décimale exacte `usdToCdf`, `rateVersion`, `effectiveAt`, source/auteur et `tenantId`. Exemple **2360** donné à des fins de test, **jamais promis comme cours BCC**.
- Les données de client peuvent indiquer une *préférence* USD, mais l'API publique de vente sur territoire RDC applique la politique CDF conservatoire jusqu'à validation juridique.

## Calcul canonique (version `CDF_LINE_HALF_UP_V1`)
1. Un prix unitaire/au kg est source USD (cents), mesuré en unité `pricingBasis` appropriée. Les modificateurs/plats, options et livraison sont des lignes de calcul identifiées.
2. **Pour chaque ligne** : `unroundedCdf = (baseUsdMinor / 100) × (orderedQuantityCanonical / pricingBasisCanonical) × usdToCdf`, avec calcul décimal exact haute précision. Les services/unité ont quantité 1 et `pricingBasis=1`.
3. Appliquer une **unique fois par ligne** l'arrondi commercial `ROUND_HALF_UP` au **franc CDF entier**. Convertir pour storage final en `cdfMinor = cdfWholeFranc × 100`.
4. Livraison/taxes/ajustements explicitement autorisés sont des lignes de calcul distinctes avec policy de taxe propre, puis appliquer la même règle et **somme des montants déjà arrondis**. Pas de deuxième arrondi caché après total.
5. Un montant facture client est la somme des lignes persistées CDF, **pas le recalcul depuis des tarifs ou taux courants**. Pour remboursement, inverser les lignes/snapshots pertinentes de la commande, selon politique de remboursement et validations humaines.

## Cas déterministes
| Offre | USD base | Quantité | Taux marchand | Attendu CDF |
|---|---:|---:|---:|---:|
| Article unité | 1.00 USD | 1 PCS | 2360 | 2 360 CDF |
| Chocolat | 20.00 USD/kg | 125 g | 2360 | 5 900 CDF |
| Chocolat | 20.00 USD/kg | 1500 g | 2360 | 70 800 CDF |
| Pizza + supplément | 10.00 + 1.50 USD | 1 | 2360 | 27 140 CDF |
| Salon | 6.00 USD/service | 1 | 2360 | 14 160 CDF |

**Cas limites** : poids 0/moins min, dépassement max, quantité pas multiple de step, prix USD 0 autorisé seulement cadeaux/échantillon explicitement gratuits, limites int64, taux extrême ou nul, valeur exactement X.5 CDF, taxe non paramétrée (aucune taxe fictive), 2 modifications concurrentes du taux, paniers de plusieurs lignes ; property-based tests. Les prix affichés estimatifs avant quote indiquent `asOf`, l'API renvoie le montant contractualisé et le taux utilisé.

## Quotes et historique
`PriceQuote` contient `organizationId, establishmentId, actor, entries, baseUsdMinor/rational, rateVersion, roundingPolicyVersion, quoteCdfMinor, expiresAt, priceRevisionFingerprint`. Toute modification de poids final, catalogue, modificateur, taxe, remise ou taux **invalide le devis**, impose recalcul/reconfirmation explicite. Checkout idempotent, montant cité/confirmé immutable ; si quote expirée → 409 + devis renouvelable.

## Risques juridiques
Le droit congolais de l'affichage/facturation en CDF et les règles de taux/arrondis doivent être confirmés. Ne pas présenter le calcul comme une conformité fiscale certifiée ; un spécialiste validera taxes, documents réglementaires et arrondis éventuels avant commercialisation.

Voir [FX](../architecture/FX-PRICING.md), [modèle](DOMAIN-MODEL.md), [gates](QUALITY-REQUIREMENTS.md).
