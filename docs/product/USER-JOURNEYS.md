# ZAMUREK — parcours utilisateurs actifs de la V1

La source normative détaillée est [BUSINESS-WORKFLOWS](../v1/BUSINESS-WORKFLOWS.md) et la [matrice des capacités](../v1/CAPABILITY-MATRIX.md).

## Acheteur
Identité globale par e-mail vérifié (aucun SMS) → entrée par APK commerçant ou ZAMUREK Discover/venue → découverte d'offres par établissement (produit, produit au poids, repas, prestation, bien sur devis, réparation, articles pharmaceutiques autorisés) → validation disponibilité et devis CDF API → commande mono-vendeur ou réservation transactionnelle → paiement marchand direct manuel/livraison/retrait → suivi de l'exécution et demande d'annulation/report.

## Marchand
Création organisation/établissement et profils métiers → configuration de chaque activité, horaires, employés/permissions, prix USD+taux USD→CDF versionné → gestion catalogue, menu/options, cuisine, pesée, rendez-vous, devis mobilier et réparation, caisse, remise, règlements et consentement de publication dans venue. IA assiste uniquement avec scopes, consentement et approbations des écritures sensibles.

## Gestionnaire venue/mall
Gère bâtiments/étages/emplacements, invitations/visibilité des entreprises consentantes et catalogue public ; **aucun accès automatique** aux commandes, clients, comptes ou agents privés des vendeurs. Opt-out d'une entreprise retire sa projection.

## Opérateur ZAMUREK
Client Windows EXE/MSI + VPN/MFA, provisioning registry et DB, contrôle des droits/établissements, abonnement BASIC 7 USD par organisation, supervision privée, politique IA et conformité. Ne prend pas possession des fonds marchands.

## Invariants
Prix/poids sans flottants ; réservations sans double booking ; actes pharmacie réglementés bloqués tant que non autorisés ; serveur de production **API uniquement**, aucun portail hébergé. Les fonctionnalités réellement offertes en 1.0.0 exigent preuves de tests bout en bout et validation juridique.
