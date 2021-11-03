# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/powx-n/

solution: https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 :
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n-1) 
        return self.myPow(x * x, n/2)