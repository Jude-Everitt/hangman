# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
## Table of contents 
1. Hangman Template - "hangman_Template.py": Provides a template of the final hangman game, outlining the order in which classes and functions are made and their docstring comments.
2. Milestone 2 - "milestone_2.py": Provides a random word from a list and checks if an inputed letter is a valid single alphebetical input.
3. Milestone 3 - "milestone_3.py": Defines two functions from milestone 2 and also evaluates if the letter input is within the randomly generated word.
4. Milestone 4 - "milestone_4.py": A Hangman class, which initializes a game of Hangman with a word list and a specified number of lives, and keeps track of the word to be guessed, the guessed letters, and the number of letters in the word.
5. Milestone 5 - "milestone_5.py": A complete game of hangman!

## Project description
(what it does) (aim of the project) (what i learned)
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

A class called "Hangman" is created to initialise a word list and a specific number of lives, and sets up the gme by choosing a random word from the list and initialising the word_guessed list. The classes parameters passed through are the list of words and the number of lives. It sets up attributes which can be used throughout the different class methods. Such attributes are; the random word generated, a display of the guessed word using correctly guessed letters by the user, the unique number of letters that have not been guess within the word by the user, the number of lives the user is on and a list of letters the user has entered/tried throught the game. These attributes are initialised within the __init__ method. 

Within the class Hangman there are two main function methods. The check_guess and ask_for_input method.

The first method, check_guess, is a function with its parameter being that of the users guess. The function checks if a guessed letter is in a word and updates the guessed word accordingly, while also keeping track of the number of lives remaining. The method converst the users input to lower case with the .lower() command. A if steament is produced, if the users input guess is within the random generated word; it prints "good guess", replaces the "empty" characters in the mystery word with the guessed input revealing all letter locations of the guess in the random word, and reduces the number of characters left in the random word. If the word is not within the random word the function will; reduced the number of users lives by 1, print the current revelation of the mystery random word, print the user made a wrong guess and print the number of lives the user currently has. 

The second method within the Hangman class asks for the users input, checks if the input is a valid guess and keeps track of the current state of the mystery hidden word (how much of the word is hidden or revealed). Firstly this method creates a while loop wkth the conditions that the number of lives arent down to zero and that the hidden mystery word hasnt been completly revealed. It asks for an input and assigns it as a guess. Then if statements are created. The first if statement checks if the users guess is alphebetical or contains multiple characters, if either of theres conditions are not met it tells the user the input is not a valid and to enter another input, where a single alphabetical character would bee valid. The next if statement then checks if the valid input hasnt already been entered, if it has already been useed it tells the user to try a different input. The else staement takes in an previously unused single aplhebtical charcter and passes it through the check_guess method to see if it is within the word. 

This concludes the class.

Outside the class there is a play_game fucntion. This allows the user to play a game of hangman using a given word list, The word_list parameter is a list of words that the Hangman game will choose from. Each word in the list represents a possible word for the player to guess. It passes in a word list and the initial number of lives the user starts with, in this case it is 5 lives. It runs a game with a while loop. The while loop will run or stop the game when certain parameters are hit. If the number of lives reaches zero, it stops the game and tells the user they have lost. If the user still has lives and still not guessed the full word, it will continue to ask, validate and check the useers input through the hangman class methods, and update the mystery word. If the word has been fully guessed and the user still has lives remaining it will stop the game and tell the user they have won. 

The `if __name__ == '__main__':` block is used to ensure that the code inside it is only executed if the script is run directly, and not if it is imported as a module. It also contains the full list of possible words the game can choose from and then starts the game. 

## Instilation instructions



## Usage instructions
## File structure
The technology stacks used in this code are Python and random. 
## License information 
