# xShop — index documentaire révisé

**Cadrage métier validé le 15 octobre 2026. G0 documentation seulement ; G1 non implémenté.**

## Priorité documentaire
1. [Décisions expressément approuvées](DECISIONS-VALIDATED-2026-10-15.md) — **prime sur les hypothèses historiques**.
2. [PRD](product/PRD.md), [fonctionnalités V1](product/V1-FUNCTIONAL-SPEC.md) et [parcours clients](product/USER-JOURNEYS.md).
3. [Architecture système](architecture/SYSTEM.md), [tenancy](architecture/TENANCY.md), [modèle de données](architecture/DATA-MODEL.md).
4. [Identité](architecture/IDENTITY.md), [auth clients](architecture/AUTH-CUSTOMER.md), [CDF/USD](architecture/CURRENCY-CDF-USD.md).
5. [Android](architecture/ANDROID.md), [clients Windows / production API-only](architecture/CLIENTS-DEPLOYMENT.md), [white-label](architecture/WHITE-LABEL.md).
6. [API](architecture/API.md) et [contrat OpenAPI initial](../packages/contracts/openapi/xshop-v1.yaml).
7. [Paiements](architecture/PAYMENTS.md), [marketplace future](architecture/MARKETPLACE.md), [événements](architecture/EVENTS.md).
8. [Sécurité](architecture/SECURITY.md), [exploitation](architecture/OPERATIONS.md).
9. [Audit G0 initial](quality/AUDIT-G0-2026-10-15.md), [tests](quality/TEST-STRATEGY.md), [conditions de recette](quality/ACCEPTANCE.md).
10. [Feuille de route](ROADMAP.md), [questions externes restantes](OPEN-QUESTIONS.md), [ADRs](decisions/README.md).

## Statuts
- **Validé** : décision métier explicitement choisie par le porteur.
- **Proposé** : choix technique délégué, encore soumise à validation d'implémentation et tests.
- **Réalisé** : existe et possède preuves d'exécution / tests ; aucun module applicatif n'a ce statut en G0.
- **Hors V1** : non requis pour premier lancement.

## Sources techniques
NestJS https://docs.nestjs.com/ ; Capacitor https://capacitorjs.com/docs/ ; Tauri 2 https://v2.tauri.app/distribute/windows-installer/ ; PostgreSQL https://www.postgresql.org/docs/ ; OWASP https://owasp.org/API-Security/ ; OpenAPI https://spec.openapis.org/oas/v3.1 .
