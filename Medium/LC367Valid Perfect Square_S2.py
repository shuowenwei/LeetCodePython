# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-perfect-square/

solution reference: https://discuss.leetcode.com/topic/54305/python-binary-search-approach-for-perfect-square

Binary Search Approach

"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True 
        low = 1 
        high = num /2 + 1 
        while high - low > 1: 
            mid = low + (high - low) / 2 
            if mid * mid == num:
                return True 
            elif mid *mid < num:
                low = mid 
            else:
                high = mid 
        return False 

