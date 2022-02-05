# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/powx-n/

LC50, LC372
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / float(self.myPow(x, -n))
        elif n % 2 == 1:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x * x, n / 2)
