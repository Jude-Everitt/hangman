import random
##parameters
word_list = ["pineapple", "coconut", "strawberry", "lime", "lemmon", "apple", "banana", "grape", "passionfruit", "melon", "watermelon", "orange"]
num_lives = 5
class Hangman(word_list, num_lives = 5):
   def __init__(self, word_list, num_lives = 5):
##attributes
      self.word = random.choice(self.word_list)
      self.word_guessed = ["_" for char in self.word]
      self.num_lives = num_lives
      self.word_list = word_list
      self.list_of_guesses = []
      pass

   def check_guess(self, guess):
      self.guess.lower()
      if self.guess in self.word:
         print("Good guess!", self.guess, ", is in the word!")
         for char in self.word:
            if self.guess == self.word[char]:
               self.word_guessed[char] == self.guess
         num_letters -= 1
      else:
         self.num_lives -= 1
         print("Unlucky!", self.guess, ", is not in the word")
         print("You have ",self.num_lives," lives left!")
      pass

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
      pass
      
def play_game(word_list):
   num_lives = 5
   game = Hangman(word_list, num_lives = 5)
   while(True):
      if num_lives == 0:
         print("Sorry! You loose.")
      elif num_lives >= 1:
         game.ask_for_input()
      elif num_lives != 0 and num_letters == 0:
         print("Congratulations, you've won!")
   pass

if __name__ == '__main__':
    word_list = ["pineapple", "coconut", "strawberry", "lime", "lemmon", "apple", "banana", "grape", "passionfruit", "melon", "watermelon", "orange"]
    play_game(word_list)
