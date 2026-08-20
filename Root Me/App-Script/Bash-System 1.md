# Bash - System 1

## Challenge Details
<table>
<tr><td>SSH access</td><td>ssh -p 2222 app-script-ch11@challenge02.root-me.org</td></tr>
<tr><td>Username</td><td>app-script-ch11</td></tr>
<tr><td>Password</td><td>app-script-ch11</td></tr>
</table>

## Walkthrough

Connect to the machine using SSH, use the above details. Use ```ls``` to view the contents of current directory.

The current directory contains a C program and the exectuable form of the C program. View the program using ```cat```. The Program is as follows;
```
include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
 
int main(void)
{
    setreuid(geteuid(), geteuid());
    system("ls /challenge/app-script/ch11/.passwd");
    return 0;
}
```
So, the program executable is used to perform ```ls``` on ```/challenge/app-script/ch11/,passwd```. To complete machine, the secret code from the .passwd file is needed but the file has following permissions.
```
-r--------  1 app-script-ch11-cracked app-script-ch11   14 Dec 10  2021 .passwd
```
Thus to view content of the file, the executable can be used since it has SUID bit, which basically grants the users sudo privileges while running the program.
```
-r-sr-x---  1 app-script-ch11-cracked app-script-ch11 7252 Dec 10  2021 ch11
```

To make the program print ,passwd content, use the following steps.

1. Determine the source file of cat using ```which cat```
2. Create a directory "Cmd" in /tmp folder.
3. Create a copy of cat file in /tmp/Cmd and name it as ```ls```
4. Set the PATH variable to /tmp/Cmd by using the command ```export PATH=/tmp/cmd```
5. Run the excutable file to print the contents of .passwd. 

The PATH variable is used by the OS to find the location of the command's source code. By changing the PATH vairbale to our desired directory (which has the source code of ```cat``` in the name of ```ls```), basically prints the contents of the file mentioned in the program instead of the ```ls``` command.
