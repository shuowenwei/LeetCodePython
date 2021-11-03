# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        
        def getNumOfDigits(num):
            numDigits = 0 
            while num > 0:
                numDigits += 1 
                num = num // 10 
            return numDigits
        res = 0 
        for n in nums:
            if getNumOfDigits(n) % 2 == 0:
                res += 1 
        return res
        """
        # solution 2: convert integers to string 
        res = 0 
        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1 
        return res 
            