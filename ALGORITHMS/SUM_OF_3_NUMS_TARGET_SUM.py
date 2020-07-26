# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:31:03 2020

@author: chra8017
"""
#Description: Find the triplets whose addition becomes targetsum

# O(N^2) time | O(n) space

def ThreeNumberSumOpt(array,targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i],array[left],array[right]])
                left = left + 1
                right = right - 1
            elif currentSum < targetSum:
                left = left + 1
            elif currentSum > targetSum:
                right = right - 1
    return triplets