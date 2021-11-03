# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-mountain-array/

"""

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False 
        
        summit = 0
        for i in range(len(arr)-1):
            if arr[i+1] == arr[i]:
                return False 
            if arr[i+1] < arr[i]:
                summit = i 
                if summit == 0:
                    return False 
                break
                
        for i in range(summit, len(arr)-1): 
            if arr[i+1] >= arr[i]:
                return False 
            
        return True
                
        