# Sécurité xShop — exigences non implémentées

## Frontières
- **Internet** : endpoints indispensables d'identité email, catalogue CDF et commandes clients protégées ; endpoints marchands uniquement sous authentification forte et permissions, segmentation si possible.
- **VPN** : toutes les opérations plateforme/opérateur ; MFA TOTP et journal d'audit.
- **Réseau privé** : PostgreSQL tenant, registry, secret manager, stockage privé, metrics, workers et backups.
- **Jamais de frontend web** hébergé ; mais API publique accessible par clients HTTP et donc sécurisée côté serveur, aucune confiance dans package Android.

## Menaces / contrôles
- IDOR inter-tenant ET deux acheteurs d'un même tenant, staff role escalation, SQL injection, tokens volés : authN/authZ partout, logs sans PII, verrouillage d'accès.
- Email takeover, reset tokens, bruteforce, SMTP indisponible : vérification e-mail usage unique, récupération sûre, rate limits et test de délivrabilité. Aucun OTP SMS ; email **n'est pas MFA forte**.
- Marchand taux USD→CDF manipulé par intrus : mises à jour réservées, concurrence optimiste, validation plage / audit / version, alertes sur changements, snapshot immuable.
- Falsification de prix CDF/checkout, double commande ou re-joue une quote expirée : calcul API autoritatif en précision décimale, quotes signées/stockées et TTL, idempotence.
- Faux paiement manuel : preuve, contrôle personnel habilité, status jamais marqué PAID par acheteur ; devise de règlement effective et rapprochement explicités.
- WebView / Tauri IPC : local-only, commandes whitelist, aucun secret dans DOM/JS, OAuth/tokens natifs, HTTPS, pas de contenu non approuvé.
- OS/hébergeur : firewall, patches, TLS, SSH privé/restriction, sauvegarde chiffrée et restauration testée.

## Conformité RDC
Prix public et documents commerciaux CDF conservatoirement ; vérifier arrêté 007/2025, règles sur taux de conversion marchand et protection des données Code numérique 23/010. Audit juridique non équivalent à certification. G4 bloqué si conformité non revue.

Sources : https://owasp.org/API-Security/ ; https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html .
