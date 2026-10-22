> **ARCHIVE HISTORIQUE — critères xShop remplacés.** La source officielle est [ZAMUREK QUALITY-REQUIREMENTS](../v1/QUALITY-REQUIREMENTS.md) et [RELEASE-GATES](../v1/RELEASE-GATES.md). Ne pas déclarer V1 complète depuis ce texte ancien.

# Critères d'acceptation xShop — édition 16 octobre 2026

## G0 documentaire
Arbitrages 16/10 enregistrés, documents actifs alignés USD source + FX merchant versionné + **CDF public RDC**, e-mail sans SMS, accès opérateur VPN, plan BASIC 7 USD, noms provisoires. Contrat OpenAPI cohérent et scripts structurels ; **aucune validation de production prétendue**.

## G1 — Fondations exécutables
NestJS/Prisma/Postgres, registry global et deux DB tenant, migrations/clients SQL limités, email auth/refresh, route taux marchand, policy territoriale RDC et segmentation routes (plateforme VPN), builds Android Kotlin/Capacitor et Windows Tauri de base, CI avec validateurs normatifs OpenAPI ; tests A/B.

## G2 — Commerce
Produit tarif USD, taux par tenant/version, prix publics CDF, devis CDF horodaté/quoteId, checkout idempotent et snapshot, paiement manuel/à livraison, livraison zone USD→CDF et annulations à la demande ; tests de réconciliation/rounding/immutabilité.

## G3 — Apps
APK acheteur et marchand distincts, console opérateur Windows EXE/MSI, ressources React embarquées, réseau/cache/sessions Kotlin et Rust, workflow devise conforme à politique RDC, pas de frontend web sur serveur.

## G4 — Préouverture commerciale
Avis juridique sur arrêté 007/2025, affichage/facture et paiement en devise, validité du taux merchant et fiscalité ; SMTP de vérification réel, VPS/domaines DNS privés sécurisés, compte opérateur MFA et VPN, sauvegarde/restauration A sans B, politique de données, contrat commercial BASIC 7 USD/mois affiché/facturé conformément aux obligations RDC.

## G5 — Industrialisation
Automatisation clients white label, anciens clients restent compatibles, pricing SaaS révisable uniquement par nouvelles versions de plan, marketplace opt-in ultérieure.

## Blocages absolus
Taux flottant non fiabilisé, faux prix CDF client, ancien montant recalculé après modification taux, SMS implémenté contre choix, interface admin web en prod, accès /platform/v1 public, commande sans auth, double commande après retry, isolation SQL non démontrée.

Des tests réels devront accompagner chaque gate. G0 n'implique pas une fonctionnalité opérationnelle.
