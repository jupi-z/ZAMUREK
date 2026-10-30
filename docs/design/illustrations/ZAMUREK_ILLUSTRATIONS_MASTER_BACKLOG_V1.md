# ZAMUREK — Registre officiel de planification des illustrations

> **Statut : backlog de conception à valider, pas illustrations déjà produites.** Version de travail 1.0 — 30 octobre 2026.

## Cadre et décisions de design

Ce document recense **275 besoins d’illustration** pour les interfaces et supports Zamurek, organisés en **33 bases de composition réutilisables**. Les entrées sont des contextes d’usage, **pas une obligation de produire 275 dessins indépendants**. Les variantes peuvent réutiliser une même illustration maître, un personnage, une pose, un objet et une animation.

**Direction artistique :** identité Zamurek d’abord, *pas* de contrainte flat design. Style libre entre dessin stylisé premium, aplats sophistiqués, couches superposées, relief modéré, dégradés contrôlés et détails expressifs ; la présence de volumes n’est acceptée que si elle sert la compréhension et la qualité. Ne pas transformer les illustrations en scènes photoréalistes ni les encombrer de paysages. Personnes et objets prioritaires.

**Palette de marque :** vert forêt `#005C45` (principal), orange `#FF8A1E`, magenta `#D21868`. Blanc dominant `#FFFFFF` en mode clair, obsidienne `#111318` en mode sombre. Tons de peau, cheveux et matériaux autorisés sans forcer une recoloration irréaliste. Logo et iconographie officiels intacts.

**État réel :** aucun dessin final ou animation n’est créé par la production de ce backlog. Le document planifie leur fabrication. Figma et Penpot ne sont pas modifiés par ce livrable.

## Vue d’ensemble

| Mesure | Valeur |
|---|---:|
| Entrées inventoriées | 275 |
| Bases de composition planifiées | 33 |
| Priorité visuelle P0 | 36 |
| Priorité visuelle P1 | 204 |
| Priorité visuelle P2 | 31 |
| Priorité visuelle P3 | 4 |

Les priorités **P0–P3 portent uniquement sur la production des illustrations**, elles ne remplacent jamais les priorités normatives du produit ni ses gates de livraison. Les ID de capacités mentionnés dans le registre sont des **associations indicatives** et ne sont pas une preuve d’implémentation.

## Principes de production non négociables

1. **Personnalisation de marque** : même famille graphique, proportions humaines cohérentes, accessoires récurrents, formes arrondies choisies, verts profonds et accents orange/magenta parcimonieux. Pas d’obligation de tout aplatir.

2. **Modularité** : séparer dans les masters SVG `personne`, `tête`, `bras`, `main`, `objet`, `accessoire`, `badge`, `ombre` (si utile) et états. Conserver des IDs stables pour animation CSS/JS ; aucun simple PNG renommé SVG.

3. **Déclinaisons** : fournir une illustration statique sur fond transparent et tester l’intégration sur blanc/obsidienne. Un seul master géométrique, adaptation de teintes et contrastes si nécessaire.

4. **Animation pertinente** : animer une action (main, appareil, roue, colis, confirmation, recherche), non chaque détail. Prévoir un état immobile et le respect de `prefers-reduced-motion`. Ne pas inventer de succès financier.

5. **Lisibilité** : recadrages à 128/192/320 px pour interfaces, contrôles à zoom 100% et sur appareils ; pas de textes intégrés indispensables à la compréhension, utiliser des libellés UI locaux.

6. **Licences** : source d’origine/URL/version/licence et modifications documentées pour chaque composant externe. Humaaans CC0 est une piste ; IRA Design MIT exige le maintien des mentions de copyright/licence en cas de copie substantielle. Aucune pièce externe n’est incluse dans ce backlog.

7. **Règles produit** : pharmacie sous gating légal ; vente POS sans confirmation fictive ; IA sans action critique autonome ; panier mono-marchand ; absence de backend autonome Zamurek.

8. **Revue** : silhouette claire, cohérence du rendu, absence de superpositions parasites, pas de détails perdus, équivalents sombre/clair, intégrité SVG, performance, accessibilité et provenance vérifiées avant acceptation.

## Familles maîtresses

