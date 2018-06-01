def gcd(a,b):
    if a == b:
        return(a)
    elif a % b == 0:
        return(b)
    elif b % a == 0:
        return(a)
    elif a > b:
        return(gcd(a % b,b))
    elif a < b:
        return(gcd(a,b % a))
        
#############output###################
#In: gcd(105,91)
#Out: 7