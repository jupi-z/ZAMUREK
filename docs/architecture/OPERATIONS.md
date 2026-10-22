# ZAMUREK — opérations et CI sur la plateforme Core Monarque Connect

**Planifié ; aucun serveur ZAMUREK autonome à déployer.** API de production ZAMUREK exposée via **backend propriétaire Monarque Connect privé** et ses workers, PostgreSQL et stockage commun. Les noms de domaine précédemment proposés sous `shuleops.com` ne sont que des hypothèses, non réservés ni configurés.

- Clients installables Android (buyer/merchant/discovery) et Windows (marchand/POS/opérateur), aucune SPA, PWA, SSR, Swagger UI ou console admin web publiquement hébergée pour ZAMUREK.
- Routes publiques limités par auth/scopes/Core entitlements, administration plateforme via VPN+MFA, bases, secrets, backups, metrics internes au réseau privé. `X-Zamurek-Channel` ne contourne jamais authorization.
- Les workflows GitHub ZAMUREK valident docs/contrats/client builds ; les tests du Core s'exécutent dans repo privé Monarque Connect. Contrat `coreCommitSha+contractVersion` verrouillé et vérifié entre deux CI avant release.
- Staging avec données synthétiques : deux org, deux établissements, deux acheteurs, caissiers/mall manager et un client POS walk-in ; pas de données réelles en public.
- Monarque Core seul et ZAMUREK activé sur la même org doivent fonctionner sans casser quote→order→invoice. Sauvegardes/restauration/export **logiques par organisation** sont des gates à démontrer.
- Facture normalisée DGI, droits pharma, marque LaJoie Mall et paiement réel sont des **gates externes non acquis**.

Références : [Network](NETWORK-EXPOSURE.md), [roadmap](../v1/INTEGRATION-ROADMAP.md), [gates](../v1/QUALITY-REQUIREMENTS.md).
