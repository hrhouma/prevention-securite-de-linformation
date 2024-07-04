## Installation de Metasploitable

### Introduction

Les tests d'intrusion doivent être réalisés dans un cadre légal pour éviter tout risque juridique. Pour s'entraîner en toute légalité, il est recommandé d'utiliser des systèmes d'exploitation vulnérables hébergés localement. Metasploitable2 et Metasploitable3 sont deux environnements populaires conçus spécifiquement pour cet usage.

### Metasploitable2

Metasploitable2 est une machine virtuelle Linux vulnérable maintenue par Rapid7. Elle est disponible [ici](https://metasploit.help.rapid7.com/docs/metasploitable-2). Voici comment l'installer :

#### Étapes d'Installation de Metasploitable2

1. **Téléchargez Metasploitable2** :
   - Rendez-vous sur la page de téléchargement de Metasploitable2 et téléchargez l'image.

2. **Installez VMware ou VirtualBox** :
   - Si vous ne l'avez pas déjà fait, téléchargez et installez [VMware](https://www.vmware.com/products/workstation-player.html) ou [VirtualBox](https://www.virtualbox.org/).

3. **Importez la machine virtuelle** :
   - Ouvrez VMware ou VirtualBox et importez l'image de Metasploitable2 téléchargée.

4. **Démarrez la machine virtuelle** :
   - Après l'importation, démarrez la machine virtuelle et connectez-vous avec les identifiants par défaut (utilisateur : `msfadmin`, mot de passe : `msfadmin`).

### Metasploitable3

Metasploitable3 est une version plus avancée, offrant à la fois des environnements Linux et Windows. Elle nécessite l'utilisation de Packer et Vagrant pour la construction des images.

#### Prérequis

- **Git**
- **Packer**
- **Vagrant**
- **VirtualBox**

#### Étapes d'Installation de Metasploitable3 sous Linux

1. **Installation de Git** :
   ```bash
   sudo apt install git -y
   ```

2. **Installation de Packer** :
   ```bash
   sudo apt install packer -y
   ```

3. **Installation de Vagrant** :
   - Téléchargez la dernière version de Vagrant :
     ```bash
     wget https://releases.hashicorp.com/vagrant/2.2.4/vagrant_2.2.4_x86_64.deb
     sudo dpkg -i vagrant_2.2.4_x86_64.deb
     ```
   - Installez les plugins nécessaires :
     ```bash
     vagrant plugin install vagrant-reload
     ```

4. **Téléchargement de Metasploitable3** :
   ```bash
   git clone https://github.com/rapid7/metasploitable3.git
   cd metasploitable3
   ```

5. **Création de la Machine Virtuelle** :
   ```bash
   vagrant box add jbarnett-r7/metasploitable3-win2k8
   ```

6. **Choix du Provider** :
   - Choisissez `1` pour `virtualbox`.

7. **Vérification du Téléchargement** :
   ```bash
   vagrant box list
   ```

8. **Initialisation et Démarrage de Metasploitable3** :
   ```bash
   vagrant init && vagrant up
   ```

9. **Connexion à la Machine Virtuelle** :
   - Utilisez les identifiants par défaut (utilisateur : `vagrant`, mot de passe : `vagrant`).

### Machines Virtuelles Jetables Windows

Pour les tests d'exploitation de clients, vous pouvez obtenir des machines Windows jetables directement depuis le site de Microsoft. Ces machines virtuelles sont gratuites pour 90 jours et disponibles [ici](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).

### Conclusion

L'utilisation de Metasploitable2 et Metasploitable3 permet de s'entraîner en toute légalité sur des environnements vulnérables. Ces machines virtuelles sont idéales pour améliorer vos compétences en tests d'intrusion sans risquer de compromettre des systèmes réels. En suivant les étapes d'installation détaillées ci-dessus, vous serez en mesure de configurer ces environnements rapidement et facilement.
