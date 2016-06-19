# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/happy-number/

"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 1: 
            return True 
            
        existing = []
        while n > 0 : 
            if 1 in existing:
                return True
            if n in existing:
                return False
            existing.append(n)
            tem = 0 
            while n > 0: 
                tem += (n%10)**2
                n = n/10 
            n = tem