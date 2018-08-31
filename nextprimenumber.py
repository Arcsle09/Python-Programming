#Enter the number to Find the next prime number 

n = int(input("Enter the number:"))

while True:
  n = n + 1
  for i in range(2,n):
    if n % i == 0:
      break
  else:
    print(n)
    break

