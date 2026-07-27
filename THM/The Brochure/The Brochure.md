# The Brochure

## Description

The brochure's hero photo has an AI fingerprint. Follow the account that posted it, and the trail doesn't end at the hotel; it ends at someone the hotel never mentioned.

## Solution

Join the room and download the zip file using the ```Download Task File``` button, unzip the zip file to find the png image of the brochure. The brochure says the following "Some things aren't posted. Some clues are. Find us on instagram or not.

So to find the flag, search for the account of Byte Lotus Resort on instagram, the accound operates under the accound handle @thebytelotusresort. In the account, there is 2 photos and the account follows only 1 person/account ```vera``` under the account handle @veratheconcierge. 

When checking Vera's account, the post captions as well images are showing base64 encoded text. Each post also starts with part and a number, which means the flag is divided and then each part is converted to base64 text.

To retrieve the original flag, convert the found text using.

```
echo <text> | base64 -d
```

After finishing all the parts, join the retrieved text according to the numerical order given in the post.
 
