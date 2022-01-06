# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subsets-ii/

https://www.youtube.com/watch?v=Vn2v6ajA7U0&list=UU_mYaQAE6-71rjSN6CeCA-g&index=4

backtracking
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def backtracking(subset, i):
            if i == len(nums): 
                res.append(subset[::])
                return
            # ALl subsets that include nums[i]
            subset.append(nums[i])
            backtracking(subset, i+1)
            subset.pop()
            
            # ALl subsets that don't include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(subset, i+1)

        backtracking([], 0) 
        return res 

