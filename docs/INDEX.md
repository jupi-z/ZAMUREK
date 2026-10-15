# Index de la documentation — xShop

**Statut : G0, conception approuvée en tant que base de travail ; implémentation non commencée.** Les fichiers dans apps/ sont des emplacements prévus, pas des applications exécutables.

## Produit
- [Vision et périmètre](product/PRD.md)
- [Spécification fonctionnelle V1](product/V1-FUNCTIONAL-SPEC.md)
- [Parcours et cas limites](product/USER-JOURNEYS.md)

## Architecture
- [Vue système](architecture/SYSTEM.md)
- [Isolation multi-tenant et provisioning](architecture/TENANCY.md)
- [Données et invariants](architecture/DATA-MODEL.md)
- [Identité et habilitations](architecture/IDENTITY.md)
- [API / contrats](architecture/API.md)
- [Paiements et commandes](architecture/PAYMENTS.md)
- [Client Android hybride à cœur Kotlin](architecture/ANDROID.md)
- [White label et génération d'apps](architecture/WHITE-LABEL.md)
- [Marketplace à venir](architecture/MARKETPLACE.md)
- [Événements et intégration](architecture/EVENTS.md)
- [Sécurité](architecture/SECURITY.md)
- [Exploitation](architecture/OPERATIONS.md)

## Pilotage
- [Audit transversal G0 : risques et corrections](quality/AUDIT-G0-2026-10-15.md)
- [Tests et vérifications](quality/TEST-STRATEGY.md)
- [Critères d'acceptation](quality/ACCEPTANCE.md)
- [Jalons G0 → G5](ROADMAP.md)
- [Décisions ouvertes](OPEN-QUESTIONS.md)
- [ADRs](decisions/README.md)
- [Contrat OpenAPI provisoire](../packages/contracts/openapi/xshop-v1.yaml)

## Comment interpréter les statuts
- **Décidé** = direction architecturale de travail, réversible par nouvel ADR.
- **Proposé** = ne pas coder comme hypothèse définitive avant validation.
- **Livré** = implémenté, testé, déployable et vérifié par la procédure de recette.
- **Hors V1** = incompatible avec le périmètre de livraison initiale, sauf arbitrage explicite.

## Sources techniques primaires
- NestJS : https://docs.nestjs.com/
- Prisma ORM v7 : https://www.prisma.io/docs/orm/v7
- PostgreSQL : https://www.postgresql.org/docs/
- Capacitor : https://capacitorjs.com/docs/
- Android Architecture : https://developer.android.com/topic/architecture
- OWASP API Security : https://owasp.org/API-Security/
- OpenAPI : https://spec.openapis.org/oas/latest.html

Ces références décrivent les technologies ; elles ne constituent pas une preuve que notre implémentation a été testée.

