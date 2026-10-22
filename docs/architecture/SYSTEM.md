# ZAMUREK V1 — architecture de système intégrée

**Normatif 22/10/2026 :** [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [Core intégré](../v1/SHARED-CORE-INTEGRATION.md), [POS](../v1/POS-AND-FISCAL-DOCUMENTS.md). Les anciennes descriptions « une DB PostgreSQL métier par tenant », « nouveau registre ZAMUREK » et « second backend autonome » sont abrogées.

Monarque Connect (dépôt privé) est le **backend NestJS/Prisma/PostgreSQL transactionnel unique** partagé entre Business OS et ZAMUREK : identité, organizations, establishments, item, sales, invoice, payments, cash, entitlements/billing, documents, events et AI Gateway/Runtime.

Les modules commerciaux spécialisés POS terminal/session/cash/document, menus et réservation restaurant, poids, services/booking, devis mobiliers, réparations et venue opt-in sont des **modules Core**, avec API et permissions propres, mais pas des copies des tables financières ni du système de gestion.

ZAMUREK (dépôt produit/applications) fournit les canaux installables Android (React UI embarquée/Capacitor + Kotlin) et Windows (Tauri/Rust), impression locale A4/thermique, écrans métiers, UX discovery/vente et tests/contrats clients. Aucun portail hébergé ZAMUREK sur production ; backend Core expose seulement API HTTP nécessaires, route opérateur derrière VPN/MFA.

Les clients online passent par acheteur e-mail vérifié, les ventes POS peuvent être effectuées avec acheteur de passage **sans compte** mais caissier authentifié. Les transactions financières Core sont atomiques/idempotentes et les factures fiscales restent sous statut bloqué tant que le dispositif légal requis n'est pas prouvé.

Schéma DB PostgreSQL **partagé** du Core avec scopes `organizationId+establishmentId+ownership` et isolation testée, sans DB ZAMUREK dédiée. La venue ne reçoit que listings publiés sur consentement. AI Agent Runtime/knowledge/policies sont également mutualisés, avec outils ZAMUREK spécifiques.
