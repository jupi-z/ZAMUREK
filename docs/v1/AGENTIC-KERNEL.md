# ZAMUREK — outils et assistants IA sur le Runtime Monarque Connect partagé

**Normatif V1 / NON IMPLÉMENTÉ.** La `Event Fabric` existante et l'intelligence déterministe 10A de Monarque Connect sont réutilisées ; l'AI Gateway en 10B et le Runtime 11.5 seront **uniques**. Les anciens mots « Agentic Fabric ZAMUREK » désignent désormais la **couche d'outils/expériences métier**, pas une infrastructure indépendante.

## Propriété
- **Monarque Connect Core** : identity, run/step/checkpoints, `ModelGateway`, `ModelRegistry`, `TenantAiPolicy`, `ToolRegistry`, `PolicyDecision`, `HumanApproval`, `MemoryScope`, audit, coûts/quotas, kill switch et événements.
- **ZAMUREK** : tools typés versionnés et adapters sur les use cases canoniques (catalogue, horaires, réservations, commandes, statistiques), expérience client/marchand et règles d'affichage des propositions.
- Pas de provider LLM directement appelé depuis Android/Windows, pas de secrets, pas de second backend agentique et pas d'accès SQL direct d'un agent. Les domain services refont RBAC/entitlement/scope/ownership à l'exécution de chaque tool.

## Classes communes A0–A4
A0 Read (catalogue public, FAQ), A1 draft (suggestion menu/catalogue), A2 action réversible (confirmation par défaut), A3 high-impact (modification prix/FX, factures, paiement, cash, annulation, membership : **confirmation humaine et transaction validée**), A4 interdit (secrets, audits altérés, export inter-tenant, prescription/diagnostic, contournement fiscal et sécurité). Approval liée à `payloadHash`, acteur, org/établissement, TTL et version ; toute modification impose nouvelle approbation.

## Trois assistants requis en ZAMUREK 1.0.0
1. **Catalogue marchand** : proposition de descriptions/catégories à publier après validation, pas de prix autonome.
2. **FAQ acheteur** : réponses sourcées et bornées au catalogue/horaires publiés du commerçant sélectionné, refuse demandes hors périmètre.
3. **Exploitation** : analyses factuelles des ventes POS + ONLINE, rendez-vous et stocks autorisés, données calculées par KPI déterministes Core, pas par hallucination LLM.

Une vraie intégration fournisseur évaluée est obligatoire avant 1.0.0, mais le site et le POS fonctionnent sans modèle. Au jalon ZAMUREK 0.1.0, seuls les contrats clients et politiques partagés de 10A.5 sont nécessaires. 10B/11.5 complètent infrastructure avant 0.7.

## Contrats et sécurité
ToolDeclaration JSON schema versionné, actor+organizationId+establishmentId+productCode+perms, allowlist, data classification, provenance, consentement, sortie validée, budgets et timeouts. Toutes sources externes = contenus non fiables contre prompt injection. Mémoire EPHEMERAL_RUN/TENANT/ESTABLISHMENT/USER_OPT_IN sous ACL et TTL, aucun retrieval cross-tenant/cross-product non consenti. Aucun journal brut de secrets ou données privées.

## Critères
Cross-tenant denied, tentative prix/FX sans approval denied, approval replay/payload tampered denied, provider indisponible et checkout toujours opérationnel, run crash/retry sans double paiement, budget dépassé et kill-switch sûrs, prompts médicaux renvoyés au personnel habilité sans conseil thérapeutique.

Référence : [ADR-0024](../decisions/0024-shared-monarque-core-zamurek.md), [Shared Core](SHARED-CORE-INTEGRATION.md), [sécurité](SECURITY-THREAT-MODEL.md).
