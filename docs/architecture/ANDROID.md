# Clients Android — React UI, Kotlin Core, Capacitor

Deux APK : **acheteur** et **marchand** séparés. Aucune UI web hébergée.

React/TypeScript/HTML/CSS = rendu/navigation/état éphémère ; Capacitor bridge typé ; **Kotlin** = HTTP, token e-mail login, cache/Room, permissions système, upload médias, jobs, validation locale UX. **Le backend** garantit montant CDF, conversion taux, devis, commande, auth/tenant.

## Acheteur
Login **e-mail vérifié, aucun SMS**, prix public CDF ; catalogue, panier, quote CDF versionnée, checkout/état commande, profil et annulation. Une préférence de devise future peut rester sauvegardée, mais pas d'affichage USD public RDC sans validation juridique.

## Marchand
Login avec MFA TOTP pour rôles sensibles, prix USD source, taux USD→CDF configurable, frais USD zone, suivi/confirmation paiements directs, staff tenant. Aucun prix client CDF saisi indépendamment.

## Performance
Ne pas franchir le bridge à chaque scroll/frame ; paquets de DTO minimaux, opérations asynchrones Kotlin, mesures cold start/mémoire/jank ; WebView reste un moteur web. Pas de promesse de performances natives pour le DOM.

## Sécurité
WebView local et origine contrôlée, bridge whitelist, refresh secrets hors React, appels TLS, aucun mot de passe/DB credentials dans JS. Acteurs client/tenant vérifiés serveur, tests appareils réels.

Références : [FX](FX-PRICING.md), [auth](AUTH-NO-SMS.md), [réseau](NETWORK-EXPOSURE.md).
