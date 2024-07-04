## Maintenir Metasploit à Jour

### Introduction

Depuis ses débuts en 2004 avec seulement 27 exploits, Metasploit a considérablement évolué pour inclure aujourd'hui plus de 1 847 exploits. Pour bénéficier des dernières fonctionnalités, des nouveaux exploits et des modules améliorés, il est essentiel de maintenir Metasploit à jour. Ce guide vous explique comment procéder.

### Mise à Jour avec `msfupdate`

Par le passé, la commande `msfupdate` était utilisée pour mettre à jour la base Metasploit. Cependant, cette commande est désormais obsolète et ne fonctionne plus lorsque Metasploit fait partie du système d'exploitation.

```bash
root@kali:~# msfupdate 
msfupdate is no longer supported when Metasploit is part of the 
operating system. Please use 'apt update; apt install 
metasploit-framework' 
```

### Mise à Jour sous Kali Linux

Pour les utilisateurs de Kali Linux, Metasploit peut maintenant être mis à jour en utilisant le gestionnaire de paquets `apt`. Voici les étapes à suivre :

1. **Mettre à jour les sources de paquets** :
   ```bash
   root@kali:~# apt update
   ```

2. **Installer la dernière version de Metasploit** :
   ```bash
   root@kali:~# apt install metasploit-framework
   ```

3. **Lancer Metasploit pour vérifier la mise à jour** :
   ```bash
   root@kali:~# msfconsole
   ```

### Exemple de Mise à Jour

Voici un exemple complet de la mise à jour de Metasploit sous Kali Linux :

```bash
root@kali:~# apt update
Hit:1 http://kali.download/kali kali-rolling InRelease
Reading package lists... Done
Building dependency tree       
Reading state information... Done
All packages are up to date.

root@kali:~# apt install metasploit-framework
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  metasploit
The following NEW packages will be installed:
  metasploit metasploit-framework
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 200 MB of archives.
After this operation, 800 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://kali.download/kali kali-rolling/main metasploit-framework all 6.2.8-0kali1 [200 MB]
Fetched 200 MB in 10s (20.0 MB/s)                                                                             
Selecting previously unselected package metasploit-framework.
(Reading database ... 352792 files and directories currently installed.)
Preparing to unpack .../metasploit-framework_6.2.8-0kali1_all.deb ...
Unpacking metasploit-framework (6.2.8-0kali1) ...
Setting up metasploit-framework (6.2.8-0kali1) ...
Processing triggers for kali-menu (2021.2.2) ...

root@kali:~# msfconsole
```

### Vérification de la Version Mise à Jour

Après avoir lancé `msfconsole`, vous verrez l'écran de démarrage de Metasploit avec la version actuelle. Par exemple :

```
     .:okOOOkdc'           'cdkOOOko:.  
   .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.  
  :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:  
 'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'  
 oOOOOOOOO.MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo  
 dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx  
 lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl  
 .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.  
  cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc  
   oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo  
    lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl  
     ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;  
      .dOOo'WM.OOOOocccxOOOO.MX'xOOd.  
        ,kOl'M.OOOOOOOOOOOOO.M'dOk,  
          :kk;.OOOOOOOOOOOOO.;Ok:  
            ;kOOOOOOOOOOOOOOOk:  
              ,xOOOOOOOOOOOx,  
                .lOOOOOOOl.  
                   ,dOd,  
                     .  
 
       =[ metasploit v6.2.8-dev                           ] 
+ -- --=[ 1852 exploits - 1046 auxiliary - 325 post       ] 
+ -- --=[ 541 payloads - 44 encoders - 10 nops            ] 
+ -- --=[ 2 evasion                                       ] 
+ -- --=[ ** This is Metasploit 6 development branch **   ] 
 
msf6 >
```

### Conclusion

Maintenir Metasploit à jour est essentiel pour tirer parti des dernières améliorations, des nouveaux exploits et des fonctionnalités ajoutées. En utilisant le gestionnaire de paquets `apt` sous Kali Linux, vous pouvez facilement mettre à jour Metasploit et vous assurer que votre environnement de test est toujours à jour.
