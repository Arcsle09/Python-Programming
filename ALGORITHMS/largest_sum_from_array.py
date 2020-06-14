# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 07:32:13 2020

@author: chra8017
"""

"""Take an array with positive or negative integers and find the maximum sum of that array"""

def largest (arr):
    if len(arr) == 0:
        return print("Too Small")
    
    max_sum = current_sum = arr[0]
    
    for i in arr[1:]:
        current_sum = max(current_sum + i,i)
        max_sum = max(current_sum,max_sum)
    
    return max_sum
    
print(largest([7,1,2,-1,3,4,10,-12,3,21,-19]))

        
        
        