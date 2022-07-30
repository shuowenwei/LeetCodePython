# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/roman-to-integer/

"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        dctRoman2Integer = {r:n for n,r in zip(integers, romans)}
        
        res = 0
        for i in range(len(s)-1):
            if dctRoman2Integer[s[i]] >= dctRoman2Integer[s[i+1]]: # must be >=, not >
                res += dctRoman2Integer[s[i]]
            else: # e.g. IV, IX
                res -= dctRoman2Integer[s[i]] # IV: 5-1 = 4
        res += dctRoman2Integer[s[-1]]
        return res 