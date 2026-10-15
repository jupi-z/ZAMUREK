# Modèle conceptuel des données — xShop V1 après arbitrages

**Deux niveaux de stockage** : registry/identity plateforme distincte et **une base PostgreSQL métier par tenant**.

## Registry (base centrale)
- tenant(id UUID, slug, status, db_secret_ref, schema_version, created_at).
- storefront_channel(id, tenant_id, client_type, app_identifier, build_config_version, status).
- global_customer_identity(id, phone_e164 unique, password_hash, phone_verified_at, status, created_at).
- customer_auth_session(id, global_customer_id, refresh_hash, revoked_at, expires_at).
- otp_challenge(id, global_customer_id, purpose, code_hash, expires_at, attempts, used_at).
- staff_identity(id, credentials_ref, status), tenant_membership(user_id, tenant_id, role, permission_set).
- platform_operator / platform_audit / provisioning_job / subscription_contract (facturation de l'abonnement xShop hors V1).
- Ne pas placer produits, commandes, adresses de livraison ou moyens de paiement marchand dans le registry.

## Dans chaque DB tenant
- store_settings (name, logo, branding, default_currency, supportedCurrencies=[CDF,USD], modes).
- category, product (name, status), product_variant(id, product_id, options, active).
- **product_variant_price(variant_id, currency_code, amount_minor)** ; contrainte unique (variant_id,currency_code) ; **2 tarifs actifs par variante commercialisée**.
- product_media (clé média, position, droits).
- delivery_zone(id, name, enabled), **delivery_zone_fee(zone_id,currency_code,amount_minor)**.
- cart(id, global_customer_id, channel_id, currency_code, expires_at), cart_item(cart_id,variant_id,quantity).
- customer_profile(id, global_customer_id, contact, consent_scope).
- order(id, tenant_local_number, global_customer_id, customer_profile_id, channel_id, currency_code, fulfillment_snapshot, subtotal_minor, delivery_minor, total_minor, status, timestamps).
- order_item(order_id, variant_snapshot, item_name_snapshot, unit_price_minor, quantity, line_total_minor, currency_code).
- payment(id, order_id, currency_code, amount_minor, method, status, merchant_reference).
- cancellation_request(order_id, requested_by, reason, status, resolved_by, resolved_at).
- order_status_history, checkout_idempotency (global_customer_id, key, request_fingerprint, response_snapshot_encrypted, expires_at).
- outbox_event, audit_log (PII-redacted).

## Invariants
- Les order / cart sont **mono-tenant, mono-devise** ; choix CDF/USD explicite, jamais conversion automatique.
- Un tarif requis manquant bloque publication / checkout ; devise livraison identique devise commande.
- Calcul serveur, snapshots et transactions ; contrôle d'accès par (global_customer_id, tenantContext, order ownership).
- Pas de guest_tracking_credential et pas de guest_session_hash en V1.
- Token/OTP hachés, jamais dans journaux ; aucune donnée commerciale tenant exposée à un autre.
- Évolution marketplace : réf (tenantId,productId), opt-in de visibilité uniquement, source of truth DB tenant.

## Migrations
Migrations distinctes registry / tenant ; versions, déploiement par cohortes, restauration ciblée, tests A/B ; exigences SQL et colonnes exactes à figer en G1.

Voir [devises](CURRENCY-CDF-USD.md), [identité](AUTH-CUSTOMER.md), [tenancy](TENANCY.md).
