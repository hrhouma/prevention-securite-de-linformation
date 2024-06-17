
# 1 - Les Étapes d'une Attaque Informatique

Les cyberattaques sont devenues une menace omniprésente pour les entreprises et les organisations de toutes tailles. Comprendre les différentes étapes d'une attaque informatique est crucial pour renforcer les défenses et protéger les systèmes d'information contre les intrusions. Une attaque informatique typique se déroule généralement en cinq étapes : récolte des informations, identification des vulnérabilités, exploitation des failles, maintien de l'intrusion, et effacement des traces. Cet article explore ces étapes en détail pour aider les responsables de la sécurité à mieux comprendre et anticiper les menaces potentielles.

### 1. Récolte des Informations

#### Informations Techniques et Sociales

Les attaquants commencent par une phase de reconnaissance pour recueillir autant d'informations que possible sur la cible. Cela peut inclure des données techniques, telles que les adresses IP des serveurs accessibles de l'extérieur (comme les serveurs web et de messagerie), ainsi que les services disponibles sur ces serveurs. Ils dressent ainsi une cartographie du système d'information. 

En parallèle, les attaquants exploitent des informations sociales obtenues par ingénierie sociale, en ciblant les employés de l'entreprise, les prestataires, et les services. Par exemple, ils peuvent utiliser les réseaux sociaux pour identifier les membres de l'organisation et les informations qu'ils partagent publiquement, comme leurs rôles, leurs coordonnées, et leurs habitudes de travail. L'objectif est de trouver des points d'entrée et des vulnérabilités humaines.

#### Méthodes de Récolte

- **Récolte Passive** : Cette méthode consiste à recueillir des informations sans interagir directement avec le système cible, ce qui la rend discrète et difficile à détecter. Les attaquants utilisent des moteurs de recherche pour trouver des informations publiques sur la cible, des bases de données accessibles (comme celles contenant des informations sur les noms de domaine), et les réseaux sociaux pour obtenir des données personnelles sur les employés.

  Par exemple, un attaquant peut utiliser des outils comme Shodan pour scanner des adresses IP à la recherche de services et de systèmes exposés. Ils peuvent également consulter les archives de sites web comme Archive.org pour obtenir des versions précédentes de sites web, qui peuvent contenir des informations précieuses sur l'infrastructure de l'entreprise.

- **Récolte Active** : Cette méthode implique l'utilisation d'outils spécifiques pour interroger directement la cible. Bien que plus efficace, cette méthode est moins discrète et peut être détectée par les systèmes de sécurité de l'entreprise. Les attaquants peuvent utiliser des outils comme Nmap pour scanner les ports ouverts et les services actifs sur les serveurs de l'entreprise, ou lancer des attaques de phishing pour obtenir des informations d'identification.

  Par exemple, un attaquant peut envoyer des courriels de phishing ciblés à des employés spécifiques, contenant des liens vers des sites web factices conçus pour capturer leurs informations de connexion. Ils peuvent également utiliser des malwares pour infecter les systèmes et recueillir des informations directement à partir de l'intérieur du réseau.

### 2. Identification des Vulnérabilités

Une fois les informations recueillies, les attaquants passent à l'analyse de ces données pour identifier les vulnérabilités exploitables. Cette phase est cruciale car elle permet de déterminer les points faibles du système cible et d'évaluer les chances de succès de l'attaque.

#### Types de Vulnérabilités

Les vulnérabilités peuvent être de nature technique ou non technique, et elles affectent la confidentialité, l'intégrité, et la disponibilité des systèmes d'information.

- **Failles Techniques** : Ce sont des faiblesses dans le système lui-même, telles que des configurations de serveur incorrectes, des systèmes d'exploitation non mis à jour, ou des failles dans les applications. Par exemple, une mauvaise configuration de serveur pourrait permettre à un attaquant d'accéder à des fichiers sensibles ou de prendre le contrôle du serveur.

  Un exemple courant de faille technique est la vulnérabilité de type SQL injection, où un attaquant peut injecter du code malveillant dans une requête SQL pour accéder à la base de données et manipuler ou voler des données.

