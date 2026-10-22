# Sécurité et surfaces d'attaque — ZAMUREK V1

## Frontières
- Internet : GET catalogue/venue public CDF, inscription e-mail, sessions, orders/appointments d'acheteur sous token ; routes marchand selon RBAC/MFA, limitation et contrôle métier.
- VPN privé : opérateur `/platform/v1`, provisioning tenants, migrations, réseau supervision.
- Privé seulement : DB PostgreSQL par org + registry, secrets, workers, backups, métriques, logs, stockage sensible, clés de modèles IA.
- Clients publics techniquement inspectables (APK, EXE/MSI) : aucun secret de base/API serveur privilégié, ni token longue durée exposé à React. Tous les contrôles côté backend ; CORS et appId ne sont pas barrières de sécurité.
- Mall venue : la gestionnaire du centre ne reçoit pas PII ou commandes tenant automatiquement ; consentement explicite, consent revocation et audit.

## Matrice de menaces (minimum)
| Risque | Contrôle attendu | Preuve |
|---|---|---|
| BOLA / cross-tenant | contexte org depuis registry vérifié, DB credentials séparés, ownership objet | essais A→B, deux clients même tenant |
| BFLA / droits employés | membership au bon établissement, rôle + action + MFA | test vendeur lecture finance refus |
| Confusion establishment | filtre et accès explicites par établissement | staff établissement A ne voit pas B |
| IDOR rendez-vous | actor + booking ownership + resource scopes | essai collision et lecture tiers |
| Manipulation prix/FX | quote backend immuable + contrôle version, merchant approval | taux concurrent change → conflit |
| Vente médicaments interdits | classification par défaut BLOCKED et module légal fail closed | tentatives checkout refusées |
| Faux paiement | preuve vérifiée marchand, audit | demande client ne passe pas PAID |
| Replay / dupe checkout | idempotency key scope+empreinte+TTL | création unique avec retries |
| Injection prompt/tool | policy indépendante du modèle, outils typés | prompt adversarial ne traverse pas tenant |
| Exfiltration mémoire IA | scopes + TTL + consent + redaction | test retrieval cross-tenant |
| DoS/disponibilité | rate limit, budgets, pools bornés, timeouts, queue bounds | tests charge/circuit breaker |
| Secrets et logs | vault, rotation, chiffrement en transit/rest, pas de PII brute logs | scans et revues |
| Backup / restore | snapshots chiffrés distincts org, restauration ciblée | restauration A sans B |
| APK/API compatibility | versions contractuelles et signature | ancien APK testé |
| Réservation concurrente | contraintes DB anti-double booking | 2 requêtes slot simultanées |
| Supply chain | dépendances permissives approuvées, SBOM, notices, vulnérabilités | audit automatique des paquets |
| Légal/fiscal | juridiction + fonctionnalité gate, approbation juriste | preuves datées avant release |

## Non-négociables de déploiement
Production API-only, 443 TLS, deny-by-default, /docs Swagger désactivé, opérateur par VPN, aucune DB ouverte, uploads inspectés et bornés, VPN et certificats testés, alertes, rotation secrets, restaus réussies. Les sous-domaines provisoires `shuleops.com` ne sont pas présumés configurés.

## Confidentialité
Obtenir consentement contextualisé, limiter données collectées par verticales (notamment réparation/numéros séries, santé), définir conservation/export/effacement, accès staff et consentement LLM. Pas de données réelles dans un fournisseur d'IA sans droit/contrat/consentement adaptés. Aucun transfert entre tenants sous prétexte de personnalisation.

Ce document est un cahier de sécurité ; aucune mesure n'est déclarée opérationnelle tant que test/proof non disponible.
