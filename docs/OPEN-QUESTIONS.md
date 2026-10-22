# Prérequis externes et décisions en attente — ZAMUREK V1

**Statut au 22 octobre 2026.** La conception complète est déléguée, mais certaines conditions exigent des ressources ou décisions externes ; ne pas simuler qu'elles sont acquises. Les besoins techniques non bloquants doivent être arbitrés par Codex selon docs/v1.

## N'empêche pas de commencer Codex / G1
- **LaJoie Mall** : partenariat seulement envisagé ; on développe `Venue` générique et jeux synthétiques, pas une application de marque utilisant LaJoie Mall sans autorisation.
- **Nom de domaine** : `shuleops.com` disponible comme famille candidate, mais `zamurek-api-test.shuleops.com` et `zamurek-api.shuleops.com` **non créés**.
- **VPS** : existence signalée, capacités inconnues ; développement local et tests via environnement isolé d'abord.
- **Commerçants réels** : utiliser organisations fictives pour toutes les verticales, avec profils et données sans information personnelle.
- **Fournisseur de modèle IA** : préparer `ModelGateway`, modèles interchangeables et simulateurs ; une vraie intégration sera obligatoire au 1.0.0 mais aucun secret/fournisseur n'est présumé.
- **Identité publique de la marque** : ZAMUREK nom retenu ; vérifications propriété des signes/marques/domaine restent nécessaires avant diffusion.

## Bloque mise en service/test VPS à distance
- E01 : fournir **sans secrets** OS, vCPU, RAM, disque, politique sauvegarde, IP/ports, charges existantes sur le VPS.
- E02 : confirmer DNS réel, TLS, sous-domaines non conflictuels.
- E03 : mettre en place isolation staging/prod, WireGuard/VPN plateforme et pare-feu API-only, DB et métriques privées.
- E04 : véritable messagerie SMTP/test de délivrabilité pour inscription et récupération **sans SMS**.

## Bloque vente commerciale / app store / fonctionnalités réglementées
- E05 : confirmation juridique RDC de prix CDF/publicité, fiscalité/facture DGI, règles de change USD→CDF commercial, retours et données numériques.
- E06 : pharmacie : vérifier statut officines, marchandises licites, prescriptions et publicité ; **médicaments réglementés bloqués** jusqu'à une validation écrite.
- E07 : autorisations sanitaires restauration, conditions de service salons, métrologie vente au poids et consentement réparation, selon cas.
- E08 : choix marchands réels, coordonnées et modalités de règlement manuel, conditions de vente, politique support et gestion des données.
- E09 : confirmer contrat BASIC à **7 USD/mois/organisation** incluant établissements de cette organisation, limites d'usage raisonnables, échéances et facturation CDF RDC, sans frais/commissions supplémentaires implicites.
- E10 : validation budget IA et fournisseur réel pour assistants, consentement données, politique opt-in, coûts et latence.
- E11 : identités éditeurs Google Play, droits marques, signature APK/EXE, distribution/avis de conformité.
- E12 : sécurité, sauvegarde/restauration, RPO/RTO, droits des données et support validés.
- E13 : le dépôt est **public**. Avant livrer le code métier propriétaire, décider de le rendre privé ou d'utiliser un repo privé distinct ; GitHub Actions peut tourner en privé.

## V1 / périmètre
Tous les 38 items `REQUIRED` de [capabilities.json](../spec/v1/capabilities.json) restent exigés ; une absence de ressource externe bloque le **release gate**, pas le droit de prétendre que la fonctionnalité est implémentée. Ordonnances pharmaceutiques/protocole médical réglementé, encaissement marketplace/escrow et POS hors ligne sont **hors V1 de façon explicite**.

## Traçabilité
Voir [charte](v1/PRODUCT-CHARTER.md), [gates juridiques](v1/LEGAL-REGULATED-GATES.md), [modèle agentique](v1/AGENTIC-KERNEL.md), [handoff Codex](v1/CODEX-HANDOFF.md).
