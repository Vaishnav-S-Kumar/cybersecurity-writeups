# vault-door-1

## Description

Can you open this safe?

I forgot the key to my safe but this program
is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

Put the password you recover into the picoCTF flag format.

## Solution

Download the java file using the hyperlink given in the description. Analyze the java code, the last block of code contains a encoded string which is assigned to the variable which indicates as a password.

Using ```base64 -d```, the password is retrieved. 
```
echo "phrase" | base64 -d
```

Insert the output inside the ```{...}``` of ```picoCTF{...}```.

