# ZAMUREK — Commerce omnicanal universel, extension du Core Monarque Connect

**État : spécifications V1 en révision pour intégration au Core. Aucune application client exécutable ni fonctionnalité V1 livrée dans ce dépôt.** Objectif : 1.0.0 complète, **pas un MVP**. Pas de lancement partiel commercial.

ZAMUREK est une marque/produit autonome couvrant vente en ligne, **vente physique POS avec cash et impression**, vente au poids, restaurants/pizzerias, salons/rendez-vous, meubles/devis, réparations, articles légalement autorisés en pharmacie, centres commerciaux/discovery et assistants IA. **LaJoie Mall est une opportunité envisagée, pas un partenariat conclu.**

## Architecture nouvelle — décision adoptée le 22 octobre 2026

**<https://github.com/jupi-z/Monarque-Connect>** est le dépôt propriétaire du **Core transactionnel partagé** : il contient actuellement organisations/établissements, identités, entitlements/FairScale, catalogue commun, prix/FX, commandes SalesOrder, factures Invoice, paiements PaymentRecord, caisse CashMovement, Event Fabric et projections Intelligence. La visibilité GitHub observée le 27/10/2026 est publique ; elle ne constitue pas une garantie de confidentialité. Certains éléments d'intégration ZAMUREK restent planifiés et ne sont pas livrés. ZAMUREK n'implémente **ni second backend NestJS commercial, ni second registry PostgreSQL, ni deuxième moteur financier**.

Les modules spécialisés ayant besoin de transactions métier sont conçus comme modules du **backend Monarque Connect**, et les applications ZAMUREK (Android React embarquée+Kotlin, Windows Tauri/Rust), adaptations de canal, matériels d'impression et tests d'intégration sont préparés ici.

La V1 utilise la **base PostgreSQL partagée de Monarque Connect**, sécurité stricte `organizationId`/`establishmentId`/objectOwner, et non l'ancienne « une DB par commerçant ». Les documents pré-convergence (notamment le draft [OpenAPI](packages/contracts/openapi/zamurek-v1.yaml)) ne définissent pas d'API déployée. L'autorité finale de l'API provient du contrat Core versionné (`/api/v1`). La PR Core #152 comporte un complément de frontières Docs/114 encore en revue : sa validation est un prérequis avant migration/implémentation POS ou multi-produits.

## Vente sur place et en ligne — fonctionnement unifié

- POS connecté : caissier authentifié, terminal et session de caisse, vente client de passage **sans compte/e-mail**, prix serveur, encaissement espèces, monnaie rendue, transferts manuels contrôlés, clôture/écarts.
- Un seul flux financier Core : commande canonique → **Invoice interne** → PaymentRecord lié → CashMovement net si espèces → Outbox, atomique et idempotent côté PostgreSQL. Reçu imprimé ≠ facture fiscale homologuée.
- Impression A4 et ticket thermique 58/80 mm depuis documents Core, pont matériel dans Kotlin/Rust. **Aucune fausse « facture normalisée DGI »** : fiscalisation selon réglementation et autorisation effectivement vérifiées.
- Magasin et vente en ligne partagent produits, commandes, droits, historiques et analyses ; venue n'est jamais propriétaire des comptes d'un commerçant.

## IA, prix et produits

Un seul modèle d'agents : AI Gateway/Agent Runtime **Monarque Connect** partagé, outils commerciaux spécifiques ZAMUREK, scopes/approbations/consentement et trois assistants exigés pour 1.0.0. En panne de modèle IA, le POS et les ventes restent opérationnels.

ZAMUREK conserve un prix source USD avec FX commerçant versionné et affichage CDF RDC selon droit confirmé, sans forcer les organisations Monarque Connect existantes à la devise USD. Offre commerciale envisagée **ZAMUREK BASIC 7 USD/mois par organisation**, indépendante des plans FairScale, limites/établissements à finaliser sur coûts réels.

**43 capacités obligatoires** sont décrites dans [manifest](spec/v1/capabilities.json) et [matrice](docs/v1/CAPABILITY-MATRIX.md), notamment POS et interopérabilité, plus sept verticales et discovery/venue. Les fonctions réglementées restent bloquées avant revue locale.

## Où commencer

1. [ADR-0024 — Core partagé et fin de la duplication](docs/decisions/0024-shared-monarque-core-zamurek.md)
2. [Architecture commune](docs/v1/SHARED-CORE-INTEGRATION.md) et [POS/factures](docs/v1/POS-AND-FISCAL-DOCUMENTS.md)
3. [Charte produit V1](docs/v1/PRODUCT-CHARTER.md) et [43 capacités](docs/v1/CAPABILITY-MATRIX.md)
4. [Feuille de route Core 10A.5 ↔ ZAMUREK](docs/v1/INTEGRATION-ROADMAP.md) et [gates 0.0.0→1.0.0](docs/v1/RELEASE-GATES.md)
5. [Nouvelle phase 0.1.0 côté clients](docs/v1/PHASE-0.1.0-ACCEPTANCE.md) et [prompt Codex d'intégration](docs/v1/CODEX-INTEGRATION-PROMPT.md)
6. [Sécurité V1](docs/v1/SECURITY-THREAT-MODEL.md), [Agentic Shared Runtime](docs/v1/AGENTIC-KERNEL.md), [politique OSS](docs/governance/OPEN-SOURCE-POLICY.md)

**Ordre obligatoire :** terminer et prouver les phases techniques Monarque Connect 10A.5, 10B, 11, 11.5 et 12 avant tout code ZAMUREK (clients, SDK, intégration runtime ou verticales). Jusqu'alors, ce dépôt reste limité au cadrage documentaire et à la revue des contrats inter-dépôts. Les contrats C0–C3/C6/C7 gelés restent nécessaires à l'intégration mais ne déclenchent pas le développement ZAMUREK. Les gates externes FairScale/juridiques/commerciaux demeurent séparés. Le précédent [prompt autonome](docs/v1/CODEX-PHASE-0.1.0-PROMPT.md) est **RETIRÉ**.

## CI des spécifications (pas preuve de runtime)

```bash
python3 scripts/validate_docs.py
python3 scripts/validate_v1_scope.py
python3 scripts/validate_convergence.py
python3 scripts/validate_agent_contracts.py
python3 -m pip install -r scripts/requirements-docs.txt
python3 scripts/validate_openapi.py
```

Ces scripts contrôlent la **cohérence documentaire et les brouillons de contrats**, pas des ventes réelles, des factures DGI, des APK/EXE ou une conformité commerciale. Les dépôts ZAMUREK et Monarque Connect sont tous deux observés **publics** le 27/10/2026. Ne publier aucun secret, donnée client ou élément dont la confidentialité est requise ; la propriété du Core et sa visibilité GitHub sont deux sujets distincts. GitHub Actions peut aussi fonctionner dans un dépôt privé selon le plan et les quotas.
