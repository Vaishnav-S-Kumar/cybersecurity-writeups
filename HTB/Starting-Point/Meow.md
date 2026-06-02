# Meow
## Very Easy Box

## Solution

Meow is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
```
sudo openvpn <openvpn file>
```
The format of completing the box is by answering the questions, the answers can be found when trying find the flag inside the machine. 

Start by seeing if the machine IP is reachable using ```ping```, 
```
ping -c 4 <IP>
```
Enumerating the machine IP using ```nmap``` to find the services/ports available.
```
sudo nmap -sV <IP>
```
The nmap output shows the following, Which means telnet is running in port number 23
```
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
```
One of the vulnerability of telnet is that it gives access without authentication/blindly trust the user if the username is root. i.e No password is required.
```
telnet -l root <IP>
```
After connecting using telnet, use ```ls``` to list the content of the current directory. Use the ```cat``` command to print the contents of the flag file.
