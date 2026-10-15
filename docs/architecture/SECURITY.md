# Sécurité — modèle de menace xShop V1

**État : exigences documentées ; pas une certification ni un système implémenté.**

## Actifs
Identité globale client (téléphone, mot de passe haché, OTP/session), données privées de chaque marchand (commandes/adresses/prix internes), staff, opérateurs, clés de signature APK/EXE, secrets de bases, backups et informations de paiement manuel.

## Risques majeurs
Broken object-level authorization : fuite inter-tenant **ou entre deux clients d'une même boutique** ; session hijacking ; OTP bruteforce, interception/réemploi ; injection SQL ou header de résolution tenant ; fausses confirmations de virement ; surcoût de DB/pool ; fuites via logs, média, WebView bridge/Tauri IPC ; malwares ou clones d'app.

## Contrôles minimaux
- TenantContext après vérification du canal et des droits côté serveur ; channelId/appId **n'est jamais une authentification**.
- **Compte client obligatoire** : bearer, session courte + refresh rotation/révocation, hash fort du mot de passe, phone possession vérifiée avant vente (provider à choisir), récupération de compte rate-limited et sans enumeration.
- Contrôle de propriété de chaque panier/commande/produit, même dans un tenant. Staff membership et permission explicite, opérateur MFA/élévation auditée.
- Tarifs CDF/USD, frais, statut et paiement **validés par serveur** ; aucune confirmation PAYÉ depuis une déclaration client.
- SQL credentials DB séparés par tenant, secret manager hors Git, accès registre limité, backpressure/pools bornés, restauration ciblée testée.
- TLS HTTPS ; validation taille/contenu uploads ; médias publics filtrés, privés protégés, logs sans secrets/PII ; alertes et rotation des clés.
- Android Kotlin et Windows Rust protègent les sessions, jamais JS ; WebView/Tauri IPC avec commandes explicitement déclarées, origines et paramètres contrôlés ; pas de code distant injecté.
- Serveur **API-only** : aucun frontend/portail/Swagger UI exposé, health/admin endpoints réservés au réseau de supervision ou à auth renforcée.
- Versionnement API et signature des clients installables ; aucun secret DB/API privilégié embarqué.

## Blocage G4
Toute fuite inter-tenant ou inter-client, fuite token, OTP de test activé en prod, double checkout après retry, mismatch devise/total, accès admin HTML public, backup/restauration non vérifié, manque de conformité commerciale bloquent lancement public.

## Références
OWASP API Security Top 10 : https://owasp.org/API-Security/ ; Android architecture : https://developer.android.com/topic/architecture .
