# Printer Shares

## Description

Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?

## Solution

Launch the instance, a netcat command with name of the machine and port will appear using the given information use the cmbclient command to list the different shares in the machine

Command:
```
smbclient -L //[IP/NAME]/ -N -p [Port No]
```
Here, -L stands for listing available shares, -N stands for not to ask password and -p to specify the port
The shares listed are

```

        Sharename       Type      Comment
        ---------       ----      -------
        <name 1>        Disk      Public Share With Guests
        <name 2>        IPC       IPC Service (Samba 4.19.5-Ubuntu)
```

Only one share can be publicly accessed by guest, using the smbclient command connect to the share, Command:
```
smbclient //[NAME]/[Sharename] -p [Port No] -N
```
After connecting to the machine, use the help command to find which all commands are available. 
Use ```ls``` to list the files in the directory, and using the command which is available open the <filename>.txt file with the file.
