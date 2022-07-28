# Pavlovs-Thresh
 Using image analysis to pull some info from League of Legends

League of Legends is a multiplayer online battle arena video game and is a highly competitive, fast paced action-strategy game. one of the playable characters Thresh has four abilities, like every other character, and the goal was to track these abilities along with other information over the course of a game.

To track this I used a tkinter interface to track game data in real time that was scraped from screen shots of the game.

![](https://i.gyazo.com/f262545fc7eac8524dcb0bc5c707d7e9.png)

I can view all ability usage as well as the current level of those abilities and my health/mana over time. There is also an option to "enable shock."

When an ability is used there is a certain amount of time that must pass before it can be used again and this number is displayed on the screen. By taking screenshots and then preforming some low level image processing one can obtain a 2d binary image of black (0) and white (255) based on the grayscale value after thresholding which can then be read by pytesseract. 

With this I could track my ability usage as well as my health and mana over the game and in some cases I could track if the ability I had used had made contact with an enemy like in the case of the ability Death Sentance.

![](https://i.gyazo.com/046c33bf108bb0e47a6cba5c1c685c90.png)

This ability reduces its cooldown if it hits so it becomes simple to monitor if the ability made contact or not just by checking for a sudden drop in cooldown.

While I only created this for Thresh It should be easily adaptable to other champions given changes are made in Main.py.

Another fun implementation I made was that every time the program detected a missed Death Sentance I sent a signal through the serial port to an Arduino to turn on a relay controlled tens unit providing myself with a small shock as an added repercussion.
