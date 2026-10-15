# ADR-0003 — React pour l'UI, Kotlin pour le cœur Android

**Statut : adopté | Date : 2026-10-15**

## Décision
WebView embarquée via Capacitor ; React/HTML/CSS pour présentation, navigation et interactions visuelles ; Kotlin pour réseau/API, données persistantes, sessions, traitements en arrière-plan et intégrations Android. Bridge typé et restreint. Le backend conserve la logique de prix, commandes et droits faisant autorité.

## Alternatives
Tout React/JS : plus simple, mais contraire à l'objectif de confier opérations hors UI au natif. Tout Compose : rendu natif, mais perd l'interface web recherchée.

## Conséquences
Deux environnements à tester ; coût du pont et de la WebView non supprimé ; ne pas traverser le bridge pour chaque frame. Le navigateur de développement utilise des adaptateurs mock, jamais une logique métier parallèle silencieuse.

## Révision
Benchmarks Android et complexité de maintenance significativement défavorables.

