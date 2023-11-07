import random
##parameters
word_list = ["pineapple", "coconut", "strawberry", "lime", "lemmon", "apple", "banana", "grape", "passionfruit", "melon", "watermelon", "orange"]
num_lives = 5

class Hangman(word_list, num_lives):
   def __init__(self):
##attributes
      self.word = random.choice(self.word_list)
      self.word_guessed = ["_" for char in self.word]
      self.num_lives = num_lives
      self.word_list = word_list
      self.list_of_guesses = []
     

   def check_guess(self, guess):
      self.guess.lower()
      if self.guess in self.word:
         print("Good guess!", self.guess, ", is in the word!")
         for char in self.word:
            if self.guess == self.word[char]:
               self.word_guessed[char] == self.guess
      else:
         self.num_lives -= 1
         print("Unlucky!", self.guess, ", is not in the word")
         print("You have ",self.num_lives," lives left!")


   def ask_for_input(self):
      while(True):
         self.guess = input("Please enter a letter.\n")
         if ((self.guess.isalpha() == False) or (len(self.guess) >= 2)):
            print("Invalid input. Please, enter a single alphabetical character")
         elif self.guess in self.list_of_guesses:
            print("You have already tried that letter!")
         else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)

Hangman(word_list, num_lives == 5)