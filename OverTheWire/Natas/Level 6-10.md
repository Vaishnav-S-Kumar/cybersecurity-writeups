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
