import socket
import struct
import time
from collections import defaultdict

# Define thresholds
THRESHOLD_PACKET_COUNT = 1000  # Adjust this based on your environment
TIME_WINDOW = 10  # Time window in seconds to check for DDoS patterns

# Initialize data structure to track IP traffic
traffic_data = defaultdict(int)

# Create a raw socket to capture all incoming packets
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

start_time = time.time()

while True:
    # Capture packets
    packet = sock.recvfrom(65565)[0]
    
    # Extract IP header
    ip_header = packet[14:34]
    ip_hdr = struct.unpack("!BBHHHBBH4s4s", ip_header)
    
    # Extract source IP address
    src_ip = socket.inet_ntoa(ip_hdr[8])
    
    # Update traffic data for the source IP
    traffic_data[src_ip] += 1
    
    # Check if the time window has elapsed
    if time.time() - start_time > TIME_WINDOW:
        for ip, packet_count in traffic_data.items():
            if packet_count > THRESHOLD_PACKET_COUNT:
                print(f"Potential DDoS attack detected from {ip} with {packet_count} packets in {TIME_WINDOW} seconds.")
        
        # Reset tracking data and timer
        traffic_data.clear()
        start_time = time.time()
