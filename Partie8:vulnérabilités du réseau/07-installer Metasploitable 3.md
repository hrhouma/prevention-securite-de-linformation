# Étapes d'Installation de Metasploitable3 sous Windows avec PowerShell dans WINDOWS

#### 1. Installation de Chocolatey (si pas déjà installé) :

Ouvrez PowerShell en tant qu'administrateur et exécutez la commande suivante pour installer Chocolatey :

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

#### 2. Installation des outils nécessaires :

##### a. Git :

Installez Git via Chocolatey avec la commande suivante :

```powershell
choco install git -y
```

##### b. Packer :

Installez Packer via Chocolatey avec la commande suivante :

```powershell
choco install packer -y
```

##### c. Vagrant :

Téléchargez et installez la dernière version de Vagrant depuis le site officiel : [https://www.vagrantup.com/downloads](https://www.vagrantup.com/downloads).

# Lien pour télécharger VAGRANT
- https://medium.com/@cnivesh/how-to-set-up-vagrant-on-windows-3bc841ea4811
- https://developer.hashicorp.com/vagrant/install?product_intent=vagrant

#### 3. Téléchargement et configuration de Metasploitable3 :

##### a. Clonez le repository Metasploitable3 depuis GitHub :

```powershell
git clone https://github.com/rapid7/metasploitable3.git
cd .\metasploitable3\
```

##### b. Téléchargez l'image Metasploitable3 pour VirtualBox :

Cela peut impliquer de télécharger une image spécifique depuis un lien fourni dans le repository Metasploitable3.

#### 4. Configuration de la machine virtuelle avec Vagrant :

##### a. Ajoutez l'image téléchargée à Vagrant :

```powershell
vagrant box add jbarnett-r7/metasploitable3-win2k8
```

##### b. Initialisez et démarrez la machine virtuelle :

```powershell
vagrant init jbarnett-r7/metasploitable3-win2k8
vagrant up
```

#### 5. Connexion à la machine virtuelle :

Utilisez les identifiants par défaut pour vous connecter à la machine virtuelle :

- **Utilisateur :** vagrant
- **Mot de passe :** vagrant

#### 6. Machines Virtuelles Jetables Windows (facultatif) :

Pour les tests d'exploitation de clients Windows, vous pouvez obtenir des machines virtuelles jetables directement depuis le site de Microsoft. Ces machines virtuelles sont gratuites pour 90 jours et disponibles ici : [https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/).

### Conclusion :

En suivant ces étapes, vous serez en mesure de configurer rapidement et facilement Metasploitable3 sous Windows à l'aide de PowerShell, Git, Packer, Vagrant et VirtualBox. Assurez-vous de suivre les instructions spécifiques dans le repository Metasploitable3 pour obtenir l'image nécessaire et configurer correctement votre environnement de test d'intrusion.

# Résumé
Voici les commandes essentielles pour installer Metasploitable3 sous Windows, présentées dans un format de script avec les commentaires pour chaque commande :

```plaintext
# Installer Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Installer Git via Chocolatey
choco install git -y

# Télécharger et installer l'exécutable de Vagrant
https://www.vagrantup.com/
# Installer Packer via Chocolatey
choco install packer -y

# Cloner le repository Metasploitable3
git clone https://github.com/rapid7/metasploitable3.git
cd .\metasploitable3\

# Ajouter l'image à Vagrant
vagrant box add jbarnett-r7/metasploitable3-win2k8

# Initialiser et démarrer la VM
vagrant init jbarnett-r7/metasploitable3-win2k8
vagrant up

# Connexion à la machine virtuelle avec les identifiants par défaut
# Utilisateur : vagrant
# Mot de passe : vagrant
```
