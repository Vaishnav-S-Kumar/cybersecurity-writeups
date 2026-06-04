# Crocodile
## Very Easy Box

## Solution

Crocodile is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
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
the output of following nmap is,
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.17.194
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Smash - Bootstrap Business Template
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-favicon: Unknown favicon MD5: 1248E68909EAE600881B8DB1AD07F356
Service Info: OS: Unix
```
Search for any known vulnerability of ftp, which allows byassing the authencation. One such vulnerability is ```Anonymous ftp``` which allows user to access the remote server by using anonymous for username and password.

After logging into the ftp platform using ```ftp <IP>```, use ```help``` command to print allowed commands in ftp. Using ```get``` command download the needed files locally, i.e
```
get <file-name>
```
Now using the IP, access the website since http service is running in port 80. Enumerate the website to find more directories using gobuster
```
gobuster dir --wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt  -u http://<IP>/ -x php,html
```
- ```dir``` is to specify directory/file enueration mode
- ```-u``` to specify the url for enumeration 
- ```--wordlist``` to specify path of the wordlist
- ```-x``` to specify the file extension to search for

After executing the command, one of the directory is a login directory. Access the directory and enter the credentials found in the file from the ftp platform.

The flag is found after logging in as the highest privileged user from the list.
