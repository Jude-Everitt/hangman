import random

word_list = ["mango", "lime", "pineapple", "coconut", "banana"]
class Word:

   def __init__(self, words):
       self.word = random.choice(words)
       self.ask_for_input()

   def ask_for_input(self):
    
       while True:
           guess = input("Enter a letter.\n")
           if ((guess.isalpha() == True) and (len(guess) == 1)):
              self.check_guess(guess) 
              print("That is a valid input.")

           else:
              print("That is not a valid input. Try again.")
              
   def check_guess(self, guess):
           
           if (guess in self.word):
              print("Good guess!", guess, "is in the word!")
              
           else:
              print("Sorry,", guess, "is not in the word. Try again.")
              

Word(word_list)


