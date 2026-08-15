# Pickle Rick

## Description

This Rick and Morty-themed challenge requires you to exploit a web server and find three ingredients to help Rick make his potion and transform himself back into a human from a pickle.

Deploy the lab machine on this task and explore the web application, 

## Walkthrough

The description provides the information about the interface, a web application. Copy the IP Address and open it using a browser. The content of the web application is the following
```
Help Morty!

Listen Morty... I need your help, I've turned myself into a pickle again and this time I can't change back!

I need you to *BURRRP*....Morty, logon to my computer and find the last three secret ingredients to finish my pickle-reverse potion. The only problem is, I have no idea what the *BURRRRRRRRP*, password was! Help Morty, Help!
```
The username as well as the password is not given, to find more information view the source code using "view page source". In the source code, the username is commented for rick but not the password. 

Check the robots.txt for more clues, It contains a random set of letters. This could be the password, thus currently the password as well as the username is found. 

To find the login, try common login directory names like login or login.php before using ```gobuster``` or ```dirb```. Login.php works, use the username and password which was found. 

### FIrst ingredient

After login, the page contains an input form for commands (linux commands) and an execute button. use ```ls``` to view the contents of the current directory. When ```cat``` is used to view the contents of the first ingredient, the following is displayed:
```
Command disabled to make it hard for future PICKLEEEE RICCCKKKK.
```
Instead, use the ```strings``` command, i.e ```strings <filename>```. To find the next ingredient, a clue is left inside a txt file.

The other challenge is difficulty to change directory, ```cd``` is not effective here instead ```ls <directory>``` should be used to view contents of each directory. 

### Second ingredient

For the next ingredient, check the /home directory using ```ls /home``` and continue searching each directory within it. The second ingredient can be found in the home directory of rick.

Use the absolute path of the ingredient along with strings to view the second ingredient.

### Third ingredient

For the third ingredient, check the /root directory since root directories require higher authorization use ```sudo ls /root```

To view the third ingredient, use the command ```sudo strings /root/<filename>``` to get the third ingredient.

Thus, we complete the challenge and rick is back to Human.

