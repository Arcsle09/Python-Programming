#Recursive Function to print the Fibonacci Series

def fibonnacci(n):
    if n <= 1:
        return(1)
    else:
        return(fibonnacci(n-1) + fibonnacci(n-2))

n = int(input('Enter the number to produce finbonnacci series: '))

for i in range(0,n):
    print(fibonnacci(i), end = " ")
    
