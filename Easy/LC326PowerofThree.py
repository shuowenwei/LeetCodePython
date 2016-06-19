# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/power-of-three/

"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: 
            return True 
        if n < 3: 
            return False 
        while n%3 == 0:
            n = n/3
            if n == 1:
                return True 
        return False 