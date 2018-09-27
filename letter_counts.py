#Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which
#occur in the string together with the number of times each letter occurs. Case should be ignored.

letter_counts = {}
for letter in "ThiS is String with Upper and lower case Letters".lower():
  letter_counts[letter] = letter_counts.get(letter,0) + 1

del letter_counts[" "]

import collections 
letter_counts = collections.OrderedDict(sorted(letter_counts.items()))

for i in letter_counts.keys():
  print(i,letter_counts[i])
