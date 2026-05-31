# Vault-Door-4

## Description
This vault uses ASCII encoding for the password.

## Solution
Download the source code file using the hyperlink, analyse the code, within the code the password is not mentioned as such but is mentioned using different encodings, i.e Decimal, Hexdecimal, Octal, Character literals. The challenge relies on a common obfuscation technique: storing a string using multiple numeric representations (decimal, hexadecimal, octal, and character literals) to make it less obvious during casual code inspection. No encryption is used. 

Identify each section and its format and start decoding. After Decoding each section, assembe the strings together and add the assembled string between ```{ }``` of the ```picoCTF{}```. 

