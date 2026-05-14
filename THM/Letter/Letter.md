# Letter

## Description

It's just another Monday morning on your mail delivery route when an unusual letter catches your eye. The envelope is battered, riddled with holes as if it's been through a storm. The address is barely legible, and your coworkers at the post office wave it off as a lost cause.

But something about it nags at you. You carefully open the damp envelope. Inside, you find a faded newspaper clipping and a short handwritten note. The clipping is torn and water-damaged, with key sections missing. The note is personal, clearly not meant for your eyes, but the fragments you can read hint at a story buried in time.

Objective: Use the clues provided in the zip file to uncover the full name and age of the person mentioned in the note.

Flag format: THM{Name_Surname_age}, only the first letter of the name and surname should be capitalised

Example: THM{Pierre-Henry_Lagaffe_23}

## Solution

Download the files and unzip it. The important contents of the file are the note(note.txt), 2 png files(letter.png & Newspaper_clipping.png) 

1. What is the postal code of the delivery address on the envelope?

Open and view the letter.png file, on the bottom right hand side of letter in the image there is specific pattern of . & |. This represents bar code of the postal code. use ```dcode.fr/french-postal-barcode``` to decrypt the pattern into plain text.

2. What is the flag?

First, convert the content of the note to english using google translate and it reads
```
My dear Édouard,

Today, while tidying the attic at my grandparents' house, I came across this old newspaper clipping. Your great-grandfather wasn't even old enough to get his driver's license when he distinguished himself that day. The youngest of the team, and certainly not the least courageous.

He would be so proud to see you on the water too.

With all my love,
Audette
```

By using Google lens, we can find the original clean photo of the newspaper. It has news on North pole expedition, which talks about the death of 26 sailors during that operation. 

Now time to look deeper into the subject, After long searching on "North Pole Expetiton, 1925" There was a website which mentioned the name of the crew members and one of the members was a boy, 15 year old. That is our flag for the final part
