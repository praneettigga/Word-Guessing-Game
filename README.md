# Word-Guessing-Game
A Python based singleplayer Word Guessing game featuring limited attempts, real-time feedback, and input validation. 
The program uses basic Python features such as loops, conditionals, string operations, and randomization to manage gameplay. The interface is kept minimal and user-friendly, focusing entirely on the core logic of guessing and validating words.

**1. Game Flow Overview**
    •	Start the game.
    •	A word is randomly selected from a predefined list.
    •	The user is given a fixed number of attempts to guess the word.
    •	After each guess:
        o	The program compares it to the correct word.
        o	Feedback is given based on correctness (e.g., matching letters).
    •	If the word is guessed correctly or attempts run out, the game ends.
    •	The player is asked if they want to play again.
   
**3. Core Components**
    •	Word Selection: Uses the random module to select a word from a list.
    •	Guess Validation: Ensures the input is of the correct length and format.
    •	Game Logic: Compares each letter of the guess with the actual word to determine correctness.
    •	Replay Loop: Uses a while loop to ask if the user wants to start a new game.

**5. Programming Concepts Used**
    •	Loops (while, for)
    •	Conditional statements (if, else)
    •	Functions (for modular code like play_game())
    •	String operations (length checking, character comparison)
    •	Random module for word selection
    •	Tkinter for GUI