| Base | Composition directrice | Éléments réutilisables | Mouvement |
|---|---|---|---|
| BASE-EMPTY | Objet principal légèrement incliné + indicateur discret de vide | Panier, loupe, cœur, réservation, boîte, cloche | Apparition légère ou petite oscillation |
| BASE-SUCCESS | Objet de contexte + signe de confirmation non ambigu | Coche, colis, ticket, calendrier | Coche dessinée puis arrêt |
| BASE-ERROR | Objet ou appareil + signe explicite de problème | Wifi barré, document, terminal, verrou | Micro-secousse limitée, jamais en boucle |
| BASE-LOADING | Objet de l’action et marqueur de progression | Loupe, sac, reçu, synchronisation | Boucle courte et réduite si motion réduite |
| BASE-DISCOVERY | Personnage récurrent accompagné d’un seul univers marchand | Smartphone, sac, symbole métier | Geste de la main ou déplacement du téléphone |
| BASE-SEARCH | Personne ou main guidant la recherche | Téléphone, loupe, filtres | Lent balayage de la loupe |
| BASE-CHECKOUT | Personnage et objet de commande clairement séparés | Panier, produit, colis, reçu | Déplacement contrôlé d’un article |
| BASE-TENDER | Main + moyen de règlement ou justificatif | Espèces, reçu, transfert manuel | Apparition de la confirmation conditionnelle |
| BASE-PROFILE | Portrait réutilisable et interface minimale | Téléphone, identifiant, adresse | Clignement ou geste de sélection |
| BASE-STORE | Marchand récurrent avec un objet de gestion | Sac, enseigne, boutique | Mouvement de main et activation |
| BASE-CATALOG | Produit isolé et action du marchand | Étiquette, variantes, balance | Apparition d’une étiquette |
| BASE-MERCHANT-ORDER | Marchand et colis/tablette de commande | Colis, liste, calendrier | Progression en trois temps |
| BASE-ANALYTICS | Commerçant face à une donnée non réelle | Courbe, panneau, avis | Barre de progression abstraite |
| BASE-POS | Caissier face à la caisse sans détail transactionnel inventé | Terminal, billet, ticket, imprimante | Mécanisme de ticket limité |
| BASE-POS-TOOLS | Action de caisse illustrée par objet et main | Scanner, reçu, QR, étiquette | Balayage de lecture court |
| BASE-FOOD | Chef, serveur ou client avec préparation / objet alimentaire | Pizza, assiette, plateau | Vapeur légère ou bras de service |
| BASE-BEAUTY | Professionnelle et cliente avec accessoires épurés | Peigne, ciseaux, miroir, calendrier | Mouvement de bras ou de peigne |
| BASE-REPAIR | Technicien avec objet ouvert ou outil | Smartphone, tournevis, loupe | Rotation légère de l’outil |
| BASE-FURNITURE | Mobilier seul ou personne et meuble | Fauteuil, lit, ruban métrique | Déplacement discret de l’objet |
| BASE-PHARMACY | Personnel qualifié générique, produits autorisés uniquement | Boîte non médicale, stock, bouclier | Aucun mouvement impliquant une promesse médicale |
| BASE-SERVICES | Prestataire en action avec accessoire propre au métier | Boîte à outils, agenda, badge | Geste du professionnel |
| BASE-WEIGHT | Objet pesé + balance et grammage sans prix inventé | Balance, paquet, grammes | Aiguille ou sélection de masse |
| BASE-VENUE | Deux marchands distincts accessibles depuis une interface | Sacs, enseignes, smartphone | Transitions entre univers |
| BASE-AI-SHOP | Assistant visuel non anthropomorphe ou personnage de conseil | Bulle, étincelle, produit | Expression douce, réponse en 2 temps |
| BASE-AI-MERCHANT | Marchand et assistant sur une surface unique | Catalogue, suggestions, validation | Apparition d’une suggestion |
| BASE-AI-OPS | Opérateur avec synthèse abstraite et badge d’approbation | Graphique, alerte, autorisation | Pulse ponctuel |
| BASE-AI-CHAT | Conversation et présence d’assistance contextualisée | Bulles, smartphone, agent | Petite alternance des bulles |
| BASE-TRUST | Identité et bouclier sans cadenas disproportionné | Clé, cadenas, bouclier, appareil | Coche ou verrouillage ponctuel |
| BASE-ONBOARDING | Personnage principal stable guidant une action | Téléphone, étapes, objet métier | Entrée légère de chaque étape |
| BASE-NOTIFY | Évènement discret associant cloche et objet concerné | Cloche, message, calendrier, commande | Apparition unique du badge |
| BASE-EDITORIAL | Deux ou trois personnages modulaires + objets, sans paysage | Sacs, appareil, terminal, colis | Animation uniquement si usage numérique |
| BASE-OPERATOR | Opérateur privé avec terminaux abstraits sans données sensibles | Serveur, graphique, contrôle d’accès | Mouvement limité des indicateurs |
| BASE-UTILITY | Objet fonctionnel unique et geste optionnel | Aide, imprimante, appareil, sauvegarde | Animation courte, si utile |

