# substitution0

## Description 

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?

## Solution

Download the message file and view it using '''cat''' to view the content. Upon analyzing the file, it can be seen that the first line "ZGSOCXPQUYHMILERVTBWNAFJDK" consist of 26 letters meaning the first line is a key, each character is in the position corresponding to the charcter it is replaced with, i.e Z for A, G for B and so on.

To unscramble the message found in the file, use the following command 
```
cat <Filename>| tr '[:lower:]' '[:upper:]' | tr <First-line> <English Alphabets CAPITAL>
```
The ```tr '[:lower:]' '[:upper:]'``` converts lower case characters to upper case. The output is the actual message and flag
