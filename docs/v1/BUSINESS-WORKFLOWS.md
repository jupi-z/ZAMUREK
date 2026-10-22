# Parcours métiers V1 — critères fonctionnels non négociables

## Parcours générique
Organisation créée → un ou plusieurs établissements → profils métiers activés → staff avec rôles → catalogue/offres/horaires/frais → client **online** e-mail vérifié OU client de passage **POS** sans compte mais caissier authentifié → découverte/vitrine → quote serveur (USD interne→CDF commercial RDC) → réservation ou commande → règlement directement marchand → exécution → remise/service rendu → historique/audit. Aucun état critique n'est réglé par une requête anonyme, un modèle IA ou un calcul de l'interface.

## W0 Point de vente physique / cash / impression — obligatoire dans tous métiers éligibles

Caissier autorisé ouvre `CashSession` sur `PosTerminal` d'un établissement, compte l'espèce initiale et vend **sans exiger une identité client/e-mail** (`WALK_IN`). Catalogue commun online/POS, prix calculés serveur, vente atomique Core `SalesOrder(origin=POS)` + `PaymentRecord` + `CashMovement` si cash + outbox avec idempotence ; monnaie rendue `tendered - due` n'est pas chiffre d'affaires. Transferts manuels jamais considérés payés sur simple promesse. Imprimer/re-imprimer facture A4 ou ticket 58/80 mm depuis état document canonique, sans nouvelle vente si imprimante échoue ; DGI conforme seulement si intégration/authentification réellement validée. Clôture de caisse = fonds attendus, espèces comptées, écarts et justificatifs, supervisor selon rôle. Les commandes physiques et en ligne convergent dans **une seule comptabilité de ventes** ; POS transactionnel offline hors V1.

## W1 Retail / boutique physique
SKU/variant + médias + disponibilité établissement, vente unitaire et bundles simples, prix source USD, panier mono-vendeur, retrait/livraison, caisse en point de vente connecté, retour/annulation manuels documentés. Les rôles propriétaires, caissiers, préparateurs et livreurs sont distincts. Pas de stock quantifié imposé : statut disponible/indisponible suffit, quantités vendues dans les commandes nécessaires.

## W2 Confiserie au poids
Une offre définit `unit=G`, `pricingBasis=1000 G` (ex. USD/kg), `min=50 G`, `step=1 G` ou précision configurée, `max`, et politique de tare si pesée. **125 g → 0.125 kg** sans float. Le moteur monétaire calcule USD proportionnel en décimal exact, convertit CDF selon taux versionné et arrondit **une seule fois selon politique documentée**. La balance matérielle n'est pas requise V1 ; saisie humaine auditée + confirmation poids final par commerçant, ajustement accepté par client si changement montant. 0/valeurs négatives/surpassement/arrondi indéterministe interdits.

## W3 Restaurant / pizzeria
Menu vendu par établissement selon disponibilité/horaires, variantes portion/taille, modificateurs (obligatoires et optionnels), limites min/max, allergènes fournis par établissement sans diagnostic, prix additionnel USD, quote CDF. Commandes sur place / retrait / livraison, immédiates ou créneaux validés, capacité configurable, état `PLACED→ACCEPTED→PREPARING→READY→FULFILLED`, ticket cuisine imprimable localement/à l'écran, refus fermeture ou hors plage. Réservations de table séparées des commandes, nombre couverts et capacité par créneau, déduplication de demandes, règle no-show configurable.

## W4 Salon / services planifiés
Service prix/durée, collaborateurs habilités, plages de travail/absences, buffers et capacités, possibilité de service simultané seulement si ressources distinctes. Client choisit établissement, prestation, employé facultatif, créneau ; maintien temporaire et réservation transactionnelle empêchent double-booking. Confirmation, rappels **dans l'app** (pas SMS), report, annulation, check-in, exécution et ticket; demande de règlement manuel si nécessaire.

## W5 Meubles / objets volumineux
Catalogue options dimensions/couleurs/matériaux, délai/estimation de disponibilité, frais de transport sur devis, emplacements et possibilité « quote required ». Client envoie paramètres/métriques ; marchand émet devis horodaté à validité limitée ; client accepte et convertit en commande sans prix arbitraire côté UI. Historique devis et modifications, livraison spéciale, remise et éventuel acompte manuel documenté.

## W6 Ordinateurs / réparation
Article neuf + service réparation sont deux types d'offre ; demande d'intervention séparée avec **consentement**, type de panne, observations du client, identifiant appareil éventuellement masqué, prise en charge avec reçu, diagnostic, devis, approbation préalable à réparation payante, travail en cours, tests, livraison/restitution, garantie fournie par marchand selon conditions. Photos/numéros de série sont données sensibles tenant, accès limités. Aucune intervention facturable acceptée implicitement.

## W7 Pharmacie
Tenant identifié comme officine sous obligation de fournir autorisation/qualité professionnelle conformément au territoire. V1 **comprend la gestion des produits autorisés non soumis à contraintes réglementaires non résolues** ; classification `NON_MEDICINAL | MEDICINE_OTC | MEDICINE_RESTRICTED | PRESCRIPTION_REQUIRED | PROHIBITED | UNCLASSIFIED` ; **MEDICINE_OTC n'est pas automatiquement non réglementé** et tout médicament/non-classé est `BLOCKED` par défaut jusqu'à la confirmation du cadre légal et des autorisations du professionnel. Pour les catégories légalement autorisées : lot, date de péremption, traçabilité de disponibilité et mentions nécessaires ; interdire la vente de lots périmés. Aucun checkout, conseil médical automatisé, diagnostic, interprétation ordonnance ou annonce publique sur des produits bloqués. Les transactions pharmaceutiques sensibles restent désactivées jusqu'à revue juridique et circuit professionnel vérifié ; ne pas contourner par faux produit générique. Le cas où la réglementation locale interdit toute vente en ligne est traité en mode catalogue non transactionnel.

## W8 Agrégation mall / centre commercial
Un lieu `venue` contient bâtiments/niveaux/zones et emplacements ; chaque membre reste sa propre organisation/DB et signe opt-in révocable pour des publications. App Discover peut naviguer par catégorie et secteur, combiner vue catalogue public non sensible, offrir filtres et entrer dans un checkout **propre à chaque commerçant**. Attribution des commandes/règlements à la bonne entreprise uniquement. Lors du retrait opt-in, retirer les index et caches au plus tard selon SLO à fixer ; aucune exfiltration d'historique. Venue manager ne voit que métriques agrégées explicitement consenties (et jamais PII/finances par défaut).

## Connexions métier / échecs
Retours/retraits/rendez-vous utilisent command/reply contrôlés ; état de paiement distinct de l'état de prestation. Si vente + réservation se croisent, idempotence sur l'opération, compensation sur échec et lock de ressources. Toutes les actions auditables et réversibles selon droit applicable. La réduction de l'affichage à CDF en RDC est un garde-fou juridique, pas une preuve de conformité fiscale.
