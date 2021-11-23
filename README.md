# PyJong
An image recognition python script to identify and highlight identical Mahjong Solitaire tiles. 

After losing a game, my girlfriend asked me if it's possible to make a program that identifies mahjong tiles for her. 
I replied: "Of course. Watch this."
She did not, in fact, "watch this" as I spent the entire evening learning how to program in Python. 

Two evenings later, I created this. A multi template, multi object matching python script that highlights all Mahjong Solitaire tiles a player can select. 
The algorithm will wait until a key is pressed for two reasons. 
#1: Conserve resources. 
#2: If it continues matching and drawing tiles the screen becomes a mess and it's impossible to distinguish....pretty much anything. 

It's not as much a programming problem as it is a practical one. I might come up with something in the future. 

In a nutshell:

1:Initialize transparent window

2:Load templates

3:Grab screenshot

4:Match i template to all objects within screenshot
5:When users presses Q, redo step 3-5 until exit. 

This is the end result. 


![Proof of concept](https://i.imgur.com/ZyWxQFE.png)
