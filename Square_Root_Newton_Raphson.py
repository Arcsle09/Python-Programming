#Newton Raption Method to find out the square root 

n = int(input("Enter the number:"))

threshold = 0.0001 

approximation = n/2

while True:
  better = (approximation + n/approximation)/2
  print(better)
  if abs(approximation - better) < threshold:
    print(better)
    break
  approximation = better
