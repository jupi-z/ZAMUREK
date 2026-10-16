# Architecture xShop — édition 16 octobre

## Un serveur de production backend/API seulement
Services NestJS : Platform Registry/provisioning, Global Identity e-mail verified, Merchant Membership + MFA, Catalog (USD source), FX (rate tenant versioned), Quote (public CDF), Cart/Checkout/Orders, Payment Manual, Fulfillment, SaaS Plan BASIC, Audit/Outbox.

Registre central + **une DB PostgreSQL métier par tenant** ; gestion pools/credentials bornés. Stockage média tenant-scopé, worker de synchronisation. Aucun HTML UI/SPA/SSR/PWA/Swagger UI hébergé.

## Applications installables
- Android acheteur : React UI → Capacitor → Kotlin API/cache/auth, boutique marque.
- Android marchand séparé : React UI → Capacitor → Kotlin, prix USD/taux USD-CDF/commandes.
- Windows opérateur : React embarquée → Tauri 2/Rust, **accès plateforme VPN**.
- Windows marchand ultérieurement, marketplace Android future opt-in.

## Frontières réseau
Endpoint clients publics en HTTPS 443 + auth et permissions ; /v1/merchant auth/RBAC+TOTP ; /platform/v1 via VPN seulement ; PostgreSQL, secrets, monitoring et stockage privé non exposés. CORS ne remplace pas auth. Domaines candidats `xshop-api-test.shuleops.com`, `xshop-api.shuleops.com` non configurés.

## Prix
USD seule source catalogue et tarif livraison, FX tenant versionné, quote CDF serveur, snapshot taux et montants sur commande ; publication/facture CDF RDC par politique réglementaire conservatoire. Aucun FX opérant dans une UI faisant autorité.

## Risques et preuves
Validation légale arrêté prix CDF, rate merchant/official, délivrance e-mail SMTP, quota VPS, restauration DB A sans B, IDOR, performances natives. Documents de référence : [FX](FX-PRICING.md), [réseau](NETWORK-EXPOSURE.md), [identité](AUTH-NO-SMS.md).
