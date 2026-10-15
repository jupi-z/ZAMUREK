# ADR-0010 — Contrat API versionné et applications anciennes

**Statut : adopté | Date : 2026-10-15**

## Décision
API /v1 exposée par OpenAPI, revue contractuelle avant code et tests de rétrocompatibilité à chaque release. Une nouvelle marketplace ou un nouvel appId ne doit pas casser une application propriétaire déjà installée.

## Alternatives
Modifier librement la forme des réponses ; vite mais casse les vieilles versions d'APK.

## Conséquences
Maintenance de variantes de schéma à court terme, télémétrie des clients, dépréciation annoncée. La durée de support exacte dépend des usages et reste ouverte.

## Révision
Politique de versions après première mise en production.

