## Créer Votre Image Docker Personnalisée

### Introduction

Docker est un outil puissant permettant de créer des environnements isolés et reproductibles pour l'exécution d'applications. Metasploit, une plateforme populaire pour le développement et l'exécution de codes d'exploit, peut facilement être exécutée dans un conteneur Docker. Dans ce cours, nous allons apprendre à créer une image Docker personnalisée contenant Metasploit et d'autres outils spécifiques.

### Exécution d'un Conteneur Metasploit

Pour exécuter un conteneur Metasploit basé sur l'image `remnux/Metasploit`, utilisez la commande suivante :

```bash
sudo docker run --rm -it -p 443:443 -v ~/.msf4:/root/.msf4 -v /tmp/msf:/tmp/data remnux/Metasploit
```

### Création d'une Image Docker Personnalisée

La véritable puissance de Docker réside dans la capacité à créer des images personnalisées contenant les éléments spécifiques dont vous avez besoin. Pour ce faire, vous devez écrire des instructions de construction dans un fichier nommé `Dockerfile`.

### Exemple de Dockerfile

Voici un exemple de `Dockerfile` qui peut être utilisé pour créer une image Docker personnalisée contenant Metasploit et d'autres outils :

```Dockerfile
# Utiliser une image de base Ubuntu
FROM ubuntu:bionic

# Mainteneur de l'image
MAINTAINER Phocean <jc@phocean.net>
ARG DEBIAN_FRONTEND=noninteractive

# Copier les scripts nécessaires
COPY ./scripts/db.sql /tmp/
COPY ./scripts/init.sh /usr/local/bin/init.sh

# Définir le répertoire de travail
WORKDIR /opt

# Installer les dépendances nécessaires
RUN apt-get -qq update \
 && apt-get -yq install --no-install-recommends \
    build-essential \
    patch \
    ruby-bundler \
    ruby-dev \
    zlib1g-dev \
    liblzma-dev \
    git \
    autoconf \
    libpcap-dev \
    libpq-dev \
    libsqlite3-dev \
    postgresql \
    postgresql-contrib \
    postgresql-client \
    ruby \
    python \
    dialog \
    apt-utils \
    nmap \
    nasm

# Configuration de la base de données
COPY ./conf/database.yml /opt/metasploit-framework/config/

# Définir les volumes pour le partage de données
VOLUME /root/.msf4/
VOLUME /tmp/data/

# Définir les locales pour tmux
ENV LANG C.UTF-8
WORKDIR /opt/metasploit-framework

# Définir le script d'initialisation comme commande de démarrage
CMD ["init.sh"]
```

### Construction de l'Image Docker

Une fois le `Dockerfile` prêt, vous pouvez construire l'image Docker localement en utilisant la commande suivante :

```bash
sudo docker build -t phocean/msf .
```

Cette commande crée une image Docker nommée `phocean/msf` à partir des instructions contenues dans le `Dockerfile`.

### Partage de l'Image Docker via DockerHub

Pour faciliter le partage de votre image Docker avec d'autres utilisateurs, vous pouvez la pousser vers DockerHub. Voici les étapes pour ce faire :

1. **Se connecter à DockerHub** :
   ```bash
   docker login
   ```

2. **Pousser l'image vers DockerHub** :
   ```bash
   docker tag phocean/msf your_dockerhub_username/phocean-msf
   docker push your_dockerhub_username/phocean-msf
   ```

Remplacez `your_dockerhub_username` par votre nom d'utilisateur DockerHub.

### Conclusion

En créant une image Docker personnalisée, vous pouvez configurer un environnement Metasploit spécifiquement adapté à vos besoins, avec tous les outils et configurations nécessaires. Cette image peut ensuite être partagée facilement avec d'autres utilisateurs via DockerHub, permettant une collaboration et une réplication aisées de l'environnement de test.
