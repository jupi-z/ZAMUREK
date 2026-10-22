# Matrice normative des capacités — ZAMUREK 1.0.0

**Règle :** une ligne marquée REQUIRED doit être implémentée et démontrée E2E pour que 1.0.0 soit publiable. Il ne s'agit pas d'un MVP. Les fonctionnalités réglementées font l'objet de *gates*, jamais d'une activation tacite.

| ID | Contexte / capacité | V1 | Tests de sortie minimum |
|---|---|---|---|
| FND-01 | Registry, tenant DB isolée, établissement + membership | REQUIRED | T1/T2, E1/E2, refus cross-tenant et cross-establishment |
| FND-02 | Identité e-mail vérifié, sessions, reset, staff MFA, opérateur VPN | REQUIRED | rejets 401/403/IDOR, replay sessions |
| FND-03 | Merchant capability profiles configurables multi-activités | REQUIRED | activer 2 métiers dans 1 établissement, masquer le reste |
| FND-04 | Catalogue commun (offering PRODUCTS/SERVICES/WEIGHTED/FOOD/REGULATED) | REQUIRED | variantes, catégorie, photos, droits, publier/masquer |
| FND-05 | Prix USD sources, FX tenant vers CDF, quotes versionnées | REQUIRED | taux change, reçu antérieur immuable, décimal exact |
| FND-06 | Client orders, statuses, historique, pièces et communications statut | REQUIRED | achat → exécution → clôture, audit |
| FND-07 | Manual payment, COD/COP, règlement, preuves, refunds manuels | REQUIRED | aucun PAID arbitraire, reversals contrôlés |
| FND-08 | Pickup/local delivery, zones/horaires/frais, contact et preuve remise | REQUIRED | indisponibilité zone, pickup, livreur manuel |
| FND-09 | Backoffice marchand Android ET Windows installable | REQUIRED | autonomie pour toutes verticales, RBAC |
| FND-10 | POS/caisse **connecté** marchand (tablette/Android/Windows) | REQUIRED | ticket/encaissement manuel, offline pas de confirmation |
| FND-11 | Abonnement unique BASIC, tenant lifecycle, audit et suspension | REQUIRED | montant 7 USD, protection commandes et données |
| FND-12 | Applications acheteur marque + Discovery/venue, opt-in | REQUIRED | 2 tenants, aucun résultat privé sans consentement |
| FND-13 | API-only prod, observabilité privée, backup tenant/restauration | REQUIRED | smoke test distribution sans web UI, restore A |
| FND-14 | Contrats/compatibilité clients, i18n français et a11y | REQUIRED | ancien build supporté, erreurs et chargement robustes |
| FND-15 | Moteur politique géographique/prix, conformité marchés | REQUIRED | CDF public RDC, désactivation vente prohibée |
| FND-16 | Outbox, audit, idempotence et notifications in-app | REQUIRED | double retry sans doublon, consommateur rejeu |
| RTL-01 | Variantes/taille/couleur, quantités commandées, disponibilité | REQUIRED | même article dans plusieurs établissements |
| WGT-01 | Prix USD / unité de mesure canonique, grammes et kilos | REQUIRED | 125 g, 250 g, 1.5 kg, bornes et arrondis |
| WGT-02 | Quantité décimale exacte, précision et politiques de pesée | REQUIRED | quantité saisie par vendeur, jamais float |
| FOD-01 | Menus, catégories, préparation, suppléments/choix obligatoires | REQUIRED | pizza avec toppings/prix, contraintes de choix |
| FOD-02 | ASAP/programmation, places disponibles, zones, cuisine tickets | REQUIRED | cuisine → prêt → remise ; capacité concurrente |
| FOD-03 | Réservation de tables, créneaux, capacité, annulation | REQUIRED | double booking interdit |
| SVC-01 | Prestations, durée, disponibilités, horaires/staff | REQUIRED | non-chevauchement et congés |
| SVC-02 | Réservation, report, annulation, arrivée, réalisation | REQUIRED | deux RDV simultanés exclusifs rejetés |
| FUR-01 | Options/dimensions, devis personnalisé, livraison spécialisée | REQUIRED | devis → approbation → commande |
| REP-01 | Dossier de réparation/diagnostic, consentement/estimation | REQUIRED | accord client avant intervention facturable |
| REP-02 | Suivi étapes, restitution, historique privé, garanties déclarées | REQUIRED | ticket → réparé → remis |
| PHA-01 | Catalogue non-médicaments autorisés, identification du vendeur | REQUIRED | produits non autorisés bloqués |
| PHA-02 | Classement réglementaire, licence/approbation et vente refusée | REQUIRED | ordonnance/produit protégé **jamais vendu** sans validation |
| VEN-01 | Venue/mall, emplacements, opt-in, découverte inter-entreprises | REQUIRED | opt-out retranche les listings et cache |
| VEN-02 | Panier et checkout propres à chaque commerçant | REQUIRED | plusieurs shops visibles mais commandes séparées |
| AGT-01 | Registry outils/agents, scopes, politiques, journalisation | REQUIRED | tool call refusé sans scope et consentement |
| AGT-02 | Workflow durable, événements, retries, approbation humaine | REQUIRED | reprise, timeouts, replay, approbation versionnée |
| AGT-03 | Modèles interchangeables et désactivation globale/tenant | REQUIRED | fournisseur indisponible : métier continue |
| AGT-04 | Assistant catalogue / FAQ / synthèse réelle et vérifiable | REQUIRED | hallucinations contrôlées, no privileged write |
| SEC-01 | Tests red-team, isolation contextuelle IA, injection prompt | REQUIRED | outil refusé selon policy indépendamment du LLM |
| OPS-01 | CI lint/compile/tests E2E mobiles/backend/Windows et scan licences | REQUIRED | logs/artefacts authentiques, aucune simulation |
| LEG-01 | Gates fiscaux/données/réglementation RDC | REQUIRED BEFORE PRODUCTION | preuves et acceptation responsable |

Chaque capacité a un owner technique à affecter dans le registre de progression, un jeu de tests positif/négatif et une preuve dans le rapport de jalon. **Un texte marqué REQUIRED n'est pas un acquis réalisé.**
