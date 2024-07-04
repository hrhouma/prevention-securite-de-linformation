## Les Phases d'un Test d'Intrusion

Les tests d'intrusion, ou pentests, sont des évaluations méthodiques de la sécurité informatique d'un système ou d'un réseau. Ils se déroulent en plusieurs phases bien définies, permettant de s'assurer que toutes les failles potentielles sont identifiées et traitées. Voici les principales phases d'un test d'intrusion selon la méthodologie PTES (Penetration Testing Execution Standard).

### 1. Engagements Préalables (Pre-engagement)

Cette phase initiale est cruciale car elle définit le cadre et les objectifs du test d'intrusion. Elle inclut :
- **Définition du périmètre** : Quelles sont les cibles spécifiques ?
- **Calendrier** : Quelles sont les dates et heures des tests ?
- **Type de tests** : S'agit-il de tests externes, internes, Wi-Fi, etc. ?
- **Niveau de connaissance** : Boîte noire, boîte grise, boîte blanche ?
- **Type d'application** : Environnement de production, préproduction, développement ?

Le client peut également imposer des limites, par exemple, interdire les tests de déni de service (DoS) sur des systèmes en production. Les contacts techniques sont établis pour répondre aux questions et résoudre les problèmes éventuels pendant les tests. Enfin, un mandat d'autorisation est rédigé et approuvé par toutes les parties.

### 2. Collecte de Renseignements (Intelligence Gathering)

Durant cette étape, l'auditeur collecte des informations sur le système cible, simulant ainsi le comportement d'un attaquant. Cela inclut :
- **Informations techniques** : Produits utilisés, versions, configurations.
- **Environnement de sécurité** : Pare-feu, VPN, CDN, etc.

Les techniques d'OSINT (Open Source Intelligence) sont souvent utilisées, bien que l'HUMINT (Human Intelligence) soit également une option, notamment pour le social engineering.

### 3. Modélisation des Menaces (Threat Modeling)

Cette phase consiste à identifier et évaluer les risques potentiels pour le périmètre audité. Il s'agit d'une analyse de risque qui prend en compte :
- **Faiblesses** : Quelles sont les vulnérabilités identifiables ?
- **Menaces** : Quels types d'attaques pourraient être envisagés ?
- **Impact** : Quelle serait la gravité de ces attaques ?

La norme ISO/CEI 27005 peut être utilisée comme guide pour ce processus.

### 4. Analyse des Vulnérabilités (Vulnerability Analysis)

Ici, l'auditeur combine les informations recueillies lors des phases précédentes pour rechercher des vulnérabilités. Cela peut se faire de manière :
- **Automatique** : Utilisation de scanneurs de vulnérabilités.
- **Manuelle** : Recherche approfondie et tests spécifiques.

Le but est de construire des scénarios d'attaque réalistes.

### 5. Exploitation (Exploitation)

Cette phase met en pratique les scénarios d'attaque développés. L'auditeur tente de :
- **Exploiter** : Utiliser les vulnérabilités identifiées pour accéder au système.
- **Contourner** : Éviter les mesures de sécurité en place.

### 6. Post-exploitation

Après la compromission initiale, l'auditeur cherche à :
- **Élever les privilèges** : Obtenir des droits supplémentaires.
- **Maintenir l'accès** : Assurer une présence continue sans être détecté.
- **Compromettre d'autres systèmes** : Étendre l'attaque à d'autres parties du réseau.

### 7. Rédaction du Rapport (Reporting)

La phase finale consiste à documenter l'ensemble du processus et des résultats. Le rapport doit être :
- **Exhaustif** : Détail de toutes les étapes et découvertes.
- **Compréhensible** : Mélange de termes techniques et non techniques.
- **Précis** : Recommandations claires pour remédier aux vulnérabilités.

Ce rapport est essentiel car il constitue souvent le seul moyen pour le client de vérifier la qualité du travail effectué.

### Méthodologie OWASP Testing Guide

En plus de la méthodologie PTES, l'OWASP Testing Guide est une autre référence importante, spécialement orientée vers les tests d'applications web et mobiles. Elle inclut des sections comme :
- **Information Gathering**
- **Configuration and Deployment Management Testing**
- **Identity Management Testing**
- **Authentication Testing**
- **Authorization Testing**
- **Session Management Testing**
- **Input Validation Testing**
- **Testing for Error Handling**
- **Testing for Weak Cryptography**
- **Business Logic Testing**
- **Client Side Testing**

### Conclusion

Les tests d'intrusion sont un élément crucial pour assurer la sécurité des systèmes informatiques. En suivant des méthodologies structurées comme PTES ou l'OWASP Testing Guide, les auditeurs peuvent identifier et corriger efficacement les vulnérabilités, contribuant ainsi à renforcer la résilience des infrastructures contre les attaques potentielles.

+------------------------------------------------+
|      Pre-engagement (Engagements Préalables)    |
+------------------------------------------------+
                      |
                      ↓
+------------------------------------------------+
| Intelligence Gathering (Collecte de Renseignements) |
+------------------------------------------------+
                      |
                      ↓
+------------------------------------------------+
|      Threat Modeling (Modélisation des Menaces)   |
+------------------------------------------------+
                      |
                      ↓
+------------------------------------------------+
| Vulnerability Analysis (Analyse des Vulnérabilités) |
+------------------------------------------------+
                      |
                      ↓
+------------------------------------------------+
|           Exploitation (Exploitation)           |
+------------------------------------------------+
                      |
                      ↓
+------------------------------------------------+
|         Post-exploitation (Post-exploitation)   |
+------------------------------------------------+
                      |
                      ↓
+------------------------------------------------+
|         Reporting (Rédaction du Rapport)        |
+------------------------------------------------+
