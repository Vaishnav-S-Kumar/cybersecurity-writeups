# Dancing
## Very Easy

## Solution

Dancing is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
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
The nmap output shows the following
```
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
```
The port 445 is a networking port dedicated to SMB/Server Message Block Protocol. It allows devices on same local network to share files, printers and serial communication. It allows applications to read and write files to and from remote servers. 

To proceed further, use ```smbclient``` command to connect to the machine
```
smbclient -L 10.129.36.138 -N
```
where -L is to list the available SMB shares and -N is to tell the client not to promt for a password. The result/output is
```
 Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        WorkShares      Disk      
```
Which shows that only one share is available for access without password, to access the share
```
smbclient //IP/share_name
```
After connecting, use "help" command to get a list of possible commands. Using ```cd```,```ls``` and ```get``` downlaod the flag file and use ```cat``` to display its content.