## Backlog exhaustif des 275 demandes

Colonnes : **ID**, désignation, priorité de création, master de composition, périmètre. Pour les fiches complètes (support, animation, risques, validations, origine), utiliser le fichier XLSX/CSV/JSON associé.

### A1 — États système / États vides
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-001` | Panier vide | P0 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-002` | Aucun résultat | P0 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-003` | Aucun favori | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-004` | Aucune commande | P0 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-005` | Aucune réservation | P0 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-006` | Aucun message | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-007` | Aucune boutique disponible | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-008` | Aucun produit disponible | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-009` | Aucun service disponible | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-010` | Aucun restaurant disponible | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-011` | Aucun historique | P2 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-012` | Aucun établissement lié | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-013` | Aucune notification | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-014` | Aucune activité récente | P1 | `BASE-EMPTY` | V1 / support à confirmer |
| `ZIL-015` | Aucune recherche récente | P1 | `BASE-EMPTY` | V1 / support à confirmer |

### A2 — États système / Succès
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-016` | Action réussie | P0 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-017` | Commande confirmée | P0 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-018` | Paiement confirmé | P0 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-019` | Réservation confirmée | P0 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-020` | Profil créé | P1 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-021` | Boutique créée | P1 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-022` | Produit ajouté avec succès | P1 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-023` | Service publié | P2 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-024` | Synchronisation réussie | P1 | `BASE-SUCCESS` | V1 / support à confirmer |
| `ZIL-025` | Impression réussie | P1 | `BASE-SUCCESS` | V1 / support à confirmer |

### A3 — États système / Erreurs et échecs
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-026` | Erreur réseau | P0 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-027` | Erreur serveur | P0 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-028` | Paiement échoué | P0 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-029` | Échec de synchronisation | P1 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-030` | Impression échouée | P1 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-031` | Produit introuvable | P1 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-032` | Action impossible | P2 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-033` | Session expirée | P1 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-034` | Accès refusé | P0 | `BASE-ERROR` | V1 / support à confirmer |
| `ZIL-035` | Données indisponibles | P1 | `BASE-ERROR` | V1 / support à confirmer |

### A4 — États système / Attente et chargement
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-036` | Chargement générique | P0 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-037` | Recherche en cours | P1 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-038` | Traitement du paiement | P0 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-039` | Génération de reçu | P1 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-040` | Synchronisation des données | P1 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-041` | Préparation de commande | P1 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-042` | Vérification du compte | P1 | `BASE-LOADING` | V1 / support à confirmer |
| `ZIL-043` | Connexion en cours | P1 | `BASE-LOADING` | V1 / support à confirmer |

### B1 — Acheteur / Découverte et accueil
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-044` | Bienvenue sur Zamurek | P0 | `BASE-DISCOVERY` | V1 / support à confirmer |
| `ZIL-045` | Découvrir les boutiques | P0 | `BASE-DISCOVERY` | V1 / support à confirmer |
| `ZIL-046` | Découvrir les restaurants | P1 | `BASE-DISCOVERY` | V1 / support à confirmer |
| `ZIL-047` | Découvrir les services | P1 | `BASE-DISCOVERY` | V1 / support à confirmer |
| `ZIL-048` | Découvrir les salons de beauté | P1 | `BASE-DISCOVERY` | V1 sous conditions / validation |
| `ZIL-049` | Découvrir les pharmacies | P1 | `BASE-DISCOVERY` | V1 sous conditions / validation |
| `ZIL-050` | Découvrir les meubles | P1 | `BASE-DISCOVERY` | V1 sous conditions / validation |
| `ZIL-051` | Découvrir les réparations | P1 | `BASE-DISCOVERY` | V1 / support à confirmer |
| `ZIL-052` | Explorer le mall / univers Zamurek | P1 | `BASE-DISCOVERY` | V1 / support à confirmer |

