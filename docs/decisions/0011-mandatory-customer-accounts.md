# ADR-0011 — Compte client global obligatoire

**Statut : ADOPTÉ pour l'obligation de compte ; modalités téléphone/SMS REMPLACÉES PAR [ADR-0016](0016-no-sms-auth.md) | 2026-10-16**

> Compte obligatoire maintenu. Le mode de login actif est email + mot de passe + vérification par email, **sans SMS**. Le contenu ancien ci-dessous est historique si contradictoire.

Le porteur exige un **compte client pour toute commande**. Checkout anonyme/guest tracking supprimé. Identité xShop globale centralisée et profils commandes tenant isolés ; aucun historique partagé sans autorisation. Auth proposée par téléphone + mot de passe, vérification de numéro OTP avant ventes réelles (fournisseur à valider). Kotlin/Rust protègent tokens, backend contrôle tenant et ownership de chaque commande.

Alternative abandonnée : checkout invité (ADR-0007), désormais incompatible avec la décision métier.

Conséquences : parcours auth et provider OTP supplémentaires, mais continuité d'identité entre futurs clients marketplace et apps boutique. Tests 401/IDOR/recovery avant production.
