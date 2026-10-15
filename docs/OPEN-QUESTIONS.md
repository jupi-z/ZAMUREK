# Derniers prérequis ouverts — état après arbitrages du 15 octobre 2026

Les **décisions produit V1 ont été fournies** et enregistrées dans [DECISIONS](DECISIONS-VALIDATED-2026-10-15.md). Ne pas rouvrir les anciens choix « guest checkout / web admins / une seule devise / abonnement vs commission / identité dépôt ».

## Bloquants pour lancer G1 (code et tests locaux)
**Aucun arbitrage métier supplémentaire indispensable.** Les choix d'implémentation sont délégués. La V1 ne peut cependant être déclarée finie avant les validations ci-dessous.

## Bloquants AVANT déploiement d'un staging sur le VPS

| ID | Prérequis | Responsable | Statut |
|---|---|---|---|
| B01 | Inventaire du VPS : OS/version, CPU, RAM, stockage, accès DNS/ports et capacités sauvegarde ; séparation test/production | Titulaire du VPS + équipe technique | Informations non fournies |
| B02 | Nom de domaine/sous-domaine pour **API seulement**, DNS/TLS et droits d'usage | Titulaire des domaines | Domaines disponibles, non identifiés |
| B03 | Plan de sauvegarde, restauration ciblée de DB tenant et tests d'isolation sur le VPS | Équipe technique | Tests à réaliser |

Ne **jamais envoyer mot de passe, clé SSH privée, token ou secret** dans les réponses au questionnaire. Les accès doivent être configurés via un moyen sécurisé au moment du déploiement.

## Bloquants AVANT vente publique (G4)

| ID | Prérequis | Motif |
|---|---|---|
| B04 | Fournisseur SMS/OTP vérifié, coût et conditions en RDC, ou révision explicite de la méthode d'authentification | Identité client avec téléphone + vérification avant première commande |
| B05 | Mentions de vente, confidentialité, protection données, taxation/facturation applicables RDC et répartition contractuelle vendeur/xShop | Ne pas inventer une conformité réglementaire |
| B06 | Modèle d'abonnement : **prix mensuel**, échéance, suspension, modalités de règlement, contrat et support | « Abonnement uniquement » validé mais montant non fixé |
| B07 | Identité juridique/compte éditeur de chaque commerçant, droits des marques, signature et règles Google Play | Distribution APK/Play au cas par cas |
| B08 | Choix d'un marchand réel pilote, coordonnées et moyens de paiement commerciaux, zones/frais en CDF/USD | Les fixtures « xShop Atelier » ne sont pas une véritable boutique |
| B09 | RPO/RTO, rétention données, supervision et obligations support adaptées au budget et au risque | Contrat d'exploitation et restauration |
| B10 | Conditions de réception et d'annulation de paiement manuel et éventuels remboursements, par vendeur | Flux commerciaux et légaux |

## Choix techniques délégués, non bloquants G1
- Tauri 2/Rust pour clients Windows ; Kotlin Android, React pour présentation.
- Devises CDF/USD via **prix indépendants** ; aucun change automatique.
- Auth globale téléphone + mot de passe avec OTP à validation externe avant exploitation réelle ; provider non choisi.
- Backend NestJS modulaire, DB tenant, OpenAPI dans Git, aucun frontend hébergé.
- Pilote fictif xShop Atelier à Kolwezi.

## Décision de confidentialité du dépôt
Le dépôt GitHub a été **vérifié privé** pendant la mise à jour. Accès à des collaborateurs uniquement selon permissions ; licence open source non accordée.

## Suite
G1 = implémenter registre tenant, auth/client, migrations multi-DB et contrats ; préparer ensuite appels sur VPS quand B01/B02 sont renseignés. Aucun accès VPS n'a été demandé ni établi.
