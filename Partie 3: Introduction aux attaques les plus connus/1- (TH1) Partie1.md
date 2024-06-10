# 1 - Introduction à la Cybersécurité
**Définition et Importance de la Cybersécurité**
- **Cybersécurité** : Ensemble de mesures techniques, organisationnelles, juridiques et humaines permettant de protéger les systèmes d'information, les réseaux et les données contre les cyberattaques.
- **Importance** : Protéger la confidentialité, l'intégrité et la disponibilité des données et des systèmes; assurer la continuité des opérations et protéger contre les pertes financières, les atteintes à la réputation et les impacts légaux.

**Bref Historique des Cyberattaques**
- **Premières attaques** : Le ver Morris (1988)
- **Évolution** : Des simples virus aux attaques complexes et organisées
- **Tendances récentes** : Attaques par ransomware, augmentation des DDoS, attaques ciblées sur les infrastructures critiques

# 2 - Les Attaques les Plus Connues
1. **Phishing**
   - **Définition** : Technique utilisée par les attaquants pour tromper les utilisateurs en les incitant à révéler des informations personnelles sensibles.
   - **Techniques courantes** :
     - **E-mails frauduleux** : Messages semblant provenir de sources fiables (banques, services en ligne)
     - **Faux sites web** : Imitation de sites légitimes pour voler des informations de connexion
   - **Études de cas célèbres** :
     - **Sony Pictures** : Cyberattaque en 2014 impliquant des e-mails de phishing pour accéder aux réseaux internes.
   - **Prévention** :
     - Sensibilisation et formation des utilisateurs
     - Utilisation de filtres anti-phishing et de solutions de sécurité des e-mails

2. **Malware (Logiciels Malveillants)**
   - **Types de malwares** :
     - **Virus** : Programme malveillant qui se réplique en s'attachant à d'autres fichiers exécutables.
     - **Vers** : Malware qui se réplique et se propage sans avoir besoin de s'attacher à des fichiers.
     - **Chevaux de Troie** : Programme qui semble légitime mais qui exécute des actions malveillantes.
     - **Ransomware** : Malware qui chiffre les fichiers d'un utilisateur et demande une rançon pour les déchiffrer.
     - **Spyware** : Programme qui collecte des informations sur l'utilisateur à son insu.
   - **Exemple célèbre** : **WannaCry ransomware** (2017)
     - **Impact** : Plus de 200 000 ordinateurs infectés dans 150 pays, perturbant des services essentiels.
   - **Prévention** :
     - Utilisation de logiciels antivirus et anti-malware
     - Maintien des systèmes et logiciels à jour
     - Sauvegardes régulières des données

3. **Attaques par Déni de Service (DDoS)**
   - **Définition** : Attaque visant à rendre un service indisponible en saturant les ressources du serveur cible.
   - **Méthodes** :
     - **Amplification** : Utilisation de protocoles comme DNS ou NTP pour amplifier le volume de trafic.
     - **Botnets** : Réseau de machines infectées utilisées pour lancer des attaques coordonnées.
   - **Exemple célèbre** : **Attaque DDoS contre Dyn (2016)**
     - **Impact** : Perturbation de nombreux services en ligne majeurs (Twitter, GitHub, Netflix).
   - **Stratégies de mitigation** :
     - Utilisation de services de protection DDoS
     - Mise en place de solutions de répartition de charge

4. **Man-in-the-Middle (MITM)**
   - **Définition** : Attaque où l'attaquant intercepte et peut modifier les communications entre deux parties sans qu'elles s'en rendent compte.
   - **Techniques** :
     - **Interception de communications** : Utilisation de techniques comme le spoofing ARP pour intercepter les communications réseau.
     - **Usurpation d’identité** : Se faire passer pour une des parties pour tromper l'autre.
   - **Exemple célèbre** : **Attaque contre les utilisateurs de Gmail en Iran**
     - **Impact** : Surveillance et interception des communications des utilisateurs.
   - **Prévention** :
     - Utilisation de protocoles sécurisés (HTTPS, SSL/TLS)
     - Surveillance des réseaux pour détecter les activités suspectes

5. **Injection SQL**
   - **Définition** : Technique où l'attaquant injecte des commandes SQL malveillantes dans des requêtes d'application pour manipuler les bases de données.
   - **Fonctionnement** : Exploitation des champs de saisie non sécurisés pour insérer des commandes SQL.
   - **Exemple célèbre** : **Attaque contre Heartland Payment Systems (2008)**
     - **Impact** : Vol de plus de 130 millions de numéros de cartes de crédit.
   - **Prévention** :
     - Validation et sanitation des entrées utilisateur
     - Utilisation de requêtes préparées et de procédures stockées

6. **Cross-Site Scripting (XSS)**
   - **Définition** : Attaque où des scripts malveillants sont injectés dans les pages web vues par d'autres utilisateurs.
   - **Types** :
     - **Réfléchi** : Les scripts sont reflétés par le serveur et renvoyés à l'utilisateur.
     - **Stocké** : Les scripts sont stockés sur le serveur et exécutés lors de l'affichage des pages.
     - **DOM-based** : Les scripts sont exécutés directement dans le navigateur via le DOM.
   - **Exemple célèbre** : **Ver Samy sur MySpace (2005)**
     - **Impact** : Le ver a infecté plus d'un million de comptes en un jour.
   - **Prévention** :
     - Validation et sanitation des entrées
     - Utilisation d’en-têtes de sécurité (CSP)

7. **Exploitation des Vulnérabilités**
   - **Exemple célèbre** : **Attaque contre Equifax (2017)**
     - **Vulnérabilité exploitée** : Apache Struts
     - **Impact** : Compromission de données personnelles de 147 millions de personnes.
   - **Importance des mises à jour** : Assurer que tous les systèmes et logiciels sont régulièrement mis à jour avec les derniers correctifs de sécurité.

# 4- Cas Pratiques et Études de Cas
- **Analyse détaillée d'attaques célèbres** : Étudier en profondeur les mécanismes, impacts et contre-mesures de chaque attaque.
- **Discussion des impacts et des leçons tirées** : Comprendre comment les attaques ont changé la perception et les pratiques de sécurité.

### Conclusion
- **Importance de la vigilance et de la formation continue** : Maintenir une culture de sécurité proactive.
- **Questions et réponses** : Séance de discussion interactive pour clarifier les concepts et répondre aux questions des participants.

### Ressources Supplémentaires
- **Livres recommandés** : "The Art of Deception" par Kevin Mitnick, "Cybersecurity and Cyberwar" par P.W. Singer et Allan Friedman.
- **Sites web et forums de cybersécurité** : OWASP, SANS Institute, forums de sécurité comme Stack Exchange Security.
- **Cours en ligne et certifications** : Cybrary, Coursera, certifications comme CISSP, CEH.
