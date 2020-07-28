# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:44:07 2020

@author: chra8017
"""

# Description:find the pair of numbers from 2 arrays that have smallest difference. 

#Time: O(nlog(n) + mlog(m)), where n is for first array ops; m is for second array ops.

#Space: O(1); we have not used stored any data hence, no memory used. 

def SmallestDiff(arrayOne,arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    point_left = 0
    point_right = 0
    smallest = float('Inf')
    current = float('Inf')
    Smallest_Pair = []
    while point_left < len(arrayOne) and point_right < len(arrayTwo):
        First_Num = arrayOne[point_left]
        Second_Num = arrayTwo[point_right]
        
        if First_Num < Second_Num:
            current = Second_Num - First_Num
            point_left += 1
        elif First_Num > Second_Num:
            current = First_Num - Second_Num
            point_right += 1
        else:
            return [First_Num,Second_Num]
        if smallest > current:
            smallest = current
            Smallest_Pair = [First_Num,Second_Num]
    
    return Smallest_Pair
    
    


