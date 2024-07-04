## Les Invites de Commandes

Pour utiliser efficacement les outils de sécurité informatique et de test d'intrusion, il est essentiel de comprendre les différentes invites de commandes et leurs significations sur différents systèmes d'exploitation. Voici une description détaillée des principales invites de commandes que vous rencontrerez.

### Unix

#### Exemple d'invites de commandes Unix

```sh
regis@kali:~$
root@kali:/usr/share#
```

Les invites de commandes Unix se présentent généralement sous cette forme. Voici une explication des différents éléments :

1. **Nom d'utilisateur** (regis, root) : Indique l'utilisateur actuellement connecté.
2. **Arobase (@)** : Séparateur entre le nom d'utilisateur et le nom de la machine.
3. **Nom de la machine** (kali) : Nom de l'ordinateur ou du serveur sur lequel l'utilisateur est connecté.
4. **Deux-points (:)** : Séparateur entre le nom de la machine et le répertoire courant.
5. **Répertoire courant** (~, /usr/share) : Le répertoire où l'utilisateur se trouve actuellement. `~` représente le répertoire personnel de l'utilisateur.
6. **Symbole de droits ($, #)** :
   - **$** : L'utilisateur a des droits limités.
   - **#** : L'utilisateur a des droits de superutilisateur (root).

#### Commandes Utiles sous Unix

- **ls** : Lister les fichiers et répertoires dans le répertoire courant.
- **cd** : Changer de répertoire.
- **cp** : Copier des fichiers ou répertoires.
- **mv** : Déplacer ou renommer des fichiers ou répertoires.
- **rm** : Supprimer des fichiers ou répertoires.
- **lsof -i** : Lister les fichiers ouverts par les processus, en particulier les connexions réseau.

### Metasploit

#### Exemple d'invite de commandes Metasploit

```sh
msf6 >
```

L'invite de commandes Metasploit est utilisée pour interagir avec le framework Metasploit. À partir de cette invite, vous pouvez exécuter toutes les commandes disponibles dans Metasploit. Voici quelques commandes utiles :
- **search** : Rechercher des exploits, payloads, etc.
- **use** : Charger un module spécifique.
- **show options** : Afficher les options configurables pour le module chargé.
- **exploit** : Lancer l'attaque.

### Meterpreter

#### Exemple d'invite de commandes Meterpreter

```sh
meterpreter >
```

Meterpreter est une puissante interface de commande qui s'exécute sur la machine cible après une exploitation réussie. À partir de cette invite, vous pouvez exécuter des commandes post-exploitation pour manipuler le système compromis, collecter des informations, ou maintenir l'accès. Quelques commandes Meterpreter courantes :
- **sysinfo** : Afficher les informations sur le système.
- **getuid** : Afficher l'identifiant utilisateur actuel.
- **download** : Télécharger un fichier depuis la machine cible.
- **upload** : Télécharger un fichier vers la machine cible.
- **shell** : Ouvrir un shell système sur la machine cible.

### Windows

#### Exemple d'invite de commandes Windows

```sh
C:\WINDOWS\system32>
```

L'invite de commandes Windows est couramment utilisée après la compromission d'une machine Windows. Elle permet d'exécuter des commandes Windows standard pour naviguer dans le système de fichiers, gérer les processus, et plus encore. Quelques commandes Windows courantes :
- **dir** : Lister les fichiers et répertoires dans le répertoire courant.
- **cd** : Changer de répertoire.
- **copy** : Copier des fichiers.
- **tasklist** : Lister les processus en cours d'exécution.
- **net user** : Gérer les utilisateurs sur la machine.
- **netstat -noa** : Afficher toutes les connexions réseau et ports d'écoute, avec les identifiants de processus associés.
- **taskkill /PID [numéro_PID] /F** : Forcer l'arrêt d'un processus spécifique en utilisant son identifiant de processus (PID).

### Conclusion

Comprendre les différentes invites de commandes et leurs contextes est crucial pour naviguer efficacement et exécuter les commandes appropriées lors des tests d'intrusion. Que vous travailliez sur un système Unix, dans Metasploit, avec Meterpreter, ou sur une machine Windows, cette connaissance vous permettra de tirer le meilleur parti des outils à votre disposition.
