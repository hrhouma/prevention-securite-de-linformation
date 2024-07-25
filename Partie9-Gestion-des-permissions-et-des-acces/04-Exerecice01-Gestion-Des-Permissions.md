# Exercice Pratique sur Kali Linux

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
