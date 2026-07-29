# SpookyPass

## Description 

All the coolest ghosts in town are going to a Haunted Houseparty - can you prove you deserve to get in?

## Solution 

Download the zip file and unzip the .zip file using the password provided. The file inside the zip is the challenge artifact, "rev_spookypass". Inside the directory is an executable file. Run the program using the command ```./<filename>``` which prints the following:
```
Welcome to the SPOOKIEST party of the year.
Before we let you in, you'll need to give us the password:
```
To find the password, start by analysing the executable, use the strings command to print the printable characters from non-text files, such as compiled binaries, executables, or core dumps. i.e
```
strings <filename>
```
Chances of hardcoded password is very high, analyse the texts printed and find the password.

Run the program once again and enter the password which was found to print the flag.

