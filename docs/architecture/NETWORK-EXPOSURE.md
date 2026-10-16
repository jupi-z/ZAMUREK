# Architecture réseau — exposition minimale, serveur API-only

**Décision : seule la surface HTTP nécessaire au fonctionnement distant des clients doit être accessible sur Internet.** « API-only » ne signifie pas « zéro endpoint public ».

## Domaines envisagés (DNS NON configuré)
- `xshop-api-test.shuleops.com` : staging / tests uniquement, accès restreint (VPN ou allowlist) autant que possible ; données synthétiques.
- `xshop-api.shuleops.com` : production plus tard, certificat TLS et DNS à vérifier.
- Noms provisoires à remplacer quand xShop sera rebaptisé. Ne pas modifier services ShuleOps préexistants ; confirmer non-collision avant enregistrement.

## Surface et segmentation
| Service | Exposition projetée |
|---|---|
| `GET /v1/storefront/config`, catégories, produits, prix CDF publics, images publiques | HTTPS public + validation canal/rate limiting |
| `/auth/v1/*` pour les acheteurs | HTTPS public, bruteforce protection, abuse detection, CAPTCHA adaptatif si nécessaire |
| `/v1/carts`, `/v1/checkouts`, commandes clients | HTTPS public mais authentification requise, authz tenant & objet |
| `/v1/merchant/*` | HTTPS public si marchands mobiles sans VPN, **RBAC strict**, MFA staff, rate limits séparés ; possibilité d'accès VPN marchand pour installation restreinte |
| `/platform/v1/*` | **VPN uniquement** / réseau privé, MFA opérateur, zéro route ouverte au public |
| PostgreSQL, secrets, stockage privé, workers, métriques, logs, admin système | réseau privé/localhost uniquement |
| Swagger UI / portail / pages HTML | **non déployés** |
| OpenAPI brut | dans Git/CI, pas exposé par défaut en production |

## Contrôles
- HTTPS 443, proxy limitant méthodes/chemins et débit, règles WAF au besoin ; pare-feu DENY par défaut, accès SSH privé ou restreint.
- AuthN/AuthZ partout où nécessaire ; n'importe quel client HTTP peut appeler une API publique, un package signé ne prouve pas une permission.
- CORS navigateur ne protège pas l'API contre les clients non navigateur.
- Pas de DB et object storage administrateur sur Internet. Uploads avec autorisation + inspection/limites.
- DNS et certificats séparés staging/production ; aucun usage de données ou clés de production en staging.
- Sauvegardes chiffrées, secrets manager, VPN WireGuard ou équivalent pour opérateurs, accès auditables et rotation.

## Avant tout déploiement
Confirmer propriété et disponibilité des DNS `shuleops.com`, caractéristiques VPS, risque de contention ShuleOps, mémoire, OS, capacité sauvegarde, IP et ports ; mesurer le budget d'exploitation. **Aucune machine ni DNS n'est connecté ou configuré à ce stade.**
