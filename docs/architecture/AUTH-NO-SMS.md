# Authentification sans SMS — Core Monarque Connect, checkout online et POS physique

**Directive : aucun SMS au lancement.** Compte client e-mail vérifié obligatoire pour checkout **en ligne** ; en **vente physique POS**, acheteur de passage sans compte ni e-mail autorisé, à condition que le caissier soit authentifié et sa session/terminal vérifiés par Monarque Connect Core. Recommandation technique : **adresse e-mail + mot de passe**, vérification de l'adresse par lien/code à usage unique envoyé via transport SMTP configuré. Le numéro de téléphone est une donnée de livraison/contact **facultative à l'inscription**, obligatoire seulement lors d'une livraison si nécessaire. Ne pas utiliser le numéro non vérifié comme preuve d'identité.

## Comptes acheteur
- Enregistrement e-mail vérifié + mot de passe, hash Argon2id/scrypt selon bibliothèque auditée. Normalisation email prudente, unicité et absence d'énumération.
- Validation possession e-mail, token aléatoire cryptographiquement sûr, TTL court, usage unique, tentatives et débit limités. Pas de traitement de données commerciales avant vérification.
- Login/refresh rotation/revocation/logout, changement email avec vérification des deux, récupération de mot de passe par e-mail avec jeton temporaire.
- Rate limits par adresse masquée et IP, anti-bruteforce, réponses discrètes, audit auth sans secrets.
- Client Android Kotlin/Tauri Rust protège access/refresh token ; JavaScript UI n'y accède pas.
- SMTP configurable (compte e-mail/relay de l'opérateur ou autre prestataire) ; **aucune dépendance à un fournisseur nommé** ; tests en staging avec transport capturant les e-mails sans envoi externe. Une délivrabilité réelle est requise **avant comptes commerciaux**.
- Pas de TOTP obligatoire pour simples acheteurs V1, mais offrir une évolution passkeys ou TOTP quand raisonnable.

## Marchand / opérateur
- E-mail + mot de passe fort + **TOTP application d'authentification** et recovery codes limités pour rôles sensibles ; opérateur VPN privé + MFA, aucune auth uniquement par IP.
- La perte du téléphone TOTP exige récupération sécurisée non déléguée à un simple e-mail.

## Pourquoi ce choix
Supprime les coûts et la dépendance SMS, utilise un canal de contact vérifiable, garde un flux de récupération normal. **Limite** : un acheteur sans e-mail ne pourra pas utiliser la V1 ; étude éventuelle des passkeys/local accounts ultérieurement. Une vérification e-mail seule **n'est pas MFA forte**.

## Sources
OWASP Email Validation & Verification : https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html
OWASP MFA : https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html
OWASP Forgot Password : https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html
