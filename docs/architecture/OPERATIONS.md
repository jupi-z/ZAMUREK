# ZAMUREK — exploitation API-only, tests et restauration

**Plan normatif, infrastructure non déployée.** VPS existant et domaines `shuleops.com` proposés, capacités/DNS non inspectés : noms candidats `zamurek-api-test.shuleops.com` et `zamurek-api.shuleops.com`.

- Production : NestJS REST API/worker, PostgreSQL registry + DB commerciale **par organisation**, stockage média contrôlé, accès secrets et supervision privés. **Aucun frontend hébergé**, y compris admin/Swagger UI.
- Internet : routes d'identité, catalogue, rendez-vous/commandes selon auth, commerce marchand protégé. `/platform/v1/*` **VPN + MFA**, DB/SSH/métriques/backup hors Internet.
- Staging et prod isolés avec clés/données distinctes. Synthétique pour toutes les 7 familles métier ; aucune donnée client réel en démo.
- Migrations expand/contract avec versionnement par org et compatibilité anciennes applications ; pool DB borné et éviction, provisioning idempotent.
- Backups chiffrés registry et DB séparées, restauration tenant A sans altérer B ; RPO/RTO et politique conservation à négocier avant production, **jamais inventés**.
- SLO latence, disponibilité, quotas IA, coûts SMTP/LLM, observabilité et support mesurés avant lancement.
- Signature APK/Windows, pipelines CI, SBOM/licences, rotation secrets et journalisation anonymisée sont gates 1.0.0.

Voir [topologie](NETWORK-EXPOSURE.md), [recette](../v1/QUALITY-REQUIREMENTS.md), [domained](../v1/DOMAIN-MODEL.md).
