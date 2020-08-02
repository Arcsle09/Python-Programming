# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 17:35:33 2020

@author: chra8017
"""

#Description: Write the array using spiral path.

def SpiralTraverse(array):
    result = []
    startRow ,endRow = 0,len(array) - 1
    startCol, endCol = 0,len(array[0]) - 1
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol,endCol+1):
            result.append(array[startRow][col])
            
        for row in range(startRow + 1,endRow +1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol,endCol)):
            result.append(array[endRow][col])
        
        for row in reversed(range(startRow+1,endRow)):
            result.append(array[row][startCol])
        
        startRow = startRow + 1
        endRow  = endRow - 1
        startCol = startCol + 1
        endCol = endCol - 1
    
    return result
