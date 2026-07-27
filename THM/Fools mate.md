# Fools Mate
## Description 
Can you bypass the engine?

## Solution
Deploy the machine and connect to the network using openvpn configuration, 
```
sudo openvpn <OpenVPN config file>
```
Enumerate the IP address of the machine using nmap, i.e.
```
sudo nmap -sV -O -v -T4 <IP address>
```
The result of the nmap program is 
```

