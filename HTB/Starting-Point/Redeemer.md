# Redeemer
## Very Easy

## Solution

Redeemer is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
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
sudo nmap -sV -p- -T5  <IP>
```
Since nmap took time to complete the scan, ```rustscan``` was used instead
```
sudo rustscan -a 10.129.42.130
```
The output given was:
```
PORT     STATE SERVICE REASON
6379/tcp open  redis   syn-ack ttl 63
```
redis is an In-memory NoSQL Database, which means it uses Key-Value to store data making it a non-relational database.

To access redis, we use the command ```redis-cli```,
```
redis-cli -h <IP> -p <PORT> 
```
To obtain the information and statistics about the Redis server, use ```info``` and to find the keys in the database use ```keys *```.

So to print a key, use the command GET "key-name" (One of the key is the flag)

