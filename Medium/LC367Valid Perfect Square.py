# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-perfect-square/

solution reference: https://discuss.leetcode.com/topic/49325/a-square-number-is-1-3-5-7-java-code

A square number is 1+3+5+7+...    n^2 = 1 + 3 + 5 + ... + (2n-1) = (1 + 2n-1)*n/2 


"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        half = num / 2 
        for i in range(1,half+1):
            if i * i == num:
                return True 
            if i * i > num: 
                return False 
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0 
