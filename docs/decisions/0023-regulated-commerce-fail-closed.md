# ADR-0023 — Commerce réglementé fail-closed

**Statut ADOPTÉ — 2026-10-22**

ZAMUREK doit accueillir les établissements pharmaceutiques, mais pas permettre une vente/licence factice de médicaments : seuls articles réellement autorisés dans la juridiction et pour le marchand peuvent être publiés/achetés. Produits `MEDICINE_RESTRICTED`, `PRESCRIPTION_REQUIRED` ou inconnus bloqués par défaut ; le responsable technique ne peut activer des ventes pharmaceutiques sur simple toggle.

Les normes de dispensation, publicité, ordonnances, titulaires/licences, données de santé et ventes à distance doivent être vérifiées localement avant toute activation. Aucune IA ne conseille des traitements, ne délivre d'ordonnance ou ne dispense un médicament. Si vente à distance non autorisée, seule gestion interne et visibilité publique autorisée restent possibles.

Référence réglementaire d'époque à vérifier, droit RDC : https://www.legali.cd/legislation/lois/o-72-359-14-09-1972-1972 ; ne pas confondre la RDC avec la République du Congo ou la France.

Voir [gates légales](../v1/LEGAL-REGULATED-GATES.md).
