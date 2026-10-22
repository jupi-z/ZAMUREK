# ZAMUREK — contrats partagés

**Normatif pour le début de G1, non implémenté :** [OpenAPI ZAMUREK V1 draft](openapi/zamurek-v1.yaml) couvrant commerces, produits au poids, restaurant, rendez-vous, meubles/devis, réparations, pharmacie sous garde-fous, venue/mall et agents.

**Contrats bas niveau IA/événements :** [event envelope JSON Schema](events/event-envelope.schema.json) et [tool definition JSON Schema](agent-tools/tool-definition.schema.json).

Le fichier [xshop-v1.yaml](openapi/xshop-v1.yaml) est conservé **comme archive**, pas utilisé pour générer la V1 universelle. Il ne doit pas être utilisé comme seul contrat de codegen.

Les nouveaux contrats sont **DRAFT**, avec composants et opérations initiales typées ; G1 doit ajouter chaque CRUD, état, policy et schéma nécessaire et réaliser validation OpenAPI complète, génération clients, tests contractuels et rétrocompatibilité. Aucun endpoint n'est opérationnel à G0.

Pas de Swagger UI hébergé en production. Voir [TECHNICAL-CONTRACTS](../../docs/v1/TECHNICAL-CONTRACTS.md) et [SECURITY](../../docs/v1/SECURITY-THREAT-MODEL.md).
