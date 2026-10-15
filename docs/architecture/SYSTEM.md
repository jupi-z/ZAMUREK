# Architecture système xShop — après arbitrages

## Production : services uniquement
- HTTPS/reverse proxy, API NestJS REST/OpenAPI (pas Swagger UI public), workers et traitements internes.
- Registry/identity centrale ; **une DB PostgreSQL métier par boutique** et comptes SQL isolés ; stockage média tenant-scopé.
- **Aucun serveur d'interface** : pas de portail web, SSR, PWA, SPA ni admin hébergée. Les assets React sont **embarqués dans des applications installables**.

## Clients V1
- App Android acheteur white-label = React UI + Capacitor + Kotlin.
- App Android marchand séparée = React UI + Capacitor + Kotlin.
- Application Windows opérateur = React UI + Tauri/Rust, livrée EXE/MSI.
- Option Windows marchand = React UI + Tauri/Rust, installable sans UI distante.
- Marketplace future = client installable d'API existante, opt-in marchand.

## Modules backend
Tenant registry/provisioner ; comptes globaux clients et auth sessions ; staff/memberships ; catalog/categories/variants/prices CDF USD ; cart mono-devise ; checkout authentifié idempotent ; orders ; payment manual/pay-on-delivery ; zone delivery + fees CDF USD ; audit et outbox ; projection discovery future.

## Invariants
Backend seul autoritaire (prix, devise de commande, identité/permissions, statuts, paiements). No cross-tenant DB connection based on user input. DB tenant sélectionnée après résolution et contrôle serveur ; secrets hors clients. **Aucune transaction cross-tenant au checkout**. Outbox locale transactionnelle ; publication/replay idempotents.

## Extensions
Pas de microservices au lancement ; DB par tenant gérée avec pools bornés/éviction. Les besoins CPU, mémoire, migrations et backup sont testés sur VPS candidat avant production.

Références : https://docs.nestjs.com/ ; https://capacitorjs.com/docs/ ; https://v2.tauri.app/distribute/windows-installer/ .
Voir [clients et déploiement](CLIENTS-DEPLOYMENT.md), [tenancy](TENANCY.md), [devises](CURRENCY-CDF-USD.md), [auth](AUTH-CUSTOMER.md).