### B2 — Acheteur / Recherche
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-053` | Recherche produit | P1 | `BASE-SEARCH` | V1 / support à confirmer |
| `ZIL-054` | Recherche boutique | P1 | `BASE-SEARCH` | V1 / support à confirmer |
| `ZIL-055` | Recherche service | P1 | `BASE-SEARCH` | V1 / support à confirmer |
| `ZIL-056` | Recherche restaurant | P1 | `BASE-SEARCH` | V1 / support à confirmer |
| `ZIL-057` | Filtres de recherche | P1 | `BASE-SEARCH` | V1 / support à confirmer |
| `ZIL-058` | Suggestions intelligentes | P1 | `BASE-SEARCH` | V1 / support à confirmer |
| `ZIL-059` | Recherche de proximité | P1 | `BASE-SEARCH` | V1 sous conditions / validation |

### B3 — Acheteur / Achat et commande
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-060` | Ajouter au panier | P0 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-061` | Panier avec articles | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-062` | Validation de commande | P0 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-063` | Choix du mode de livraison | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-064` | Choix du retrait | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-065` | Confirmation finale | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-066` | Suivi de commande | P0 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-067` | Colis prêt | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-068` | Commande livrée | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |
| `ZIL-069` | Commande retirée | P1 | `BASE-CHECKOUT` | V1 / support à confirmer |

### B4 — Acheteur / Paiement
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-070` | Paiement espèces à la livraison | P1 | `BASE-TENDER` | V1 sous conditions / validation |
| `ZIL-071` | Paiement par transfert | P1 | `BASE-TENDER` | V1 / support à confirmer |
| `ZIL-072` | Paiement confirmé | P1 | `BASE-TENDER` | V1 / support à confirmer |
| `ZIL-073` | Attente de confirmation | P1 | `BASE-TENDER` | V1 / support à confirmer |
| `ZIL-074` | Remboursement / retour | P1 | `BASE-TENDER` | V1 sous conditions / validation |
| `ZIL-075` | Réception d'une facture ou d'un reçu | P1 | `BASE-TENDER` | V1 / support à confirmer |

### B5 — Acheteur / Compte client
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-076` | Création de compte | P0 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-077` | Connexion | P0 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-078` | Vérification du compte | P1 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-079` | Profil utilisateur | P1 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-080` | Historique de commandes | P1 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-081` | Favoris / liste d'envies | P1 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-082` | Adresse de livraison | P1 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-083` | Moyens de contact | P1 | `BASE-PROFILE` | V1 / support à confirmer |
| `ZIL-084` | Support client | P1 | `BASE-PROFILE` | V1 / support à confirmer |

### C1 — Marchand / Ouverture de boutique
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-085` | Création de boutique | P0 | `BASE-STORE` | V1 / support à confirmer |
| `ZIL-086` | Configuration du profil marchand | P1 | `BASE-STORE` | V1 / support à confirmer |
| `ZIL-087` | Ajout du logo ou de l'identité | P1 | `BASE-STORE` | V1 / support à confirmer |
| `ZIL-088` | Activation de la boutique | P1 | `BASE-STORE` | V1 / support à confirmer |
| `ZIL-089` | Boutique en attente de validation | P1 | `BASE-STORE` | V1 / support à confirmer |
| `ZIL-090` | Boutique active | P1 | `BASE-STORE` | V1 / support à confirmer |

### C2 — Marchand / Catalogue
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-091` | Ajouter un produit | P0 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-092` | Modifier un produit | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-093` | Organiser le catalogue | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-094` | Produit indisponible | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-095` | Gestion des variantes | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-096` | Produit au poids / grammage | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-097` | Service publié | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-098` | Service désactivé | P1 | `BASE-CATALOG` | V1 / support à confirmer |
| `ZIL-099` | Produit mis en avant | P1 | `BASE-CATALOG` | V1 / support à confirmer |

### C3 — Marchand / Gestion commerciale
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-100` | Nouvelle commande | P0 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-101` | Préparation de commande | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-102` | Commande prête | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-103` | Commande remise | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-104` | Commande annulée | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-105` | Réservation reçue | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-106` | Réservation confirmée | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-107` | Réservation refusée | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |
| `ZIL-108` | Historique marchand | P1 | `BASE-MERCHANT-ORDER` | V1 / support à confirmer |

