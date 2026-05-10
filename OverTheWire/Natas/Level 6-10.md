# Natas

Find the password from the website, No SSH login.

## Level 6

The text displayed in the website is
```
 Input secret: 
```
It has a input form with submit query button. Also it has a view sourcecode hyperlink which displays the source code. A script used in the source code to validate the input is 
```
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```
thus if we add the file to the URL and select the source code of the file page, the secret is shows. Enter the secret in the input form and password is displayed.

## Level 7

There are two hyperlinks present in the page, ```home``` and ```about```
```
Home

This is the front page 
```
and 
```
About 

This is the about page
```
As the page changes, the URL also changes ```http://natas7.natas.labs.overthewire.org/index.php?page=<name>``` the <name> can be about or home. Which could mean this could be a injection point, to find the right payload start by checking the source code. The code contains a comment with a file path. Place the file path in place of <name>.

## Level 8

Level 8 has the same layout as level 6 and also have a view sourcecode hyperlink which displays the source code. The php script in the source code is 
``` 
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

Here the secret hardcoded is the encoded version which is passed through multiple, The process is 
1. Convert secret input to base64
2. Reverse the base64 text
3. Convert the text into Hexadecimal

So to get original text, the following process should be done using cyberchef. 
1. Convert the text using ```From Hex``` option
2. Reverse the text using ```reverse``` 
3. Decode the text using ```From Base64``` option

Enter the final text into the input form in the website and submit, The password for the next level is displayed.

## Level 9

The text displayed in this level is 
```
Find words containing: 
```
Along with a input form and a search button. The function of the website is to display a list of words with following characters eneterd in the input form. 

Also there is a View sourcecode hyperlink which displays the code working behind the scene. The code is as follows
```
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
</pre>
```
After analysis, it is clear that it could be used for OS injection. From previous levels it is clear the password is stored in ```/etc/natas_webpass/natas<no>``` to access the contents of the file use OS injection payloads like 
1. ```<command> | <command>``` where | or pipe is used execute a command after receiving the output(stdout) of the first command as the input(stdin) for second.
OR
2. ```<command> ; <command>``` where ; is used to execute commands sequentially. Even if first one fails second one is executed.

Here, we can use both instead of the first command, use an word and second command as ```cat```. ie
```
test | cat /filepath
```
OR 
```
test ; cat /filepath
```

but methods will display the contents of the file, i.e password for the next level.

## Level 10

Level 10 has the same outline and functionality as level 9 except it displays an additional text which is as follows:
```
For security reasons, we now filter on certain characters

```
So to find the change use the View sourcecode option to analyse the script. Th code has following
```
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
</pre>
```
After analysis, it is clear that metacharacters are not allowed in the input form. So to bypass this one way is by exploiting ```grep```. Since ```grep``` can take two or more files as input to search a specific word, the same idea can be applied here. Use a single alphabet as input and rest as the file path which we have found in the earlier challenges. i.e
```
<alphabet> /etc/natas_webpass/natas<number>
```
and the password will displayed(if the character is part of the password or try changing the character). 
 
