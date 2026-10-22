# ADR-0019 — Plateforme ZAMUREK propriétaire ; briques open source permissives

**Statut : ADOPTÉ — 2026-10-22.** Décision explicite du propriétaire.

## Contexte
ZAMUREK est la nouvelle identité de la plateforme commerciale universelle, multi-tenant et AI-native née du projet xShop. Elle doit gérer différents types d'activités et rester indépendante des moteurs de commerce externes. Le propriétaire interdit l'utilisation de **Mercur / Mercure** comme fondation et choisit de développer un système commercial propriétaire.

## Décision
1. Les **règles métier, les modules, l'orchestration, les modèles de données, les API de domaine, les parcours métier, les connecteurs et la couche agentique de ZAMUREK sont conçus et implémentés spécifiquement pour ZAMUREK** ; leur code est propriétaire.
2. **Ne pas utiliser Mercur, ni reprendre/adapter son cœur, ni le substituer à un autre moteur commercial complet** (Medusa, Saleor, Vendure, Magento ou analogue). Aucun système ERP/e-commerce prêt à l'emploi ne devient le moteur de référence.
3. L'utilisation de **frameworks, moteurs techniques généralistes et bibliothèques open source** est encouragée pour éviter de réécrire la roue, à condition de respecter les licences et de garder ZAMUREK maître de son domaine, de ses données et de son architecture.
4. Par défaut, dépendances dont la licence est **MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause ou ISC**, sous réserve de la licence exacte de chaque paquet/version et de ses dépendances transitives. Une double licence est examinée et l'option permissive valablement choisie si applicable.
5. **GPL, AGPL, SSPL, LGPL, EPL, MPL, BUSL et licences propriétaires/fair-source/non-OSI** ne sont **pas autorisées par défaut**, même si certaines permettent légalement certains usages commerciaux. Toute exception exige revue juridique/technique explicite, ADR et autorisation avant intégration.
6. Respecter notices, copyright, licence, attribution, conditions de redistribution, brevets et obligations de chaque dépendance ; dépôt de licence et notices de tiers, génération de SBOM et contrôle automatique CI.
7. Éviter le verrouillage à un fournisseur, toute dépendance qui dicte l'architecture métier ou force l'hébergement d'une interface, et toute transmission de données tenant à un tiers sans décision et garanties.
8. La couche IA/agents est **nativement prévue dans l'architecture propriétaire** (registre d'outils, politiques de permissions, audit, supervision humaine, isolation tenant, événements et mémoire), tout en pouvant utiliser des moteurs/modèles/bibliothèques techniques permissifs. Aucune solution agentique prête à l'emploi ne possède l'autorité commerciale ou les clés des tenants.

## Conséquences et contrôles
- Architecture fonctionnelle et implémentation vérifiables par modules propriétaires ; pas de fork ni d'habillage d'un moteur complet.
- Inventaire de dépendances directes/transitives, scans de licences dans CI, liste des licences approuvées, fiches d'exception et notices de redistribution.
- Ce choix de propriété du code **n'implique pas** que les composants open source tiers deviennent propriétaires ; leurs licences restent applicables.
- Aucun achat, partenariat LaJoie Mall, nom définitif de domaine ou validation juridique n'est présumé réalisé.

Voir [politique de dépendances](../../docs/governance/OPEN-SOURCE-POLICY.md) et [architecture](../architecture/SYSTEM.md).
