# Digital Footprint(OSINT)

This was an easy OSINT challenge involving a company “ACME Jet Solutions”. OSINT stands for Open-Source Intelligence, which is the process of collecting and analyzing publicly available information to obtain useful intelligence about a person, organization, or dataset. The information gathered through OSINT can include files, videos, audio, images, and other openly accessible sources.

## First Challenge - Leaked Image

The first challenge was to locate the city where the house in the leaked photo is situated. The image provided only had few noticeable items, one was sign board of “ADT Armed Response”. 

I googled **“where ADT armed Response was mainly working”** and found out it is mainly throughout South Africa but also provides service in America. i tried google lens to see if it could pick something out. 

Then i remembered, every image has metadata and location is one of it. I used the exiftool to print the metadata out and found the GPS coordinates. Which I simply copied and pasted in google, the google search engine AI showed the city name and all other details. 

The flag was THM{city_name}.

## Second Challenge - Website

ACME Jet Solutions (warc-acme.com/jef/) was claiming to be started in 2025 but some claims it started earlier than that. To prove this, I jumped into internet archives where I initially provided the full URL but didn’t show any result. So I removed the /jef/ from it and tried again, this time I got a file, the information regarding when it was started was available. 

The flag for this challenge was THM{YYYYMMDDHHMMSS} where these detail are regarding when the site was started

## Third Challenge - Landmark

The third challenge was to find the building name near a monument shown in the image file. On initial analysis of the image, I understood it was from Dublin, Ireland since there was a sign with Dublin in it. I also used google lens and it confirmed my findings, it also revealed the monument name is “**Spire of Dublin”** AKA “**Monument of Light”**. The Flag for this challenge is the name of the building right to this monument which played an important role in the independence of Ireland, THM{name_of_Building} 

## Fourth and Final Challenge - Internal Document

The internal document shared by an employee is available, it is .odt file (OpenDocument Text File). After opening the file, it talks about how bugs have been fixed and so on. One of the line in it mentions about video being shared from the user. 

Again using the exfiltool, i was able find the name of the user. but still couldn’t find the flag. Then the line hit me. I knew it would be YouTube, since is largest video sharing platform. I opened Youtube and search the username (@username), there was account in that username.
