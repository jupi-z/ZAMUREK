# ADR-0007 — Checkout invité et préparation de l'identité globale

**Statut : REMPLACÉ PAR [ADR-0011](0011-mandatory-customer-accounts.md) | Historique uniquement | Date : 2026-10-15**

> Ne plus appliquer cette décision : l'utilisateur a confirmé le compte client obligatoire, et aucune commande invitée en V1.

## Décision
Aucun compte acheteur obligatoire pour commander. Suivi possible via token secret propre à la commande. Employer PlatformIdentity global et CustomerProfile local comme concepts distincts ; aucune fusion automatique de PII entre boutiques.

## Alternatives
Imposer compte central à tous les achats ; facile pour marketplace mais augmente friction et obligations de données trop tôt.

## Conséquences
Confidentialité et adoption simplifiées, mais perte du token de suivi nécessite futur parcours de récupération vérifié. Association compte global soumise à consentement.

## Révision
Usage réel, exigences antifraude et marketplace.

