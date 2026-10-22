# Infrastructure ZAMUREK — CLIENTS, pas un second Core

**Aucun backend à déployer depuis ce dépôt.** Monarque Connect privé possède le backend transactionnel NestJS/Prisma/PostgreSQL, identités, tenancy, ventes, caisse, factures, Billing, Event Fabric et IA. Le projet ZAMUREK fournit clients et tests d'intégration, pas de registry autonome ni DB par commerçant.

Pour tests G1, utiliser un Core local/staging synthétique **fourni par Monarque Connect phase 10A.5** avec deux organisations logiquement séparées dans PostgreSQL Core, deux établissements sous une organisation, buyers C1/C2, caissier walk-in, fonctionnalités canal opt-in et fake mail en développement uniquement. Pas de secrets ni de DB métier sensible dans ce dépôt public.

CI ZAMUREK compile ses clients et vérifie compatibilité avec la version identifiée des contrats Core; la CI backend complète appartient au Core privé. Les API publiques doivent être HTTPS et scopes côté serveur ; administrateur via VPN/MFA, aucun frontend web de production.

VPS/DNS proposés ne sont pas configurés et ne doivent pas être créés automatiquement. Voir [architecture](../docs/v1/SHARED-CORE-INTEGRATION.md) et [roadmap](../docs/v1/INTEGRATION-ROADMAP.md).
