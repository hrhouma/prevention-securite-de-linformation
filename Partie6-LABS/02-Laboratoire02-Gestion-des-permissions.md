# Choix de Laboratoire

Chers étudiants, pour notre prochain laboratoire sur la gestion des permissions et des utilisateurs sous Linux, vous avez le choix entre cinq options différentes. Chaque option est conçue pour renforcer vos compétences et votre compréhension de différents aspects de la sécurité et de la gestion des systèmes sous Linux. Veuillez lire attentivement chaque option et choisir celle qui correspond le mieux à vos intérêts et objectifs d'apprentissage.

#### **Option 1: Gestion des Permissions et des Utilisateurs sur Kali Linux et Ubuntu 22.04**
- **Focus**: Utilisation de commandes basiques comme `chmod`, `chown`, `useradd`, et `visudo`.
- **Compétences clés**: Création de fichiers, modification de permissions, gestion de l'accès utilisateur, et sécurisation des privilèges administratifs.

#### **Option 2: Gestion des Permissions sous Linux avec Ubuntu 22.04**
- **Focus**: Processus détaillé de création de l'environnement, création des utilisateurs, et gestion des permissions de fichiers et de répertoires.
- **Compétences clés**: Création de fichiers et répertoires, attribution initiale de permissions, tests interactifs des permissions.

#### **Option 3: Laboratoire Approfondi sur Kali Linux**
- **Focus**: Approche détaillée sur l'utilisation des commandes `chmod`, `chown`, `useradd`, et `usermod`.
- **Compétences clés**: Gestion des permissions de fichiers, création et modification d'utilisateurs, utilisation avancée de la ligne de commande.

#### **Option 4: Création et Gestion des Utilisateurs et Permissions dans Linux**
- **Focus**: Méthodes multiples pour ajouter des utilisateurs au groupe `sudoers`, y compris l'utilisation de scripts et Ansible pour l'automatisation.
- **Compétences clés**: Création d'utilisateurs, ajout aux sudoers via différentes méthodes, scripts d'automatisation.

#### **Option 5: Gestion Pratique des Utilisateurs et Permissions**
- **Focus**: Création de plusieurs utilisateurs et attribution de permissions spécifiques sur des fichiers, dossiers, et scripts.
- **Compétences clés**: Configuration détaillée des ACLs, tests pratiques des permissions, gestion sécurisée des accès.

### Instructions de Sélection
Après avoir évalué les options, veuillez sélectionner celle qui vous intéresse le plus pour le laboratoire. Cette sélection nous aidera à personnaliser les sessions en fonction des intérêts de chacun et à assurer une expérience d'apprentissage optimale. Partagez votre choix avec votre instructeur avant la date prévue pour le laboratoire.

Nous vous encourageons à explorer les options qui vous pousseront à développer de nouvelles compétences et à approfondir votre compréhension de la gestion des systèmes sous Linux.



🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# OPTION 1 
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇

### Exercice Pratique Combiné sur la Gestion des Permissions et des Utilisateurs sur Kali Linux et Ubuntu 22.04

#### Introduction
Cet exercice vous guide à travers les commandes de gestion des permissions et des utilisateurs sur Kali Linux et Ubuntu 22.04. Vous apprendrez à utiliser `chmod`, `chown`, `useradd`, `usermod`, et `visudo` pour gérer les permissions des fichiers, des utilisateurs, et des groupes.

#### Prérequis
- Une machine avec Kali Linux ou Ubuntu 22.04 installé.
- Accès root ou un utilisateur avec des privilèges sudo.

### Partie 1: Gestion des Permissions avec `chmod`

#### a. Créer et gérer un fichier de test
```bash
touch monfichier1.txt
touch monfichier2.txt
touch monfichier3.txt
chmod u+x monfichier1.txt  # Ajoute la permission d'exécution pour l'utilisateur
chmod +x monfichier2.txt   # Ajoute la permission d'exécution pour tous
chmod g+w monfichier3.txt  # Ajoute la permission d'écriture pour le groupe
ls -l monfichier1.txt
ls -l monfichier2.txt
ls -l monfichier3.txt
```
Vous observerez les changements de permissions après chaque commande.

### Partie 2: Gestion des Utilisateurs et Groupes

