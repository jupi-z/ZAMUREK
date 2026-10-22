# ZAMUREK — sécurité transversale

**Document actif**, détaillé dans [Threat Model V1](../v1/SECURITY-THREAT-MODEL.md) et [Agentic Fabric](../v1/AGENTIC-KERNEL.md).

1. **Actor + Organization + Establishment + Owner + Capability** vérifiés côté backend à chaque opération, y compris outils IA et venue. DB commerciales par organisation, SQL credentials distincts, niveau établissement autorisé séparément.
2. E-mail et mot de passe vérifiés **sans SMS** pour acheteurs ; MFA TOTP et récupération renforcée pour staff privilégiés et opérateurs ; opérateurs par VPN et RBAC de plateforme.
3. HTTPS public réduit aux besoins clients ; API admin opérateur VPN seulement, aucune DB/métrique/secret/Swagger UI/page HTML public.
4. Prix en USD source, taux USD→CDF marchand versionné ; quote CDF serveur, checksum/TTL/reconfirmation et snapshot historique. Paiements manuels rapprochés par marchand, jamais auto-payés par client.
5. Réservations transactionnelles/locks de ressources, pas de double booking ; réparation seulement après consentement et approbation devis.
6. Pharmacies : bloque produits réglementés non autorisés ; pas d'avis médical par IA ni contournement au moyen de produits génériques.
7. Tool agents contrôlés par **policy indépendante du modèle**, permission locale, approvals hashées et expirantes, redteam injection/exfiltration/mémoire croisée, kill-switch et données minimisées.
8. Secrets manager, builds signés/compatibles, attestation de licences permissives, backups/restauration vérifiés et journaux sans PII.
9. Aucune conformité, audit sécurité ou résultat de tests ne peut être revendiqué avant preuves.

Les clauses légales RDC restent à valider avant ouverture commerciale ; voir [Legal Gates](../v1/LEGAL-REGULATED-GATES.md).
