# ZAMUREK — événements sur la Event Fabric commune

**La Event Fabric et l'Outbox Monarque Connect sont canoniques** (modèles, contrat, publication, métriques 10A). Ne pas déployer `eventEnvelope`, worker, broker ou outbox transactionnelle **ZAMUREK indépendante**.

Les modules métiers ZAMUREK enregistrent leurs événements **dans la même transaction Core** que SalesOrder/PaymentRecord/CashMovement ou bookings concernés. Ils utilisent le schéma de `Docs/43_DOMAIN_EVENT_CONTRACT.md` du Core, avec eventId/type/version, org, établissement, scope, correlation/causation et classification. Aucune PII ou historique financier dans les projections venue/mall publiques.

Événements spécialisés envisagés : `pos.session.opened`, `pos.sale.paid`, `pos.session.closed`, `restaurant.order.preparing`, `appointment.booked`, `repair.case.updated`, `venue.optin.revoked`. Les noms et formes seront fixés dans le Core en 10A.5 et versionnés ; ce document ne prouve pas leur existence.

Tool/Agent runs ZAMUREK réutilisent Gateway/Runtime commun Monarque Connect et ses permissions. Les schemas JSON locaux restent des **brouillons non canoniques** jusqu'à génération depuis le Core.