- **Failles Non Techniques** : Ces failles sont liées aux comportements humains et aux processus organisationnels. Elles incluent des mots de passe faibles, des droits d'utilisateur trop permissifs, et des pratiques de sécurité inadéquates. Par exemple, un employé utilisant un mot de passe simple et facile à deviner expose l'entreprise à un risque élevé d'intrusion.

  Un exemple de faille non technique est l'ingénierie sociale, où un attaquant manipule les employés pour obtenir des informations confidentielles. Par exemple, un attaquant pourrait se faire passer pour un membre du service informatique et demander des informations de connexion sous prétexte de maintenance.

#### Évaluation des Vulnérabilités

Les attaquants utilisent divers outils pour identifier et évaluer les vulnérabilités. Des scanners de vulnérabilités comme Nessus ou OpenVAS peuvent être utilisés pour analyser les systèmes et identifier les failles. Les résultats de ces analyses permettent aux attaquants de planifier leurs attaques en fonction des faiblesses découvertes.

### 3. Exploitation des Failles

Une fois les vulnérabilités identifiées, les attaquants passent à l'exécution de l'attaque. L'exploitation des failles peut prendre différentes formes, selon la nature de la vulnérabilité et les objectifs de l'attaquant.

#### Types d'Exploitation

- **Injection de Code Malveillant** : Les attaquants peuvent injecter du code malveillant dans les applications ou les systèmes d'exploitation vulnérables pour en prendre le contrôle. Par exemple, une vulnérabilité de type buffer overflow peut être exploitée pour exécuter du code arbitraire sur le système cible.

  Un exemple courant est l'exploitation des failles de type XSS (cross-site scripting) dans les applications web, où un attaquant injecte du code JavaScript malveillant pour voler des cookies de session ou rediriger les utilisateurs vers des sites malveillants.

- **Attaques par Déni de Service (DDoS)** : Les attaquants peuvent viser la disponibilité des systèmes en lançant des attaques par déni de service, qui saturent les ressources du système cible et le rendent inaccessible. Par exemple, une attaque DDoS peut inonder un serveur web de requêtes, le faisant planter et empêchant les utilisateurs légitimes d'accéder au site.

  Un exemple est l'utilisation de botnets, où un grand nombre de dispositifs compromis sont utilisés pour envoyer un volume massif de trafic vers le système cible, le rendant indisponible.

- **Vol d'Informations** : Les attaquants peuvent voler des informations sensibles en exploitant des vulnérabilités dans les bases de données ou en utilisant l'ingénierie sociale. Par exemple, une base de données vulnérable peut permettre à un attaquant d'extraire des informations personnelles ou financières.

  Un exemple est l'attaque sur Equifax en 2017, où des attaquants ont exploité une vulnérabilité dans une application web pour accéder à des informations personnelles de plus de 140 millions de personnes.

### 4. Maintien de l'Intrusion

Après avoir réussi à s'introduire dans le système, l'attaquant cherche à maintenir son accès pour de futures actions malveillantes. Cette étape est essentielle pour garantir que l'attaquant puisse revenir dans le système sans être détecté.

#### Techniques de Maintien

- **Porte Dérobée (Backdoor)** : Les attaquants installent des malwares ou des rootkits qui permettent un accès continu et discret au système. Ces portes dérobées sont conçues pour se lancer automatiquement à chaque démarrage du système, garantissant ainsi un accès persistant.

  Par exemple, un attaquant peut utiliser un rootkit pour modifier le noyau du système d'exploitation et masquer la présence du malware, rendant sa détection extrêmement difficile.

- **Élévation des Privilèges** : L'attaquant cherche à obtenir des droits élevés sur le système pour exécuter des actions administratives. Cela peut impliquer l'exploitation de vulnérabilités supplémentaires pour obtenir un accès root ou administrateur.

  Un exemple est l'utilisation d'une attaque de type privilege escalation, où un attaquant utilise des failles dans le système pour obtenir des droits plus élevés que ceux initialement obtenus.

