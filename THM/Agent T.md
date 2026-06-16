# Agent T

## Description

Something seems a little off with the server. 

Agent T uncovered this website, which looks innocent enough, but something seems off about how the server responds...

## Walkthrough 

Deploy the machine and connect to the network using openvpn configuration, 
```
sudo openvpn <OpenVPN config file>
```com
Enumerate the IP address of the machine using nmap, i.e.
```
sudo nmap -sV -O -v -T4 <IP address>
```
The result of the nmap program is 
```
PORT   STATE SERVICE VERSION
80/tcp open  http    PHP cli server 5.5 or later (PHP 8.1.0-dev)
Device type: general purpose
Running: Linux 4.X|5.X
```
The website displayed for the IP address is a Admin Dashboard and the majority of the functions doesn't work. Use ```curl``` to find more details on the website through the HTTP response. 
```
curl -i <URL>
```
The response shows the php version used, the information on the php version can be used to exploit the website. The PHP version has Remote Code Execution vulnerability and can be easily accessed after running the python program. 

The exploit code can be used access the terminal of the website. After gaining remote access, use the command 
```
find / -type f -name flag.txt 2>/dev/null
```
which gives the location of the file containing the flag. Open the flag file using ```cat``` and complete the challenge.