### C4 — Marchand / Performance et croissance
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-109` | Statistiques boutique | P1 | `BASE-ANALYTICS` | V1 / support à confirmer |
| `ZIL-110` | Ventes en hausse | P1 | `BASE-ANALYTICS` | V1 / support à confirmer |
| `ZIL-111` | Produit populaire | P1 | `BASE-ANALYTICS` | V1 / support à confirmer |
| `ZIL-112` | Nouveau client | P1 | `BASE-ANALYTICS` | V1 / support à confirmer |
| `ZIL-113` | Fidélisation | P3 | `BASE-ANALYTICS` | Hors V1 (candidat futur) |
| `ZIL-114` | Offre promotionnelle | P1 | `BASE-ANALYTICS` | V1 sous conditions / validation |
| `ZIL-115` | Campagne de mise en avant | P2 | `BASE-ANALYTICS` | V1 / support à confirmer |
| `ZIL-116` | Avis client / satisfaction | P2 | `BASE-ANALYTICS` | V1 / support à confirmer |

### D1 — POS / Point de vente
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-117` | Ouverture de caisse | P0 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-118` | Session de caisse active | P1 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-119` | Vente enregistrée | P2 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-120` | Impression de ticket | P1 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-121` | Ticket imprimé | P1 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-122` | Encaissement espèces | P0 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-123` | Rendu de monnaie | P0 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-124` | Fermeture de caisse | P1 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-125` | Rapprochement caisse | P1 | `BASE-POS` | V1 / support à confirmer |
| `ZIL-126` | Historique POS | P1 | `BASE-POS` | V1 / support à confirmer |

### D2 — POS / Opérations de magasin
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-127` | Scan produit | P0 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-128` | Recherche rapide article | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-129` | Vente rapide | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-130` | Ajout manuel article | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-131` | Annulation de ligne | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-132` | Réduction / remise | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-133` | Reçu interne ou document fiscal sous condition | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-134` | QR interne | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-135` | Reprise / retour | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |
| `ZIL-136` | Incident de caisse | P1 | `BASE-POS-TOOLS` | V1 / support à confirmer |

### E1 — Métiers / Restaurants et pizzerias
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-137` | Commander un repas | P0 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-138` | Restaurant disponible | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-139` | Menu / carte | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-140` | Plat prêt | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-141` | Livraison repas | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-142` | Réservation de table | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-143` | Pizza | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-144` | Chocolat / vente au gramme | P1 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-145` | Boisson / café | P2 | `BASE-FOOD` | V1 / support à confirmer |
| `ZIL-146` | Cuisine en préparation | P1 | `BASE-FOOD` | V1 / support à confirmer |

### E2 — Métiers / Beauté et coiffure
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-147` | Réserver un service beauté | P0 | `BASE-BEAUTY` | V1 / support à confirmer |
| `ZIL-148` | Coiffure en cours | P1 | `BASE-BEAUTY` | V1 / support à confirmer |
| `ZIL-149` | Salon disponible | P1 | `BASE-BEAUTY` | V1 / support à confirmer |
| `ZIL-150` | Beauté / esthétique | P1 | `BASE-BEAUTY` | V1 / support à confirmer |
| `ZIL-151` | Onglerie / soin | P2 | `BASE-BEAUTY` | V1 / support à confirmer |
| `ZIL-152` | Rendez-vous confirmé | P1 | `BASE-BEAUTY` | V1 / support à confirmer |
| `ZIL-153` | Attente en salon | P2 | `BASE-BEAUTY` | V1 / support à confirmer |

### E3 — Métiers / Réparation et maintenance
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-154` | Réparation smartphone | P0 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-155` | Diagnostic appareil | P1 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-156` | Technicien au travail | P1 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-157` | Appareil prêt | P1 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-158` | Appareil en attente | P1 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-159` | Outil / atelier | P1 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-160` | Réparation validée | P1 | `BASE-REPAIR` | V1 / support à confirmer |
| `ZIL-161` | Remise au client | P1 | `BASE-REPAIR` | V1 / support à confirmer |

