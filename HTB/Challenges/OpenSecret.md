# OpenSecret

## Description

A simple help desk portal where users can submit support tickets. The application uses JWT tokens for session management, but something seems off about how they're implemented. Can you find the security flaw?

## Solution

Launch the instance and an IP address with a port number is displayed, copy and paste the address in the browser to view the website since it is a web based challenge and challenge artifact is presented.

The website consist of normal support form with Name, Email address and Descritpion. Enter test/dummy information and click submit Ticket.

<img width="804" height="793" alt="image" src="https://github.com/user-attachments/assets/bacf15f6-1658-45dc-bb91-9f55ad77a4e1" />


A text is displayed, saying "No session token provided". To find the cause check the source code using "Veiw Page Source" 

In the Javascript section, The Flag is displayed. Copy the flag and finish the challenge.
