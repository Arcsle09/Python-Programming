#Collatz Sequence from "The Collatz Problem"

n = int(input("""Enter any positive number to create "The Collatz Sequence":"""))
print(end="\n")

while n != 1:
  print(n,end=", ")
  if n % 2 == 0:
    n = n // 2
# In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2. 
# The former is floating point division, and the latter is floor division, sometimes also called integer division.
  else:
    n = n*3 + 1
print(n,end = ".\n")


# More Mathematical Insights about the algorithm: #http://mathworld.wolfram.com/CollatzProblem.html
