
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
        if n == 1: 
            return True

        while n%2 == 0:
            n = n/2
        while n%3 == 0:
            n = n/3
        while n%5 == 0:
            n = n/5
            
        if n == 1: 
            return True
        else:
            return False 