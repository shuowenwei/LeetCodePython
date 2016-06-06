# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/power-of-four/

"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 4:
            return False
        while num%4 == 0:
            num = num / 4
            if num == 1:
                 return True
        return False 