# Deux devises par boutique — CDF / USD

**Décision validée :** une boutique propose simultanément des prix en CDF et en USD. Les montants sont fixés **séparément** par le marchand. **Aucun calcul implicite de taux de change**, aucun prestataire FX nécessaire à la V1.

## Domaine
- StoreSettings.supportedCurrencies = [CDF, USD] ; StoreSettings.defaultCurrency une des deux.
- ProductVariantPrice (variantId, currencyCode) clé unique ; priceMinor entier >= 0, précision 64 bits.
- DeliveryZoneFee (zoneId, currencyCode) clé unique ; feeMinor >= 0.
- Si les deux monnaies sont activées pour tous les produits commandables, une variante ACTIVE doit posséder **les deux** tarifs valides. Le commerçant ne peut pas publier un produit incomplet.
- Panier : `currencyCode` choisi par client parmi CDF/USD, lignes et frais recalculés dans cette monnaie. Changement de devise recalcule intégralement ; ne convertit pas de nombres côté client.
- Checkout : verrouiller currencyCode, snapshots prix produit et livraison, total et mode de paiement dans cette devise. Un paiement manuel ou à la livraison doit être libellé dans la devise de commande ; confirmation du commerçant dans la même monnaie.
- Paiement reçu dans une autre devise : hors V1, ne pas marquer PAID ; procédure de rapprochement/traitement ultérieure explicite.
- Administration : formulaire de prix CDF + USD, frais livraison CDF + USD, mode d'encaissement par devise ; aucune cotation automatique.
- Les unités mineures de chaque monnaie suivent ISO 4217 et la table de précision documentée/testée. JSON: `amountMinor` sous forme de chaîne décimale pour éviter les pertes de précision JS.
- Tri prix, filtres et affichage utilisent toujours une monnaie explicite. Aucun total mélangeant des monnaies.

## Contraintes
- La confirmation de prix repose sur le backend, non la WebView/Kotlin/Rust.
- Devise de la commande immuable après validation.
- Une même boutique peut posséder des paniers distincts selon devise ; un panier a exactement une monnaie.
- Fiscalité, règles d'arrondi, preuve de règlement et obligations de prix en RDC à vérifier avant exploitation.

## Cas de test bloquants
Deux tarifs pour une variante ; achat en CDF et en USD ; switch du panier ; livraison tarifée dans chacune ; publication sans un tarif rejetée ; tentative de paiement en devise différente rejetée ; retry idempotent ; prix modifié entre panier et checkout = montant serveur confirmé / conflit explicite ; isolation tenant A/B.

Voir [modèle de données](DATA-MODEL.md) et [paiements](PAYMENTS.md).
