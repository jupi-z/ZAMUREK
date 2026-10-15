# Storefront Android white-label (prévu ; non implémenté)

Base d'application personnalisable : **React/Vite/TypeScript** pour l'affichage exclusivement, **Capacitor** comme bridge, **Kotlin** pour réseau, cache, session et intégrations Android.

## À créer durant G1/G3
- Répertoire React src/ : screens, components, theme, typed bridge seulement.
- Projet Android généré par Capacitor et commité après son initialisation réelle.
- Plugin Kotlin local Storefront avec contrats prédéfinis ; repositories, Retrofit/OkHttp, Room, coroutines.
- Configuration canal / branding injectée au build, aucune clé serveur.
- Deux flavors de démonstration en staging avec tenants A et B.

**Important** : aucun projet Android Gradle/APK utilisable n'existe encore.

Voir [ANDROID](../../docs/architecture/ANDROID.md) et [WHITE-LABEL](../../docs/architecture/WHITE-LABEL.md).

