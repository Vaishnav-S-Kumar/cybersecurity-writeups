# Simple CTF

## Description 

Beginner Level CTF, Deploy the machine and attempt the questions!

## Walkthrough

The Simple CTF consist of multiple questions leading the user to the flags, Each question is answered after a certain step in pentesting is performed. 

Start the machine and copy the IP address. Check the IP address is reachable using ```ping```, ```-c 4``` denotes number of packets to be sent.  
```
ping -c 4 <IP address>
```
If ```4 received, 0% packet loss``` is printed as output, IP is reachable.

For enumeration, start by using nmap to scan the IP and find open ports and services.

```
sudo nmap -sV -O -v <IP address>

PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
```
After executing nmap, the output shows HTTP service running in port 80. The website can be accessed using a browser which display a ```Apache2 Ubuntu Default Page```. To find if any other directories are available, use ```gobuster```
```
gobuster dir --url <URL> --wordlist=/path/to/wordlist
```
The result of the command shows the URL has accessible directories which are ```/index.html```,```/robots.txt``` and ```/simple```. The ```/simple``` directory is uncommon directory which means a different webpage would be existing.

Access the directory by adding the directory name to the URL. The webpage displayed is proof that the website uses CMS Made Simple technology for their CMS(Content Management System), It is an application which allows users to build, manage, and publish digital content and websites without requiring advanced coding knowledge. 

CMS Made Simple 2.2.8 has CVE of Base Score 8.1, ```CVE-2019-9053```. The Vulnerability is exploited using crafted URL to achive unauthenticated blind time-based SQL injection. The Website also uses the same version of the CMS.

To gain Access to the machine/Exploit the vulnerability, Download the exploit from exploit-db. The name of the exploit is ``` CMS Made Simple < 2.2.10 - SQL Injection```.

To run the exploit, minor changes has to be made for resolving syntax error and also download certain packages inside a python virtual enviornment. To understand how to use the exploit use ```python exploit.py```
```
[+] Specify an url target
[+] Example usage (no cracking password): exploit.py -u http://target-uri
[+] Example usage (with cracking password): exploit.py -u http://target-uri --crack -w /path-wordlist
[+] Setup the variable TIME with an appropriate time, because this sql injection is a time based.
```
which prints the above. 

So the command to execute the exploit is
```
python exploit.py --url <URL> --wordlist=/path/to/wordlist --crack
```
After completing the exploit, The username, email, password salt and password was found along with the cracked password.

So since the username and password was found, it means the website has a login page. Therefore to find the login page use ```gobuster``` using the entire URL (including /simple).

The result shows another directory available in the ```/simple``` directory. Add the directory name to the URL and a login page is displayed.

Since ```ssh``` is on port 2222, the command for ```ssh``` is 
```
ssh -p 2222 <username>@<IP address>
```
The first command to try after accessing the machine is ```ls``` to list the files and directories in the current directory. Which shows a file called ```user.txt``` using ```cat``` print the contents of ```user.txt```. That is the user flag.

To see which is the current working directory, use ```pwd```. Also to find if there are other users, use the command ```users```

Next, to escalate privilege use the command ```sudo -l``` to list the users security privileges and allowed commands
```
    (root) NOPASSWD: /usr/bin/vim
```
which means the user can use sudo vim <file> without entering the password. So, to gain root privileges use ```sudo vim``` and use ```shifit key +;``` and enter the following ```!/bin/bash``` and root privilege is gained. 

use ```cd``` to change directory to ```root```, use ```ls``` to list contents of root directory and use ```cat``` to display contents of ```root.txt```. 

That is the root flag.
