# Appointment
## Very Easy

## Solution

Appointment is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
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
sudo nmap -sV -v 10.129.42.166
```
The output given was:
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
```
This means the IP has a website running on port 80, which uses ```http```, upon visiting the website using a browser a log in page is shown. 

Since the login pages are tested using ```SQL Injection```, try sql injection payloads like '-- or '# at the end admin, administrator. 

After successfully logging in, the flag is displayed in the page.
