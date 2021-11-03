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
        """
        # solution 1: two pointers 
        res = 0
        fast, slow = 0, 0
        for fast in range(len(nums)): 
            if nums[fast] == 0:
                res = max(res, fast - slow)
                slow = fast + 1 
            if fast == len(nums) - 1:
                res = max(res, fast - slow + 1)
        return res 
        """
        # solution 2: using one flag 
        res = 0 
        currConsec = 0 
        for i in nums:
            if i == 1:
                currConsec += 1 
            else:
                res = max(res, currConsec)
                currConsec = 0
        res = max(res, currConsec)
        return res
