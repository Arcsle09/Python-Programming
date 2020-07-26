# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:13:20 2020

@author: chra8017
"""

# Decsription: find the pair of numbers from array whose sum is target-sum.

# First Algorithm: O(N^2) time / O(1) space

def TwoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstnum = array[i]
        for j in range(i+1,len(array)):
            secondnum = array[j]
            if firstnum + secondnum == targetSum:
                return [firstnum,secondnum]
    
    return []


# Optimized Algorithm using hash datastructure i.e dictionary
# O(N) time || O(n) space
    
def TwoNumberSumHash(array,targetSum):
    nums_dict = {}
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums_dict:
            return[potential_match,num]
        else:
            nums_dict[num] = True
    return []


# Most optmized solution
# O(nlog(n)) time || O(1) space

def TwoNumberSumOpt(array,targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left == left + 1
        elif currentSum > targetSum:
            right = right - 1
    
    return []
        