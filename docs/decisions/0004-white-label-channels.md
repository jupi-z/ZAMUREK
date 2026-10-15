# ADR-0004 — White-label basé sur canaux

**Statut : adopté | Date : 2026-10-15**

## Décision
Le code storefront reste partagé. Un StorefrontChannel attribue à chaque application un identifiant, un tenant et sa configuration publique. L'application comporte package Android, icônes, branding et signature propres ; les secrets restent serveur.

## Alternatives
Fork source par client ; une application universelle imposée dès V1.

## Conséquences
Builds et maintenance plus faciles ; automatisation de signature, release et règles anti-apps répétitives Google Play à anticiper. Déployer de nouveaux canaux sans altérer les précédents.

## Révision
Contraintes de distribution et personnalisation client excessive.

