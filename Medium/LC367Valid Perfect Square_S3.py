# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-perfect-square/

solution reference: https://discuss.leetcode.com/topic/54486/c-0-ms-solution-using-newton-s-method

Newton's Method

"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        prev = num 
        cur = num
        
        while (prev*prev - num) / float(2*prev) >= 1 : 
            cur = prev - (prev*prev - num) / float(2*prev)
            diff = prev - cur 
            prev = cur 
        
        x = int(cur)
        return x*x == num 

