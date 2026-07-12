# substitution2

## Description

It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?

## Solution

Download the message file and view it using '''cat''' to view the content. Upon analyzing the file, It is clear that there is no fixed pattern like ceasar's cipher or ROT13. It uses a mono-alphabetic substitution, meaning using a fixed key, and giving a one to one mapping of plaintext (P) to ciphertext (C). Additionally the words are joined together forming a single text line file.

To find the key to print the original text use frequescy analysis to find the most used alphabets in the message. use the following command to find the occurence of each character.
```
for i in {a..z}; do cat message.txt|tr '[:upper:]' '[:lower:]' |tr -cd $i| wc -c| tr -d "\n"; printf " $i \n"; done | sort -nr
```
The result for the above command would be
```
<Number of occurence> <Alphabet> 
```
Arrange the result of the above command in a single line format for example ```THYFJSIMAPQWERY...``` . Use google or chatgpt to find the list of alphabets that occur most till the one which occur least. for example it would be like ```ETAOINSHRDLUCMWYFGPBVKJXQ```

Using the default frequency analysis occurence-set "etaoinshrducmfywgpbvkxqjzETAOINSHRDUCMFYWGPBVKXQJZ"  using ```tr``` command. i.e
```
cat <filename> | tr "result-set(small & CAPS)" "etaoinshrducmfywgpbvkxqjzETAOINSHRDUCMFYWGPBVKXQJZ"
```

Provides a rough formation of the original text but would still require further modification. So after analysis, modify the occurence-set to form the original message. 

Thus after further iteration, the original message and flag is printed.
