# ZAMUREK — modèle multi-tenant V1, Core Monarque Connect

**Normatif après ADR-0024.** L'ancien modèle « registry ZAMUREK + DB PostgreSQL dédiée par organization » est **abrogé** pour V1.

## Stockage partagé et droits
Monarque Connect conserve **une seule architecture PostgreSQL partagée**, avec `organizationId` obligatoire en logique serveur et `establishmentId` pour les activités dépendantes de l'établissement. Ce sont les tables et le PrismaService canoniques de Monarque Connect, pas une copie ZAMUREK. L'existence d'une seule DB physique **ne réduit pas** l'obligation d'isolation et de restauration sélective.

Contexte chaque commande : `actorId`/scope (`BUYER`, `MERCHANT`, `CASHIER`, `OPERATOR`, `AGENT`), `organizationId`, `establishmentId`, `objectOwner`, `productCode`, `entitlement`, `channelId`. Un `channelId` public **n'accorde aucun rôle** et ne choisit pas arbitrairement une organisation.

## Buyer / vendeur / venue
Achat **ONLINE** : buyer e-mail vérifié, relation avec la commande contrôlée par ID serveur, aucune obligation d'être Membership staff de la boutique. **POS physique** : acheteur walk-in sans compte/e-mail, mais caissier authentifié avec terminal/session ouverts et permissions établissement.

`Venue/Mall` ne gère que des consentements opt-in et projections *publiques*. Aucun gestionnaire de venue ne voit, par simple appartenance au centre commercial, les paiements, devis privés, historiques clients ou dossiers de réparation.

## Test et exploitation
P0 : cross-org T1/T2 et T2→T1; cross-establishment E1/E2, staff rôle insuffisant, customer C1→C2; product entitlements ZAMUREK-only≠CRM/Enterprise; agent tool unauthorized; venue→ledger refused; idempotence finance concurrente et prix CDF. Sauvegarde du Core et **export/restauration ciblée d'une organisation** réellement testés, non simple restauration de DB entière.

## Extension ultérieure
Bases dédiées par client = **possible option future**, jamais prérequis G1 ni V1 ; nécessite ADR, adapter de persistance et migrations/recovery testées sans rupture des identifiants.

Références : [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [Core](../v1/SHARED-CORE-INTEGRATION.md), [menaces](../v1/SECURITY-THREAT-MODEL.md).
