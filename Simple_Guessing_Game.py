# This program makes use of the mathematical law of trichotomy (given real numbers a and b, exactly one of these three must be true: a > b, a < b, or a == b)

import random 

rng = random.Random()

number = rng.randrange(1,100)

guesses = 0

message = ""

while True:
  guess = int(input(message + "\nGuess My Number between 1 and 100: "))
  guesses = guesses + 1
  if guess > number:
    message = message + str(guess) + " is too high.\n"
  elif guess < number:
    message = message + str(guess) + " is too low.\n"
  else:
    break
input("\n\nGreat, you got it in "+str(guesses)+" guesses!\n\n")
