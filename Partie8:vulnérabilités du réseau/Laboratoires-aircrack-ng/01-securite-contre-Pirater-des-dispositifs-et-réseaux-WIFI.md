# Introduction
Dans cet article, je vais vous guider à travers le piratage des points d'accès WIFI et des dispositifs compatibles WIFI. Veuillez noter que pour suivre pleinement ce guide, vous avez besoin d'une carte sans fil capable d'injection de paquets et prenant en charge le mode moniteur. Si vous n'êtes pas sûr que votre carte prenne en charge le mode moniteur, vous pouvez la tester de cette manière :

```bash
iwconfig #Vérifiez le nom de l'interface de votre carte sans fil
airmon-ng start nom_interface_ici 
# Si la commande fonctionne, votre carte sans fil prend en charge le mode moniteur.
```

### Tous les protocoles de sécurité WIFI actuels
**WEP**

WEP est le premier protocole de sécurité WIFI, introduit à la fin des années 1990. De nos jours, il est quasiment inutile en termes de sécurité, car de nombreuses vulnérabilités critiques ont été découvertes et le mot de passe lui-même est très facile à craquer.

**WPA2**

C'est le protocole de sécurité le plus populaire aujourd'hui, presque tous les réseaux sans fil utilisant WPA2 personnel ou entreprise. Étant donné que WPA2 est la norme actuelle, nous allons principalement nous concentrer sur le piratage de celui-ci.

**WPA3**

WPA3 est le protocole le plus récent, introduit en 2018. Étant si nouveau, il n'a pas encore été suffisamment testé et a probablement de nombreuses vulnérabilités de sécurité à corriger avant d'être mis en œuvre par défaut sur les réseaux domestiques.

### Concepts expliqués
**Deauth/Deauthentication**

Le protocole IEEE 802.11 (WIFI) possède un paquet appelé trame de désauthentification WIFI, utilisé par le client ou le point d'accès pour informer l'autre partie que la connexion est fermée et d'arrêter d'envoyer des données.

C'est cependant un système défectueux, car l'origine du paquet de désauthentification peut être falsifiée. Cela signifie que nous, en tant qu'attaquants, pouvons envoyer un paquet de désauthentification falsifié au client ou au point d'accès, en prétendant être l'autre appareil, avec pour conséquence que la cible perdra la connexion au point d'accès.

**Mode moniteur**

Le mode moniteur est une fonctionnalité de la carte sans fil qui permet de capturer et d'analyser le trafic réseau sans fil sans être connecté à un réseau particulier.

**Portail captif**

Un portail captif est une page vers laquelle un routeur sans fil redirige les utilisateurs s'ils essaient de naviguer sur le web (ou elle apparaît automatiquement). Les portails captifs sont généralement utilisés dans les WIFI gratuits pour obliger l'utilisateur à enregistrer un compte sur le réseau afin de prévenir les abus, mais cela peut également être exploité en mettant en place un faux portail captif sur un réseau WIFI faux pour tromper l'utilisateur en lui faisant, par exemple, se connecter à son "compte Google", qui est en réalité un site de phishing hébergé sur l'ordinateur de l'attaquant.

### Piratage du WIFI (la partie excitante)
Dans cette section, je vais couvrir deux des meilleures attaques que vous pouvez effectuer sur les points d'accès et les dispositifs compatibles WIFI.

**Craquer les handshakes WIFI**

