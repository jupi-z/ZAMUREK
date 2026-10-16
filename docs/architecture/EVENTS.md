# Événements et outbox — futur xShop

Pattern transactionnel proposé : événements enregistrés dans outbox de la DB tenant au même commit que la mutation métier, publication asynchronous avec retries et consommateurs idempotents. Aucune garantie exactly-once hors DB ; aucun broker requis en G0.

Types futurs : `product.changed.v1`, `fx_rate.changed.v1` (tenant/version/audit, pas données privées), `order.placed.v1` (sans PII), `order.status_changed.v1`, `tenant.updated.v1`, `subscription.state_changed.v1`.

Important : modification du taux marchand exige invalidation/régénération des projections prix CDF catalogue et des devis non confirmés ; **n'affecte pas anciennes commandes**, qui capturent leur taux et total. Une marketplace future indexe uniquement le catalogue opt-in public par territoire/devises d'affichage légalement autorisées. Retard d'index implique validation serveur au checkout, pas promesse de prix.

Validation avec duplications, retards, crash worker, replay historique, suppression opt-in et séparation tenant.
