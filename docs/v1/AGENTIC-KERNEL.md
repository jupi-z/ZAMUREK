# Agentic Fabric ZAMUREK V1 — conception normative AI-native

**But** : les agents utilisent des capacités métier dont la sécurité existe **en dessous** du LLM. L'IA n'est ni source de vérité, ni unique moteur de vente, ni détenteur de secrets tenant. L'indisponibilité du LLM ne bloque pas les commandes, les réservations ou la caisse.

## 1. Contrats fondamentaux
- `ModelGateway` : interface interchangeable pour modèles locaux/distants, version/policy, quotas, coût, timeout, failover et redaction.
- `ToolDefinition` : id stable versionné, contexte métier, JSON Schema strict input/output, `requiredPermissions`, `tenantScope`, `establishmentScope`, niveau de risque, caractère idempotent, limites d'exécution.
- `AgentDefinition` : objectif, modèle autorisé, version des prompts, outils accordés, limites coûts/tokens/temps, règles de récupération, politiques.
- `AgentRun` : requestedBy/actor+org/establishment, correlationId, policyVersion, modelVersion, promptVersion, status, checkpoints, événements et budget.
- `HumanApproval` : target tool + empreinte exacte du payload, auteur, tenant, étape, décision, expiry, approbateur avec permissions distinctes. Rejet ou expiration empêche effet.
- `MemoryScope` : EPHEMERAL_RUN / TENANT / ESTABLISHMENT / USER_OPT_IN ; TTL, classification, provenance, consentement, suppression et chiffrement. Jamais partage entre tenants.

## 2. Moteur et politique
Un orchestrateur propriétaire traite événements/outbox et tâches durables ; une couche d'outils interne expose les **mêmes use cases** que les API sans contourner RBAC. Avant chaque action : identité de l'initiateur, tenant/établissement, droits, politique du canal, classification des données, budget, consentement et version du schéma. Revalider **au moment de l'exécution**, pas seulement à la planification.

`READ_PUBLIC` : lecture publique ; `READ_TENANT` : consentement et RBAC ; `DRAFT_WRITE` : proposition réversible et audit ; `SENSITIVE_WRITE` (prix, FX, remboursements, publication, commande, annulation, compte, retrait de données) : **approbation humaine obligatoire et commande idempotente** ; `FORBIDDEN` : accès inter-tenant, secrets, changement de droits, prescription médicale, vente régulée non habilitée, paiement sans preuve, action non déclarée.

## 3. Modèle de sécurité des outils
- Tout contenu externe (message client, catalogue, images/OCR éventuels, document, résultat de recherche) = **donnée non fiable**, jamais instruction système. Séparation system/developer/tool/context, interdiction des changements de rôle par contenu externe.
- JSON Schema strict, taille bornée, timeout, circuit-breaker, rate limiting, outbound allowlist ; pas de bash ni navigateur autonome avec accès indiscriminé aux tenants en V1.
- Les réponses d'outils contiennent seulement les champs permis et PII minimisée ; stockage de prompts sous politiques de confidentialité ; tracer hashes/versions plutôt que tokens ou données personnelles dans logs.
- Défense en profondeur contre injection de prompt, exfiltration, tool poisoning, influence inter-tenant et privilège persistante ; tests automatisés rouges/blancs. Aucune confiance basée sur « confiance du modèle ».

## 4. Socle V1 entièrement fonctionnel
A. **Assistant de catalogue marchand** : classe/corrige titre/description, propose variantes et catégories, mais ne publie ni ne modifie prix sans approbation ; résultats éditables et provenance.
B. **Assistant FAQ acheteur** : répond uniquement à partir du catalogue/horaires/politiques publiées du commerce sélectionné avec source, indique quand la réponse n'est pas dans les données ; aucune information autre tenant ou commande d'autrui.
C. **Assistant d'exploitation marchand** : synthèses factuelles de commandes/rendez-vous/ventes agrégées autorisées et recommandations ; calcul des indicateurs via SQL/backend vérifié (pas estimation du LLM), aucun accès plateforme.
D. **Noyau d'exécution** : registre outils, planification/checkpoints, reprise retries idempotents, approbation humaine, modèles interchangeables, pause/kill-switch et quotas, observabilité.

Les trois assistants A/B/C sont exigés pour 1.0.0 avec une **intégration modèle réelle testée**, mode dégradé sécurisé et possibilité de désactivation par tenant. Choix/contrat de modèle et budget d'inférence non verrouillés tant que non validés.

## 5. Événements
`catalog.item.created.v1`, `order.placed.v1`, `appointment.booked.v1`, `repair.case.updated.v1`, `fx.rate.changed.v1`, `venue.optin.revoked.v1`, `agent.run.requested.v1`, `agent.tool.approval.v1`. Envelope : `eventId`, `eventType`, `schemaVersion`, `organizationId`, `establishmentId?`, `correlationId`, `occurredAt`, `payloadRef`, `classification`. Déduplication eventId + idempotence par acteur/capacité.

## 6. Recette incontournable
- LLM indisponible : achat, réservation, caisse, SAV fonctionnent normalement.
- Injection cachée dans fiche restaurant demande lecture commandes autre tenant : policy bloque, audit et test passent.
- Agent essaye d'augmenter le taux USD→CDF sans approval : rejet, pas de changement DB.
- Approval A pour payload X réutilisé sur Y : rejet. Revocation droit avant exécution : rejet.
- Récupération de mémoire tenant A depuis B : aucun résultat, preuve E2E.
- Crash milieu de workflow : reprise au checkpoint, aucune double commande ni double règlement.
- Budget dépassé/taux de requête dépassé : arrêt contrôlé ; kill-switch tenant et global effectif.
- Les réponses médicales/ordonnances déclenchent garde-fou et renvoi vers personnel habilité, sans acte transactionnel.
- Mesures : sécurité, pertinence, coût, latence, hallucination, PII et taux approbation avec tests sur données synthétiques.

## 7. Briques techniques
Autoriser bibliothèques génériques open source **permissives vérifiées**, pas reprendre une plateforme agentique qui impose le domaine ou les contrôles. Une base relationnelle + index de recherche local tenant-aware suffit au démarrage ; vector store externe n'est pas une dépendance obligatoire. Rendre `ModelGateway` provider-neutral, sans clés dans APK/EXE.

Voir [modèle de domaine](DOMAIN-MODEL.md), [sécurité](SECURITY-THREAT-MODEL.md), [gates](RELEASE-GATES.md).
