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
