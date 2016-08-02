# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number-ii/

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

This is a silly solution that uses much more extra memory 

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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

