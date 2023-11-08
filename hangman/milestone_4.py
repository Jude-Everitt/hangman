import random
##parameters
word_list = ["pineapple", "coconut", "strawberry", "lime", "lemmon", "apple", "banana", "grape", "passionfruit", "melon", "watermelon", "orange"]
num_lives = 5

# The Hangman class initializes a game of Hangman with a word list and a specified number of lives,
# and keeps track of the word to be guessed, the guessed letters, and the number of letters in the
# word.
class Hangman():
       '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
   def __init__(self, word_list, num_lives = 5):
##attributes
      self.word_list = word_list
      self.num_lives = num_lives
      self.word = random.choice(self.word_list)
      self.word_guessed = ["_" for char in self.word]
      self.list_of_guesses = []
      self.num_letters = len(set(self.word))
      print("The mystery word has,", self.num_letters, "characters")
      print(self.word_guessed)
      pass

   def check_guess(self, guess):
      """
      The function `check_guess` takes a guess as input, checks if the guess is in the word, updates the
      word_guessed list if the guess is correct, decreases the number of remaining letters if the guess is
      correct, decreases the number of lives if the guess is incorrect, and prints appropriate messages.
      
      :param guess: The `guess` parameter is a string that represents the player's guess for a letter in
      the word
      """
      self.guess.lower()
      if self.guess in self.word:
         print("Good guess!", self.guess, ", is in the word!")
         for char in range(len(self.word)):
            if self.guess == self.word[char]:
               self.word_guessed[char] = self.guess
         print(self.word_guessed)
         self.num_letters -= 1
         
         
      else:
         print(self.word_guessed)
         self.num_lives -= 1
         print("Unlucky!", self.guess, ", is not in the word")
         print("You have ",self.num_lives," lives left!")
      pass

   def ask_for_input(self):
      """
      The function asks the user to input a letter, checks if the input is valid, and keeps track of the
      guessed letters.
      """
      while (self.num_lives != 0 and self.num_letters != 0):
         self.guess = input("Please enter a letter.\n")
         if ((self.guess.isalpha() == False) or (len(self.guess) >= 2)):
            print("Invalid input. Please, enter a single alphabetical character")
         elif self.guess in self.list_of_guesses:
            print("You have already tried that letter!")
            print("Already guessed letters:", self.list_of_guesses)    
         else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)
            print("Already guessed letters:", self.list_of_guesses)  
            
      pass
      

test = Hangman(word_list, num_lives == 5)
print(test.word_list)