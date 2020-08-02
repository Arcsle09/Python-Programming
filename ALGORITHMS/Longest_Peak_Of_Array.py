# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 00:28:13 2020

@author: chra8017
"""



#O(N) time || O(1) Space

def LongestPeak(array):
    longest_peak_len = 0
    i = 1
    while i < (len(array)-1):
        ispeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not ispeak:
            i = i + 1
            continue
        
        left_index = i-2
        
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index = left_index - 1
        
        right_index = i + 2
        
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index = right_index + 1
            
        current_peak_len = right_index - left_index - 1
        
        longest_peak_len = max(longest_peak_len,current_peak_len)
        
        i = right_index
    
    return longest_peak_len

LongestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3])  