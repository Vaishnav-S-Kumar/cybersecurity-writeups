# Transformation

## Description

I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Solution

Download the encrypted textg using the hyperlink in the challenge. From the description it is clear that the string of code tranformed the flag into the encrypted text which consist of chinese text:
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽                                                                              ```
Step 1:

Analyse and elaborate the single line code.
```
chrc=[]
for i in range(0,len(flag),2):
    ord1=ord(flag[i])<<8
    ord2=ord(flag[i+1])

    ord_final=ord1+ord2
    charcter=chr(ord_final)
    chrc.append(character)
result= ''.join(chrc)
```
Step 2: Create Program flow
### Program flow
```
        Empty list Created
                |
                v
        For Loop initiated
                |
                v
    ord() converts characters to ASCII
        [ord value shifted left by 8]
                |
                v
        Sum of ASCII Value 
                |
                v
    chr() converts ASCII to character
                |
                v
        adds ouput to list
                |
                v
    joins list elements to form string
```
Step 2: Create a script to reverse the output,

```
ecoded="<text>"
result= []
for ch in encoded:
    print(ch)
    value = ord(ch)

    first_char = chr(value >> 8)
    second_char = chr(value & 0xff)

    result.append(first_char)
    result.append(second_char)

Flag = ''.join(result)

print(Flag)
```
Step 3: change variable values and run the program
