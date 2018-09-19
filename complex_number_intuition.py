x = input('Enter the complex number:')

#x input will be stored as string and we need to remove spaces from the complex number before using complex function.

#if the user does not enter spaces,it will do nothing. 


x = complex(x.replace(" ", ""))

x = (x.real,x.imag)

if x[0] > x[1]:
    print('%f is the greater.' %x[0])
else:
    print('%f is the greater.' %x[1])