#### a. Création et gestion de nouveaux utilisateurs
```bash
sudo useradd -m nouvelutilisateur  # Crée un nouvel utilisateur avec un répertoire personnel
ls -l /home                         # Voir le répertoire créé pour cet utilisateur + les permissions accordées
sudo passwd nouvelutilisateur      # Définit un mot de passe pour le nouvel utilisateur
sudo usermod -aG sudo nouvelutilisateur  # Ajoute l'utilisateur au groupe sudo
groups nouvelutilisateur           # Vérifie les groupes de l'utilisateur
```
# application 1 :  Créez un utilisateur avec votre nom et reéxécutez les mêmes commandes ci-haut.
# application 2 :  déconnectez vous de la machine linux et reconnecter avec votre utilisateur + mot de passe.
# application 3 :  déconnectez vous de la machine linux et reconnecter avec l'utilisateur proncipal que vous aviez déjà.

#### b. Manipulation avancée des utilisateurs
```bash
sudo deluser nouvelutilisateur sudo  # Retire l'utilisateur du groupe sudo
sudo deluser --remove-home nouvelutilisateur  # Supprime l'utilisateur et son répertoire personnel
```

# application 4 :  Retirevotre utilisateur du groupe sudo
# application 5 :  Supprimer votre utilisateur et son répertoire personnel, vérifier avec la commande suivante : (ls -l /home) .

### Partie 3: Utilisation de `chown` et `chgrp`

#### a. Changer la propriété d'un fichier
```bash
touch fichierpourchown.txt
sudo chown nouvelutilisateur fichierpourchown.txt  # Change le propriétaire
sudo chgrp sudo fichierpourchown.txt               # Change le groupe
ls -l fichierpourchown.txt
```

### Partie 4: Modification Directe du Fichier Sudoers

#### a. Ajout sécurisé d'un utilisateur au fichier sudoers
```bash
sudo visudo
```
Dans l'éditeur qui s'ouvre, ajoutez la ligne suivante pour donner à `nouvelutilisateur` la possibilité d'exécuter toutes les commandes:
```
nouvelutilisateur ALL=(ALL:ALL) ALL
```
Utilisez `Ctrl+X`, puis `Y` pour enregistrer et quitter si vous utilisez `nano` comme éditeur dans `visudo`.

### Conclusion

Ce laboratoire pratique vous a montré comment gérer efficacement les permissions des fichiers et les utilisateurs sur les systèmes Kali Linux et Ubuntu 22.04. Vous avez appris les commandes essentielles pour la modification des permissions, la gestion des utilisateurs, et la sécurisation de l'accès administratif. Utilisez [Explainshell](https://explainshell.com/) pour des explications détaillées sur les commandes et les options.

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# OPTION 2
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇

### Objectifs du Laboratoire
- Comprendre les bases des permissions sous Linux.
- Créer et gérer des utilisateurs et des groupes.
- Appliquer et modifier les permissions de fichiers et de répertoires.
- Tester les permissions en se connectant avec différents utilisateurs.

### Prérequis
- Un PC avec Ubuntu 22.04 installé.
- Droits d'administrateur sur la machine.

### Étape 1: Création de l'Environnement
1. **Ouverture d'un Terminal**: Demandez aux étudiants d'ouvrir un terminal.
2. **Mise à jour du système**:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

### Étape 2: Création des Utilisateurs
1. **Créer plusieurs utilisateurs**:
   ```bash
   sudo adduser etudiant1
   sudo adduser etudiant2
   ```
   Répétez pour autant d'utilisateurs que nécessaire.

### Étape 3: Création et Gestion des Permissions
1. **Créer un fichier et un répertoire pour tester les permissions**:
   ```bash
   touch fichier_test
   mkdir dossier_test
   ```
2. **Attribuer des permissions initiales**:
   ```bash
   sudo chown etudiant1:etudiant1 fichier_test
   sudo chmod 764 fichier_test
   sudo chown etudiant1:etudiant1 dossier_test
   sudo chmod 775 dossier_test
   ```

### Étape 4: Modification et Vérification des Permissions
1. **Modifier les permissions**:
   ```bash
   sudo chmod 774 fichier_test
   ```
2. **Vérifier les permissions avec un autre utilisateur**:
   - Demandez aux étudiants de se déconnecter et de se reconnecter avec `etudiant2`.
   - Tester l'accès:
     ```bash
     cat fichier_test
     cd dossier_test
     touch test_inside
     ```

### Étape 5: Tableau Récapitulatif des Permissions
Créez un tableau récapitulatif pour que les étudiants puissent suivre les permissions attribuées et les résultats attendus lors des tests:

| Utilisateur  | Fichier / Répertoire | Permissions | Action de Test | Résultat Attendu |
|--------------|----------------------|-------------|----------------|------------------|
| etudiant1    | fichier_test         | 774         | `cat`          | Succès           |
| etudiant2    | fichier_test         | 774         | `cat`          | Permission refusée |
| etudiant1    | dossier_test         | 775         | `touch test`   | Succès           |
| etudiant2    | dossier_test         | 775         | `touch test`   | Succès           |

