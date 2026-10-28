# ZAMUREK — Figma Design System & UI handoff V1

**Statut :** fondations et composants Figma partiellement livrés; écrans applicatifs à concevoir. Ce fichier est un contrat de conception, **pas un logiciel opérationnel**.

**Fichier de travail Figma :** https://www.figma.com/design/Q5VQfVbvjmRaqFIhHGjVwQ  
**Référence dépôt :** `packages/branding/` (15 SVG de contours, tokens CSS/JSON et provenance documentée).  
**Contexte :** V1 Zamurek omnicanale, 43 capacités obligatoires, backend transactionnel commun Monarque Connect; ne pas créer un second backend ni confondre maquettes avec fonctionnalités exécutées.

## 1. Décisions visuelles bloquantes

- Logo : symbole conservé dans sa forme approuvée + logotype Zamurek épais. `Z/mure` vert, `a` orange, `k` magenta. Ne pas redessiner, fusionner ou réinterpréter le symbole.
- Tricolore : forêt `#005C45`, orange `#FF8A1E`, magenta `#D21868`.
- Mode clair : arrière-plan **majoritairement blanc** `#FFFFFF`, texte `#17251F`, surfaces `#F4F7F5`, bordures `#E6EBE8`.
- Mode sombre : arrière-plan **majoritairement obsidienne** `#111318`, texte `#F6F7F8`, surfaces `#202329`, bordures `#30353A`.
- Accent vert d'action sur sombre : `#55D6A6`, uniquement si la lisibilité est confirmée.
- UI : épurée, flat, sans élévations/ombres décoratives. Les panneaux sont réservés aux regroupements fonctionnels, pas à la décoration.
- Typographie d'interface de départ : Poppins (présente sur le brandboard retenu), **à confirmer en revue UX** ; l'artwork du logo ne dépend d'aucune police de substitution.
- Ne pas introduire de noms de vendeurs, chiffres de vente, stocks, prix, horaires ou témoignages inventés comme informations réelles. Les valeurs des maquettes doivent être clairement marquées « données fictives ».

## 2. Pages du fichier Figma

Le fichier Figma Starter admet actuellement 3 pages :
1. `00 · Identity & Foundations` — brandboard, colorimétrie, référence du logo, typographie, thèmes.
2. `01 · Components & UI Kit` — composants maîtres et exemples, états et propriétés.
3. `02 · Application Screens` — les frames mobiles et desktop, regroupés par préfixe et par parcours.

### Fondations déjà créées en Figma

- Collections de variables : `ZAMUREK / Brand`, `ZAMUREK / Theme`, `ZAMUREK / Theme Dark`, `ZAMUREK / Layout`.
- **Contrainte compte Starter** : plusieurs modes sont indisponibles dans une même collection; les thèmes clair/sombre sont séparés en collections jusqu'à adoption d'une solution de publication/alias appropriée.
- Brandboard éditable présent sur la page 00.
- Composants Figma sur la page 01 : boutons à variantes primaire/orange/magenta, champ recherche, catégorie, navigation inférieure; espace de spécimens.
- Les SVG Figma sont des traces des contours du PNG validé, et **non** des masters couleur à dégradés identiques. Ne pas les présenter comme définitifs pour impression.

## 3. Inventaire des écrans à concevoir

### Acheteur Android (React UI embarquée, Kotlin services natifs)

| ID | Frame | Objectif UX | Critères |
|---|---|---|---|
| BUY-01 | Découverte / Accueil | Recherche globale, accès boutiques/restaurants/beauté/services, promotions explicites | thèmes clair et sombre, chargement/vide/erreur |
| BUY-02 | Recherche / Liste | Recherches, filtres par verticale, disponibilité vérifiable | aucun résultat inventé |
| BUY-03 | Boutique / Détails | Marchand sélectionné, modes livraison/retrait, produit, variantes et unité | frontières multi-marchands claires |
| BUY-04 | Panier et commande | Un seul vendeur par commande, devise USD / affichage CDF basé sur cotation autorisée | ne jamais présenter un prix mock comme prix serveur confirmé |
| BUY-05 | Auth / Compte | Inscription e-mail pour achats, parcours connexion et réinitialisation | compte client ≠ rôle staff |
| BUY-06 | Suivi commande | Liste, détail, statuts explicitement attribués au Core | états de panne / données inconnues |

