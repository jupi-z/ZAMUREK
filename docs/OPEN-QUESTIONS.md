# Registre des décisions ouvertes

Les choix techniques ont été pris comme **hypothèses de travail de conception** à la demande du porteur de projet. Les éléments ci-dessous exigent validation avant implémentation ou mise en production.

| ID | Question | Défaut proposé | Échéance |
|---|---|---|---|
| Q01 | Encaissement | Chaque commerçant encaisse directement ; xShop n'est pas agent de paiement | avant G2 |
| Q02 | Prestataire(s) Mobile Money / carte en RDC | Aucun fournisseur engagé avant test + contrat | avant paiement électronique |
| Q03 | Langues, territoires et devises | FR ; devise fixée par boutique, aucun taux de change | avant G3 |
| Q04 | Gestion de stock | Statut de disponibilité simple, aucun stock chiffré | G2 |
| Q05 | Identité client globale | Invité V1, liaison volontaire dans évolution | avant marketplace |
| Q06 | Hébergement et budget | Mesurer charge pilote, décider VPS/DB et stockage | avant G1 production |
| Q07 | Rétention PII / règles applicables | Minimisation + validation juridique selon territoires | avant G4 |
| Q08 | Publication multi-app Google Play | Évaluer différenciation ; PWA alternative | avant G3 release |
| Q09 | Propriété / comptes de signature | Publication et signature sous comptes autorisés, procédure de transfert | avant publication |
| Q10 | Modèle de facturation de xShop | Non implémenté | avant commercialisation |
| Q11 | Politique d'annulation / remboursement | Le marchand arbitre selon procédure et obligations | avant G4 |
| Q12 | RPO/RTO, backups et support | Aucune promesse contractuelle avant exercice de restauration | avant G4 |
| Q13 | Noms, domaines et package IDs | Configurables par commerçant | avant build G3 |
| Q14 | Licence du dépôt public | Aucune licence accordée par défaut | dès décision de diffusion |
| Q15 | Seuils de qualité (latence, mémoire, disponibilité) | Fixés après instrumenter pilote Android/backend | avant G4 |
| Q16 | Méthode de livraison et zones | Retrait + zones/frais manuels | avant G2 |
| Q17 | Boutique pilote / catégorie produits | Commencer par un commerçant de produits physiques standard | avant G1 |
| Q18 | Notifications marchand/client | Actualisation admin et suivi app d'abord ; push/SMS après évaluation | avant G3 |
| Q19 | Catalogue marketplace opt-in | Participation volontaire, désactivée par défaut | avant marketplace |
| Q20 | Périmètre des canaux au pilote | Android client + console marchand web + console opérateur minimale | avant G1 |
| Q21 | Modes de contact et support | Contact marchand public + processus support xShop distinct | avant G3 |
| Q22 | Portage légal et fiscal des ventes | À définir contractuellement et vérifier juridiquement selon les territoires | avant G4 |

Pour les choix opérationnels (hébergement, RPO/RTO, qualité), définir budget et attentes, puis déléguer les paramètres techniques à l'équipe après tests. Un défaut proposé n'est **pas une décision validée**.

Voir [audit G0](quality/AUDIT-G0-2026-10-15.md).

## Procédure d'arbitrage
Documenter la décision, sa motivation, les alternatives et les effets sur le contrat API ; mettre à jour ADR/PRD/spec si nécessaire. Éviter de coder une hypothèse comme règle irréversible.

