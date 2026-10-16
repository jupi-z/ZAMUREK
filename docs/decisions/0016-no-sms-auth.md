# ADR-0016 — Authentification sans SMS

**Statut : ADOPTÉ comme architecture de départ — 2026-10-16**

Client obligatoire via e-mail + mot de passe, e-mail vérifié par challenge à usage unique et SMTP configurable (fournisseur à tester avant vraie vente) ; récupération par e-mail ; aucun SMS. Téléphone réservé au contact livraison/commande. Marchand/opérateur avec TOTP et récupération renforcée ; opérateur via VPN.

Remplace les hypothèses téléphone + OTP SMS présentes dans docs du 15 octobre 2026. Risque assumé : acheteurs sans e-mail exclus V1 ; plus tard passkeys/alternatives sous ADR.

Références : https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html ; https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html .
