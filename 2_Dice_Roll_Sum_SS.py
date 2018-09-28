# 2 sets represent 2 identical Dices(Dice values are from 1 to 6)
# Write a python script to produce sample space to get a sum of dice values 
# when they are rolled N times

dice1 = {1,2,3,4,5,6}

dice2 = {1,2,3,4,5,6}

print('The sample space: {', end=" ")
products = [print(roll1+roll2,end=" ") for roll1 in dice1 for roll2 in dice2] 
print("}")

#The sample space: { 2 3 4 5 6 7 3 4 5 6 7 8 4 5 6 7 8 9 5 6 7 8 9 10 6 7 8 9 10 11 7 8 9 10 11 12 }
