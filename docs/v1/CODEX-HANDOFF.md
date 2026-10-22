# Instructions de transfert à Codex — ZAMUREK 0.0.0 → 1.0.0

**Mission :** transformer le dépôt `jupi-z/ZAMUREK` en système exécutable propriétaire complet, sans implémenter un MVP limité. Ne pas considérer les documents G0 historiques comme source de vérité lorsqu'ils contredisent `docs/v1/*`.

## Ordre de lecture obligatoire
1. `docs/v1/PRODUCT-CHARTER.md`
2. `docs/v1/CAPABILITY-MATRIX.md`
3. `docs/v1/BUSINESS-WORKFLOWS.md`
4. `docs/v1/DOMAIN-MODEL.md`
5. `docs/v1/AGENTIC-KERNEL.md`
6. `docs/v1/SECURITY-THREAT-MODEL.md`
7. `docs/v1/QUALITY-REQUIREMENTS.md`
8. `docs/v1/RELEASE-GATES.md`
9. `docs/v1/TECHNICAL-CONTRACTS.md`
10. `docs/governance/OPEN-SOURCE-POLICY.md`, `docs/legal/RDC-INITIAL-REVIEW.md`
11. `spec/v1/capabilities.json`, `spec/v1/progress-template.json` et `packages/contracts/openapi/zamurek-v1.yaml`.

## Règles absolues
- **Ne jamais bâtir sur Mercur/Medusa/Saleor/Vendure/ERPNext/Frappe ni autre moteur de commerce**, et ne pas forker de plateforme concurrente ; noyau métier, IA, API et tenancy propriétaires. Autoriser frameworks génériques et packages permissifs audités licence/transitives.
- Serveur de production **API + worker + DB/stockage uniquement** ; aucun frontend HTML/SPA/PWA/SSR ou Swagger UI public. Tous les écrans en clients installables Android et Windows ; React UI embarquée, Kotlin/Rust pour système/sécurité.
- **Même code métier configurable** pour retail, vente au poids, restauration, coiffure, mobilier, réparations et pharmacie non réglementée ; mall/venue indépendant opt-in ; base DB par entreprise et établissements multiples.
- **L'Agentic Fabric est fondatrice dès 0.1.0**, pas un plugin à la fin. Les actions sensibles imposent policy+RBAC+approbation humaine, outils versionnés, mémoire tenant cloisonnée, modèles interchangeables et fallback.
- Prix source USD, taux commerçant versionné, devis backend CDF sur territoire RDC et snapshots ; pas de calcul monétaire float/JS authoritative ; pesée décimale exacte.
- Sans SMS, compte acheteur e-mail vérifié ; rôles privileged MFA et accès opérateur VPN ; paiement manuel direct marchand, SaaS BASIC initial 7 USD/mois selon politique de facturation locale.
- Ne pas supprimer de fonctionnalités `REQUIRED` pour tenir une date. Les produits pharmaceutiques soumis aux règles non vérifiées restent **bloqués**, jamais artificiellement vendables.
- Ne jamais enregistrer de secret, clé de signature, données personnelles ou documents privés dans le GitHub public. Prévenir du risque IP et conseiller dépôt privé avant publication du code métier.
- Aucun déploiement de production, facturation réelle, changement de DNS, connexion VPS, publication magasin ou envoi d'e-mails réels sans autorisation explicite.

## Procédure sans dérive
A. Inspecter branche/CI/README/code, établir un tableau `planned / implemented / tested / blocked / accepted` et créer `docs/implementation/PROGRESS.json` à partir de `spec/v1/progress-template.json`. Marquer 0 pour tout ce qui n'est pas réalisé/testé.
B. Pour chaque sous-étape : comparer le backlog au code, implémenter en petits lots cohérents, modifier tests/migrations/OpenAPI/docs simultanément, exécuter lint/typecheck/unit/integration/E2E pertinentes, lire les échecs, réparer, re-tester, ne passer à la suite qu'avec preuves PASS.
C. Communiquer progression **par sous-étape, par version et globale**, calculée avec poids documentés. Jamais de pourcentages inventés. Reporter les blocages externes séparément du travail logiciel et conserver le gate de release fermé.
D. À chaque jalon, produire `docs/implementation/REPORT-<VERSION>.md` avec commits, modules, tests (commandes/résultats), preuve sur appareils, captures/livraison, risques et décisions ; statut du jalon seulement si aucun P0/P1 non validé.
E. Exécuter en continu jusqu'à la clôture de la portée autorisée et l'épuisement des tâches réalisables. **Ne pas s'arrêter après créer des fichiers vides/squelettes.** Si un service/propriété non accessible empêche une étape, documenter la preuve de blocage, continuer toutes autres tâches indépendantes et ne jamais prétendre avoir terminé la release.
F. Demander à l'utilisateur uniquement les ressources externes réellement bloquantes (DNS, VPS, boîte d'envoi SMTP, contrats, signers, compte éditeur, expert juridique, clés modèle et décisions nouvelles non déléguées). Ne jamais collecter les secrets en clair ou inventer leurs valeurs.
G. Avant tout statut `1.0.0 ready`, comparer chaque ligne du `spec/v1/capabilities.json` à une preuve E2E, test des 7 activités, 3 assistants, mobile + Windows, exactitude FX/poids, isolation DB, restauration, licences, juridique et sécurité.

## Cadence de versions
Voir `docs/v1/RELEASE-GATES.md`. Chaque checkpoint `0.x.0` peut être travaillé sur branche, livré seulement quand preuves complètes ; objectif global `1.0.0` commercialement complet et validé. Les contraintes juridiques restent des conditions réelles et ne peuvent être contournées par un simple feature flag.

## Définition de réussite
- Un collaborateur peut cloner, installer dépendances, lancer registry/PostgreSQL et backend local, compiler les APK Android et EXE/MSI Windows, se connecter au tenant de test et réaliser chaque parcours.
- Documentation API normative fonctionnelle, tests (positifs, négatifs, concurrence, résilience) réellement exécutés ; aucune isolation violée, zéro finding critique.
- Agents IA réels mais cantonnés à leurs scopes, approbations et audit ; le commerce fonctionne si l'IA est désactivée.
- Les engagements externes avant commercialisation ont des validations séparées ; sans elles **code complete n'est pas production ready**.

## Ne pas modifier la politique produit sans décision
Les seules incertitudes restantes doivent être consignées dans `docs/OPEN-QUESTIONS.md` ; privilégier solutions techniques déléguées et sûres, mais ne jamais prétendre conclure un partenariat LaJoie Mall ou obtenir une autorisation pharmaceutique.
