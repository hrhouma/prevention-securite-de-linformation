## Rappel sur l’éthique des tests d'intrusion

### Cadre Légal en France

En France, les tests d'intrusion sont strictement encadrés par la loi pour protéger les systèmes informatiques contre les accès non autorisés. Voici quelques articles du Code pénal pertinents :

#### Article 323-1 du Code pénal :
"Le fait d’accéder ou de se maintenir, frauduleusement, dans tout ou partie d’un STAD (Système de Traitement Automatisé de Données) est puni de deux ans d’emprisonnement et de 30 000 euros d’amende."

Le terme "frauduleusement" est crucial car il différencie un accès légitime d'un accès illégitime. Pour garantir la légitimité d'un test d'intrusion, il est impératif que le client et l'auditeur s'accordent sur :
- Le périmètre à auditer.
- Les actions autorisées et celles à éviter.

### Mandat d'Autorisation

Avant de réaliser un test d'intrusion, un mandat d'autorisation doit être signé par toutes les parties concernées (client, auditeur, et parfois l'hébergeur des applications). Ce document doit préciser :
- Les cibles à auditer.
- Les dates et horaires des tests.
- Les types de tests à effectuer (externes, internes, Wi-Fi, etc.).
- Le niveau de connaissance de l'auditeur (boîte noire, grise, ou blanche).
- Les limites des tests (par exemple, interdiction des tests de déni de service en environnement de production).

Le mandat protège l'auditeur contre les accusations de fraude en établissant un cadre légal pour les tests.

### Autres Articles du Code Pénal

#### Article 323-2 :
"Pénétrer, modifier ou effacer des données dans un STAD sans autorisation est puni de cinq ans d'emprisonnement et de 75 000 euros d'amende."

#### Article 323-3 :
"Le fait d'entraver ou de fausser le fonctionnement d'un STAD est puni de cinq ans d'emprisonnement et de 75 000 euros d'amende."

Ces articles renforcent l'importance d'obtenir une autorisation préalable pour toute action susceptible de modifier ou perturber un système.

### Certification PASSI

L'ANSSI (Agence nationale de la sécurité des systèmes d’information) a mis en place la qualification PASSI (Prestataires d’Audit de la Sécurité des Systèmes d’Information) pour garantir la qualité et l'éthique des audits de sécurité. La certification PASSI impose des critères stricts :
- **Compétences des auditeurs** : Les auditeurs doivent prouver leurs compétences techniques et méthodologiques.
- **Déontologie et Confidentialité** : Les audits doivent être réalisés dans le respect de la confidentialité des données et des informations échangées.
- **Méthodologie** : Utilisation de méthodes standardisées et approuvées pour conduire les audits de sécurité.
- **Recours** : Possibilité pour le client de faire appel auprès de l'ANSSI en cas de non-conformité de l'audit au référentiel PASSI.

### Responsabilité

L'auteur et les éditeurs de ce livre déclinent toute responsabilité si les techniques décrites sont utilisées de manière non éthique ou illégale. Chaque utilisateur est entièrement responsable de ses actions et doit veiller à respecter les lois en vigueur.

---

## Installation native de Metasploit

### Pré-requis Matériels

Pour une utilisation optimale de Metasploit, la configuration matérielle suivante est recommandée :
- **Processeur** : 2 GHz ou plus.
- **Mémoire RAM** : Minimum de 4 Go (8 Go recommandés).
- **Espace disque** : Minimum de 1 Go (50 Go recommandés).

Ces spécifications peuvent évoluer. Consultez la documentation officielle sur le site de Rapid7 pour les mises à jour.

### Désactivation de l'Antivirus et du Pare-feu

Metasploit exploite des vulnérabilités similaires à celles utilisées par des logiciels malveillants, ce qui peut entraîner des blocages par les antivirus et pare-feux. Pour éviter ces problèmes :
- **Désactivez temporairement l'antivirus** ou configurez-le pour ignorer le répertoire Metasploit.
- **Désactivez le pare-feu** ou configurez-le pour permettre les connexions nécessaires aux payloads de Metasploit.

### Droits d'Administration

Des droits d'administration sont nécessaires pour installer Metasploit et ses composants. Assurez-vous de disposer des permissions appropriées.

### Installation sous Linux ou OS X

1. **Téléchargement** :
   Rendez-vous sur le GitHub officiel de Metasploit pour télécharger les nightly installers : [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers).

2. **Exécution du script d'installation** :
    ```bash
    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
    chmod 755 msfinstall
    ./msfinstall
    ```
    Ce script télécharge et installe Metasploit avec toutes ses dépendances.

3. **Lancement de Metasploit** :
    ```bash
    msfconsole
    ```
    Cette commande démarre Metasploit et permet d'accéder à son interface.

### Installation sous Windows

1. **Téléchargement** :
   Téléchargez la dernière version de Metasploit pour Windows depuis le site officiel : [Metasploit Latest](https://windows.metasploit.com/metasploitframework-latest.msi).

2. **Installation** :
   Double-cliquez sur le fichier téléchargé et suivez les instructions de l'assistant d'installation. Assurez-vous de désactiver ou configurer l'antivirus pour ignorer le répertoire d'installation de Metasploit (par défaut, c:\metasploit).

### Utilisation Alternative

Pour éviter de modifier votre configuration système, vous pouvez utiliser Metasploit via des machines virtuelles ou des conteneurs Docker.

#### Systèmes d'Exploitation Orientés Sécurité

Des distributions comme Kali Linux, Parrot Security OS, et BlackArch incluent Metasploit et de nombreux autres outils de sécurité.

- **Kali Linux** : Basée sur Debian, Kali Linux contient plus de 600 outils de sécurité et est supportée par une communauté active. Elle est idéale pour les professionnels de la sécurité.

#### Docker

Docker permet de lancer Metasploit sans installation locale sur le système hôte. Utilisez les commandes suivantes pour démarrer Metasploit via Docker :
```bash
sudo docker run --rm -it -p 443:443 -v ~/.msf4:/root/.msf4 -v /tmp/msf:/tmp/data remnux/metasploit
```

#### Amazon Web Services

Si vous manquez d'espace disque ou de droits d'administration, vous pouvez utiliser une instance EC2 d'Amazon Web Services (AWS) avec une image Kali Linux pré-configurée. Ces instances peuvent être accédées via SSH pour utiliser Metasploit.

### Conclusion

Metasploit est un outil puissant pour les tests de sécurité, mais son utilisation doit toujours respecter les lois et les pratiques éthiques. En suivant les recommandations de Rapid7 et les directives légales, vous pouvez exploiter pleinement les capacités de cet outil tout en respectant le cadre légal.
