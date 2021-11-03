# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sort-colors/submissions/

solution:

"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        i = 0 
        j = 0 
        k = len(nums) - 1 
        while j <= k: 
            if nums[j] == 0: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1 
            else: #elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1