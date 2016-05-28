
# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/ugly-number/

"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num 
        if n <= 0:
            return False 
        for x in [2,3,5]:
            while n%x == 0:
                n = n/x
        return n == 1 