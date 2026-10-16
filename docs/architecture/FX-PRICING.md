# Architecture monétaire — source USD et conversion contrôlée

**Décision du 16/10/2026.** Un seul prix catalogue USD par variante ; un seul tarif de base USD par zone de livraison. Le vendeur configure un taux USD→CDF versionné. **Aucun prix CDF indépendant sur les variantes.**

## Source de vérité
- `product_variant.price_usd_minor` (int64, cents USD) et `delivery_zone.fee_usd_minor`.
- `tenant_fx_rate` : id, baseCurrency='USD', quoteCurrency='CDF', numerator, denominator, decimalText, version, effectiveAt, changedBy, createdAt, isActive. Conserver historique immuable.
- Taux pilotage initial exemple `2360 CDF / USD` fourni par propriétaire : **paramètre de démonstration uniquement** avant confirmation du commerçant ; distinct des taux BCC.
- Pour un CDF affiché, **backend** convertit en entier minor-unit avec arithmétique exacte, pas de `Number`/float binaire pour les opérations monétaires. Politique proposée V1 : arrondir chaque prix unitaire et chaque frais converti au **CDF entier** le plus proche (arrondi commercial HALF_UP), puis multiplier les prix unitaires par quantités et sommer ; régler la politique finale après essais caisse/conformité. Préférer une bibliothèque décimale testée ou une fraction exacte ; vérifier overflow.
- CDF = quantité en cents CDF égale à USD cents × (taux CDF/USD) (les deux devises ont 2 décimales ISO). Arrondir à la granularité CDF visée (p. ex. 100 cents CDF), **une seule fois au niveau spécifié**, pas dans React.
- `fxQuote` : devise de vente CDF, taux/ID de version, quantité, prix USD source, montant CDF recalculé, TTL, empreinte de panier, tax/delivery policy. Tant que la version change, la quote expire et le client doit reconfirmer explicitement.
- `order` : price snapshots USD, amount CDF final, `fxRateSnapshot`, `rateVersion`, date, devise de facturation/paiement CDF ; immuable après confirmation.
- Le marchand peut mettre à jour son taux via authentification forte et audit. Définir plage raisonnable configurable par opérateur / confirmation pour changement extrême ; validation `rate > 0`, précision/limites, protection concurrence et versionnement.

## Légalité territoriale RDC — attention
Sources 2025 indiquent **affichage commercial et factures en CDF seulement** (en ligne compris). Ne pas activer le commutateur USD de l'acheteur à Kolwezi avant avis juridique sur la dernière réglementation. On peut conserver devise d'affichage préférée dans le profil mais `territoryCurrencyPolicy.allowedPublicDisplayCurrencies = ['CDF']` en RDC et CDF requis en réponses publiques.

Le règlement en USD peut être autorisé dans certains cadres distincts ; ne pas en inférer que le prix peut être affiché en USD. Traiter devises d'encaissement et d'affichage comme deux politiques séparées. Toute future autorisation de vente/affichage USD devra être justifiée par règle locale et paramétrage serveur, pas simple choix client.

## Tests incontournables
- Taux initial 2360 et taux nouveau 2300 produisent deux quotes différentes et ne modifient pas anciennes commandes.
- Prix unité 1 USD → 2360 CDF ; plusieurs unités, frais livraison, arrondis des fractions et grand panier : sortie reproductible sans float.
- Changement taux pendant panier → prix serveur recalculé et demande de reconfirmation ; anciennes commandes inchangées.
- Un client ne choisit pas taux, ni monnaie commerciale si territoire interdit ; tentative de checkout USD RDC rejetée / soumise à policy.
- Contrôles de permissions marchands A/B, audit du taux, rollback version nouveau taux, latence.

## Sources
BCC taux indicatifs : https://www.bcc.cd/ (pas une obligation d'utiliser le cours BCC dans tous les contrats sans analyse).
Arrêté 007/2025 : https://www.radiookapi.net/node/276555 ; https://leganews.pro/articles/0198f7d0-72af-7abe-bfcb-013cb9aec343 .
