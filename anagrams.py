# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:26:34 2020

@author: chra8017
"""

#NOT AN OPTIMAL SOLUTIONS; used in-built function
def anagram(s1,s2):
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    return sorted(s1) == sorted(s2)

anagram('aa','bb')


# Algorithm without using inb-built function

#Step1: check if we have same number of letters in each string

#s1 = 'dog'
#
#s2 = 'god'

def anagram_2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1) != len(s2):
        return False

#Step2: count the frequency of each letter
    count = {}
                
    for letter in s1:
        if letter in count:
            count[letter] = count[letter] + 1
        else:
            count[letter] = 1  
            
#Do reverse for second string    
            
    for letter in s2:
        if letter in count:
            count[letter] = count[letter] - 1
        else:
            count[letter] = 1

#                
    for k in count:
        if count[k] != 0:
            return False
                
    return True
anagram_2('Clint Eastwood','old west action')