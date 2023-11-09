# The code is importing the `random` module, which allows us to generate random numbers or make random
# choices.
import random

word_list = ["mango", "lime", "pineapple", "coconut", "banana"]
word = random.choice(word_list)
guess = input("Enter a letter.\n")

def check_guess():
   """
   The function checks if a guess is in a word and prints a corresponding message.
   """
   if (guess in word):
      print("Good guess!", guess, "is in the word!")      
   else:
      print("Sorry,", guess, "is not in the word. Try again.") 

def ask_for_input():
   """
   The function asks the user to enter a single letter and checks if the input is valid.
   """
   while (True):
      
      if ((guess.isalpha() == True) and (len(guess) == 1)):
         print("That is a valid input.")
         break
      else:
         print("That is not a valid input. Try again.")
   check_guess() 
   
ask_for_input()


