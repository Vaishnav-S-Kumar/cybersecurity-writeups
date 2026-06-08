# Responder
## Very Easy

## Solution

Responder is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
```
sudo openvpn <openvpn file>
```
The format of completing the box is by answering the questions, the answers can be found when trying find the flag inside the machine. 

Start by seeing if the machine IP is reachable using ```ping```, 
```
ping -c 4 <IP>
```
Enumerating the machine IP using ```nmap``` to find the services/ports available but using ```-p-``` and ```-T5``` to scan all ports but at a faster rate. 
```
sudo nmap -sV -p- -sC -T5  <IP>
```

