# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1 
        p = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == prev:
                continue
            nums[p] = nums[i]
            p+=1
            prev = nums[i]
            
        return p
