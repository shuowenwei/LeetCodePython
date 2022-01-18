# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/set-mismatch/submissions/

https://labuladong.gitee.io/algo/4/30/121/

LC645
"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution 1: no extra space
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] *= -1 
                
        missing = -1 
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing] 
    
    # my solution: 
        # set_nums = set()
        # for n in nums:
        #     if n in set_nums:
        #         dup = n 
        #     set_nums.add(n)
        # missing = sum(nums) - sum(set_nums)
        n = len(nums)
        dup = sum(nums) - sum(set(nums))
        missing = (1+n)*n/2- sum(set(nums))
        return [dup, missing]