### E4 — Métiers / Meubles et maison
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-162` | Mobilier en vitrine | P1 | `BASE-FURNITURE` | V1 / support à confirmer |
| `ZIL-163` | Consultation d'un meuble | P1 | `BASE-FURNITURE` | V1 / support à confirmer |
| `ZIL-164` | Commande de meuble | P1 | `BASE-FURNITURE` | V1 / support à confirmer |
| `ZIL-165` | Livraison meuble | P1 | `BASE-FURNITURE` | V1 / support à confirmer |
| `ZIL-166` | Catalogue maison | P2 | `BASE-FURNITURE` | V1 / support à confirmer |
| `ZIL-167` | Décoration intérieure | P2 | `BASE-FURNITURE` | V1 / support à confirmer |
| `ZIL-168` | Article volumineux | P2 | `BASE-FURNITURE` | V1 / support à confirmer |

### E5 — Métiers / Pharmacie autorisée
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-169` | Recherche de produit de santé autorisé | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |
| `ZIL-170` | Pharmacie disponible | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |
| `ZIL-171` | Produit de santé autorisé | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |
| `ZIL-172` | Conseil pharmacie non médical | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |
| `ZIL-173` | Commande pharmacie autorisée | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |
| `ZIL-174` | Disponibilité confirmée | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |
| `ZIL-175` | Restrictions / sécurité | P1 | `BASE-PHARMACY` | V1 sous conditions / validation |

### E6 — Métiers / Services généraux
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-176` | Réserver un service | P2 | `BASE-SERVICES` | V1 / support à confirmer |
| `ZIL-177` | Prestation en cours | P1 | `BASE-SERVICES` | V1 / support à confirmer |
| `ZIL-178` | Service terminé | P1 | `BASE-SERVICES` | V1 / support à confirmer |
| `ZIL-179` | Prestataire disponible | P1 | `BASE-SERVICES` | V1 / support à confirmer |
| `ZIL-180` | Service professionnel | P1 | `BASE-SERVICES` | V1 / support à confirmer |
| `ZIL-181` | Demande envoyée | P1 | `BASE-SERVICES` | V1 / support à confirmer |
| `ZIL-182` | Service validé | P2 | `BASE-SERVICES` | V1 / support à confirmer |

### E7 — Métiers / Vente au poids
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-183` | Pesée produit | P0 | `BASE-WEIGHT` | V1 / support à confirmer |
| `ZIL-184` | Choix de grammage | P1 | `BASE-WEIGHT` | V1 / support à confirmer |
| `ZIL-185` | Sachet / emballage | P1 | `BASE-WEIGHT` | V1 / support à confirmer |
| `ZIL-186` | Produit prêt à l'achat | P1 | `BASE-WEIGHT` | V1 / support à confirmer |
| `ZIL-187` | Prix calculé par poids | P1 | `BASE-WEIGHT` | V1 / support à confirmer |

### F — Discovery / Mall / Découverte multi-marchands
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-188` | Explorer les univers Zamurek | P1 | `BASE-VENUE` | V1 / support à confirmer |
| `ZIL-189` | Parcourir plusieurs boutiques | P1 | `BASE-VENUE` | V1 / support à confirmer |
| `ZIL-190` | Recommandations personnalisées | P3 | `BASE-VENUE` | Hors V1 (candidat futur) |
| `ZIL-191` | Sélection du moment | P1 | `BASE-VENUE` | V1 sous conditions / validation |
| `ZIL-192` | Promotions du mall | P1 | `BASE-VENUE` | V1 sous conditions / validation |
| `ZIL-193` | Nouvelles boutiques | P1 | `BASE-VENUE` | V1 sous conditions / validation |
| `ZIL-194` | Parcours de découverte | P1 | `BASE-VENUE` | V1 sous conditions / validation |
| `ZIL-195` | Favoris multi-boutiques | P1 | `BASE-VENUE` | V1 sous conditions / validation |
| `ZIL-196` | Collections et sélections | P2 | `BASE-VENUE` | V1 sous conditions / validation |
| `ZIL-197` | Expérience unifiée, tout au même endroit | P1 | `BASE-VENUE` | V1 / support à confirmer |

### G1 — IA / Assistant acheteur
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-198` | Assistant de recommandation | P0 | `BASE-AI-SHOP` | V1 sous conditions / validation |
| `ZIL-199` | Suggestions personnalisées | P1 | `BASE-AI-SHOP` | V1 sous conditions / validation |
| `ZIL-200` | Aide à trouver un produit | P3 | `BASE-AI-SHOP` | Hors V1 (candidat futur) |
| `ZIL-201` | Comparaison assistée | P1 | `BASE-AI-SHOP` | V1 sous conditions / validation |
| `ZIL-202` | Conseiller d'achat | P1 | `BASE-AI-SHOP` | V1 sous conditions / validation |

