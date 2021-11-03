# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        left = 0 
        right = x 
        while left < right:
            mid = (left + right)//2
            mid_squre = mid **2
            if mid_squre == x: 
                return mid          
            if mid_squre < x and (mid+1)**2 > x:
                return mid 
            if mid * mid > x:
                right = mid
            if mid * mid < x: 
                left = mid + 1 # this will cover x==1
        return left 
        