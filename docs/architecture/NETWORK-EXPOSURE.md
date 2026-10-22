# ZAMUREK — topologie API-only et réseau minimal

**Statut : architecture V1, pas une configuration réelle de VPS, DNS ou VPN.**

## Domaines provisoires CANDIDATS, non créés
- `zamurek-api-test.shuleops.com` (staging, accès restreint, aucune donnée réelle)
- `zamurek-api.shuleops.com` (production future, HTTPS)
Tous deux requièrent confirmation de propriété du domaine, absence de conflit ShuleOps, DNS/TLS et vérification de l'infrastructure. Le serveur existant n'a pas été inspecté.

## Routes
| Surface | Accès |
|---|---|
| Catalogue, menu, disponibilités, venue opt-in publiés | HTTPS public en lecture, territorial CDF, rate-limit |
| Identité acheteur email/password, panier, commandes, rendez-vous | HTTPS public **mais session, RBAC/ownership, consentement et anti-abus** |
| API marchand (catalogue, FX, caisse, appointments, réparation, agents autorisés) | HTTPS authentifié + tenant/establishment scopes, MFA/step-up sensible, surveillance |
| API plateforme provisioning/billing/tenant/agent admin | **VPN privé + MFA opérateur** ; refus du trafic public au proxy |
| DB registry/tenant, secrets, object store admin, files workers, métriques, SSH, backups | **réseau privé seulement**, deny-default |
| Swagger UI, SPA, SSR, PWA, portail marchand/administrateur hébergé | **non déployés** |

## Règles
Protéger routes derrière reverse proxy explicite + firewall ; aucun trust basé sur channelId, CORS, user-agent, device-id ou signature APK. TLS 443, authentification backends, rate-limits distincts, upload contrôlé, aucun endpoint général du serveur exposé. VPN WireGuard ou alternative approuvée, MFA et audit. Media public diffusé par mécanisme contrôlé, media privé par autorisations strictes.

## Séparation environnements
Local → staging isolé → production validée ; données synthétiques en staging ; pas de migration/restore automatique production à partir de staging. Backups chiffrés, restauration testée et monitoring privé. Aucune route web frontend hébergée.

Voir [menaces V1](../v1/SECURITY-THREAT-MODEL.md), [contrats](../v1/TECHNICAL-CONTRACTS.md).
