import random
##parameters
word_list = ["pineapple", "coconut", "strawberry", "lime", "lemmon", "apple", "banana", "grape", "passionfruit", "melon", "watermelon", "orange"]
num_lives = 5
class Hangman():
   def __init__(self, word_list, num_lives = 5):
##attributes
      self.word_list = word_list
      self.num_lives = num_lives
      self.word = random.choice(self.word_list)
      self.word_guessed = str(["_"] * len(self.word))
      self.list_of_guesses = []
      self.num_letters = len(set(self.word))
      print("The mystery word has,", self.num_letters, "characters")
      print(self.word_guessed)
      pass

   def check_guess(self, guess):
      self.guess.lower()
      if self.guess in self.word:
         print("Good guess!", self.guess, ", is in the word!")
         for char in range(len(self.word)):
            if self.guess == self.word[char]:
               self.word_guessed[char] == self.guess
               print(self.word_guessed)
         self.num_letters -= 1
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
            print("Already guessed letters:", self.list_of_guesses)
      pass
      
def play_game(word_list):
   num_lives = 5
   game = Hangman(word_list, num_lives = 5)
   while(True):
      if num_lives == 0:
         print("Sorry! You loose.")
         break
      elif num_lives >= 1:
         game.ask_for_input()
      elif num_lives != 0 and num_letters == 0:
         print("Congratulations, you've won!")
         break
   pass

if __name__ == '__main__':
    word_list = ["pineapple", "coconut", "strawberry", "lime", "lemmon", "apple", "banana", "grape", "passionfruit", "melon", "watermelon", "orange"]
    play_game(word_list)
    