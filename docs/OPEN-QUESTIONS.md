# ZAMUREK — décisions externes et dépendances ouvertes après convergence

**Statut 22/10/2026.** Les décisions d'architecture du [Core partagé](v1/SHARED-CORE-INTEGRATION.md) sont adoptées, les implémentations sont à réaliser. Aucun statut de contrat juridique, fiscal ou commercial n'est présumé obtenu.

## Dépendances techniques priorisées
- **D01** Monarque Connect **10A.5** : C0–C3/C6/C7 canonique, contrats OpenAPI signés/versionnés, scopes et entitlements ; **bloque la clôture ZAMUREK 0.1.0**.
- **D02** Monarque Connect **10A.5 C4/C5** : POS cash atomique, sessions de caisse, facture/reçu et renderer ; **bloque les ventes ZAMUREK 0.2.0**.
- **D03** Backend Core privé, repo ZAMUREK public : protéger code propriétaire futur, définir publication d'artefacts contracts entre repos sans fuite de code/secrets.
- **D04** Compatibilité Auth : acheteur online vérifié ≠ staff membership, POS walk-in sans adresse e-mail.
- **D05** Choix/licence d'imprimantes test (58/80mm ESC/POS/A4) et environnement Android/Windows réel ; pas de faux « imprimé ».
- **D06** FX et fiscalité : vérifier droit RDC à afficher/pricer CDF, statut facture normalisée DGI, taxes et homologation/solution fiscale, conservation de documents.
- **D07** Formule **ZAMUREK BASIC 7 USD/mois/org** : fixer par contrat nombre d'établissements/caisses/employés inclus, usage IA, coût SMTP/support/transaction, règles de suspension et facturation CDF. Aucun établissement illimité présumé.
- **D08** AI provider et coûts, consentement, contrat traitement données, seuils évaluation et confidentialité, en coordination MC 10B/11.5.
- **D09** Infrastructure Core API-only : VPS, DNS, TLS, VPN opérateur, SMTP, backups/restauration logique et sécurité ; aucun sous-domaine proposé n'est considéré déployé.
- **D10** Apps/signature/distribution : identités éditeurs, droit d'usage marques et compatibilité magasins d'apps.

## Activités réglementées, partenaires et commerce
- **E01** LaJoie Mall n'est qu'un partenariat éventuel, aucun logo/nom public ou déploiement sous sa marque sans accord.
- **E02** Médicaments et prescriptions **bloqués** tant que licences officines, classification, obligations en ligne et protocole professionnel ne sont pas légalement vérifiés.
- **E03** Restaurant/santé/hygiène, coiffure, métrologie vente au poids, réparation et données clients : textes/autorisation selon juridiction.
- **E04** Paiements marchands : cash/à livraison et transferts manuels autorisés ; procédures anti-fraude, remboursement/rapprochement, contrôle de preuve. Aucun portefeuille/escrow marketplace V1.

## Traçabilité
Le manifeste V1 contient **43 capacités** `REQUIRED`, y compris 3 POS et 2 Core integration. Les gates externes bloquent la **commercialisation**, pas l'implémentation synthétique. Voir [roadmap intégrée](v1/INTEGRATION-ROADMAP.md) et [qualité](v1/QUALITY-REQUIREMENTS.md).
