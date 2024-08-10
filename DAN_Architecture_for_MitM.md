## Architecture Description
The architecture of DAN can be visualized as follows:

### Host A (Running DAN):

- Sends a burst of ICMP packets to a target host on the LAN.
- Processes the response packets to profile the network link using an anomaly detection algorithm.
- Stores profiles for future reference and comparison.
### Target Host (Host B):

- Receives the ICMP packets from Host A and sends back a response.
### MitM Detector (DAN):

- Continuously monitors the link between Host A and Host B.
- Detects deviations in packet timing and profiles to identify potential MitM attacks.
### Local Network (LAN):

- Contains multiple hosts including Host A and Host B, connected through switches and routers.
### Detection Process:

- DAN uses a technique inspired by acoustic signal processing to model the network environment.
- ICMP packets act as "probes," and the returning signals are analyzed for timing anomalies and environmental changes.

## Architecture Diagram

![image](https://github.com/user-attachments/assets/a72c3201-cbe0-46ac-a815-dfbc48d30457)
