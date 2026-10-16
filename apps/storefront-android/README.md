# Acheteur Android xShop — G0 non implémenté

React/Vite/TypeScript UI **embarquée**, Capacitor bridge, **Kotlin** réseau/cache/sessions. Compte acheteur obligatoire **e-mail + mot de passe vérifié, zéro SMS**. Catalogue sur boutique, produit USD interne mais **prix public CDF** converti par serveur via taux marchand, panier, quoteId CDF, confirmation checkout et historique authentifié.

Ne jamais convertir prix de manière autoritative dans React ni permettre choix d'affichage USD en RDC sans validation juridique. Aucun secret DB/backend dans APK. APK pilote puis publication par commerçant selon règles Play.

Voir [FX](../../docs/architecture/FX-PRICING.md), [auth sans SMS](../../docs/architecture/AUTH-NO-SMS.md).
