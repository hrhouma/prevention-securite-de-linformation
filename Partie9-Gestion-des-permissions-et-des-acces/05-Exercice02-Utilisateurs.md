### Création et gestion des utilisateurs dans Linux : Ajout aux sudoers

Pour créer des utilisateurs et les ajouter au groupe `sudoers` (qui leur donne des privilèges administratifs), il existe plusieurs méthodes détaillées ci-dessous. **Remarque : La méthode 5 utilisant Ansible n'est pas obligatoire et peut être ignorée par les étudiants.**

# Méthode 1 : Utiliser la ligne de commande

1. **Créer un nouvel utilisateur nommé Albert :**
   ```bash
   sudo adduser albert
   ```

   Cette commande vous demandera de fournir des informations comme le mot de passe, le nom complet, etc.

2. **Ajouter l'utilisateur Albert au groupe sudo :**
   ```bash
   sudo usermod -aG sudo albert
   ```

   `-aG` signifie "append" (ajouter) et "group" (groupe). Cette commande ajoute l'utilisateur au groupe sudo sans retirer ses autres appartenances aux groupes.

3. **Vérifier qu'Albert est bien dans le groupe sudo :**
   ```bash
   groups albert
   ```

   Cette commande affichera les groupes auxquels appartient Albert, y compris `sudo` s'il a été ajouté correctement.

# Méthode 2 : Modifier directement le fichier sudoers

1. **Ouvrir le fichier sudoers avec visudo :**
   ```bash
   sudo visudo
   ```

   `visudo` est l'éditeur recommandé car il vérifie les erreurs de syntaxe.

2. **Ajouter Albert directement dans le fichier sudoers :**
   Recherchez la ligne qui commence par `%sudo` et ajoutez une ligne pour Albert juste en dessous :
   ```bash
   albert ALL=(ALL:ALL) ALL
   ```

   Cela permet à `albert` d'exécuter toutes les commandes en tant que n'importe quel utilisateur ou groupe.

# Méthode 3 : Utiliser des groupes spécifiques pour les privilèges sudo

1. **Créer un groupe spécifique pour sudo :**
   ```bash
   sudo groupadd admin
   ```

2. **Ajouter Albert au groupe admin :**
   ```bash
   sudo usermod -aG admin albert
   ```

3. **Modifier le fichier sudoers pour inclure le groupe admin :**
   Ouvrez le fichier sudoers :
   ```bash
   sudo visudo
   ```

   Et ajoutez la ligne suivante :
   ```bash
   %admin ALL=(ALL) ALL
   ```

# Méthode 4 (À IGNORER): Utiliser des scripts pour automatiser le processus

1. **Créer un script shell pour ajouter des utilisateurs :**
   ```bash
   #!/bin/bash

   # Vérifier si le script est exécuté en tant que root
   if [ "$(id -u)" -ne 0 ]; then
       echo "Ce script doit être exécuté avec les privilèges root."
       exit 1
   fi

   # Lire le nom de l'utilisateur
   read -p "Entrez le nom de l'utilisateur : " username

   # Créer l'utilisateur
   adduser $username

   # Ajouter l'utilisateur au groupe sudo
   usermod -aG sudo $username

   echo "L'utilisateur $username a été créé et ajouté au groupe sudo."
   ```

2. **Rendre le script exécutable et l'exécuter :**
   ```bash
   chmod +x create_sudo_user.sh
   sudo ./create_sudo_user.sh
   ```

#### Méthode 5 : Utiliser Ansible pour gérer les utilisateurs (Ignoré pour les étudiants)

Ansible est un outil d'automatisation qui peut gérer les configurations à grande échelle. Cette méthode peut être ignorée par les étudiants.

1. **Installer Ansible :**
   ```bash
   sudo apt update
   sudo apt install ansible -y
   ```

2. **Créer un playbook Ansible pour ajouter un utilisateur sudo :**
   ```yaml
   ---
   - name: Ajouter un utilisateur et l'ajouter au groupe sudo
     hosts: localhost
     become: true
     tasks:
       - name: Ajouter un nouvel utilisateur
         user:
           name: albert
           state: present
           groups: sudo
           append: yes
   ```

3. **Exécuter le playbook Ansible :**
   ```bash
   ansible-playbook ajouter_utilisateur.yml
   ```

# Conclusion

Chaque méthode a ses avantages en fonction du contexte et des besoins spécifiques. Utiliser la ligne de commande est simple et direct, tandis que l'utilisation de scripts permet d'automatiser le processus, ce qui est utile pour gérer un grand nombre d'utilisateurs.
