# Python Wrangling

## Description 

Python scripts are invoked kind of like programs in the Terminal...
Can you run ende.py using password.txt to get flag.txt.en?

## Solution

Download the python script, password.txt and encrypted text containing file using the hyperlink.

Analyse the python script, after analysis it is clear that the script uses three options:
1. -e to encrypt
2. -d to decrypt 
3. -h to provide help statement

The format for executing the program is 
```
python3 <python script> -d/-e <filename>
```
When execution process starts a password prompt is printed, enter the password.

For finding the flag use the -d option with encrypted text contatining file in place of <filename>.
