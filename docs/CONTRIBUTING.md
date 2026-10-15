# Guide de contribution

## Git
Branche de travail depuis main, commits explicites (docs:, feat:, fix:, test:, chore:), PR avec impact tenant/sécurité/API et preuve de test. Pas de force-push sur main.

## Documentation-first
Chaque changement de règle : mettre à jour PRD/spec, ADR si structurel, contrat OpenAPI et cas de test. Toutes les références Markdown locales doivent être valides.

## Sécurité
Ne pas commiter .env, credentials, tokens, signatures Android, données réelles. Revue obligatoire pour auth, pricing, paiements, résolution tenant et migrations.

## État G0
Validation documentaire via python3 scripts/validate_docs.py. Les builds JavaScript/Android commencent au jalon G1 seulement.

