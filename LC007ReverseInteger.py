# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-integer/

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # solution is from http://www.jiuzhang.com/solutions/reverse-integer/ 
        if x == 0:
            return 0
        neg = 1
        if x < 0:
            neg = -1
            x = - x
        res = 0
        while x > 0: 
            res = res * 10 + x % 10 
            x = x / 10
        res = res* neg 
        if res < -(1<<31) or res > (1<<31)-1:
            return 0
        return res 