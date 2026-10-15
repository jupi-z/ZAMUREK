# ADR-0001 — Monorepo et backend monolithe modulaire

**Statut : adopté pour conception | Date : 2026-10-15**

## Contexte
Une plateforme commune alimente plusieurs commerçants. Le projet part de zéro ; les microservices compliqueraient orchestration, déploiement et transactions trop tôt.

## Décision
Un monorepo xShop contient backend NestJS modulaire, storefront Android, consoles, contrats, documents et infrastructure. Un seul déploiement logique du backend au départ, modules délimités et interfaces explicites.

## Alternatives
Un dépôt par commerçant : duplication et incompatibilité. Microservices immédiats : complexité disproportionnée sans charge mesurée.

## Conséquences
Déploiement simple, transactions dans une DB tenant, conventions partagées. Attention aux dépendances circulaires et à la croissance du code ; interdire import direct dans les détails internes d'un autre module.

## Révision
Charge ou organisation imposant des frontières opérationnelles prouvées.

