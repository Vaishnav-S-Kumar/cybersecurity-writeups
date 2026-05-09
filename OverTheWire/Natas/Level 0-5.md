# Natas 

Find the password from the website, No SSH login.

## Level 0

Username: natas0
Password: natas0
URL:      http://natas0.natas.labs.overthewire.org

Visit the website, a form pops up askinng the password (this would be repeated in all the levels), Enter the username and password. 

Only thing displayed is 
```
You can find the password for the next level on this page.
```

Check the source code, whenever visiting the website such as this to find extra information [the password of the next level is found there].

## Level 1

Username: natas1
URL:      http://natas1.natas.labs.overthewire.org

Text displayed in the website is 
```
You can find the password for the next level on this page, but rightclicking has been blocked!
```
Instead of right clicking, use F12 to open the dev tools, choose elements tab  and expand the source code to find the password. 
Dev tools also contain other tabs such as network, performace, memory etc. 

## Level 2

Username: natas2
URL:      http://natas2.natas.labs.overthewire.org

Text displayed in the website is 
```
There is nothing on this page 
```
View the source code to find the clues, a website is mentioned as the source of an image. Visit the website and change the URL [delete png file part, keep the directory name]. Along with the png file, a txt file is also present in the directory. View the txt file and find the password.

## Level 3

Username: natas3
URL:      http://natas3.natas.labs.overthewire.org

Text displayed in the website is 
```
There is nothing on this page
```
View the source code, the comment in the source code is 
```
<!-- No more information leaks!! Not even Google will find it this time... -->
```
meaning the passowrd is hidden, in the robots.txt file which tells search engine crawlers which URLs the crawler can access on your site. 

Add /robots.txt to the URL to access the file, inside the file another directory is mentioned. Replace /robots.txt with the directory name.

The directory contains a .txt file, access the .txt file to find the password.

## Level 4

The text displayed in the website is 
```
Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```
2 ways can be used to change the address, 
1. Capture the request using burpsuite and change the Referer address in the request to http://natas5.overthewire.org/ and send the request
2. Using curl to print the response in the terminal, i.e
```
curl http://natas4.overthewire.org/ -H "Referer:http://natas5.overthewire.org/" -H "authorization: Basic *********"
```
The -H is used to mention the header which is used to pass additional metadatas
The respoonse shall contain the password for the next level.

## Level 5

The text displayed in the website is 
```
Access disallowed. You are not logged in
```
Use the dev tools by using the F12 key. In the storage tab, within the cookies section there is category called loggedin which has value 0 change value to 1 and refresh the page. 

After the page is loaded, the password is displayed.

