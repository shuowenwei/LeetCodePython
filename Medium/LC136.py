# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number/

LC136, LC137, LC260
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        The idea hinges on 3 properties of xor:
            (1) that its a commutative operation (i.e. B xor A = B xor A). 
            (2) that something xor itself is 0. So: A xor A = 0. 
            (3) 0 xor A = A.
        These three properties mean that: A xor B xor A = A xor A xor B = 0 xor B = B.
        """
        res = 0
        for e in nums:
            res = res ^ e
        return res 

        # solution 2:
        return 2*sum(set(nums)) - sum(nums)
        
        