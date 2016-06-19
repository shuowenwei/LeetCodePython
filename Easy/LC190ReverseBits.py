# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-bits/

"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution from http://www.jiuzhang.com/solutions/reverse-bits/
        res = 0
        i = 0 
        while n >= 1:
            res = res + (n%2)*2**(31-i)
            n=n/2
            i=i+1
        return res 