### Étape 6: Conclusion et Questions de Réflexion
- **Questions pour les étudiants**: Qu'arrive-t-il si on change les permissions en 660 pour `fichier_test` et qu'un des utilisateurs essaie de lire le fichier?
- **Réflexion**: Comment les permissions affectent-elles la sécurité du système?

Ce laboratoire devrait offrir une introduction complète et pratique à la gestion des permissions sous Linux, tout en assurant que les étudiants comprennent chaque étape grâce à des explications détaillées et des tests interactifs.

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# OPTION 3
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇

#### Introduction
Cet exercice vous guidera à travers plusieurs commandes de gestion des permissions et des utilisateurs sur Kali Linux. Vous apprendrez à utiliser `chmod`, `chown`, `useradd`, `usermod`, et d'autres commandes pour gérer les permissions des fichiers et des utilisateurs. Utilisez [Explainshell](https://explainshell.com/) pour obtenir des explications détaillées sur les commandes et les options si quelque chose n'est pas clair.

#### Prérequis
- Une machine avec Kali Linux installé.
- Accès root ou un utilisateur avec des privilèges sudo.

### 1. Les Permissions avec `chmod`

#### a. Créer un fichier de test
```bash
touch monfichier.txt
```
`touch` crée un nouveau fichier vide nommé `monfichier.txt`.

```bash
ls -l monfichier.txt
```
`ls -l` affiche les détails du fichier, y compris les permissions, le propriétaire, et le groupe. Vous verrez quelque chose comme :
```
-rw-r--r-- 1 votreutilisateur votreutilisateur 0 date heure monfichier.txt
```
- `-rw-r--r--` : Indique les permissions du fichier (lecture/écriture pour le propriétaire, lecture seule pour le groupe et les autres).
- `1` : Nombre de liens.
- `votreutilisateur` : Propriétaire du fichier.
- `votreutilisateur` : Groupe du fichier.
- `0` : Taille du fichier (en octets).
- `date heure` : Date et heure de la dernière modification.
- `monfichier.txt` : Nom du fichier.

#### b. Ajouter la permission d'exécution pour l'utilisateur (`u+x`)
```bash
chmod u+x monfichier.txt
```
`chmod u+x` ajoute la permission d'exécution pour l'utilisateur propriétaire du fichier.

```bash
ls -l monfichier.txt
```
Vous verrez maintenant :
```
-rwxr--r-- 1 votreutilisateur votreutilisateur 0 date heure monfichier.txt
```
- `-rwxr--r--` : Le `x` ajouté pour l'utilisateur indique que l'utilisateur peut exécuter le fichier.

#### c. Ajouter la permission d'exécution pour tout le monde (`+x`)
```bash
chmod +x monfichier.txt
```
`chmod +x` ajoute la permission d'exécution pour tout le monde (utilisateur, groupe, et autres).

```bash
ls -l monfichier.txt
```
Vous verrez :
```
-rwxr-xr-x 1 votreutilisateur votreutilisateur 0 date heure monfichier.txt
```
- `-rwxr-xr-x` : Le `x` ajouté pour tous indique que tout le monde peut exécuter le fichier.

#### d. Ajouter les permissions d'écriture pour le groupe (`g+w`)
```bash
chmod g+w monfichier.txt
```
`chmod g+w` ajoute la permission d'écriture pour le groupe.

```bash
ls -l monfichier.txt
```
Vous verrez :
```
-rwxrwxr-x 1 votreutilisateur votreutilisateur 0 date heure monfichier.txt
```
- `-rwxrwxr-x` : Le `w` ajouté pour le groupe indique que les membres du groupe peuvent écrire dans le fichier.

### 2. Gestion des Utilisateurs

#### a. Créer un nouvel utilisateur
```bash
sudo useradd -m nouvelutilisateur
```
- `sudo` : Exécute la commande avec des privilèges administratifs.
- `useradd` : Commande pour ajouter un nouvel utilisateur.
- `-m` : Crée un répertoire personnel pour le nouvel utilisateur.

```bash
sudo passwd nouvelutilisateur
```
- `passwd` : Change le mot de passe de l'utilisateur spécifié.

#### b. Ajouter l'utilisateur au groupe sudo
```bash
sudo usermod -aG sudo nouvelutilisateur
```
- `usermod` : Modifie un utilisateur.
- `-aG` : Ajoute l'utilisateur à un groupe sans supprimer l'utilisateur d'autres groupes.

