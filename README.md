# DAN-Integrator-Unified-Detection-of-MitM-Sniffing-and-DDoS-Attacks
The DAN Integrator is a cutting-edge tool designed to provide comprehensive security for Local Area Networks (LANs) by detecting multiple types of network attacks, including Man-in-the-Middle (MitM), sniffing, and Distributed Denial of Service (DDoS) attacks.

# Overview
In this repository you will find a man in the middle detection tool for local area networks. 


## What is DAN?

DAN (Detection and Analysis of Networks) is a sophisticated network security tool designed to detect and analyze potential threats within Local Area Networks (LANs). Originally developed to identify Man-in-the-Middle (MitM) attacks, DAN has evolved into a versatile solution capable of detecting multiple types of network intrusions, including sniffing and Distributed Denial of Service (DDoS) attacks.

DAN operates by sending periodic probes, such as ICMP packets, to network hosts and analyzing the responses to build a profile of the network environment. By monitoring for anomalies in packet timing, ARP traffic, and overall traffic patterns, DAN can identify suspicious activities that may indicate an ongoing attack. The tool leverages advanced machine learning algorithms to distinguish between legitimate network behavior and potential threats, providing real-time alerts to network administrators.

DAN's ability to detect and respond to various attack vectors makes it an essential tool for maintaining network security, particularly in environments where the integrity and availability of network communication are critical. Its flexibility and effectiveness make DAN a valuable asset for organizations seeking to protect their network infrastructure from evolving cyber threats.

## What can DAN Do?

DAN detects Man-in-the-Middle (MitM) attacks, sniffing, and DDoS attacks within LANs by analyzing network traffic for anomalies, providing real-time alerts to protect network integrity.


## How Does DAN Work (brief)
DAN (Detection and Analysis of Networks) operates through a series of methodical steps to detect and analyze potential network threats like Man-in-the-Middle (MitM) attacks, sniffing, and DDoS attacks. Here’s a step-by-step breakdown of how DAN functions:

### 1. Probe Initiation:
DAN begins by sending a series of ICMP echo requests (pings) or ARP requests to a target host within the LAN. These probes are crafted to measure the response characteristics of the network, similar to how sonar measures distances by analyzing echoes.
### 2. Response Analysis:
The target host responds to these probes, and DAN captures the returning packets. This response includes details like packet timing, jitter, and any anomalies that may indicate interference or modification during transit.
### 3. Profile Creation:
Using the captured data, DAN creates a profile of the normal network behavior between the probing host and the target host. This profile includes baseline metrics such as round-trip time, response consistency, and packet handling characteristics of the network devices involved.
### 4. Anomaly Detection:
DAN continuously monitors network traffic by sending periodic probes and comparing the real-time responses against the established profile. Any significant deviation from the expected behavior triggers an anomaly alert. This could indicate a MitM attack, where an unauthorized intermediary is altering or delaying traffic, or sniffing activities, where ARP traffic is being manipulated.
### 5. Machine Learning Integration:
To improve accuracy, DAN employs machine learning algorithms like Local Outlier Factor (LOF). These algorithms help in distinguishing between normal network fluctuations and actual attacks by identifying patterns and outliers in the traffic data.
### 6. DDoS Detection:
For DDoS detection, DAN monitors traffic volume and patterns across the network. Unusual spikes in traffic, particularly ICMP, TCP, or UDP packets, are analyzed for signs of coordinated attack efforts, prompting alerts when necessary.
### 7. Alert and Response:
When DAN detects an anomaly, it immediately alerts network administrators. The alert includes details about the type of anomaly, the affected hosts, and the time of detection. This allows for swift investigation and mitigation.
### 8. Continuous Learning and Adaptation:
DAN’s profiling is adaptive, meaning it can learn and update its understanding of normal network behavior over time, reducing false positives and improving detection accuracy.

## Where is DAN Deployed?

- **Host A (Network Endpoints)**: DAN is deployed on individual network hosts to monitor and protect specific links within a LAN.
- **Network Gateway (Router)**: DAN can be installed on the network gateway to monitor and secure inbound and outbound traffic.
- **Entire LAN**: For comprehensive protection, DAN can be deployed across all hosts within a LAN.

## Architecture Diagram

![image](https://github.com/user-attachments/assets/a7f31076-6049-4978-9f4e-36aa7ba84ea5)


# The DAN Tool

## Implementation Notes: 

* This is a python implementation of DAN which wraps C/C++ code using cython. The C/C++ code is used to perform the ICMP probing quickly and accurately.
* This implementation uses local outlier factor (LOF) for anomaly detection (BlackHat'19) and not autoencoders (NDSS'18).
* The current version of DAN has been tuned to detect all of these cases except IP-DH where the exact same model is being used (i.e., the tool can detect the difference between two different 1Gps switches, but not identical ones). The tuned version will be released at a later date.  
* This tool currently does not currently implement detection of attacks on DAN itself. 
* The source code has been tested with Python 2.7.12 on a Linux 64bit machine (Kali). To port the tool to Windows, some C++ libraries must be changed.
* Python dependencies: prettytable, cython  

To install prettytable and cython, run this in the terminal:
```
pip install prettytable cython
```
 


## Using the Tool
Since the tool uses raw sockets, you **must** run DAN with sudo privileges. For example:
```
$ sudo python DAN.py
```

The first time you run DAN.py, cython will compile the necessary C++ libraries. When launched, DAN will monitor the IPv4 addresses in the local file IPs.csv, unless a target IP address is provided as an argument. A profile is trained for each host and is saved to disk (automatically retrieved each time the tool is started). The configuration of the last run is saved to disk (except the real-time plotting toggle argument). Note, this tool only works when monitoring a link contained within a LAN (switches only). Do not provide external IPs.

For complete instructions on how to use DAN, type into the command line
```
$ python DAN.py -h

usage: DAN.py [-h] [-i [I [I ...]]] [-t T] [-p] [-f F] [-r R] [-w W]
                 [--reset]

optional arguments:
  -h, --help      show this help message and exit
  -i [I [I ...]]  Monitor the given IP address(es) <I> only. If an IP's profile exists on disk, it will be loaded and used.
                  You can also provide the path to a file containing a list of IPs, where each entry is on a separate line.
                  Example: python DAN.py -i 192.168.0.12
                  Example: python DAN.py -i 192.168.0.10 192.168.0.42
                  Example: python DAN.py -i ips.csv
  -t T            set the train size with the given number of probes <T>. If profiles already exist, the training will be shortened or expanded accordingly. a
                  Default is 200.
                  Example: python DAN.py -i 192.168.0.12 -t 400
  -p              Plot anomaly scores in real-time. 
                  Example: python DAN.py -p
  -f F            load/save profiles from the given directory <F>. If is does not exist, it will be created. 
                  Default path is ./DAN_profiles.
  -r R            Sets the wait time <R> between each probe in milliseconds. 
                  Default is 0.
  -w W            Sets the sliding window size <W> used to average the anomaly scores. A larger window will provide fewer false alarms, but it will also increase the detection delay. 
                  Default is 10.
  --reset         Deletes the current configuration and all IP profiles stored on disk before initializing DAN.
```


# TO DO
* Add adversarial detection
* Tune hyperparemeters to differentiate between same model devices
* Port to Windows
* Decrease false alarms by introducing custom thesholds (currently using sklearn's lof built-in threshold)

