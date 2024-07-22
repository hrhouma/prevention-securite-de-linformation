### Cours complet sur l'utilisateur root et les permissions sous Unix/Linux

---

#### 1. Introduction à l'utilisateur root

L'utilisateur root, ou superutilisateur, dans un système Unix/Linux possède des privilèges administratifs complets. Contrairement aux autres utilisateurs, root a la capacité d'exécuter toutes les commandes et d'accéder à tous les fichiers du système, y compris ceux appartenant à d'autres utilisateurs. 

#### 2. Les risques d'utilisation fréquente de l'utilisateur root

Utiliser fréquemment l'utilisateur root présente plusieurs risques :

- **Modifications non souhaitées** : Une erreur de commande en tant que root peut entraîner la suppression ou la modification de fichiers système critiques.
- **Sécurité** : Les attaques visant l'utilisateur root peuvent compromettre l'ensemble du système.
- **Accidents** : Les actions accidentelles, comme la suppression de fichiers importants, peuvent causer des dommages significatifs au système.

#### 3. Exécution d'applications non-root

Certaines applications demandent à ne pas être exécutées en tant que root pour des raisons de sécurité :

- **Vulnérabilités** : Les applications exécutées avec des privilèges root peuvent être plus facilement exploitées par des attaquants.
- **Stabilité** : Les erreurs dans les applications peuvent affecter l'ensemble du système si elles sont exécutées avec des privilèges root.

#### 4. Avantages d'utiliser un utilisateur non-root

Utiliser un utilisateur non-root pour les applications et services offre plusieurs avantages :

- **Sécurité renforcée** : Les actions des utilisateurs non-root sont limitées, ce qui réduit les risques de compromission du système.
- **Réduction des risques de dommages accidentels** : Les utilisateurs non-root ne peuvent pas modifier les fichiers système critiques.

#### 5. Utilisation de sudo

La commande `sudo` permet d'exécuter des commandes avec des privilèges administratifs sans utiliser directement l'utilisateur root. Cela permet de limiter l'accès aux privilèges root tout en permettant des actions administratives :

- **Exécution sécurisée** : `sudo` limite les risques associés à l'utilisation directe de root.
- **Suivi des actions** : Les commandes exécutées avec `sudo` peuvent être journalisées, facilitant le suivi des actions administratives.

#### 6. Ajout d'un utilisateur au groupe sudoers

Pour permettre à un utilisateur d'utiliser `sudo`, il faut l'ajouter au groupe sudoers :

- **usermod** : `usermod -aG sudo <nom_utilisateur>` ajoute l'utilisateur au groupe sudo.
- **adduser** : `adduser <nom_utilisateur> sudo` (sur certaines distributions) ajoute également l'utilisateur au groupe sudo.

#### 7. Désactivation et verrouillage de l'utilisateur root

Pour sécuriser un système en production, il est recommandé de désactiver ou de verrouiller le compte root :

- **Désactivation** : `passwd -l root` verrouille le mot de passe du compte root, empêchant les connexions directes.
- **Vérification de l'état** : `sudo passwd -S root` permet de vérifier l'état du compte root.

#### 8. Permissions des fichiers sous Unix/Linux

Les permissions des fichiers et des répertoires sous Unix/Linux sont cruciales pour la sécurité :

- **Types de permissions** : Lecture (r), Écriture (w), Exécution (x).
- **Catégories d'utilisateurs** : Propriétaire, Groupe, Autres.
- **Notation octale** : Les permissions peuvent être représentées par des chiffres (par exemple, 755).

##### Exemples de commandes chmod

- **Lecture, écriture et exécution pour le propriétaire, lecture et exécution pour le groupe et les autres** : `chmod 755 <fichier>`
- **Lecture et écriture pour le propriétaire, lecture pour le groupe et les autres** : `chmod 644 <fichier>`

#### 9. Gestion des permissions spécifiques

Pour sécuriser des fichiers sensibles, les permissions doivent être définies correctement :

- **Fichiers de configuration** : `chmod 600 <fichier>` donne des droits de lecture et écriture uniquement au propriétaire.
- **Scripts exécutables** : `chmod 700 <script>` permet uniquement au propriétaire de lire, écrire et exécuter le fichier.

##### Commandes utiles pour gérer les permissions

- **Afficher les permissions** : `ls -l` affiche les permissions détaillées des fichiers et répertoires.
- **Modifier les permissions** : `chmod` permet de changer les permissions des fichiers.

---

#### 10. Sécurité avancée avec sudo

Pour une gestion sécurisée des privilèges administratifs, `sudo` est un outil essentiel :

- **Configuration** : Le fichier `/etc/sudoers` contrôle les permissions de `sudo`. Utilisez `visudo` pour modifier ce fichier en toute sécurité.
- **Commandes spécifiques** : Vous pouvez configurer `sudo` pour permettre à des utilisateurs d'exécuter uniquement certaines commandes administratives.

##### Exemples d'utilisation de sudo

- **Exécution d'une commande** : `sudo <commande>` exécute la commande avec des privilèges administratifs.
- **Accès root temporaire** : `sudo -i` ouvre un shell avec les privilèges root.

#### Conclusion

La gestion des utilisateurs et des permissions est essentielle pour la sécurité et la stabilité des systèmes Unix/Linux. En limitant l'utilisation de l'utilisateur root, en utilisant `sudo` pour les actions administratives, et en définissant correctement les permissions des fichiers, vous pouvez protéger efficacement votre système contre les erreurs et les menaces de sécurité.

En suivant ces pratiques, vous garantirez un environnement sécurisé et stable pour vos utilisateurs et applications.
