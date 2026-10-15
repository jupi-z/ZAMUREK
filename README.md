# xShop

**Plateforme de commerce électronique multi-tenant, conçue pour lancer des boutiques indépendantes avec des applications Android personnalisées, puis les réunir éventuellement dans une marketplace commune.**

> État du projet : **G0 — fondations et spécifications**. Ce dépôt décrit la cible et les contrats initiaux ; aucun backend, application Android ou paiement opérationnel n'est encore livré. Ne pas présenter les éléments documentés comme implémentés.

## Principes structurants

1. **Un cœur commercial commun** : API de commerce et services partagés ; aucune copie indépendante du backend par commerçant.
2. **Une base PostgreSQL métier dédiée à chaque tenant**, plus un registre de plateforme distinct. Provisioning, migrations, sauvegardes et isolation obligatoires.
3. **Des applications personnalisées qui coexistent** avec une future marketplace ; les applications existantes ne sont jamais rendues obsolètes par l'ajout d'un nouveau canal.
4. **Android : React pour l'interface uniquement** ; Capacitor pour le pont ; Kotlin pour les requêtes, la persistance, l'authentification côté appareil et les intégrations système. Le serveur reste autoritaire.
5. **MVP réellement achetable** : catalogue, panier, commande, retrait/livraison, paiement à la livraison ou manuel, gestion marchand et suivi. Les paiements électroniques seront intégrés après validation du prestataire.
6. **Contrats versionnés, contrôle d'accès rigoureux et dépendances maîtrisées**. Ne jamais déduire les autorisations d'un tenant ID fourni par le client.

## Applications prévues

- `apps/api` : backend NestJS modulaire.
- `apps/storefront-android` : socle Android white-label React + Capacitor + Kotlin.
- `apps/merchant-admin` : espace de gestion de chaque commerce.
- `apps/platform-admin` : création et supervision des boutiques.
- `apps/marketplace` : emplacement réservé, hors V1.
- `packages/contracts` : API OpenAPI et contrats d'intégration.

## Documentation : commencer ici

- [Index et état des livrables](docs/INDEX.md)
- [Vision / PRD](docs/product/PRD.md)
- [Spécifications fonctionnelles V1](docs/product/V1-FUNCTIONAL-SPEC.md)
- [Architecture système](docs/architecture/SYSTEM.md)
- [Isolation multi-tenant](docs/architecture/TENANCY.md)
- [Modèle de données](docs/architecture/DATA-MODEL.md)
- [Paiements et commandes](docs/architecture/PAYMENTS.md)
- [Architecture Android](docs/architecture/ANDROID.md)
- [Personnalisation des applications](docs/architecture/WHITE-LABEL.md)
- [Préparation de la marketplace](docs/architecture/MARKETPLACE.md)
- [Sécurité et conformité](docs/architecture/SECURITY.md)
- [Exploitation](docs/architecture/OPERATIONS.md)
- [Tests et exigences de qualité](docs/quality/TEST-STRATEGY.md)
- [Contrat API initial](packages/contracts/openapi/xshop-v1.yaml)
- [Feuille de route et jalons](docs/ROADMAP.md)
- [Décisions ouvertes](docs/OPEN-QUESTIONS.md)
- [ADR — décisions architecturales](docs/decisions/README.md)

## État et démarrage

Le dépôt est volontairement **documentation-first** : les arborescences applicatives contiennent des README, mais les projets NestJS et Android ne sont pas encore générés. Les commandes `pnpm build`, `pnpm test` et les builds Android n'existent pas encore et ne doivent pas être présentés comme fonctionnels.

Exécuter `python3 scripts/validate_docs.py` pour vérifier les chemins et les liens Markdown locaux. La CI reproduit ce contrôle.

Les variables d'environnement proposées figurent dans `.env.example` ; aucun secret ni identifiant marchand ne doit être commité. Les versions exactes, fournisseurs de paiements, hébergement et politiques de sauvegarde sont conditionnés aux essais et décisions listés dans la documentation.

## Gouvernance

- Travailler par branches et pull requests dès les premiers développements ; `main` doit rester documenté et cohérent.
- Mettre à jour les ADR et les contrats lors des évolutions incompatibles.
- Une fonctionnalité n'est « faite » que si les critères de sortie et tests associés sont satisfaits.
- **Licence non décidée** : ne pas supposer qu'un dépôt public accorde automatiquement une autorisation de réutilisation.

Projet initié le 15 octobre 2026.
