#You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wednesday). 

#You return home after 137 sleeps. 

#Write a general version of the program which asks for the starting day number, and the length of your stay, and 

#It will tell you the name of day of the week you will return on.


n = int(input("On which day_number of week you left the home:"))

length_of_stay = int(input("How many sleeps you will have away from home:"))

week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

day = (length_of_stay + n) % 7

print("You will return on",week[day])
