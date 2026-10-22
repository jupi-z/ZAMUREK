# ZAMUREK 1.0.0 — Definition of Done et matrice qualité

## Definition of Done (toute fonctionnalité)
Code compilé, tests unité/intégration et E2E sur le scénario visé, OpenAPI et schéma à jour, validation rôles & ownership, logs/audit, gestion erreurs et concurrence, tests haute/basse latence, sans secrets/PII, documentation, couverture négative et lien preuve. Aucune simple présence de endpoint ne vaut recette.

## Contrôles P0 (bloquants absolus)
1. **Isolation** : shared PostgreSQL Core avec organisations T1/T2 logiquement isolées, permissions établissement E1/E2 et ownership ; BOLA/BFLA IDOR clients/staff/agents et projections mall.
2. **Finance** : décimal exact, conversion USD/CDF par **CDF_LINE_HALF_UP_V1** et arrondi déterministes, quote TTL, immutabilité des montants et conformité territorial prix.
3. **Réservations** : pas de réservation concurrente de même ressource/intervalle ; transactions et compensations ; cancellation policies.
4. **États** : vente, service, restauration et réparation possèdent des transitions permises, idempotency sur chaque mutation, audit.
5. **Paiements** : cash POS enregistré atomiquement avec SalesOrder/PaymentRecord/CashMovement, rendu monnaie, sessions clôturées, paiements manuels sans fausse auto-confirmation, remboursements encadrés, abonnements produits séparés.
6. **Agentique** : pas d'outil sensible sans policy et approbation humaine, injection/exfiltration cross-tenant bloquées ; fallback sans modèle.
7. **Pharmacie** : produits réglementés refusés en catalogue transactionnel/checkout tant que juridique non validé, aucun conseil médical automatisé.
8. **Réseau** : op routes via VPN et MFA, DB/metrics/backups privés, API client authentifiée, TLS, aucun frontend web prod.
9. **Restore & build** : sauvegarde/export/restauration logique Core sélective par organisation A sans fuite B ; API partagée, Android acheteur/marchand/Discover et Windows marchand/POS/opérateur, builds réels.
10. **POS, factures et impression** : walk-in sans compte client, terminal/session, ticket 58/80mm/A4, erreur papier sans paiement doublé, statut fiscal fail-closed ; les documents normalisés nécessitent authentification légale vérifiée.
11. **Core partagé** : les deux canaux utilisent mêmes commandes/payments et agents/entitlements, SHA contrats Core comparés automatiquement ; aucun second serveur métier ZAMUREK.
12. **Compliance** : obligations commerciales, données, droits des tiers et licences vérifiés ; aucune conformité annoncée par présomption.

## P1 — fonctionnel complet
- Catalogue et prix pour toutes les 7 verticales, édition et gestion établissement, rôles, retour/annulation, reçus, images et recherche.
- Restaurant : menu/choix requis, horaires, tickets de cuisine, réservations de tables.
- Coiffure : staff/horaires/buffers, report/no-show, verrouillage créneaux.
- Poids : grammes/kilos, prix/kg, précision et arrondi, pesée finale et accord client.
- Meubles : devis personnalisé, dimensions et transport.
- Réparation : diagnostic, devis, approbation, étapes, preuve remise.
- Venue : multi organisations opt-in, filtres, index à jour, retrait opt-in.
- IA : 3 assistants réels fiables, traçabilité des propositions, désactivation et contrôle coûts.
- i18n français complet, accessibilité, latence mesurée, erreurs réseau et reprise.

## P2 — améliorations non critiques
Micro-animations, métriques avancées, optimisations UX non bloquantes ou outils de confort, à condition d'absence de défaut bloquant. Ne pas y mettre une activité métier V1.

## Tests minimaux mesurables
**API** : unitaires par module, tests d'intégration sur PostgreSQL vrai, property-based sur FX/poids, E2E multi-tenants et concurrent stress booking.
**Android** : appareils/émulateurs officiels, parcours acheteur, marchand/POS et discovery, bridge permissions, test imprimante réelle (ou statut BLOCKED), mode offline UX sans validation, orientation/taille.
**Windows** : build sur Windows pour EXE/MSI, install/uninstall, stockage sessions, VPN et workflows merchandising/booking/POS, impression A4/thermique et périphérique caissier ; artefacts signés si release publique.
**Sécurité** : OWASP API top 10, outil IA redteam, fuzz de DTO, scans SCA/SBOM/licences.
**Performance** : définir SLO p95 de checkout, listing et création rendez-vous via tests réels sur VPS ciblé ; seuils validés avant release, pas de chiffres fictifs.
**Disaster recovery** : RPO/RTO décidés selon contrat avant release et démontrés ; versionner migrations et rollback.
**Légal** : texte arrêté prix/facturation CDF applicable vérifié, données, vente de médicaments, facturation fiscale et obligations locales qualifiées.

## Reporting
Chaque rapport montre pour chaque P0/P1 : statut PASS/FAIL/BLOCKED/NOT_RUN, procédure, commit/artefact, date, environnement, owner et next action. Aucune assertion `100%` si test non exécuté ou dépendance externe sans preuve.
