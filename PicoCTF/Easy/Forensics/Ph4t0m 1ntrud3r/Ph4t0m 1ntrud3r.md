# Ph4t0m 1ntrud3r

## Description

A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.

To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!

## Solution

Download the PCAP file using the hyperlink and open the .pcap file using WireShark, A series packet transimission is captured and stored. Change the order of the data as the time of certain packets are in negative. 

Change the order with respect to time, view the details of the packets in the order. It can be seen that certain packets have base64 text in it. Copy the base64 text from the hex decimal display section of the packet. 

Store these text in file and use the following command.
```
cat <filename.txt> | base64 -d
```

The flag is printed.
