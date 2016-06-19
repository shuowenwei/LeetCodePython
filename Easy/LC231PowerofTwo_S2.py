# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/power-of-two/

"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """
        if n<=0: 
            return False
        if n==1 or n==2: 
            return True 
        while n%2 == 0:
            if n == 2: 
                return True
            n = n/2 
        return False 
        """
        return n > 0 and not (n & n-1)
        