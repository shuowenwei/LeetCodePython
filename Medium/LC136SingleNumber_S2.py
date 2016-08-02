# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number/

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        The idea hinges on 3 properties of xor:
            (1) that its a commutative operation (i.e. a xor b = b xor a). 
            (2) that something xor itself is 0. So a xor a = 0. 
            (3) 0 xor a = a. 
            
        These three properties mean that a xor b xor a = a xor a xor b = 0 xor b = b.
        """
        res = 0
        for e in nums:
            res = res ^ e
        return res 