# Installer Wiki.js sur Ubuntu 22.04 LTS

Ubuntu 22.04 LTS (iso)
[https://releases.ubuntu.com/22.04/ubuntu-22.04-live-server-amd64.iso](https://releases.ubuntu.com/22.04/ubuntu-22.04-live-server-amd64.iso)

## Introduction

Ce document guide à travers l'installation de Wiki.js, un moteur Wiki moderne et puissant basé sur Node.js, Git, et Markdown. Wiki.js est distribué sous la licence Affero GNU General Public License et supporte plusieurs systèmes de gestion de bases de données.

## Prérequis

- Ubuntu 22.04 LTS
- Accès à un terminal avec droits sudo
- Connexion internet

## Installation de Git

Wiki.js nécessite Git. Pour l'installer sur Ubuntu 22.04, suivez ces étapes :

```bash
sudo apt update
sudo apt install git
```

Vérifiez l'installation :

```bash
git --version
```

## Installation de Node.js

Wiki.js fonctionne avec Node.js. Installez la version LTS de Node.js en utilisant le script de NodeSource :

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Vérifiez les versions installées :

```bash
node -v && npm -v
```

## Installation et configuration de MariaDB

Installez MariaDB pour gérer les données de Wiki.js :

```bash
sudo apt install mariadb-server mariadb-client
sudo systemctl status mariadb
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo systemctl status mariadb
sudo mariadb-secure-installation
```

Connectez-vous à MariaDB et configurez la base de données :

```bash
sudo mysql -u root -p
CREATE DATABASE wikidb;
CREATE USER 'wikidb_user'@'localhost' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON wikidb.* TO 'wikidb_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## Téléchargement et installation de Wiki.js

Créez un utilisateur et un dossier pour Wiki.js :

```bash
sudo adduser --system --group wikijs
sudo mkdir -p /var/www/wikijs
sudo chown wikijs:wikijs /var/www/wikijs
```

Téléchargez et installez Wiki.js :

```bash
sudo su - wikijs
cd /var/www/wikijs
wget https://github.com/Requarks/wiki/releases/latest/download/wiki-js.tar.gz
tar xzf wiki-js.tar.gz
rm wiki-js.tar.gz
cp config.sample.yml config.yml
nano config.yml
```

Configurez le fichier `config.yml` pour utiliser MariaDB.

## Création d'un service systemd

Créez un service pour gérer Wiki.js :

```bash
sudo nano /etc/systemd/system/wikijs.service
```

Ajoutez le contenu suivant :

```ini
[Unit]
Description=Wiki.js
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/node server
Restart=always
User=wikijs
Environment=NODE_ENV=production
WorkingDirectory=/var/www/wikijs

[Install]
WantedBy=multi-user.target
```

Activez et démarrez le service :

```bash
sudo systemctl daemon-reload
sudo systemctl start wikijs
sudo systemctl enable wikijs
systemctl status wikijs
```

## Accès à Wiki.js

Accédez à Wiki.js via votre navigateur en utilisant l'URL : `http://<adresse_IP>:3000`. Suivez les instructions pour créer un compte administrateur et terminer l'installation.

---

Ce guide fournit toutes les étapes nécessaires pour configurer Wiki.js sur une machine Ubuntu 22.04, en utilisant MariaDB comme système de gestion de base de données.