- **Déplacement Horizontal** : Une fois dans le système, l'attaquant explore le réseau interne pour accéder à d'autres systèmes et ressources. Cela permet à l'attaquant d'étendre son contrôle et de compromettre davantage d'éléments du réseau.

  Par exemple, un attaquant qui a compromis un poste de travail peut utiliser des outils comme Mimikatz pour voler des informations d'identification et accéder à d'autres systèmes sur le réseau.

### 5. Effacement des Traces

Pour éviter d'être détecté et pour compliquer les efforts de remédiation, l'attaquant efface toutes les traces de son intrusion. Cette étape est cruciale pour assurer l'anonymat de l'attaquant et pour prolonger la durée de l'intrusion.

#### Techniques d'Effacement

- **Effacement des Fichiers Journaux** : L'attaquant supprime ou modifie les journaux d'événements du système pour éliminer les preuves de son activité. Les journaux d'événements contiennent des enregistrements de toutes les actions effectuées sur le système, et leur manipulation permet de masquer l'intrusion.

  Par exemple, un attaquant peut utiliser des scripts pour automatiser la suppression ou la falsification des logs,

 rendant son activité indétectable.

- **Falsification des Fichiers Journaux** : En plus de supprimer les logs, l'attaquant peut les falsifier pour créer de fausses pistes et détourner l'attention des enquêteurs. Cela complique l'analyse forensique et rend plus difficile l'identification de l'attaquant.

  Un exemple est l'utilisation d'outils pour modifier les horodatages et les contenus des logs, créant ainsi une fausse chronologie des événements.

- **Anonymisation en Amont** : Avant même de lancer l'attaque, l'attaquant prend des mesures pour anonymiser ses actions, comme l'utilisation de VPN, de proxies, et de services anonymes pour masquer son adresse IP et ses traces numériques.

  Par exemple, un attaquant peut utiliser le réseau Tor pour masquer son emplacement et rendre plus difficile la traçabilité de ses actions.

### Conclusion

Une cyberattaque ne se limite pas à l'intrusion initiale, mais englobe l'ensemble des étapes de préparation, d'exécution, et de dissimulation. Comprendre ces étapes permet aux responsables de la sécurité de mieux anticiper et prévenir les attaques. En identifiant et en corrigeant les vulnérabilités, en surveillant les systèmes pour détecter les activités suspectes, et en mettant en place des mesures de sécurité robustes, les organisations peuvent se protéger efficacement contre les cyberattaques. Une analyse régulière des risques et des vulnérabilités est essentielle pour maintenir un haut niveau de sécurité et pour prévenir les intrusions.


# 2 -  (Les Logiciels Utilisés) - Étapes d'une Attaque Informatique et 

