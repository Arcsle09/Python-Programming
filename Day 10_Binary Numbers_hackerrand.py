n = int(input('Enter the numer: '))
lst = []
while (n > 0):
    lst.append(n%2)
    n = n // 2

lst = "".join(map(str,lst))

current_consec = 0
max_consec = 0
#print(len(lst))
counter = len(lst)
while (counter):
    if lst[len(lst)-counter] == '1':
        current_consec += 1
        if current_consec > max_consec:
            max_consec = current_consec
    else:
        current_consec = 0
    counter = counter - 1
print(max_consec)
