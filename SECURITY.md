# ZAMUREK — sécurité et signalement

Le projet ZAMUREK est une plateforme commerciale propriétaire, en phase de conception. Ce dépôt est **public** au moment de la rédaction, et n'a pas de licence open source générale.

## Signaler une vulnérabilité
Ne pas publier de secrets, preuves d'exploitation contenant données personnelles, mots de passe ou clés dans les issues publiques. Contacter le mainteneur du dépôt par les moyens privés GitHub disponibles ; **ne pas inventer ni supposer une adresse e-mail de sécurité**. Si l'option de signalement privé GitHub est activée, privilégier cette fonctionnalité.

## Politique de secrets
- Aucun identifiant DB/VPS, token LLM, clé SMTP, clé de signature, données client/transaction réelles dans Git ou CI logs.
- En CI, permissions minimum, secrets injectés par outils dédiés, logs redigés et artefacts anonymisés ; aucun secret d'infrastructure dans les applications installables.
- Routes opérateur via VPN/MFA, séparation multi-tenant vérifiée côté backend et non au travers de l'application ou du CORS.
- Tests sécurité obligatoires sur isolation, prix, bookings, prompt injections, contenu réglementé et restauration avant lancement.

## Licence et distribution
Lire [politique tierce](docs/governance/OPEN-SOURCE-POLICY.md), [ADR propriété](docs/decisions/0019-proprietary-platform-permissive-oss.md) et [gates de sécurité V1](docs/v1/SECURITY-THREAT-MODEL.md). Une dépendance permissive demeure sous sa licence propre. Aucune assertion de sécurité certifiée à G0.
