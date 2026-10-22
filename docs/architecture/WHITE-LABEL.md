# ZAMUREK — identités commerciales et canaux installables

ZAMUREK peut générer **une APK acheteur personnalisée par commerçant**, ainsi qu'une APK générale `ZAMUREK Discover` incluant une vue lieu/centre commercial autorisé. L'identité LaJoie Mall n'est **pas** présumée autorisée : pas d'utilisation sans contrat/licence de marque.

Chaque canal possède package ID/signature/config/thème/assets/translations versionnés, établit la correspondance organisation/établissement/venue via registry, **ne prouve jamais identité ni autorisation à lui seul**.

Clients V1 : Android acheteur marque, Android marchand, Android Discover/venue ; Windows marchand et opérateur via React UI embarquée et Tauri/Rust, Windows opérateur VPN+MFA. Toute interface est installable ; **jamais de frontend HTML hébergé en production**.

Le catalogue/public RDC reçoit prix CDF du backend depuis l'USD/taux marchand ; fonctionnalités par `CapabilityProfile` (retail, weight, food, service, furniture, repair, pharmacy autorisée) avec composantes UI communes et modules spécifiques. Checkout toujours mono-vendeur ; le canal venue ne fusionne pas DB commerciales.

Google Play : publication dépend des comptes éditeurs et des règles sur les applications répétitives ; aucun app store n'est présumé approuvé. Aucun secret backend, clé privée, token privilégié ou DB credentials dans APK/EXE.

Voir [charte V1](../v1/PRODUCT-CHARTER.md), [clients](CLIENTS-DEPLOYMENT.md), [tenancy](TENANCY.md).
