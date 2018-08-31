#TowerOfHanoi 
def towerofhanoi(n,start,aux,end):
    if n >= 1:
        towerofhanoi(n-1,start,end,aux)
        print("move " + start + " to " + end)
        towerofhanoi(n-1,aux,start,end)

######################output#################
#towerofhanoi(4,'start','aux','end')
#move start to aux
#move start to end
#move aux to end
#move start to aux
#move end to start
#move end to aux
#move start to aux
#move start to end
#move aux to end
#move aux to start
#move end to start
#move aux to end
#move start to aux
#move start to end
#move aux to end
