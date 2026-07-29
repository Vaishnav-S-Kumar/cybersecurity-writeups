# Flag Command

## Description
Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!

## Solution
Start the challenge, this would print an IP address. Using the given IP address open the website.

Website is like a terminal displays a lot of text; i.e
```
You abruptly find yourself lucid in the middle of a bizarre, alien forest.

How the hell did you end up here?

Eerie, indistinguishable sounds ripple through the gnarled trees, setting the hairs on your neck on edge.

Glancing around, you spot a gangly, grinning figure lurking in the shadows, muttering 'Xclow3n' like some sort of deranged mantra, clearly waiting for you to pass out or something. Creepy much?

Heads up! This forest isn't your grandmother's backyard.

It's packed with enough freaks and frights to make a horror movie blush. Time to find your way out.

The stakes? Oh, nothing big. Just your friends, plunged into an abyss of darkness and despair.

Punch in 'start' to kick things off in this twisted adventure!
```
Enter Start to continue, which would display the following;
```
YOU WAKE UP IN A FOREST.

You have 4 options!

HEAD NORTH

HEAD SOUTH

HEAD EAST

HEAD WEST
```

Any answer may not suffice, to find the proper answer check the source code using "View Page Source" option. In the source there is 3 JavaScript which act as the backend script. View each script. 

In one of the script, the following is displayed:

```
if (currentCommand == 'HEAD NORTH') {
                    currentStep = '2';
                }
else if (currentCommand == 'FOLLOW A MYSTERIOUS PATH') {
                    currentStep = '3'
                }
else if (currentCommand == 'SET UP CAMP') {
                    currentStep = '4'
                }

let lineBreak = document.createElement("br");
```

Means if we enter the above following answer may lead to the flag but as we progress it would reach a dead end. In the same script, Another block of code shows how the flag would be displayed. i.e
```
    if (availableOptions[currentStep].includes(currentCommand) || availableOptions['secret'].includes(currentCommand)) {
        await fetch('/api/monitor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'command': currentCommand })
        })
```
Meaning if we find the 'secret', then the program would display the flag, Since all options are displayed from script or JSON, It could be shared to the application when it starts.

So to find the secret, open developer tools and check the network tab. To find the script, refresh the website and find the JSON. When the JSON is opened to view, it contains a section called 'secret'. Copy the content of secret and paste it in the program. 

The flag would be displayed.

