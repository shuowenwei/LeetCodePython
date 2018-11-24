# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/max-consecutive-ones/

"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        current = 0 
        for i in nums:
            if i == 1:
                current += 1 
            else:
                res = max(res, current)
                current = 0 
        res = max(res, current)
        return res
