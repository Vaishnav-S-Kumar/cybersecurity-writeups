# Plumbing

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?

## Solution

Launch the instance and connect to the machine using netcat/nc. After connecting, non stop lines of words is outputed and the connection is terminated. As given in the description, the solution starts by finding a way to keep the output. One way to store the output is by saving it to a file using ```>>```, i.e
```
nc <address> <port> >> <filename> 
```
After saving the output, use ```cat``` and ```grep``` command, i.e 
```
cat <filename> | grep -i pico
```
Another way to achieve this is without saving the output is using  ```|``` and ```grep```. i.e
```
nc <address> <port> | grep -i pico
```
This way only the output, we require is displayed.
