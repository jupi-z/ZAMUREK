# Modèle de données — contrat conceptuel V1

## Identifiants et montants
UUIDs/identifiants opaques pour les entités. Chaque objet métier existe dans **une DB tenant**. IDs exposés avec contexte tenant ; jamais utiliser un ID seul pour autoriser. Prix et frais en entier signé 64 bits d'unités mineures, sérialisés en **chaîne décimale** dans les DTO JSON pour éviter les pertes IEEE-754 en JS. Devise ISO 4217 par commande ; conversion multi-devises hors V1.

## Base registry
- tenant : id, slug unique, status, db_ref, schema_version, timestamps.
- storefront_channel : id, tenant_id, kind, identifier unique, config_version, enabled.
- platform_user / staff_identity : données de connexion distinctes des fiches clients métier.
- tenant_membership : user_id, tenant_id, role, status.
- provisioning_job : tenant_id, idempotency_key, step, state, attempts, audit.
- platform_audit_log : acteur, action, cible, raison, correlation_id, instant.

## Base tenant
- store_settings : branding, devise, contact public, modes de remise, statut commerce.
- category : id, parent_id nullable, name, slug, sort_order, state.
- product : id, category_id, sku nullable, name, description, status, timestamps.
- product_variant : id, product_id, public_options JSON validé, price_minor, currency_code, status. Un produit sans variantes conserve une variante par défaut.
- product_media : id, product_id, key média, ordering, alt_text, status.
- delivery_zone : id, name, fee_minor, currency_code, enabled.
- cart : id, channel_id, guest_session_hash, currency_code, expires_at.
- cart_item : id, cart_id, variant_id, quantity > 0, added_at.
- customer_profile : id, display_name, phone, contact_consent ; optional_global_identity_ref (sans clé d'accès globale).
- order : id, tenant_local_number unique, channel_id, customer_snapshot, fulfillment_snapshot, status, currency_code, subtotal_minor, delivery_minor, total_minor, created_at.
- order_item : id, order_id, variant_id nullable, sku_snapshot, name_snapshot, options_snapshot, unit_price_minor, quantity, line_total_minor.
- payment : id, order_id, method, provider nullable, status, amount_minor, currency_code, external_ref nullable ; aucun PAN stocké.
- payment_event : id, payment_id, provider_event_id unique sous provider, signature_verified, processed_at.
- checkout_idempotency : tenant_id implicitement porté par DB, actor/session, key, request_fingerprint, response_replay_encrypted, expires_at. Le replay du secret invité a une durée courte, un chiffrement côté serveur et une vérification stricte du même acteur/session. La preuve durable de suivi reste uniquement son hash.
- order_status_history : order_id, from, to, actor, note, timestamp.
- guest_tracking_credential : order_id, token_hash, created_at, expires_at, revoked_at.
- outbox_event : id, type, version, aggregate_id, payload filtré, created_at, published_at, retry_count.
- audit_log : actor, action, object_id, correlation_id, occurred_at, redactable metadata.

## Invariants relationnels
- Une commande est mono-tenant et mono-devise ; items liés à la même DB uniquement.
- total = sous-total + frais de remise (moins réductions à introduire plus tard). Les montants sont recalculés serveur.
- Les snapshots de commande ne suivent jamais une modification ultérieure de produit.
- Idempotence checkout unique par acteur/session et clé, avec empreinte de requête ; même clé + payload différent = 409.
- Les transitions d'état sont explicitement contrôlées.
- Contraintes SQL/transactions pour ne jamais enregistrer commande sans ses lignes.

## Contrat de migration
Distinguer schéma du registre et schéma des tenants. Migration de chaque nouveau tenant de zéro jusqu'à version actuelle ; tests d'upgrade entre deux versions précédentes. Aucune table partagée de produits ou commandes dans registry.

