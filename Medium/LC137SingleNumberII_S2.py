# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number-ii/

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Solution reference link: 
	https://discuss.leetcode.com/topic/2031/challenge-me-thx/2

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
        
        ones = 0 
        twos = 0
        for e in nums:
            ones = (ones ^ e) & ~twos
            twos = (twos ^ e) & ~ones
        return ones 

