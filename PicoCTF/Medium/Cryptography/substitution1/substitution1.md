# substitution1

## Description 

A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.

## Solution

Download the message file and view it using '''cat''' to view the content. Upon analyzing the file, It is clear that there is no fixed pattern like ceasar's cipher or ROT13. It uses a mono-alphabetic substitution, meaning using a fixed key, and giving a one to one mapping of plaintext (P) to ciphertext (C).

To find the key to print the original text use frequescy analysis to find the most used alphabets in the message. use the following command to find the occurence of each character.
```
for i in {A..Z}; do cat message.txt|tr '[:lower:]' '[:upper:]' |tr -cd $i| wc -c| tr -d "\n"; printf " $i \n"; done | sort -nr
```
he result for the above command would be
```
<Number of occurence> <Alphabet> 
```
Arrange the result of the above command in a single line format for example ```THYFJSIMAPQWERY...``` . Use google or chatgpt to find the list of alphabets that occur most till the one which occur least. for example it would be like ```ETAOINSHRDLUCMWYFGPBVKJXQ```

Also additional information can be found after we try to replace small words with common words such as "yar" is "the" etc. Using these infomation, construct a ```tr``` command. i.e 

```
cat <filename> | tr <result-set> <occurence-set>
```
Modify  the occurence-set until and unless a clear message appears, thus the flag is found.

 
