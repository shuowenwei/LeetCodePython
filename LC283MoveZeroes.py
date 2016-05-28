# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/move-zeroes/

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        if not nums:
            return []

        for i in range(len(nums)):
            if nums[i] == 0: 
                nums.remove(0)
                nums.append(0)
        """
        total = nums.count(0)
        for i in range(total):
            nums.remove(0)
            nums.append(0) 