### G2 — IA / Assistant marchand
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-203` | Aide à la création de catalogue | P0 | `BASE-AI-MERCHANT` | V1 / support à confirmer |
| `ZIL-204` | Suggestion de mise en avant | P1 | `BASE-AI-MERCHANT` | V1 / support à confirmer |
| `ZIL-205` | Aide à la gestion des commandes | P1 | `BASE-AI-MERCHANT` | V1 sous conditions / validation |
| `ZIL-206` | Assistant marketing marchand | P2 | `BASE-AI-MERCHANT` | V1 sous conditions / validation |
| `ZIL-207` | Conseils d'optimisation | P1 | `BASE-AI-MERCHANT` | V1 sous conditions / validation |

### G3 — IA / Assistant opérateur
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-208` | Assistant de supervision | P2 | `BASE-AI-OPS` | V1 / support à confirmer |
| `ZIL-209` | Résumé des activités | P1 | `BASE-AI-OPS` | V1 / support à confirmer |
| `ZIL-210` | Alerte intelligente | P1 | `BASE-AI-OPS` | V1 sous conditions / validation |
| `ZIL-211` | Analyse automatique | P1 | `BASE-AI-OPS` | V1 sous conditions / validation |
| `ZIL-212` | Aide à la décision | P2 | `BASE-AI-OPS` | V1 sous conditions / validation |

### G4 — IA / Conversation et assistance
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-213` | Support intelligent | P1 | `BASE-AI-CHAT` | V1 / support à confirmer |
| `ZIL-214` | Discussion assistant-client | P1 | `BASE-AI-CHAT` | V1 / support à confirmer |
| `ZIL-215` | Discussion assistant-marchand | P1 | `BASE-AI-CHAT` | V1 / support à confirmer |
| `ZIL-216` | Recherche assistée | P1 | `BASE-AI-CHAT` | V1 / support à confirmer |
| `ZIL-217` | Notification intelligente | P1 | `BASE-AI-CHAT` | V1 sous conditions / validation |

### H — Sécurité et confiance / Accès et permissions
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-218` | Connexion sécurisée | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-219` | Création de mot de passe | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-220` | Vérification du compte | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-221` | Compte protégé | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-222` | Données sécurisées | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-223` | Autorisation refusée | P2 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-224` | Vérification identité | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-225` | Session expirée | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-226` | Validation de permissions | P1 | `BASE-TRUST` | V1 / support à confirmer |
| `ZIL-227` | Appareil autorisé | P1 | `BASE-TRUST` | V1 / support à confirmer |

### I — Onboarding / Premiers pas et tutoriels
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-228` | Bienvenue utilisateur | P0 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-229` | Bienvenue marchand | P1 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-230` | Comment acheter sur Zamurek | P1 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-231` | Comment vendre sur Zamurek | P1 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-232` | Comment suivre une commande | P1 | `BASE-ONBOARDING` | V1 sous conditions / validation |
| `ZIL-233` | Comment gérer sa boutique | P1 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-234` | Comment utiliser le POS | P0 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-235` | Découverte des univers | P1 | `BASE-ONBOARDING` | V1 / support à confirmer |
| `ZIL-236` | Personnalisation de l'expérience | P2 | `BASE-ONBOARDING` | V1 sous conditions / validation |
| `ZIL-237` | Premiers pas avec l'assistant IA | P1 | `BASE-ONBOARDING` | V1 / support à confirmer |

### J — Communication / Notifications et retours
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-238` | Nouvelle notification | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-239` | Promotion reçue | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-240` | Message du marchand | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-241` | Commande mise à jour | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-242` | Paiement confirmé | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-243` | Réservation rappelée | P1 | `BASE-NOTIFY` | V1 sous conditions / validation |
| `ZIL-244` | Alerte importante | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-245` | Message d'assistance | P1 | `BASE-NOTIFY` | V1 / support à confirmer |
| `ZIL-246` | Fidélité / récompense avancée | P3 | `BASE-NOTIFY` | Hors V1 (candidat futur) |

