# Python
Pour exécuter des scripts Python sur Kali Linux, vous devez suivre plusieurs étapes : écrire le code, l'exécuter, et parfois installer des modules supplémentaires. 
### 1. Écriture du Code
Utilisez un éditeur de texte comme `nano`, `vim`, ou `gedit` pour écrire votre code. Par exemple, si vous utilisez `nano` :

```bash
nano port_scanner.py
```

Collez le code de votre script Python dans l'éditeur, puis enregistrez et fermez le fichier.

### 2. Installation des Modules (si nécessaire)
Certains scripts Python nécessitent des modules supplémentaires. Utilisez `pip` pour installer les modules nécessaires. Par exemple :

```bash
pip install requests
pip install scapy
pip install paramiko
```

### 3. Exécution du Script
Pour exécuter un script Python, utilisez la commande `python` ou `python3` selon votre version de Python. Par exemple :

```bash
python3 port_scanner.py
```

### Exemples pour les Scripts Fournis

#### 1. Port Scanner
1. Écrire le code :
    ```bash
    nano port_scan.py
    ```
    Collez le code du port scanner, enregistrez et fermez.

2. Exécuter :
    ```bash
    python3 port_scan.py
    ```

#### 2. ARP Spoofing
1. Écrire le code :
    ```bash
    nano arp_spoof.py
    ```
    Collez le code d'ARP Spoofing, enregistrez et fermez.

2. Installer les modules nécessaires :
    ```bash
    pip install scapy
    ```

3. Exécuter :
    ```bash
    sudo python3 arp_spoof.py
    ```

#### 3. SSH Brute Force
1. Écrire le code :
    ```bash
    nano ssh_brute_force.py
    ```
    Collez le code du brute forcer SSH, enregistrez et fermez.

2. Installer les modules nécessaires :
    ```bash
    pip install paramiko
    ```

3. Exécuter :
    ```bash
    python3 ssh_brute_force.py
    ```

### Notes Importantes
1. **Permissions** : Certains scripts nécessitent des privilèges root. Utilisez `sudo` pour exécuter ces scripts si nécessaire.
2. **Modules** : Assurez-vous d'installer tous les modules Python requis pour le script.
3. **Sécurité** : Utilisez ces scripts uniquement dans un environnement de test ou avec la permission explicite du propriétaire du réseau. L'utilisation non autorisée de ces outils est illégale.

En suivant ces étapes, vous pourrez écrire et exécuter vos scripts Python sur Kali Linux.

# C
Pour exécuter ces scripts en C sur Kali Linux, vous devez suivre plusieurs étapes : écrire le code, le compiler et l'exécuter. 

### 1. Écriture du Code
Utilisez un éditeur de texte comme `nano`, `vim`, ou `gedit` pour écrire votre code. Par exemple, si vous utilisez `nano` :

```bash
nano port_scanner.c
```

Collez le code de votre script dans l'éditeur, puis enregistrez et fermez le fichier.

### 2. Compilation du Code
Utilisez le compilateur `gcc` pour compiler votre code C. Par exemple, pour compiler `port_scanner.c` :

```bash
gcc -o port_scanner port_scanner.c
```

### 3. Exécution du Script
Après avoir compilé le script, vous pouvez l'exécuter. Vous aurez peut-être besoin de privilèges administratifs pour certains scripts, surtout ceux qui manipulent des paquets réseau ou des interfaces réseau. Utilisez `sudo` pour exécuter le programme avec des privilèges élevés.

Pour exécuter le script compilé :

```bash
sudo ./port_scanner
```

### Exemples pour les Scripts Fournis

#### 1. Port Scanner
1. Écrire le code :
    ```bash
    nano port_scanner.c
    ```
    Collez le code du port scanner, enregistrez et fermez.

2. Compiler :
    ```bash
    gcc -o port_scanner port_scanner.c
    ```

3. Exécuter :
    ```bash
    sudo ./port_scanner
    ```

#### 2. ARP Spoofing
1. Écrire le code :
    ```bash
    nano arp_spoof.c
    ```
    Collez le code d'ARP Spoofing, enregistrez et fermez.

2. Compiler :
    ```bash
    gcc -o arp_spoof arp_spoof.c
    ```

3. Exécuter :
    ```bash
    sudo ./arp_spoof
    ```

#### 3. DNS Spoofing
1. Écrire le code :
    ```bash
    nano dns_spoof.c
    ```
    Collez le code de DNS Spoofing, enregistrez et fermez.

2. Compiler :
    ```bash
    gcc -o dns_spoof dns_spoof.c
    ```

3. Exécuter :
    ```bash
    sudo ./dns_spoof
    ```

### Notes Importantes
1. **Permissions** : Certains scripts nécessitent des privilèges root. Utilisez `sudo` pour exécuter ces scripts.
2. **Dépendances** : Assurez-vous d'avoir les bibliothèques nécessaires installées. Par exemple, `libpcap` peut être nécessaire pour certains scripts réseau.
3. **Sécurité** : Utilisez ces scripts uniquement dans un environnement de test ou avec la permission explicite du propriétaire du réseau. L'utilisation non autorisée de ces outils est illégale.

En suivant ces étapes, vous pourrez compiler et exécuter vos scripts en C sur Kali Linux.
