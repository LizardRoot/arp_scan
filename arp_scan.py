import scapy.all as scapy

def scan(ip):
	arp_packet = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
	arp_packet_broadcast = broadcast/arp_packet
	ans, unans = scapy.srp(arp_packet_broadcast, timeout = 1)
	print(ans.summary())

scan('192.168.1.1/24')