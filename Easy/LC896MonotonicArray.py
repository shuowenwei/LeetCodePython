# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/monotonic-array/

"""
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = True 
        decreasing = True 
        for i in range(len(A)-1):
            if A[i] > A[i+1]: 
                increasing = False 
            if A[i] < A[i+1]:
                decreasing = False 
        return increasing or decreasing 
    
        """
        if len(A) <= 2: 
            return True
        increaseFlag = False 
        decreaseFlag = False 
        for i in range(1, len(A)):
            # as long as there's one pair incresing 
            if A[i] > A[i-1]:  
                increaseFlag = True
            # as long as there's oen pair decreasing 
            if A[i] < A[i-1]: 
                decreaseFlag = True 
            if increaseFlag and decreaseFlag: 
                return False 
        return True 
        """ 