#### c. Vérifier l'appartenance au groupe sudo
```bash
groups nouvelutilisateur
```
`groups` affiche les groupes auxquels appartient l'utilisateur spécifié.

#### d. Retirer l'utilisateur du groupe sudo
```bash
sudo deluser nouvelutilisateur sudo
```
`deluser` supprime l'utilisateur du groupe spécifié.

#### e. Supprimer l'utilisateur
```bash
sudo deluser --remove-home nouvelutilisateur
```
- `--remove-home` : Supprime le répertoire personnel de l'utilisateur en même temps que l'utilisateur.

### 3. Utilisation de `chown` et `chgrp`

#### a. Créer un fichier de test
```bash
touch fichierpourchown.txt
```
`touch` crée un nouveau fichier vide nommé `fichierpourchown.txt`.

#### b. Changer le propriétaire du fichier
```bash
sudo chown nouvelutilisateur fichierpourchown.txt
```
`chown` change le propriétaire du fichier spécifié.

```bash
ls -l fichierpourchown.txt
```
Vous verrez quelque chose comme :
```
-rw-r--r-- 1 nouvelutilisateur votreutilisateur 0 date heure fichierpourchown.txt
```
- `nouvelutilisateur` : Nouveau propriétaire du fichier.

#### c. Changer le groupe du fichier
```bash
sudo chgrp sudo fichierpourchown.txt
```
`chgrp` change le groupe du fichier spécifié.

```bash
ls -l fichierpourchown.txt
```
Vous verrez :
```
-rw-r--r-- 1 nouvelutilisateur sudo 0 date heure fichierpourchown.txt
```
- `sudo` : Nouveau groupe du fichier.

#### d. Changer à la fois le propriétaire et le groupe
```bash
sudo chown votreutilisateur:sudo fichierpourchown.txt
```
`chown` change le propriétaire et le groupe du fichier spécifié.

```bash
ls -l fichierpourchown.txt
```
Vous verrez :
```
-rw-r--r-- 1 votreutilisateur sudo 0 date heure fichierpourchown.txt
```
- `votreutilisateur:sudo` : Nouveau propriétaire et groupe du fichier.

### Conclusion

