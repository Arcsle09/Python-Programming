# Rock-Paper-Scissors Game 

# Sample Function being used. 

from random import *

userchoice = input("Do you choose rock,paper or scissors? ")

items = ['rock','paper','scissors']

computerchoice = sample(items,1)

def compare(computerchoice,userchoice):
    if computerchoice[0] == userchoice:
        print('It is tie !')
    elif computerchoice[0] == 'rock':
        if userchoice == 'scissors':
            print('rock wins !')
        else:
            print('paper wins !')
    elif computerchoice[0] == 'paper':
        if userchoice == 'rock':
            print('paper wins !')
        else:
            print('scissors win !')
    elif computerchoice[0] == 'scissors':
        if userchoice == 'rock':
            print('rock wins !')
        else:
            print('scissors win !')

compare(computerchoice,userchoice)
