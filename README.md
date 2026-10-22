# ZAMUREK — Universal Commerce & Services Platform

**Version de référence : 0.0.0 — cadrage pré-développement. Objectif : 1.0.0 intégralement fonctionnelle, pas MVP.** Architecture, documents et contrats sont en cours de préparation ; **il n'existe pas encore de backend ni d'applications opérationnels dans ce dépôt**.

> **Source normative actuelle : [ZAMUREK V1](docs/v1/README.md)**. Les anciens documents xShop sont des archives historiques lorsque leurs prescriptions sont incompatibles avec la nouvelle V1.

ZAMUREK est une plateforme commerciale et de services **100 % propriétaire**, multi-tenant, multi-établissement et AI-native, conçue pour les commerces indépendants et les centres commerciaux. LaJoie Mall est **un partenariat possible, non conclu** : aucune dépendance commerciale ou usage de marque tiers n'est supposé acquis.

## La V1 complète couvre
- **Boutiques classiques** : produits, variantes, photos, disponibilité, commandes, caisse, livraison/retrait.
- **Ventes au poids** : grammes/kilogrammes, précision décimale, pesée réelle et tarification exacte.
- **Restaurants/pizzerias** : cartes, suppléments, préparation, cuisine, tables et réservations.
- **Salons/prestataires** : prestations, staff, créneaux, rendez-vous, reports et annulations.
- **Meubles/volumineux** : variantes, devis approuvés, livraison spécialisée.
- **Électronique/réparations** : devis, diagnostic/consentement, workflow réparation et restitution.
- **Pharmacies** : commerce des articles légalement autorisés ; médicaments/prescriptions bloqués par défaut avant vérification réglementaire.
- **Venue/Mall** : regroupement volontaire de marchands indépendants, découverte multi-commerce, commandes séparées par commerçant, contrôle opt-in et révocation.
- **AI-native** : outils métier typés, moteur de politiques, événements, agents, mémoire cloisonnée, validations humaines, mode dégradé et trois assistants réellement fonctionnels.

**Les 38 capacités V1 sont obligatoires pour déclarer 1.0.0 prête.** Les médicaments non autorisés et les fonctionnalités explicitement exclues ne sont pas des engagements contournables.

## Architecture incontournable
- Backend NestJS modulaire propriétaire + registry global PostgreSQL + **base commerciale PostgreSQL séparée par organisation**, multi-établissements, API REST/OpenAPI ; workers & outbox.
- **Production API-only** : pas de portail web hébergé, SPA/SSR/PWA/Swagger UI. Clients installables Android acheteur, Android marchand et Discovery ; Windows marchand et opérateur (EXE/MSI).
- **IA en profondeur** : `Agentic Fabric` dans le domaine et les événements dès la fondation, pas un chatbot plaqué ; agents n'obtiennent aucun privilège de plus que les humains.
- **USD source** et taux USD→CDF configuré/versionné par marchand. Prix/devis publics CDF pour le territoire RDC jusqu'à avis juridique, calcul exact côté API ; commande contient snapshot tarif/taux.
- **Sans SMS** en V1 ; e-mail vérifié, MFA staff/opérateur, VPN pour administration, accès public réseau minimal, paiement direct commerçant.
- **Une seule offre SaaS de départ BASIC 7 USD/mois par organisation commerçante**, sans commission, modalités contractuelles/redevances additionnelles non présumées.
- **Aucun Mercur/Medusa/Saleor/Vendure ou moteur commercial tiers**. Frameworks/bibliothèques techniques MIT/Apache/BSD/ISC possibles sous revue de leurs licences exactes et transitives.

## Lecture et exécution
1. [Charte V1](docs/v1/PRODUCT-CHARTER.md)
2. [Matrice de capacités](docs/v1/CAPABILITY-MATRIX.md)
3. [Architecture de domaine](docs/v1/DOMAIN-MODEL.md)
4. [Fabric IA native](docs/v1/AGENTIC-KERNEL.md)
5. [Tarification USD/CDF et pesée exacte](docs/v1/MONETARY-AND-QUANTITY-POLICY.md)
6. [Parcours commerciaux](docs/v1/BUSINESS-WORKFLOWS.md)
7. [Gates 0.0.0 → 1.0.0](docs/v1/RELEASE-GATES.md)
8. [Critères de qualité](docs/v1/QUALITY-REQUIREMENTS.md)
9. [Contrat OpenAPI brouillon](packages/contracts/openapi/zamurek-v1.yaml)
10. [Manifeste V1 contrôlable](spec/v1/capabilities.json), [progression Codex](spec/v1/progress-template.json) et [fixtures synthétiques](spec/v1/fixtures.json)
11. [**Premier prompt Codex — phase 0.1.0**](docs/v1/CODEX-PHASE-0.1.0-PROMPT.md)
12. [**Dossier pour Codex**](docs/v1/CODEX-HANDOFF.md)

## Vérifications de conception
```bash
python3 scripts/validate_docs.py
python3 scripts/validate_v1_scope.py
python3 scripts/validate_agent_contracts.py
python3 -m pip install -r scripts/requirements-docs.txt
python3 scripts/validate_openapi.py
```
**Attention : ces validations sont statiques/documentaires**. Elles ne prouvent pas les builds, tests sécurité, conformité légale, qualité IA ni production prête. Codex doit apporter des preuves d'exécution réelles à chaque checkpoint.

## Ressources et propriété
- Domaines provisoires candidats sous `shuleops.com` ; aucun DNS ou VPS configuré par le dépôt.
- Le dépôt est **PUBLIC** au 22/10/2026 ; **ZAMUREK reste un projet propriétaire**. Le dépôt public n'est pas nécessaire pour exécuter GitHub Actions. Préférer un dépôt privé pour l'implémentation métier et les composants sensibles.
- [Notice propriétaire](PROPRIETARY-NOTICE.md), [sécurité](SECURITY.md), [politique open source](docs/governance/OPEN-SOURCE-POLICY.md).

Ne jamais publier de secrets, données personnelles ou preuves de client réel dans ce dépôt.