Cet exercice vous a montré comment utiliser les commandes de base pour gérer les permissions des fichiers et les utilisateurs sur Kali Linux. Vous avez appris à utiliser `chmod` pour modifier les permissions des fichiers, `chown` et `chgrp` pour changer les propriétaires et les groupes, ainsi que les commandes `useradd`, `usermod`, et `deluser` pour gérer les utilisateurs. Utilisez [Explainshell](https://explainshell.com/) pour des explications détaillées sur les commandes et les options.

Ces compétences sont essentielles pour administrer efficacement un système Linux, en particulier dans un environnement de sécurité comme Kali Linux.

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# OPTION 4
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇

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


-----

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇
# OPTION 5
🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇


### Exercice : Gestion des Utilisateurs et des Permissions

#### Objectif :
Créer plusieurs utilisateurs, leur attribuer des permissions spécifiques sur des fichiers, des dossiers et des scripts.

#### Consignes :
1. **Créer les utilisateurs :**
   - Créez les utilisateurs suivants : `albert`, `bernard`, `claude`, `danielle`.
   - Attribuez un mot de passe à chaque utilisateur.

2. **Attribuer des permissions spécifiques :**
   - Créez les fichiers et dossiers suivants :
     - `/home/shared_data`
     - `/home/shared_data/file1.txt`
     - `/home/shared_data/file2.txt`
     - `/home/shared_data/dossier1`
     - `/home/shared_data/dossier1/script1.sh`
     - `/home/shared_data/dossier1/script2.sh`

3. **Attribuer les permissions :**
   - `albert` doit pouvoir lire et écrire dans `/home/shared_data/file1.txt`, mais seulement lire `/home/shared_data/file2.txt`.
   - `bernard` doit pouvoir lire et écrire dans `/home/shared_data/file2.txt` et exécuter `/home/shared_data/dossier1/script1.sh`.
   - `claude` doit pouvoir lire et écrire dans `/home/shared_data/dossier1` mais ne doit pas pouvoir exécuter les scripts présents dans ce dossier.
   - `danielle` doit avoir tous les droits (lecture, écriture, exécution) sur tous les fichiers et dossiers.

#### Tableau des Permissions

| Utilisateur | Fichier/Dossier                      | Permissions                            |
|-------------|--------------------------------------|----------------------------------------|
| albert      | /home/shared_data/file1.txt          | Lecture, Écriture                      |
| albert      | /home/shared_data/file2.txt          | Lecture                                |
| bernard     | /home/shared_data/file2.txt          | Lecture, Écriture                      |
| bernard     | /home/shared_data/dossier1/script1.sh| Exécution                              |
| claude      | /home/shared_data/dossier1           | Lecture, Écriture                      |
| claude      | /home/shared_data/dossier1/script1.sh| Aucune                                 |
| claude      | /home/shared_data/dossier1/script2.sh| Aucune                                 |
| danielle    | /home/shared_data/file1.txt          | Lecture, Écriture, Exécution           |
| danielle    | /home/shared_data/file2.txt          | Lecture, Écriture, Exécution           |
| danielle    | /home/shared_data/dossier1           | Lecture, Écriture, Exécution           |
| danielle    | /home/shared_data/dossier1/script1.sh| Lecture, Écriture, Exécution           |
| danielle    | /home/shared_data/dossier1/script2.sh| Lecture, Écriture, Exécution           |

#### Instructions pour les Étudiants :

##### Étape 1 : Créer les Utilisateurs

1. **Créer les utilisateurs :**
   ```bash
   sudo adduser albert
   sudo adduser bernard
   sudo adduser claude
   sudo adduser danielle
   ```

##### Étape 2 : Créer les Fichiers et Dossiers

1. **Créer le dossier `shared_data` et ses sous-dossiers et fichiers :**
   ```bash
   sudo mkdir -p /home/shared_data/dossier1
   sudo touch /home/shared_data/file1.txt /home/shared_data/file2.txt
   sudo touch /home/shared_data/dossier1/script1.sh /home/shared_data/dossier1/script2.sh
   sudo chmod +x /home/shared_data/dossier1/script1.sh /home/shared_data/dossier1/script2.sh
   ```

##### Étape 3 : Attribuer les Permissions

1. **Attribuer les permissions à `albert` :**
   ```bash
   sudo setfacl -m u:albert:rw /home/shared_data/file1.txt
   sudo setfacl -m u:albert:r /home/shared_data/file2.txt
   ```

2. **Attribuer les permissions à `bernard` :**
   ```bash
   sudo setfacl -m u:bernard:rw /home/shared_data/file2.txt
   sudo setfacl -m u:bernard:x /home/shared_data/dossier1/script1.sh
   ```

3. **Attribuer les permissions à `claude` :**
   ```bash
   sudo setfacl -m u:claude:rw /home/shared_data/dossier1
   sudo setfacl -x u:claude /home/shared_data/dossier1/script1.sh
   sudo setfacl -x u:claude /home/shared_data/dossier1/script2.sh
   ```

4. **Attribuer les permissions à `danielle` :**
   ```bash
   sudo setfacl -m u:danielle:rwx /home/shared_data/file1.txt
   sudo setfacl -m u:danielle:rwx /home/shared_data/file2.txt
   sudo setfacl -m u:danielle:rwx /home/shared_data/dossier1
   sudo setfacl -m u:danielle:rwx /home/shared_data/dossier1/script1.sh
   sudo setfacl -m u:danielle:rwx /home/shared_data/dossier1/script2.sh
   ```

##### Vérification

Pour vérifier que les permissions ont été correctement attribuées, chaque utilisateur peut exécuter les commandes suivantes :

1. **Vérifier les permissions de `file1.txt` et `file2.txt` :**
   ```bash
   getfacl /home/shared_data/file1.txt
   getfacl /home/shared_data/file2.txt
   ```

2. **Vérifier les permissions des scripts :**
   ```bash
   getfacl /home/shared_data/dossier1/script1.sh
   getfacl /home/shared_data/dossier1/script2.sh
   ```

3. **Tester les accès en se connectant en tant que chaque utilisateur :**
   ```bash
   su - albert
   cat /home/shared_data/file1.txt
   echo "Test" >> /home/shared_data/file1.txt
   cat /home/shared_data/file2.txt

   su - bernard
   echo "Test" >> /home/shared_data/file2.txt
   /home/shared_data/dossier1/script1.sh

   su - claude
   echo "Test" >> /home/shared_data/dossier1
   /home/shared_data/dossier1/script1.sh  # devrait échouer

   su - danielle
   cat /home/shared_data/file1.txt
   echo "Test" >> /home/shared_data/file1.txt
   /home/shared_data/dossier1/script1.sh
   ```

### Conclusion

Cet exercice permet aux étudiants de pratiquer la création d'utilisateurs, l'attribution de permissions spécifiques et la gestion des accès sur un système Kali Linux. Assurez-vous qu'ils comprennent l'importance de chaque étape et de la sécurité dans la gestion des permissions.

