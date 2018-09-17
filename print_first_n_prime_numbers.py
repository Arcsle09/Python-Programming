n = int(input("Enter the number of prime numbers you want:"))
primes = []
p = 2
while len(primes) < n:
    for i in primes:
        if p % i == 0:
            break

    else:
        primes.append(p)
    p = p + 1 
    
print(primes)