Lorsque qu'un dispositif se connecte à un réseau sans fil protégé par un mot de passe, le réseau et le dispositif effectuent une poignée de main en quatre étapes, qui tente de créer une ligne de communication chiffrée avec le routeur sans fil, validant également le mot de passe. Si nous capturons cette poignée de main complète, nous aurons suffisamment d'informations pour essayer de craquer le mot de passe du réseau sans fil localement. Voici une explication très détaillée si vous êtes intéressé : [https://www.cyberpunk.rs/capturing-wpa-wpa2-handshake](https://www.cyberpunk.rs/capturing-wpa-wpa2-handshake).

Pour capturer la poignée de main en quatre étapes, nous pouvons soit attendre que quelqu'un se connecte au réseau cible, soit, ma méthode préférée, effectuer une attaque de désauthentification sur un dispositif connecté au réseau et attendre quelques secondes que le dispositif se reconnecte automatiquement (ce que nous allons faire).

**Commençons !**

1. Activer le mode moniteur

```bash
airmon-ng start <interface>
```

La sortie devrait indiquer "mode moniteur activé".

2. Découvrir votre cible

Exécutez la commande suivante pour renifler quels points d'accès (AP) et dispositifs compatibles WIFI se trouvent autour de vous :

```bash
airodump-ng <interface>
```

Une fois que vous avez sélectionné votre cible, regardez la colonne "CH". Cela nous indique sur quel canal/fréquence fonctionne le réseau cible. Arrêtez la numérisation avec CTRL + c.

Astuce : si le CH > 100, le réseau est en 5G.

3. Changer votre canal

Les adaptateurs sans fil ne peuvent généralement pas écouter sur plusieurs canaux en même temps, mais nous devons être sur le même canal que la cible pour que nos attaques soient efficaces, donc changez le canal de votre carte sans fil pour celui de la cible comme ceci :

```bash
iw <interface> set channel <target_channel>
```

4. Commencer à renifler

Maintenant, démarrez à nouveau airodump-ng, mais cette fois-ci pour enregistrer la poignée de main.

```bash
airodump-ng -c <target_channel> -w <où_enregistrer_handshake_cap> <interface>
```

5. Désauthentifier

Une fois airodump-ng démarré, commencez l'attaque de désauthentification pour déconnecter les clients du réseau. Il existe de nombreux outils pour cela, mais mon préféré est mdk4.

```bash
mdk4 <interface> d -E <cible_ESSID (nom)> -c <target_channel>
```

Lorsque vous voyez des messages tels que "envoi de paquet", attendez environ 5 secondes pour que l'outil fasse son travail, puis appuyez sur CTRL + c pour arrêter la désauthentification. Maintenant, attendez simplement; si vous avez de la chance, cela a fonctionné du premier coup et vous devriez voir "poignée de main capturée : bla bla bla" en haut à droite d'airodump-ng, à ce moment-là, vous pouvez fermer airodump-ng. Si vous avez attendu environ 10 secondes sans aucune poignée de main, recommencez la désauthentification, et répétez jusqu'à ce que vous obteniez une poignée de main.

6. Craquer la poignée de main

Félicitations ! Vous avez maintenant une poignée de main capturée dans le fichier *.cap. Il est maintenant temps de la craquer. Vous avez plusieurs façons de le faire. La première est d'utiliser aircrack-ng et la seconde est d'utiliser hashcat. Peu importe laquelle vous utilisez; hashcat nécessite juste un peu plus d'efforts pour fonctionner.

**Craquer avec aircrack-ng (exemples) :**

#Méthode 1 : Craquer avec un dictionnaire

```bash
aircrack-ng <chemin_vers_fichier_cap> -w <fichier_wordlist>
```

#Méthode 2 : Pipe un wordlist à aircrack-ng

```bash
crunch 8 8 0123456789 | aircrack-ng <chemin_vers_fichier_cap>
```

**Craquer avec hashcat (exemple) :**

#D'abord convertir le fichier cap au format hashcat

```bash
aircrack-ng -j <chemin_vers_sauvegarde_fichier_HCCAPX> <chemin_vers_fichier_cap>
```

#Essayer de craquer le mot de passe WIFI en supposant que c'est un PIN de 8 chiffres

```bash
hashcat -a 3 -m 22000 <chemin_vers_sauvegarde_fichier_HCCAPX> ?d?d?d?d?d?d?d?d
```

7. Ligne d'arrivée

Vous devriez maintenant avoir le mot de passe en clair craqué. Allez-y et connectez-vous au réseau ou faites ce que vous voulez avec.

### Créer un jumeau maléfique (attaque EVIL TWIN)
Lorsque vous configurez votre téléphone ou un autre dispositif pour "se souvenir" d'un réseau, cela fait que le dispositif envoie des requêtes de probe, ce qui revient à demander constamment autour de lui, "Bonjour, un réseau avec le nom XXX est-il ici ?" et si le réseau est à portée, il répondra en disant, "Oui, je suis ici, regardez mon ESSID (nom du réseau)" et le téléphone s'y connectera.

Si le réseau enregistré n'est pas protégé par un mot de passe, nous pouvons faire quelque chose appelé une attaque de jumeau maléfique, ce qui signifie que nous écoutons ces requêtes de probe, puis nous créons nous-mêmes un réseau identique, trompant le dispositif en se connectant à nous. Si la cible est déjà connectée à un réseau, nous pouvons continuer à désauthentifier le dispositif du réseau afin qu'il se connecte automatiquement à la deuxième meilleure option, qui est très probablement notre réseau faux.



Cela ne serait pas pire qu'une attaque DOS, mais lorsqu'il est couplé avec quelque chose comme un portail captif et/ou un spoofing DNS, cela devient une attaque très puissante.

1. Télécharger create_ap

Create_ap est un programme très facile à utiliser pour Linux pour configurer des points d'accès. Il n'est plus maintenu, mais fonctionne toujours parfaitement; je n'ai jamais eu de problème avec.

Installez-le en copiant et collant ces lignes :

```bash
git clone https://github.com/oblique/create_ap
cd create_ap
make install
```

2. Découvrir le dispositif cible

```bash
airodump-ng <interface>
```

Regardez la section "probes" en bas. Cela contient tous les réseaux WIFI demandés/probés par chaque dispositif.

Maintenant, décidez quel dispositif vous voulez attaquer et quel réseau WIFI vous allez créer. Ensuite, regardez la section "BSSID" du dispositif que vous ciblez. "(non associé)" signifie que le dispositif n'est actuellement pas connecté à un réseau, et vous pouvez passer à l'étape suivante. Cependant, si vous voyez une adresse MAC là-bas, cela signifie que vous devez le désauthentifier.

3. Désauthentifier (seulement si la cible est connectée à un autre WIFI)

Pour obtenir les informations de canal et l'ESSID, trouvez le BSSID auquel le dispositif est connecté dans la liste des BSSID dans la partie supérieure d'airodump. BTW, "station" signifie la même chose que l'adresse MAC du dispositif cible (comme un téléphone).

Maintenant, fermez airodump-ng et exécutez :

```bash
iw <interface> set channel <target_channel>
mdk4 <interface> d -E <nom_ap> -c <target_channel> -S <mac_dispositif>
```

Laissez cela en arrière-plan et continuez avec le reste du guide.

4. Créer le point d'accès rogue

```bash
create_ap -n <interface> <nom_ap>
```

"-n" signifie qu'il ne recevra pas de connexion Internet. Il peut seulement se connecter à l'ordinateur de l'attaquant, qui serait le routeur sans fil pour le dispositif cible. Nom_ap est l'ESSID que vous avez trouvé qu'un dispositif demandait à l'étape 2.

5. Lancer un site de phishing

Maintenant, vous devez décider quel site vous voulez servir en tant que portail captif. Vous pouvez utiliser n'importe quel outil que vous voulez ou en créer un vous-même, mais pour simplifier, je vais utiliser un outil appelé "HiddenEye" ([https://github.com/Morsmalleo/HiddenEye_Legacy](https://github.com/Morsmalleo/HiddenEye_Legacy)) pour lancer un site de phishing Google sur le port 80. Pour ce faire, il suffit d'installer l'outil, de l'exécuter, et de sélectionner la page de phishing Google standard, mais de changer l'hôte et le port d'écoute en 0.0.0.0:80. Si vous le souhaitez, vous pouvez également configurer un écouteur HTTPS au cas où la cible essaierait d'aller sur un site HTTPS.

6. Spoofing DNS

C'est la partie qui va transformer simplement l'ordinateur avec un serveur web en un véritable portail captif. Comment cela fonctionne, c'est que chaque fois que la cible essaie d'aller sur un site web comme helloworld.com, notre ordinateur enverra une réponse DNS falsifiée en disant, "oui, je sais où est helloworld.com; c'est à <insérer notre propre IP>" envoyant l'utilisateur vers notre page de phishing au lieu du vrai site web.

D'abord, vous devez savoir quelle est votre IP dans le nouveau réseau WIFI créé. Pour la trouver, exécutez :

```bash
ifconfig
# OU
ip a
```

Votre IP devrait être listée sous l'interface "tun".

Pour le spoofing, je préfère utiliser un outil appelé ettercap-gui. C'est un programme assez ancien, mais toujours, à mon avis, le plus capable de tous. Pour commencer, ouvrez le fichier dns d'ettercap à /etc/ettercap/etter.dns et ajoutez cette ligne :

```bash
* A <votre_ip_ici>
```

Enregistrez le fichier et ouvrez ettercap en mode gui. Ensuite, naviguez vers plugins, gérer les plugins, et activez le plugin dns_spoof.

7. Ligne d'arrivée

C'est tout ! Maintenant que le dispositif devrait être connecté au faux réseau, la prochaine fois que l'utilisateur essaiera d'aller sur un site web, il devrait s'afficher avec le portail captif que nous voulions servir.

J'espère que cet article vous a aidé ❤

**Pirater le WIFI**
**Wifi**
**Sécurité des réseaux sans fil**
**Jumeau Maléfique**
**Craquage de Wifi**
