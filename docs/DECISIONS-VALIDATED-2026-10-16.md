# xShop — arbitrages G0 révisés le 16 octobre 2026

**Statut : HISTORIQUE xShop. Pour ZAMUREK 1.0.0, [les spécifications ZAMUREK V1](v1/README.md) et les ADR-0020→0023 prévalent.** Au 16/10 ce document remplaçait les décisions xShop du 15/10. Le nom `xShop` est provisoire ; ne pas le figer dans le branding utilisateur final. Le code du système n'est pas encore implémenté.

## Décisions nouvelles du propriétaire

1. **Prix de référence USD seulement** pour les catalogues/variantes et tarifs de livraison. CDF **calculé**, non saisi comme prix indépendant.
2. **Taux USD→CDF configurable par marchand** et historisé. Exemple fourni : `1 USD = 2 360 CDF` ; c'est une hypothèse de paramétrage du marchand, **pas un cours officiel vérifié**. La BCC publie ses propres cours indicatifs ; la configuration de chaque commerçant doit être confirmée avant vente réelle.
3. **La conversion qui engage la commande est calculée par le backend** à partir du prix USD et du taux retenu ; React/Kotlin/Rust ne peuvent effectuer qu'un aperçu non contraignant. Une commande conserve ses montants, devise de transaction, version du taux et snapshots, même après modification du taux.
4. **Production serveur strictement API-only**. Ne pas exposer l'administration plateforme sur Internet public. Les routes d'achat et d'identité nécessaires aux applications distantes sont publiques au sens réseau, mais protégées. Bases, secrets, métriques, backups et panneau opérateur restent réseau privé/VPN.
5. Les domaines `shuleops.com` sont disponibles comme **base provisoire des sous-domaines xShop**. Proposition non réservée : `xshop-api-test.shuleops.com` pour tests, `xshop-api.shuleops.com` pour production future. Aucune modification DNS ni déploiement effectués.
6. **Pas de SMS au départ.** Identité client recommandée : e-mail + mot de passe, vérification de possession par e-mail (SMTP configurable), récupération sécurisée ; MFA TOTP pour comptes marchands et opérateurs. Aucun prestataire e-mail n'est contracté ; SMTP réel est une dépendance avant vente.
7. **Offre SaaS unique** : `7 USD / mois / boutique` ; aucun frais d'installation, ni commission sur les commandes V1. Tarification de référence USD, présentation/facturation RDC en CDF suivant règles applicables et taux de facturation **plateforme**, séparé du taux du marchand.
8. Commerçant pilote réel **non fixé**. Utiliser le tenant **démonstration synthétique** `xShop Atelier` uniquement pour tests ; coordonnées/moyens de paiement fictifs. Le commerçant réel et ses informations ne sont pas requis pour coder G1/G2.
9. Continuer Android acheteur + Android marchand, Windows installable pour opérateur ; aucun client web déployé. Futur marketplace opt-in, sans obsolescence des apps personnalisées.

## Alerte juridique majeure découverte et garde-fou de conception

L'arrêté ministériel RDC **n° 007/CAB/VPM/MIN-ECONAT/DMS/AKM/2025 du 14 juillet 2025**, rapporté comme publié au Journal officiel en août 2025, impose, selon les sources publiques identifiées, la **publicité des prix et la facturation en CDF**, y compris en ligne ; le règlement en devises peut rester permis selon réglementation BCC.

En conséquence, pour le pilote RDC :
- La base tarifaire **peut rester USD en interne**, mais l'affichage commercial acheteur est **CDF seulement** par défaut.
- Une préférence client « afficher USD » ne doit **pas** être activée sur les surfaces commerciales RDC tant qu'une validation juridique fiable ne justifie pas cette possibilité.
- Checkout commercial et preuve/facture client RDC sont libellés **CDF** ; si un règlement USD est admis, il est enregistré avec devise et conversion conformément au cadre confirmé (pas de mélange silencieux). Ne pas activer la collecte USD sans validation.
- Le compte marchand peut gérer son **taux de conversion**, mais les interfaces de prix commercial public appliquent les règles du pays.
- Garder un `territoryCurrencyPolicy` paramétrable pour de futurs pays ; ne jamais contourner le garde-fou par simple toggle de préférence client.

Sources consultées (revue non juridique) :
- Arrêté 007/2025, synthèse publique : https://www.radiookapi.net/node/276555
- Rapport juridique sur la publication et l'affichage CDF : https://leganews.pro/articles/0198f7d0-72af-7abe-bfcb-013cb9aec343
- Banque centrale du Congo, taux : https://www.bcc.cd/
- Code du numérique, ordonnance-loi 23/010 du 13 mars 2023, source officielle : https://are.gouv.cd/download/ordonnance-loi-23-010-du-13-mars-portant-code-du-numerique/

Ce document est **une mesure conservatoire de conception**, pas une opinion juridique formelle. Vérifier texte officiel actuel, exceptions applicables, taxes et facturation avant ouverture commerciale.

## Architecture technique décidée par délégation

- PostgreSQL tenant : `product_variant.price_usd_minor` ; `delivery_zone.base_fee_usd_minor` ; `fx_rate_version(tenant, USD→CDF, decimalRate, changedBy, effectiveAt, version)`.
- Checkout quote côté backend : dérivation CDF en précision décimale, arrondi documenté ; devis CDF confirmé et figé en commande avec snapshots USD / taux / CDF. Aucun simple calcul React faisant autorité.
- Déclencheur de reconfirmation si taux, prix ou livraison change avant commande.
- Identité globale e-mail vérifié, hash de mot de passe et sessions sécurisées ; staff/opérateurs avec TOTP.
- Accès publique Internet minimal par allowlist de routes /v1 publiques de catalogue et /auth/v1 ; routes /v1/merchant protégées par auth/roles/rate limits, /platform/v1 accessible via VPN uniquement.
- SMTP configurable, API backend HTTPS, objets médias limités, DB privée ; aucune console HTML hébergée.
- Abonnement `BASIC` à 7 USD mensuel unique, séparé de l'encaissement marchand ; aucun mode de reversement xShop.
- Aucun hébergement ou sous-domaine présumé fonctionnel avant preuve d'inventaire et tests DNS.

## Supersession explicite

Remplace :
- l'ADR-0012 « deux prix USD et CDF indépendants » ;
- le choix `téléphone + OTP SMS` dans l'ancienne proposition AUTH-CUSTOMER ;
- l'hypothèse de devises affichées librement dans la V1 RDC ;
- les valeurs d'offre SaaS non renseignées.

À intégrer dans tous les documents actifs, OpenAPI et tests. Les ADR historiques restent accessibles mais **marqués remplacés**.
