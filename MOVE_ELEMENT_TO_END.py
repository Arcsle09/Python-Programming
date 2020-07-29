# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 02:17:06 2020

@author: chra8017
"""

#Description: Move element to end

#MoveElementToEnd([2,1,2,2,2,3,4,2],2)

#[4,1,3,2,2,2,2,2]

def MoveElementToEnd(array,num):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == num:
            j = j - 1
        if array[i] == num:
            array[i],array[j] = array[j],array[i]
        i = i + 1
    return array
    
    