| Phase                        | Description                                                                                                                                                                     | Exemples de Logiciels Utilisés                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Récolte des Informations** | **Informations Techniques et Sociales** : Collecte des données sur la cible par des moyens passifs et actifs.                                                                   | Nmap, Recon-ng, Shodan, Maltego, theHarvester, FOCA, SpiderFoot        |
|                              | **Méthodes de Récolte Passive** : Utilisation de moteurs de recherche, bases de données et réseaux sociaux pour obtenir des informations.                                      | Google Dorks, LinkedIn, Facebook, Whois, DNSDumpster                   |
|                              | **Méthodes de Récolte Active** : Utilisation d'outils spécifiques pour interroger directement la cible.                                                                        | Nmap, Nessus, OpenVAS, Nikto, Metasploit                               |
| **Identification des Vulnérabilités** | Analyse des informations collectées pour trouver des failles exploitables.                                                                                                          | Nessus, OpenVAS, Nexpose, Burp Suite, ZAP, Acunetix, SQLMap            |
| **Exploitation des Failles** | **Injection de Code Malveillant** : Utilisation de vulnérabilités pour exécuter du code malveillant sur la cible.                                                              | Metasploit, SQLMap, BeEF, ExploitDB, Commix, XSSer                     |
|                              | **Attaques par Déni de Service (DDoS)** : Saturation des ressources du système cible pour le rendre inaccessible.                                                               | LOIC, HOIC, Slowloris, Hping, DDoS-Guard, PyLoris                      |
|                              | **Vol d'Informations** : Exploitation des failles pour accéder et voler des informations sensibles.                                                                            | SQLMap, Hydra, John the Ripper, Wireshark, Aircrack-ng                 |
| **Maintien de l'Intrusion**  | **Porte Dérobée (Backdoor)** : Installation de malwares pour un accès continu et discret.                                                                                      | Metasploit, Netcat, Empire, Cobalt Strike, Mimikatz                    |
|                              | **Élévation des Privilèges** : Exploitation des vulnérabilités pour obtenir des droits administratifs.                                                                         | Metasploit, Mimikatz, PowerSploit, Dirty COW, WinPwn                   |
|                              | **Déplacement Horizontal** : Exploration du réseau interne pour compromettre d'autres systèmes.                                                                               | BloodHound, CrackMapExec, Responder, Impacket, smbclient               |
| **Effacement des Traces**    | **Effacement des Fichiers Journaux** : Suppression ou modification des logs pour éliminer les preuves.                                                                        | Metasploit, CCleaner, BleachBit, Log Cleaner, PowerShell scripts       |
|                              | **Falsification des Fichiers Journaux** : Modification des logs pour créer de fausses pistes.                                                                                  | Metasploit, Auditpol, EventLog Explorer, Klog                          |
|                              | **Anonymisation en Amont** : Utilisation de techniques pour rester anonyme et masquer les traces numériques.                                                                  | Tor, VPNs, ProxyChains, Whonix, Tails                                  |

### Description des Logiciels

