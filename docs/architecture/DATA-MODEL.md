# Modèle de données conceptuel xShop V1 — 16 octobre 2026

## Registry / identité globales
- tenant(id UUID, slug, status, databaseSecretRef, schemaVersion), storefront_channel(id, tenantId, platform, appId).
- global_customer_identity(id, emailOriginal, emailCanonical unique, passwordHash, verifiedAt, status) ; session_refresh(id, identityId, tokenHash, expiresAt, revokedAt) ; email_challenge(identityId, purpose, tokenHash, expiresAt, consumedAt, attempts).
- merchant_staff(id, emailCanonical, hash, totpCredentialRef), tenant_membership(staffId, tenantId, role, enabled).
- platform_operator(id, authRef, totpCredentialRef), platform_audit, provisioning_job.
- subscription_plan(id, code BASIC, **basePriceUsdMinor = 700**, periodMonths=1), merchant_subscription(tenantId, plan, state, cycle).
- platform_fx_rate/version (distinct du marchand) pour calcul réglementaire CDF des factures xShop, sans toucher aux commandes boutiques.

## Base PostgreSQL par commerçant
- store_settings(..., `baseCurrency='USD'`, `territory='CD'`, legal_display_currency='CDF', fulfillment flags).
- product(id,name,status), product_variant(id, productId, attributes, **basePriceUsdMinor**), product_media, category.
- delivery_zone(id,name,enabled, **baseFeeUsdMinor**).
- **tenant_fx_rate**(id, usdToCdfNumerator, usdToCdfDenominator, decimalText, version, activeFrom, changedBy, audit) — historique immuable ; référence utilisateur 2360 uniquement pour test, confirmer en vente.
- cart(id, ownerGlobalIdentityId, channelId, rateVersion, quoteExpiresAt, **saleCurrency='CDF'**), cart_item(variantId, quantity).
- price_quote(id, cartId, rateVersion, pricesSourceUsd, amountsCdf, roundingPolicyVersion, expiresAt, fingerprint), transactionnel et contrôlé serveur.
- order(id, customerGlobalIdentityId, orderLocalNumber, currency='CDF', rateSnapshot, rateVersion, **subtotalCdfMinor**, feeCdfMinor, totalCdfMinor, recipientSnapshot, createdAt, state).
- order_item(variantId, productSnapshot, unitBaseUsdMinor, **unitCdfMinor**, quantity, lineCdfMinor) ; payment(id, orderId, receivedCurrency, receiptAmountMinor, saleCurrency='CDF', dueCdfMinor, status, merchantRef).
- cancellation_request, checkout_idempotency, outbox_event, audit_log.

## Invariants
- Référence produit **uniquement USD**, pas `product_variant_price` dual-table ; calcul des valeurs CDF effectué par le backend.
- Affichage commercial et libellé des documents RDC en CDF par politique conservatoire ; aucune option client USD sur territoire CD sauf validation légale ultérieure.
- Snapshot immuable du taux et des montants au moment du checkout ; changer le taux ne réécrit ni anciennes commandes ni historique.
- Pas de `phone_e164` dans l'auth V1, mais téléphone du destinataire de livraison dans les commandes tenant.
- Facturation xShop 7 USD mensuel en référence interne, **CDF public/facture RDC via taux plateforme** ; pas de commission sur commandes.
- Séparation tenant SQL, validation (identité, tenant, propriété de l'objet) pour chaque accès.

## Gate G1
Établir migrations, contraintes d'intégrité, test des arrondis et TTL de quote, deux DB tenant, sauvegarde ciblée. Ne pas utiliser de float pour la monnaie.

Voir [FX-PRICING](FX-PRICING.md), [AUTH-NO-SMS](AUTH-NO-SMS.md), [legal](../legal/RDC-INITIAL-REVIEW.md), [abonnement](SUBSCRIPTIONS.md).
