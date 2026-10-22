# ZAMUREK — environnement G1 à construire

Aucun déploiement, fichier Docker opérationnel ou serveur validé n'est actuellement présent.

Pour 0.1.0, Codex doit fournir des ressources reproductibles pour **PostgreSQL registry**, **deux DB commerciales d'organisations indépendantes**, au moins **deux établissements dans une même organisation**, migrations, test SMTP/local capture, stockage objet local, workers/outbox/Agentic Fabric et observabilité privée.

VPS et DNS provisoires `zamurek-api-test.shuleops.com` / `zamurek-api.shuleops.com` **non configurés**. Staging isolé et datasets synthétiques obligatoires. Le serveur **n'héberge aucune interface web** ; seuls API/workers/DB/stockage, services internes privés et points TLS nécessaires peuvent tourner.

CI doit tester migrations, droits des DB, policies réseau, fail-close en absence de secrets/LLM, backup/restoration d'un tenant et conformité dépendances avant prétendre production-ready.

Voir [tenancy](../docs/architecture/TENANCY.md), [network](../docs/architecture/NETWORK-EXPOSURE.md), [gates](../docs/v1/RELEASE-GATES.md).
