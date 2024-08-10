## Architecture Description
The architecture of DAN can be visualized as follows:

### Host A (Running DAN):

- Monitors ARP traffic on the LAN for anomalies that could indicate ARP poisoning or sniffing attacks.
- Uses machine learning to identify patterns associated with sniffing activities.
### MitM Detector (Extended DAN):

- Detects unusual patterns in network traffic that suggest packet sniffing.
- Alerts the user when a potential sniffing attack is detected.
### Local Network (LAN):

- Multiple hosts connected through switches and routers, with ARP traffic being monitored.

## Architecture Diagram

![image](https://github.com/user-attachments/assets/452be2ef-b500-4920-8829-62b1e4aaabb9)
