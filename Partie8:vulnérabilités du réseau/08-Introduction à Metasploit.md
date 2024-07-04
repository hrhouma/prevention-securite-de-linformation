## Introduction à Metasploit

Depuis sa première version en 2003, Metasploit a connu une évolution constante, devenant le framework d'exploitation le plus complet et le plus utilisé. Sa popularité est due à sa facilité d'utilisation, à la diversité de ses options, interfaces et utilitaires. Pour bien comprendre l'utilisation de Metasploit, il est essentiel de maîtriser certains termes clés.

### Terminologie

#### Exploit

Un exploit est un code permettant d'exploiter une faille de sécurité dans un système informatique cible. Il peut être utilisé contre une machine distante (remote exploit) ou localement sur la machine de l'attaquant (local exploit). Les conséquences de l'exploitation peuvent varier, allant de la compromission du système à l'élévation de privilèges ou au déni de service (DoS).

#### Payload

Le payload est la charge malveillante exécutée par l'exploit. Il peut s'agir de :
- Création d'une connexion entre la machine de l'attaquant et la machine cible (bind shell ou reverse shell).
- Exécution de commandes.
- Ajout d'un utilisateur sur le système cible.

#### Auxiliaire (auxiliary)

Les auxiliaires sont des modules de Metasploit ayant divers objectifs tels que la réalisation de scans, l'écoute réseau ou le fuzzing. Ils sont utilisés pour la collecte d'informations et d'autres tâches pré-exploit.

#### Encoder

Un encoder modifie la charge utile (payload) pour qu'elle ne soit pas détectée par les systèmes de défense comme les antivirus ou les IDS (Intrusion Detection System). C'est un moyen de contourner les mécanismes de détection.

#### Listener

Un listener est un composant en attente d'une connexion entrante. Par exemple, si le payload d'un exploit crée une connexion de la machine victime vers celle de l'attaquant, un listener est nécessaire pour recevoir cette connexion.

#### Post

Les modules de post-exploitation sont utilisés après l'exploitation initiale d'une vulnérabilité. Ils permettent de récupérer des informations supplémentaires sur le système compromis ou d'obtenir un accès privilégié.

#### Bind Shell vs Reverse Shell

Les payloads peuvent être de type bind shell ou reverse shell :
- **Bind shell** : La machine cible ouvre un port et attend une connexion de la part de l'attaquant.
- **Reverse shell** : La machine cible initie une connexion vers la machine de l'attaquant, utile pour contourner les NAT ou les pare-feux.

### Interaction avec la Cible

Pour interagir avec une machine cible, trois informations sont nécessaires :
1. **Adresse IP** de la cible (RHOST).
2. **Numéro de port** sur lequel le service cible écoute (RPORT).
3. **Protocole utilisé** (TCP/UDP).

Ces informations permettent de contacter un service en écoute sur la machine cible. Les numéros de port standard (par exemple, SSH sur le port 22, FTP sur le port 21) sont souvent déjà spécifiés dans les modules de Metasploit mais peuvent être modifiés si nécessaire.

#### Variables RHOST et RPORT

- **RHOST** : Adresse IP de la machine cible.
- **RPORT** : Port sur lequel le service cible écoute.

#### Variables LHOST et LPORT

Pour les modules de type reverse, la machine cible doit connaître l'adresse IP et le port de la machine de l'attaquant :
- **LHOST** : Adresse IP de la machine de l'attaquant.
- **LPORT** : Port sur lequel la machine de l'attaquant écoute.

#### Variable RHOSTS

Certains modules peuvent utiliser la variable **RHOSTS** pour spécifier plusieurs adresses IP, permettant ainsi une exploitation massive.

### Conclusion

Comprendre ces termes et concepts est crucial pour utiliser efficacement Metasploit. Que vous soyez un débutant ou un utilisateur expérimenté, cette connaissance vous aidera à naviguer dans le framework et à tirer parti de ses nombreuses fonctionnalités.
