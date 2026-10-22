# Distribution V1 — applications clientes installables uniquement

| Client | Runtime | V1 |
|---|---|---|
| APK boutique acheteur | React UI embarquée + Capacitor/Kotlin | REQUIRED |
| APK ZAMUREK Discovery / venue | React UI embarquée + Capacitor/Kotlin | REQUIRED |
| APK marchand | React UI embarquée + Capacitor/Kotlin | REQUIRED |
| Windows marchand EXE/MSI | React UI embarquée + Tauri 2/Rust | REQUIRED |
| Windows opérateur EXE/MSI | React UI embarquée + Tauri 2/Rust, VPN/MFA | REQUIRED |

Le noyau commercial de production s'exécute derrière **API HTTPS seulement**. Aucun web UI, SSR/SPA/PWA, portail opérateur/marchand, Swagger UI public. Les logiciels installables s'appuient sur l'API propriétaire versionnée et n'intègrent pas de secrets serveur. Signature, build, installateur, désinstallation et support compatibilité sont testés.

APK des commerçants sur leur compte éditeur si admissibilité Google Play vérifiée et publication autorisée. Les droits de LaJoie Mall ne sont pas acquis, aucune app ne peut utiliser sa marque avant partenariat/licence.

Sous-domaines candidats `zamurek-api-test.shuleops.com` et `zamurek-api.shuleops.com` non configurés. Console opérateur et services sensibles non exposés publiquement.

Tauri v2 documentation installateurs : https://v2.tauri.app/distribute/windows-installer/ . Voir [contrat](../v1/TECHNICAL-CONTRACTS.md), [gates](../v1/RELEASE-GATES.md).
