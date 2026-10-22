# ZAMUREK — réseau API-only sur Core Monarque Connect

**Statut : architecture cible non déployée.** Pas de serveur ZAMUREK autonome. Le backend REST dans le dépôt privé Monarque Connect expose les routes nécessaires à ZAMUREK via contrats d'intégration versionnés, préfixe `/api/v1` et canal public non privilégié.

| Surface | Réseau et politique |
|---|---|
| Catalogue public, menu, venue opt-in | HTTPS, lecture limitée aux données publiées, rate limit |
| Buyer online, commandes, rendez-vous | HTTPS + buyer authentifié, ownership object strict |
| Marchand, caisse POS, imprimables | HTTPS + staff/cashier authenticated, RBAC/establishment/MFA selon opération |
| Administration plateforme et clés IA | VPN privé + MFA opérateur, aucun accès public |
| PostgreSQL, secrets, workers, médias privés, sauvegarde, métriques | réseau interne exclusivement |

Production ZAMUREK : **pas de SPA, SSR, PWA ni console web**. Applications installées conservent UI embarquée et appellent uniquement Core HTTP autorisé. HTTPS/CORS/channelId ne remplacent pas authz. Aucune donnée financière venue ou autre tenant ne peut être exposée.

Les anciens candidats `zamurek-api-test.shuleops.com` et `zamurek-api.shuleops.com` n'ont **pas** été configurés ni validés ; un routage DNS pourrait pointer vers Core mais doit être arbitré avec propriété domaine, environnement, TLS et proxy. Aucun DNS/serveur/modèle fournisseur n'est affirmé en service.

Voir [intégration](../v1/SHARED-CORE-INTEGRATION.md) et [sécurité](../v1/SECURITY-THREAT-MODEL.md).
