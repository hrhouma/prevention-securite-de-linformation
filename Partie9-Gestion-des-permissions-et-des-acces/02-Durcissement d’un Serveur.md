# 02 - Gestion des Permissions et Accès - PARTIE 02 (Durcissement d’un Serveur)

Le durcissement d'un serveur est un ensemble de pratiques visant à renforcer la sécurité des systèmes informatiques contre les menaces potentielles. Ce cours détaillé couvre les différents aspects du durcissement d'un serveur, en se concentrant sur les politiques réseau, la sécurité des pods, la configuration de l'authentification et de l'autorisation, la gestion de la charge, la haute disponibilité, et l'autoscaling.

---

#### Table des Matières
1. [Introduction au Durcissement de Serveur](#introduction)
2. [Politiques Réseau et Sécurité](#politiques-reseau)
   - [Gestion du Trafic Réseau](#gestion-trafic)
   - [Politiques de Sécurité](#politiques-securite)
3. [Authentification et Autorisation Basées sur les Rôles (RBAC)](#rbac)
4. [Application des Politiques Réseau](#application-politiques)
   - [Contrôle du Trafic Réseau](#controle-trafic)
5. [Gestion de la Charge et Haute Disponibilité](#gestion-charge)
   - [Services et Load Balancers](#services-load-balancers)
   - [Réplication et Autoscaling](#replication-autoscaling)
6. [Conclusion](#conclusion)

---

### <a name="introduction"></a> 1. Introduction au Durcissement de Serveur
Le durcissement d’un serveur consiste à renforcer la sécurité d’un serveur en appliquant des mesures de protection pour minimiser les vulnérabilités. Ce processus est crucial pour protéger les données et les services contre les attaques malveillantes. Le durcissement inclut la configuration sécurisée du système d'exploitation, l'application de correctifs de sécurité, la gestion des accès, et la surveillance continue des activités du serveur.

[Revenir en haut](#table-des-matieres)

---

### <a name="politiques-reseau"></a> 2. Politiques Réseau et Sécurité

#### <a name="gestion-trafic"></a> Gestion du Trafic Réseau
La gestion du trafic réseau implique le contrôle des données qui transitent entre les serveurs et les clients. Les administrateurs réseau doivent configurer des pare-feu, des routeurs et des commutateurs pour surveiller et filtrer le trafic afin de prévenir les accès non autorisés. Cela inclut :

- **Pare-feu :** Définir des règles pour bloquer ou autoriser le trafic réseau basé sur des adresses IP, des ports et des protocoles spécifiques. Par exemple, avec `iptables` :
  ```bash
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
  sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
  sudo iptables -A INPUT -j DROP
  ```

- **Listes de Contrôle d'Accès (ACL) :** Configurer des ACL sur les routeurs et les commutateurs pour restreindre les accès aux ressources critiques. Par exemple, avec Cisco IOS :
  ```plaintext
  access-list 100 permit tcp any any eq 22
  access-list 100 permit tcp any any eq 80
  access-list 100 permit tcp any any eq 443
  access-list 100 deny ip any any
  ```

- **Systèmes de Détection et de Prévention d'Intrusion (IDS/IPS) :** Utiliser des IDS/IPS pour détecter et prévenir les tentatives d'intrusion. Par exemple, avec Snort :
  ```plaintext
  alert tcp any any -> any 80 (msg:"HTTP connection detected"; sid:1000001; rev:1;)
  ```

#### <a name="politiques-securite"></a> Politiques de Sécurité
Les politiques de sécurité sont des règles définies pour protéger les ressources réseau. Elles peuvent inclure des mesures telles que le chiffrement des communications, la mise en place de VPN, et la configuration de listes de contrôle d'accès (ACL) pour restreindre les connexions. Quelques exemples incluent :

- **Chiffrement :** Utiliser SSL/TLS pour chiffrer les communications entre les clients et les serveurs. Par exemple, configurer Nginx pour utiliser SSL :
  ```plaintext
  server {
      listen 443 ssl;
      server_name example.com;
      ssl_certificate /etc/nginx/ssl/nginx.crt;
      ssl_certificate_key /etc/nginx/ssl/nginx.key;
      ...
  }
  ```

- **VPN :** Configurer des réseaux privés virtuels pour sécuriser les connexions à distance. Par exemple, avec OpenVPN :
  ```bash
  sudo apt-get install openvpn
  sudo openvpn --config /etc/openvpn/server.conf
  ```

- **Segmentation Réseau :** Diviser le réseau en segments pour limiter la propagation des attaques. Par exemple, configurer des VLANs sur un switch Cisco :
  ```plaintext
  vlan 10
   name Sales
  vlan 20
   name Engineering
  interface GigabitEthernet0/1
   switchport mode access
   switchport access vlan 10
  ```

[Revenir en haut](#table-des-matieres)

---

### <a name="rbac"></a> 3. Authentification et Autorisation Basées sur les Rôles (RBAC)

L'authentification et l'autorisation basées sur les rôles (RBAC) sont des mécanismes de sécurité qui permettent de contrôler l'accès aux ressources en fonction des rôles attribués aux utilisateurs. RBAC simplifie la gestion des permissions et renforce la sécurité en limitant l'accès aux ressources sensibles uniquement aux utilisateurs autorisés. Les étapes incluent :

- **Définition des Rôles :** Identifier et créer des rôles en fonction des responsabilités des utilisateurs.
- **Assignation des Rôles :** Assigner des rôles aux utilisateurs en fonction de leurs fonctions et besoins.
- **Politiques d'Accès :** Définir des politiques d'accès pour chaque rôle, spécifiant les actions autorisées sur les ressources.

Exemple de configuration RBAC avec Windows Active Directory :
```plaintext
Add-ADGroupMember -Identity "IT Administrators" -Members "JohnDoe"
New-ADUser -Name "JaneDoe" -AccountPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) -Enabled $true
Add-ADUserToGroup -Identity "JaneDoe" -Group "HR Managers"
```

[Revenir en haut](#table-des-matieres)

---

### <a name="application-politiques"></a> 4. Application des Politiques Réseau

#### <a name="controle-trafic"></a> Contrôle du Trafic Réseau
L'application des politiques réseau permet de contrôler le trafic réseau entrant et sortant. Cela peut inclure la configuration de pare-feu pour bloquer les connexions indésirables, l'utilisation de filtres de paquets pour analyser les données, et la mise en œuvre de politiques de qualité de service (QoS) pour prioriser certains types de trafic. Les mesures spécifiques comprennent :

- **Filtrage des Paquets :** Configurer des règles pour analyser et filtrer les paquets réseau.
- **Qualité de Service (QoS) :** Définir des priorités pour différents types de trafic afin d'assurer une performance optimale.
- **Isolation de Réseau :** Utiliser des VLAN pour isoler les différentes parties du réseau.

Exemple de configuration QoS avec Cisco IOS :
```plaintext
class-map match-any VOIP
 match protocol rtp
policy-map QOS
 class VOIP
  priority 1000
 class class-default
  fair-queue
interface GigabitEthernet0/1
 service-policy output QOS
```

[Revenir en haut](#table-des-matieres)

---

### <a name="gestion-charge"></a> 5. Gestion de la Charge et Haute Disponibilité

#### <a name="services-load-balancers"></a> Services et Load Balancers
Les services et les load balancers sont utilisés pour répartir la charge de travail entre plusieurs serveurs, assurant ainsi une meilleure performance et une haute disponibilité des applications. Un load balancer distribue les requêtes des clients aux serveurs disponibles, réduisant ainsi les temps d'arrêt et améliorant l'expérience utilisateur. Les types de load balancers incluent :

- **Load Balancers Matériels :** Dispositifs physiques dédiés à la répartition de charge.
- **Load Balancers Logiciels :** Applications qui distribuent les requêtes sur les serveurs.
- **Algorithmes de Répartition :** Utiliser des algorithmes comme le round-robin, la répartition par charge, et la répartition par géolocalisation.

Exemple de configuration d'un load balancer avec HAProxy :
```plaintext
frontend http_front
   bind *:80
   stats uri /haproxy?stats
   default_backend http_back

backend http_back
   balance roundrobin
   server server1 10.0.0.1:80 check
   server server2 10.0.0.2:80 check
```

#### <a name="replication-autoscaling"></a> Réplication et Autoscaling
La réplication consiste à dupliquer des données ou des services sur plusieurs serveurs pour assurer la redondance et la disponibilité. L'autoscaling

 permet d'ajuster automatiquement les ressources en fonction de la demande, garantissant ainsi que les services restent disponibles même en cas de forte charge. Les stratégies incluent :

- **Réplication de Données :** Utiliser des bases de données répliquées pour assurer la disponibilité des données.
- **Autoscaling Horizontal :** Ajouter ou retirer des instances de serveur en fonction de la demande.
- **Autoscaling Vertical :** Ajuster les ressources (CPU, RAM) des serveurs existants en fonction de la charge.

Exemple de configuration de l'autoscaling avec AWS EC2 Auto Scaling :
```plaintext
aws autoscaling create-launch-configuration --launch-configuration-name my-launch-config --image-id ami-12345678 --instance-type t2.micro
aws autoscaling create-auto-scaling-group --auto-scaling-group-name my-auto-scaling-group --launch-configuration-name my-launch-config --min-size 1 --max-size 10 --desired-capacity 2 --availability-zones us-west-2a us-west-2b
```

[Revenir en haut](#table-des-matieres)

---

### <a name="conclusion"></a> 6. Conclusion

Le durcissement d’un serveur est un processus continu qui nécessite une vigilance constante et une adaptation aux nouvelles menaces. En mettant en œuvre des politiques réseau strictes, en utilisant RBAC pour la gestion des accès, et en assurant une haute disponibilité grâce à la gestion de la charge et à l'autoscaling, les administrateurs peuvent renforcer la sécurité de leurs serveurs et protéger les données sensibles. L'intégration de ces pratiques dans le cadre global de la sécurité informatique contribue à la résilience des infrastructures contre les cyberattaques.
