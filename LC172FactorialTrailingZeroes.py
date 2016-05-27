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
        zeroCount = 0 
        while n > 0: 
            n = n / 5
            zeroCount += n
        return zeroCount 