
# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/ugly-number/

"""
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # if n == 1:
        #     return True
        for factor in (2,3,5):
            while n % factor == 0:
                n =  n // factor
        return n == 1