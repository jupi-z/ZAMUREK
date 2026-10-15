# ADR-0013 — Aucun frontend hébergé en production

**Statut : ADOPTÉ | 2026-10-15**

Le serveur de production expose **backend/API uniquement**, aucune UI HTML commerciale/admin, SSR, SPA, PWA ni Swagger UI public. Apps acheteur et marchand Android séparées, React UI embarquée + Capacitor/Kotlin. Consoles Windows opérateur/marchand React embarquée + Tauri 2/Rust, installateurs EXE/MSI.

Alternative abandonnée : consoles marchand/platform **web hébergées** évoquées pendant G0 initial. Les anciens répertoires merchant-admin/platform-admin ont été retirés au profit de clients installables.

Conséquences : pipeline signing/distribution plus lourd, aucune administration de secours par navigateur, tests Windows réels indispensables. OpenAPI uniquement document/artefact CI par défaut. Référence : https://v2.tauri.app/distribute/windows-installer/ .
