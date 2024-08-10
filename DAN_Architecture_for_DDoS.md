## Architecture Description
The architecture of DAN can be visualized as follows:

### Host A (Running DAN):

- Monitors traffic flow for unusual spikes in ICMP, TCP, or UDP packets that could indicate a DDoS attack.
- Uses anomaly detection and clustering to identify coordinated attack patterns.
### DDoS Detector (Extended DAN):

- Continuously analyzes network traffic to detect potential DDoS attacks.
- Sends alerts and logs incidents when suspicious traffic patterns are identified.
### Local Network (LAN):

- High-traffic environment with multiple hosts and potential attack vectors.

## Architecture Diagram

![image](https://github.com/user-attachments/assets/f67bd19d-907b-4692-8648-d72d033a0727)