1. **Nmap** : Outil de scan réseau pour découvrir les hôtes et services sur un réseau.
2. **Recon-ng** : Cadre de reconnaissance web écrit en Python, conçu pour effectuer des tâches de reconnaissance web de manière efficace et modulaire.
3. **Shodan** : Moteur de recherche pour trouver des appareils connectés à l'internet.
4. **Maltego** : Outil d'analyse de données et de cartographie de réseau qui permet de relier et de visualiser des informations provenant de diverses sources.
5. **theHarvester** : Outil de collecte d'e-mails, de noms d'utilisateurs et d'informations d'hôte ou de domaine à partir de différentes sources publiques.
6. **FOCA** : Outil de collecte d'informations et de métadonnées à partir de documents et de fichiers trouvés en ligne.
7. **SpiderFoot** : Outil d'automatisation de reconnaissance qui collecte des informations sur les cibles à partir de sources ouvertes.
8. **Google Dorks** : Techniques de recherche avancées utilisant Google pour trouver des informations sensibles.
9. **LinkedIn, Facebook** : Réseaux sociaux utilisés pour la reconnaissance sociale.
10. **Whois** : Outil de recherche d'informations sur les noms de domaine.
11. **DNSDumpster** : Outil de reconnaissance DNS.
12. **Nessus, OpenVAS, Nexpose** : Scanners de vulnérabilités pour identifier les failles dans les systèmes et applications.
13. **Burp Suite, ZAP** : Outils d'analyse et de test de sécurité pour les applications web.
14. **Acunetix** : Scanner de vulnérabilités web automatisé.
15. **SQLMap** : Outil d'automatisation de tests d'injections SQL.
16. **BeEF** : Framework pour tester les vulnérabilités XSS.
17. **ExploitDB** : Base de données d'exploits connus et de proof-of-concepts.
18. **Commix** : Outil d'exploitation des injections de commandes dans les applications web.
19. **XSSer** : Outil d'exploitation des vulnérabilités de type XSS.
20. **LOIC, HOIC** : Outils pour lancer des attaques par déni de service.
21. **Slowloris** : Outil pour lancer des attaques DoS en gardant les connexions ouvertes sur un serveur.
22. **Hping** : Outil de génération de paquets TCP/IP pour des tests et des attaques réseau.
23. **DDoS-Guard** : Outil pour protéger contre les attaques DDoS.
24. **PyLoris** : Outil pour lancer des attaques DoS sur les services web.
25. **Hydra** : Outil de force brute pour casser les mots de passe.
26. **John the Ripper** : Outil de cassage de mots de passe.
27. **Wireshark** : Analyseur de paquets réseau.
28. **Aircrack-ng** : Suite d'outils pour évaluer la sécurité des réseaux Wi-Fi.
29. **Netcat** : Outil pour lire et écrire des données sur les connexions réseau.
30. **Empire** : Framework de post-exploitation pour Windows et Unix.
31. **Cobalt Strike** : Outil de red teaming pour la simulation d'attaques avancées.
32. **Mimikatz** : Outil pour extraire des informations d'identification en mémoire sur Windows.
33. **PowerSploit** : Collection de modules PowerShell utilisés pour les tests d'intrusion.
34. **Dirty COW** : Exploit de type privilege escalation pour Linux.
35. **WinPwn** : Collection d'outils et de scripts pour l'exploitation de Windows.
36. **BloodHound** : Outil d'analyse Active Directory pour trouver les chemins d'attaque dans les réseaux Windows.
37. **CrackMapExec** : Outil de post-exploitation pour automatiser les tests Active Directory.
38. **Responder** : Outil pour la capture de noms d'utilisateur et de mots de passe sur un réseau local.
39. **Impacket** : Collection de scripts Python pour la manipulation des protocoles réseau.
40. **smbclient** : Outil pour interagir avec les partages de fichiers SMB/CIFS.
41. **CCleaner, BleachBit** : Outils de nettoyage des fichiers et des traces sur les systèmes d'exploitation.
42. **Log Cleaner** : Outil pour nettoyer les fichiers journaux.
43. **PowerShell scripts** : Scripts pour automatiser les tâches d'effacement et de modification des logs.
44. **Auditpol** : Utilitaire Windows pour la gestion des politiques d'audit.
45. **EventLog Explorer** : Outil pour visualiser et manipuler les logs Windows.
46. **Klog** : Outil pour la gestion et la manipulation des logs.
47. **Tor** : Réseau pour naviguer anonymement sur Internet.
48. **VPNs** : Réseaux privés virtuels pour masquer l'adresse IP.
49. **ProxyChains** : Outil pour enchaîner les connexions via plusieurs proxys.
50. **Whonix, Tails** : Systèmes d'exploitation conçus pour la sécurité et l'anonymat.


# 3 - Annexe - Logiciels Utilisés pour Chaque Phase d'une Attaque Informatique

#### Phase 1: Récolte des Informations

**Récolte Passive :**

1. **Google Dorks**: Techniques avancées de recherche sur Google pour trouver des informations sensibles.
2. **LinkedIn, Facebook**: Utilisés pour collecter des informations sociales et professionnelles.
3. **Whois**: Recherche d'informations sur les noms de domaine et les propriétaires.
4. **DNSDumpster**: Outil de reconnaissance DNS pour cartographier l'infrastructure d'un domaine.
5. **FOCA**: Analyse les documents pour extraire les métadonnées.

**Récolte Active :**

1. **Nmap**: Outil de scan réseau pour découvrir les hôtes et services.
2. **Nessus**: Scanner de vulnérabilités pour identifier les failles dans les systèmes.
3. **OpenVAS**: Système avancé de scan de vulnérabilités.
4. **Metasploit**: Framework pour tester les exploits et les vulnérabilités.
5. **Recon-ng**: Cadre de reconnaissance web pour automatiser la collecte de données.

#### Phase 2: Identification des Vulnérabilités

1. **Nessus**: Identifie les vulnérabilités à partir des informations collectées.
2. **OpenVAS**: Scanner de vulnérabilités open-source.
3. **Nexpose**: Plateforme de gestion de vulnérabilités.
4. **Burp Suite**: Outil de test de sécurité des applications web.
5. **ZAP (Zed Attack Proxy)**: Scanner de vulnérabilités pour les applications web.
6. **Acunetix**: Scanner de vulnérabilités web automatisé.
7. **SQLMap**: Outil d'automatisation des tests d'injections SQL.
8. **BeEF (Browser Exploitation Framework)**: Framework pour tester les vulnérabilités XSS.

