# VERSION-HISTORY

## Description 

I wrote some FAQs about this CTF. Took me a few commits to get it right though.

## Solution

Visit the website, the text displayed in the website is 

```
CTF FAQs
How does it work?

In summary, we will release several challenges during the CTF, and each challenge has a secret value (a "flag") with the format CTF{AAAAAAAAAAAAAAAAAAAAAAAAAAAA}. If you find the flag, you can submit it for points.
Changelog

v1.1: commited a fix for redacting the sample flag.

v1.0: initial version.
```
Which means it contains /.git directory to confirm it run ```dirsearch```, i.e
```
dirsearch -u <URL>
```
check /.git/logs/HEAD, which displays the log as well commit hash of each commit made, the repositery can be downloaded to find the version of the website with the flag using ```git_dumper``` repositery link below:
```
git clone https://github.com/arthaud/git-dumper
```
after downloading and running the script use 
```
git checkout <commit-hash>
```
to move the repositery to commit where the flag is displayed in the index.html.

 
