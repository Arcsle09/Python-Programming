# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:21:38 2020

@author: chra8017
"""

#Description: Check if the input array is Monotonic

#Time: O(n) | Space: O(1)

def isMonotonic(array):
    increasing = True
    decreasing = True
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            increasing = False
        elif array[i] > array[i-1]:
            decreasing = False
    
    return increasing or decreasing

#isMonotonic([-1,-5,-10,-1100,-1100,-1101,-1102,-9001]) will return True