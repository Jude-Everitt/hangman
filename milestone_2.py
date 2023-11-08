# The code is importing the `random` module, which allows us to generate random numbers or make random
# choices.
import random

word_list = ["mango", "lime", "pineapple", "coconut", "banana"]
word = random.choice(word_list)
guess = input("Enter a letter.\n")
if ((guess.isalpha() == True) and (len(guess) == 1)):
    print("That is a valid input.")
else:
    print("That is not a valid input. Try again.")