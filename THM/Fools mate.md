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
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Node.js Express framework
```
Open the website hosted using the IP address, The website shows a chess board with an incomplete set, like a custom game. The rook can be shifted to the end row for checkmate but when tried, the following message pops up;
```
I'll shut down your PC if you play that.
```
To find the way to checkmate, understand how the request is sent. 

Open burpsuite and capture a request by moving an peice without checkmating the black king, the request is in the form of JSON;
```
{"from":"g2","to":"g4"}
```
Change the"from" and "to" to the position of the rook from the starting to the position where it can checkmate the king. 

The request is allowed by the website and black is defeated, revealing the flag.
