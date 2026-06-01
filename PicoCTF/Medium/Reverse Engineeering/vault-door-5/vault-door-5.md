# vault-door-3

## description

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding!

## Solution

Download the source code of the progam using the hyperlink, Analyse the code. The public function has a set of encoded strings (3 string sets), Each string is URL encoded and later encoded using baase64. Therefore to get the original string, decode the given string using cyberchef.io by using the options ```from Base64``` and ```URL Decode```. Combine the three strings together to form the original string. Thus, by adding the original string between ```{ }``` in ```picoCTF{}``` is the flag for the challenge. 