#### Phase 3: Exploitation des Failles

**Injection de Code Malveillant :**

1. **Metasploit**: Exploite les vulnérabilités pour exécuter du code malveillant.
2. **SQLMap**: Utilisé pour exploiter les injections SQL.
3. **BeEF**: Exploite les vulnérabilités XSS dans les navigateurs.
4. **Commix**: Outil pour l'injection de commandes dans les applications web.
5. **XSSer**: Automatisation des attaques XSS.

**Attaques par Déni de Service (DDoS) :**

1. **LOIC (Low Orbit Ion Cannon)**: Outil pour lancer des attaques DDoS.
2. **HOIC (High Orbit Ion Cannon)**: Outil DDoS avancé.
3. **Slowloris**: Attaque DoS qui garde les connexions ouvertes sur un serveur.
4. **Hping**: Générateur de paquets TCP/IP pour des tests réseau.
5. **PyLoris**: Outil DDoS pour les services web.

**Vol d'Informations :**

1. **Hydra**: Outil de force brute pour casser les mots de passe.
2. **John the Ripper**: Outil pour casser les mots de passe.
3. **Wireshark**: Analyseur de paquets réseau.
4. **Aircrack-ng**: Suite d'outils pour évaluer la sécurité des réseaux Wi-Fi.

#### Phase 4: Maintien de l'Intrusion

**Porte Dérobée (Backdoor) :**

1. **Netcat**: Outil pour lire et écrire des données sur les connexions réseau.
2. **Empire**: Framework de post-exploitation pour Windows et Unix.
3. **Cobalt Strike**: Outil de red teaming pour simuler des attaques avancées.
4. **Mimikatz**: Extraction d'informations d'identification en mémoire.
5. **Metasploit**: Installation de portes dérobées.

**Élévation des Privilèges :**

1. **Mimikatz**: Élévation des privilèges sur les systèmes Windows.
2. **PowerSploit**: Collection de modules PowerShell pour les tests d'intrusion.
3. **Dirty COW**: Exploit de type privilege escalation pour Linux.
4. **WinPwn**: Scripts pour l'exploitation de Windows.

**Déplacement Horizontal :**

1. **BloodHound**: Analyse Active Directory pour trouver des chemins d'attaque.
2. **CrackMapExec**: Automatisation des tests Active Directory.
3. **Responder**: Capture des noms d'utilisateur et des mots de passe sur un réseau.
4. **Impacket**: Scripts pour la manipulation des protocoles réseau.
5. **smbclient**: Interagir avec les partages de fichiers SMB/CIFS.

#### Phase 5: Effacement des Traces

**Effacement des Fichiers Journaux :**

1. **CCleaner**: Nettoyage des fichiers et des traces sur les systèmes.
2. **BleachBit**: Outil de nettoyage des fichiers.
3. **Log Cleaner**: Nettoyage des fichiers journaux.
4. **Metasploit**: Modules pour effacer les traces.

**Falsification des Fichiers Journaux :**

1. **Auditpol**: Gestion des politiques d'audit sur Windows.
2. **EventLog Explorer**: Visualisation et manipulation des logs Windows.
3. **Klog**: Outil pour gérer et falsifier les logs.

**Anonymisation en Amont :**

1. **Tor**: Réseau pour naviguer anonymement.
2. **VPNs**: Réseaux privés virtuels pour masquer l'adresse IP.
3. **ProxyChains**: Chainer les connexions via plusieurs proxys.
4. **Whonix**: Système d'exploitation pour la sécurité et l'anonymat.
5. **Tails**: Système d'exploitation conçu pour la sécurité et l'anonymat.

- Cette table résume les logiciels couramment utilisés à chaque étape d'une cyberattaque, offrant ainsi un aperçu des outils disponibles pour les attaquants et des moyens de défense possibles pour les responsables de la sécurité.
