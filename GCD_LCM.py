#Using Euclid's algorithm
# https://en.wikipedia.org/wiki/Greatest_common_divisor

def GCD(a,b):
    if a == b:
        return(a)
    elif a % b == 0:
        return(b)
    elif b % a == 0:
        return(a)
    elif a > b:
        return(GCD(a % b,b))
    elif a < b:
        return(GCD(a,b % a))
    
def LCM(a,b):
    return(a*b/GCD(a,b))

