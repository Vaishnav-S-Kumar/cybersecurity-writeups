# Agent Sudo

## Description
You found a secret server located under the deep sea. Your task is to hack inside the server and reveal the truth. 
The task is simple, capture the flags just like the other CTF room. Have Fun!

## Walthrough

The Challenge consist of different section with different set of objectives and questions.

Start the machine and copy the IP address. Check the IP address is reachable using ```ping```, ```-c 4``` denotes number of packets to be sent.  
```
ping -c 4 <IP address>
```
If ```4 received, 0% packet loss``` is printed as output, IP is reachable.

For enumeration, start by using nmap to scan the IP and find open ports and services.
```
sudo nmap -sV -sC -O -v <IP Address>

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
|   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
|_  256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Annoucement
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

```
The output shows that 3 ports are open and one of port has HTTP services meaning website is hosted using the IP. The website displayed the following text
```
Dear agents,

Use your own codename as user-agent to access the site.

From,
Agent R
```

Capture the request using burpsuite, the request looks like the following
```
GET / HTTP/1.1
Host: 10.113.151.114
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```
Change the ```User-agent``` and try different alphabets. Use Intruder with the wordlist of entire english alphabets. When one of the alphabet is used the output/response changes slightly. An additional attribute called ```location``` is also displayed in the repsonse. 

Use the ```location``` value and use it as web directory in the URL. A different page will appear.

The content of the page is 
```
Attention <name>,

Do you still remember our deal? Please tell agent <alphabet> about the stuff ASAP. Also, change your god damn password, is weak!

From,
Agent R 
```
As we discovered earlier, FTP and SSH is open therefore <user> could be one of the users. To find the password use hydra, which is a brute forcing tool.
```
hydra -l <user> -P /path/to/wordlist <IP address> ftp
```
After completing the process, the password for FTP login is printed/outputed to the terminal.

The FTP portal has 3 files one txt and 2 image file (png & jpg). 

The text file showed the following
```

Dear agent J,

All these alien like photos are fake! Agent R stored the real picture inside your directory. Your login password is somehow stored in the fake picture. It shouldn't be a problem for you.

From,
Agent C

```

To see if there is any embeded file use ```binwalk``` on both images