### Marchand Android + Windows POS

| ID | Frame | Objectif UX | Critères |
|---|---|---|---|
| MER-01 | Sélection établissement | Accès à organisation / établissement autorisé | séparation org A/B et établissement E1/E2 |
| MER-02 | Catalogue | Produits, poids au gramme, catégories, disponibilité | conversion de quantité décimale exacte en couche Core |
| POS-01 | Vente comptoir | Client de passage sans compte, vendeur authentifié | aucune capture de paiement mock présentée comme réelle |
| POS-02 | Espèces | Total, espèces reçues, monnaie rendue, confirmation | idempotence et caisse Core obligatoires |
| POS-03 | Documents et impression | Reçu, A4, 58/80mm, état imprimante | ne pas affirmer « facture DGI homologuée » |
| MER-03 | Réservations / Activités | Restaurant, salon, interventions spécialisées | états de réservation et conflits clairs |

### Discovery / Mall et opérations

- VEN-01 : liste des marchands publiés par consentement, boutiques indépendantes.
- VEN-02 : pages de mall et espaces de découverte, sans fuite de données de caisse ni de clientèle.
- OPS-01 : console opérateur privée Windows, VPN/MFA; **pas d'admin web public**.

## 4. Composants à compléter dans Figma

- Buttons: primary, secondary, accent, outline, text; états default/pressed/disabled/loading, tailles S/M/L.
- Fields: recherche, e-mail, téléphone, montant, quantité, sélecteur de devises (USD/CDF), unité.
- Layout: header, bottom navigation, desktop sidebar, section heading, dividers.
- Commerce: price + FX info, unit picker, variant selector, stock badge, merchant tile, product row, cart line, order status.
- POS: cashier state, session state, tender, money change, print status, confirmation, pending/failed.
- Feedback: empty, loading, permission denied, disconnected, warning, actionable errors.
- Accessibilité: taille cible tactile, contrastes, navigation clavier Windows, focus visible, labels FR.
- Un composant maître Figma réutilisable pour chaque motif répété; instances dans les écrans.

## 5. Parcours normatifs à dessiner

1. **Acheteur** : découverte → recherche → marchand → détail → panier mono-vendeur → authentification e-mail → récapitulatif → commande (contrat Core réel requis).
2. **POS espèces** : session caissier → catalogue → montant → tender → confirmation transactionnelle Core → impression reçue. Si erreur, ne pas afficher une vente réussie.
3. **Salon** : prestation → employé/ressource → créneau disponible → confirmation → report/annulation.
4. **Restaurants** : carte / modificateurs → panier → commande / préparation → livraison/retrait ou sur place.
5. **Venue** : consentement marchand opt-in → publication → révocation → disparition du listing, sans accès finances.

## 6. Conditions de recette design

- Chaque écran a un ID, un statut de conception, au minimum un mode clair et sombre pour les parcours principaux et des états non-heureux.
- Les textes FR sont la référence initiale; les chaînes sont externalisables (EN ultérieurement si validé).
- Tous les visuels de l'icône viennent du master retenu, jamais d'une reconstitution libre.
- UI n'implique aucune preuve API. Les chemins dépendant de C3–C5 restent maquettes uniquement jusqu'aux contrats et tests Core.
- Figma → dépôt : préserver la trace des composants, tokens, exports autorisés et une revue visuelle. Aucun code transactionnel généré automatiquement depuis la maquette.
- Les maquettes « exemples » ne doivent pas contenir de fausses données présentées comme réelles.

## 7. Dernier état d'exécution et reprise

- Le fichier Figma Design `Q5VQfVbvjmRaqFIhHGjVwQ` a été créé le 28/10/2026.
- Fondations/tokens et brandboard réalisés sur la page 00; composants de base réalisés sur la page 01.
- La création des écrans BUY/MER/POS sur la page 02 **n'est pas faite** : blocage de la limite d'appels Figma MCP pour le plan Starter. La page 02 existe mais reste à compléter.
- Aucune maquette, prototype ou design system « complet » ne doit être revendiqué avant livraison des écrans et contrôle visuel.
- Prochaine intervention Figma : commencer BUY-01 clair/sombre, puis BUY-02 et MER-01 / POS-01, valider chaque groupe d'écrans; utiliser les composants existants.
