# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/factorial-trailing-zeroes/

"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        zeroCount = 0 
        while n > 0: 
            n = n / 5
            zeroCount += n
        return zeroCount 
        """
        
        #only 5, 25 ,125...can increase the 0 numbers.
        if n < 5:
             return 0
        elif n == 5 :
            return 1 
        else: 
            re = 0
            i = 1 
            re = 0
            while n >= 5**i: 
                re +=  n/(5**i)
                i += 1
        return re 