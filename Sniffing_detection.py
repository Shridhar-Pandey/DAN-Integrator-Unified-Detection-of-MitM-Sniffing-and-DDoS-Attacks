from scapy.all import ARP, sniff
import collections

# Define the IP range to monitor (e.g., the local subnet)
IP_RANGE = "192.168.1.0/24"

# Time window in seconds for checking ARP requests
TIME_WINDOW = 10

# Threshold for ARP requests from a single source within the time window
THRESHOLD_ARP_REQUESTS = 10

# Dictionary to track ARP requests count for each MAC address
arp_requests_count = collections.defaultdict(int)

def monitor_arp(packet):
    """Function to monitor and analyze ARP packets."""
    if packet.haslayer(ARP):
        # Check if the packet is an ARP request
        if packet[ARP].op == 1:
            # Increment the count for the MAC address making the request
            mac_address = packet[ARP].hwsrc
            arp_requests_count[mac_address] += 1

            # Check if the number of requests exceeds the threshold
            if arp_requests_count[mac_address] > THRESHOLD_ARP_REQUESTS:
                print(f"Potential sniffing attack detected from MAC address: {mac_address}")
                print(f"Number of ARP requests: {arp_requests_count[mac_address]} within {TIME_WINDOW} seconds")

# Start sniffing ARP packets on the network
sniff(filter="arp", prn=monitor_arp, store=0, timeout=TIME_WINDOW)

# Clear the ARP request count dictionary after each time window
arp_requests_count.clear()
