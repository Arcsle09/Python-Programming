def persistence(n,step=0):
    if len(str(n)) == 1:
        print('The total steps are: ',str(step))
        return 'DONE'
    digits = [int(i) for i in str(n)]
    result = 1
    step = step + 1
    for j in digits:
        result = result * j
    print(result)
    persistence(result,step)

#277777788888899 is the number that has the highest multiplicative persistence(step=11)

persistence(277777788888899)

need to discover the number that has multiplicative persistence > (step=11)        
