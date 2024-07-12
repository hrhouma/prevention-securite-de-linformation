
# Installation de Snipe-IT sur Windows et Linux

#### **Sur Windows**

1. **Prérequis** :
   - XAMPP (inclut Apache, MySQL, PHP)
   - Composer
   - Snipe-IT

2. **Installation de XAMPP** :
   - Téléchargez et installez XAMPP depuis le site officiel.
   - Démarrez Apache et MySQL via le panneau de contrôle XAMPP.

3. **Configuration de la base de données** :
   - Accédez à phpMyAdmin via http://localhost/phpmyadmin.
   - Créez une nouvelle base de données nommée `snipeit`.
   - Créez un utilisateur avec tous les privilèges pour cette base de données.

4. **Téléchargement et configuration de Snipe-IT** :
   - Téléchargez Snipe-IT depuis le site officiel ou GitHub.
   - Extrayez les fichiers dans le répertoire `htdocs` de XAMPP (par exemple, `C:\xampp\htdocs\snipe-it`).
   - Ouvrez une invite de commande et naviguez vers le répertoire de Snipe-IT :
     ```bash
     cd C:\xampp\htdocs\snipe-it
     ```
   - Installez Composer si ce n'est pas déjà fait, puis exécutez :
     ```bash
     composer install --no-dev --prefer-source
     ```

5. **Configuration de l'environnement** :
   - Copiez le fichier `.env.example` en `.env` et modifiez-le pour correspondre à votre configuration (base de données, URL de l'application, etc.).
   - Générez la clé de l'application :
     ```bash
     php artisan key:generate
     ```

6. **Installation via le navigateur** :
   - Accédez à http://localhost/snipe-it dans votre navigateur.
   - Suivez les instructions de l'assistant d'installation.

#### **Sur Linux (Ubuntu 22.04)**

1. **Prérequis** :
   - Un serveur LEMP (Linux, Nginx, MySQL, PHP)
   - Composer
   - Git

2. **Installation des dépendances** :
   ```bash
   sudo apt update
   sudo apt install nginx mariadb-server php php-{bcmath,common,ctype,curl,fileinfo,fpm,gd,iconv,intl,mbstring,mysql,soap,xml,xsl,zip} git composer
   ```

3. **Configuration de la base de données** :
   - Connectez-vous à MySQL :
     ```bash
     sudo mysql
     ```
   - Créez la base de données et l'utilisateur :
     ```sql
     CREATE DATABASE snipeit;
     GRANT ALL ON snipeit.* TO 'snipeituser'@'localhost' IDENTIFIED BY 'password';
     FLUSH PRIVILEGES;
     EXIT;
     ```

4. **Téléchargement et configuration de Snipe-IT** :
   - Clonez le dépôt Snipe-IT :
     ```bash
     cd /var/www/html
     sudo git clone https://github.com/snipe/snipe-it snipe-it
     cd snipe-it
     sudo composer install --no-dev --prefer-source
     ```

5. **Configuration de l'environnement** :
   - Copiez le fichier `.env.example` en `.env` et modifiez-le pour correspondre à votre configuration.
   - Générez la clé de l'application :
     ```bash
     sudo php artisan key:generate
     ```

6. **Configuration de Nginx** :
   - Créez un fichier de configuration pour Snipe-IT :
     ```bash
     sudo nano /etc/nginx/sites-available/snipeit
     ```
   - Ajoutez la configuration suivante :
     ```nginx
     server {
         listen 80;
         server_name your_domain_or_ip;
         root /var/www/html/snipe-it/public;
         index index.php;

         location / {
             try_files $uri $uri/ /index.php?$query_string;
         }

         location ~ \.php$ {
             include snippets/fastcgi-php.conf;
             fastcgi_pass unix:/run/php/php8.1-fpm.sock;
             fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
             include fastcgi_params;
         }
     }
     ```
   - Activez le site et redémarrez Nginx :
     ```bash
     sudo ln -s /etc/nginx/sites-available/snipeit /etc/nginx/sites-enabled/
     sudo systemctl restart nginx
     ```

7. **Installation via le navigateur** :
   - Accédez à http://your_domain_or_ip dans votre navigateur.
   - Suivez les instructions de l'assistant d'installation.

Ces étapes vous permettront d'installer et de configurer Snipe-IT sur Windows et Linux. Pour plus de détails, vous pouvez consulter la documentation officielle de Snipe-IT[1][3][6][9].

Citations:
[1] https://snipe-it.readme.io/docs/installation
[2] https://www.youtube.com/watch?v=joiUjMhDaOk
[3] https://www.rosehosting.com/blog/how-to-install-snipe-it-on-ubuntu-22-04/
[4] https://snipe-it.readme.io/docs/windowsiis
[5] https://www.atlantic.net/dedicated-server-hosting/how-to-install-snipe-it-on-ubuntu-22-04/
[6] https://blog.masteringmdm.com/snipe-it-installation-on-windows-server/
[7] https://www.youtube.com/watch?v=eA5RpNXJPxo
[8] https://www.youtube.com/watch?v=h5hMWkgTusc
[9] https://snipe-it.readme.io/docs/linuxosx
[10] https://snipeitapp.com/download
[11] https://docs.vultr.com/how-to-install-snipe-it-on-ubuntu-20-04
[12] https://www.youtube.com/watch?v=qLbxcaI0aPU
[13] https://www.youtube.com/watch?v=Cn0YT1TLDNI
[14] https://www.youtube.com/watch?v=T0HzzMTqH4o
[15] https://www.youtube.com/watch?v=11W7Jukp9XE
