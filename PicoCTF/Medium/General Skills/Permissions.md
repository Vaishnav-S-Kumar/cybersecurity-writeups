# Permissions

## Description

Can you read files in the root file?

The system admin has provisioned an account for you on the main server.

## Solution

Launch the instance and connect to the system using ssh. After connecting to the machine, use ```sudo -l``` to find what all permissions the user has
```
User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```
This means the user can use/run vi as a root. This could be used to perform shell escape. Basically by using ```sudo  vi test```, the file test is created/edited by a root user. 

### Explaination

Shell escape works by using the following commands, start by pressing ESC key and entering ```:!/bin/bash ```. After pressing privilege escalation is completed. Now the user has root access. 

```sudo vi test``` creates a file called test and pressing ESC provide access to command-line.
```:!/bin/bash``` tells vi to run an external command, here /bin/bash by which root shell is opened.


After gaining root access use ```cd```, ```ls``` and ```cat``` to display the flag.
