> **ARCHIVE HISTORIQUE — stratégie de test xShop remplacée.** Recettes officielles dans [ZAMUREK QUALITY-REQUIREMENTS](../v1/QUALITY-REQUIREMENTS.md), [AGENTIC-KERNEL](../v1/AGENTIC-KERNEL.md) et [CAPABILITY-MATRIX](../v1/CAPABILITY-MATRIX.md).

# Tests xShop — état cible après arbitrages 16 octobre 2026

## Architecture/métier
- Deux tenants avec DB et credentials distincts ; deux acheteurs même tenant ; IDOR inter-tenant et inter-client refusés.
- Catalogue produit USD seul, pas de deuxième prix CDF indépendant. Prix publics RDC **CDF uniquement**, pas de sélecteur USD actif.
- Taux USD→CDF commerçant versionné, audit auteur/date ; exemple synthétique 2360, puis taux modifié ; ancien historique reste identique.
- Calcul monétaire avec précision décimale/fraction exacte, arrondi stable au CDF entier selon règle versionnée et tests des valeurs limites, grandes quantités, frais livraison, overflow, taux négatif/nul.
- Devis CDF serveur `quoteId` et expiry ; prix/taux/frais changé depuis devis → 409/reconfirm, aucun checkout sans devis frais/tx valide. Idempotence d'une commande avec même clé et empreinte.
- Paiements livraison/transfert manuel direct marchand ; aucune auto-certification de PAID ; gestion devise réception distincte, pas de paiement USD automatisé sans validation.
- Abonnement plateforme BASIC **700 cents USD/mois**, zéro commission, taux plateforme indépendant pour facturation publique CDF RDC.

## Identité
- Inscription e-mail/mot de passe, e-mail verification unique, login, rotation refresh, recovery, révocation ; **aucun appel SMS** ni dépendance SMS ; provider SMTP simulé en tests.
- Staff marchand MFA TOTP si privilégié, opérateur MFA + VPN ; tests bruteforce, IDOR, perte récupération.

## Réseau
- En simulation de prod, `/platform/v1` n'est **pas accessible depuis Internet public** ; DB/metrics/stockage privé non exposés ; /auth/v1/checkout publics uniquement selon auth/TLS.
- Aucune SPA/PWA/SSR/admin web/Swagger UI livrée en production ; Android React UI+Kotlin et Windows Tauri/Rust installables et signés.

## CI
G0 : `validate_docs.py` et `validate_openapi.py` ; une validation normative OpenAPI de tiers reste nécessaire en G1. Aucune suite d'intégration ou benchmark prod n'est déclarée exécutée.

## Gate G4
Texte légal RDC prix CDF et cas règlement devise / taux marchand / facturation/TVA validés ; SMTP réel, commerçant pilote, DNS et VPS, sauvegarde tenant/restauration et UX mobile confirmés.
