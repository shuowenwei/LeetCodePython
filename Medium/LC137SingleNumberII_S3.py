# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number-ii/

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Solution reference link: 
	https://discuss.leetcode.com/topic/11877/detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers/2

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        d = {}
        for a in nums:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
                
        for k,v in d.items():
            if v == 1:
                return k 
        """
        # don't understand ...............
        x1 = 0 
        x2 = 0 
        mask = 0 
        for e in nums:
            x2 ^= x1 & e
            x1 ^= e
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1
