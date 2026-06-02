# Fawn
## Very Easy

## Solution

Fawn is a linux machine, start the machine and connect to the HTB network using OpenVPN.

Start by seeing if the machine IP is reachable using ```ping```
```
ping -c 4 <IP>
```
Enumerate the IP using nmap to display the services/ports open
```
sudo nmap -sV <IP>
```
The output of the nmap scan shows that a FTP/File Tranfer Protocol port is open. The version of the FTP is vsftpd 3.0.3
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
```
Search for any known vulnerability of ftp, which allows byassing the authencation. One such vulnerability is ```Anonymous ftp``` which allows user to access the remote server by using anonymous for username and password.
```
ftp <IP>
```
After executing the above command, the prompt for username and password is shown. After logging in, use ```help``` to print the commands available in ftp. Using the given set of commands, use ```dir``` to list the files in the ftp server and use ```get``` to download the file from remote server. 

After downloading, use ```cat``` to display the contents of the flag file.