### K — Marketing / Institutionnel et acquisition
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-247` | Zamurek comme mall digital | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-248` | Tout un univers, une seule destination | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-249` | Commerce local connecté | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-250` | Multi-activité | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-251` | Marchands et clients reliés | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-252` | Expérience omnicanale | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-253` | POS + commerce digital | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-254` | Assistant IA au cœur du système | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-255` | Croissance des commerçants | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |
| `ZIL-256` | Confiance et proximité | P2 | `BASE-EDITORIAL` | Communication éditoriale (hors gate fonctionnel) |

### L — Opérateur / Back-office privé
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-257` | Supervision globale | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-258` | Tableau de bord opérateur | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-259` | Gestion des établissements | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-260` | Gestion des permissions | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-261` | Monitoring des activités | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-262` | Alertes opérationnelles | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-263` | Vérification des flux | P1 | `BASE-OPERATOR` | V1 sous conditions / validation |
| `ZIL-264` | Contrôle des incidents | P1 | `BASE-OPERATOR` | V1 / support à confirmer |
| `ZIL-265` | Vue réseau marchands / services | P1 | `BASE-OPERATOR` | V1 / support à confirmer |

### M — Utilitaires / Assistance et systèmes
| ID | Illustration à produire | Priorité | Base | Statut V1 |
|---|---|---|---|---|
| `ZIL-266` | Support / aide | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-267` | Contact / assistance | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-268` | FAQ / centre d'aide | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-269` | Mise à jour disponible | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-270` | Synchronisation en cas de déconnexion | P2 | `BASE-UTILITY` | V1 sous conditions / validation |
| `ZIL-271` | Appareil connecté | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-272` | Appareil non connecté | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-273` | Export / impression | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-274` | Historique | P1 | `BASE-UTILITY` | V1 / support à confirmer |
| `ZIL-275` | Sauvegarde réussie | P1 | `BASE-UTILITY` | V1 / support à confirmer |


## Livrables attendus par illustration acceptée

- `master.svg` multicouche structuré (ou un autre format vectoriel natif quand nécessaire, documenté).
- `static.svg` optimisé pour usage final ; `motion.svg`/CSS/JS uniquement si mouvement justifié.
- Variantes jour/nuit testées, avec le même repère visuel.
- `preview-light.png`, `preview-dark.png` et une capture à petite taille.
- Source de licence avec mentions requises si dérivé d’un asset tiers ; note de modifications et validation.

## Séquençage de l’exécution

| Lot | Contenu | Porte de sortie |
|---|---|---|
| L0 — Fondations | 1 à 3 personnages maîtres, poses, mains, objets, conventions SVG, tests d’intégration | Direction créative approuvée sur 3 illustrations pilotes |
| L1 — P0 | États essentiels, découverte, commande, compte, POS, principales verticales, IA | 36 demandes P0 traitées par réutilisation intelligente et inspection visuelle |
| L2 — P1 | Parcours métier et états secondaires | Couverture UX démontrée et duplications maîtrisées |
| L3 — P2/P3 | Variations longues, éditorial, nouveautés hors V1 | Choix explicite selon besoin produit et licence |
| L4 — Handoff | Exports, animation, intégration, contrats de fichiers et documentation | Contrôles statiques + UI réel + reduced-motion |

## Limites et sources

- Le dépôt officiel déclare les 43 capacités V1 et indique qu’elles ne sont **pas encore implémentées** au stade documenté. Ne pas assimiler icône ou illustration à fonctionnalité.

- Les recommandations de composition, de priorité et de nombre de bases sont des décisions de **planification créative**, non des exigences fournies par les bibliothèques externes.

- Le projet doit valider les licences de toute ressource externe réellement téléchargée *au moment de son incorporation*.

- https://github.com/jupi-z/ZAMUREK/blob/main/spec/v1/capabilities.json
- https://github.com/jupi-z/ZAMUREK/blob/main/docs/v1/PRODUCT-CHARTER.md
- https://github.com/jupi-z/ZAMUREK/blob/main/docs/v1/RELEASE-GATES.md
- https://github.com/jupi-z/ZAMUREK/blob/main/packages/branding/README.md
- https://github.com/jupi-z/ZAMUREK/blob/main/packages/iconography/README.md
- https://www.humaaans.com/ (CC0 indiqué par l’éditeur)
- https://github.com/ira-design/ira-illustrations/blob/master/LICENSE.md (MIT, avis à conserver)
- https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/animate (mouvement et accessibilité)