# Guide détaillé pour installer GLPI sur un serveur Linux :

1. Prérequis :
   - Un serveur Linux (Ubuntu ou Debian recommandé)
   - Un serveur web (Apache)
   - PHP et ses extensions
   - Une base de données (MariaDB ou MySQL)

2. Installation des composants nécessaires :

```
sudo apt update
sudo apt install apache2 php php-{apcu,cli,common,curl,gd,imap,ldap,mysql,xmlrpc,xml,mbstring,bcmath,intl,zip,bz2} libapache2-mod-php mariadb-server
```

3. Configuration de la base de données :

```
sudo mysql_secure_installation
sudo mysql
CREATE DATABASE glpidb;
CREATE USER 'glpiuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON glpidb.* TO 'glpiuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

4. Téléchargement et extraction de GLPI :

```
cd /tmp
wget https://github.com/glpi-project/glpi/releases/download/10.0.7/glpi-10.0.7.tgz
sudo tar xvf glpi-10.0.7.tgz -C /var/www/html/
```

5. Configuration des permissions :

```
sudo chown -R www-data:www-data /var/www/html/glpi
sudo chmod -R 775 /var/www/html/glpi
```

6. Configuration d'Apache :

Créez un fichier de configuration pour GLPI :

```
sudo nano /etc/apache2/sites-available/glpi.conf
```

Ajoutez le contenu suivant :

```
<VirtualHost *:80>
    ServerName your_domain_or_ip
    DocumentRoot /var/www/html/glpi/public
    
    <Directory /var/www/html/glpi/public>
        Options FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/glpi_error.log
    CustomLog ${APACHE_LOG_DIR}/glpi_access.log combined
</VirtualHost>
```

Activez la configuration et redémarrez Apache :

```
sudo a2ensite glpi.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

7. Installation via l'interface web :
   - Ouvrez un navigateur et accédez à http://your_domain_or_ip/glpi
   - Suivez l'assistant d'installation en sélectionnant la langue, acceptant la licence, et en fournissant les informations de la base de données.

8. Finalisation :
   - Une fois l'installation terminée, connectez-vous avec les identifiants par défaut (glpi/glpi pour l'administrateur)
   - Changez immédiatement les mots de passe par défaut
   - Supprimez le fichier install.php pour des raisons de sécurité :
     ```
     sudo rm /var/www/html/glpi/install/install.php
     ```

Votre instance GLPI est maintenant installée et prête à être utilisée. N'oubliez pas de configurer les sauvegardes régulières et de maintenir le système à jour.

Citations:
[1] https://glpi-install.readthedocs.io/en/latest/

[2] https://glpi-install.readthedocs.io/en/latest/install/index.html

[3] https://glpi-project.org/fr/glpi-documentation/

[4] https://glpi-project.org/how-to-install-glpi-on-ubuntu/

[5] https://www.tecmint.com/install-glpi-asset-management-rhel/

[6] https://glpi-project.org/fr/comment-installer-glpi-sur-ubuntu/

[7] https://faq.teclib.com/03_knowledgebase/procedures/install_glpi/

[8] https://ipv6.rs/tutorial/Fedora_Server_Latest/GLPI/

[9] https://openclassrooms.com/fr/courses/1730516-gerez-votre-parc-informatique-avec-glpi/5993816-installez-votre-serveur-glpi

[10] https://www.youtube.com/watch?v=Dc0dy1Z6MyM

[11] https://www.awoui.com/post/installation-de-glpi

[12] https://www.youtube.com/watch?v=AF5pJaQJXvU

[13] https://www.it-connect.fr/installation-pas-a-pas-de-glpi-10-sur-debian-12/

[14] https://glpi-project.org/documentation/

[15] https://github.com/glpi-project/doc-install
