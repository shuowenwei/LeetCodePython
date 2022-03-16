# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subsets-ii/

https://www.youtube.com/watch?v=Vn2v6ajA7U0&list=UU_mYaQAE6-71rjSN6CeCA-g&index=4

backtracking
LC78, LC90
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def backtrack(subset, i):
            if i == len(nums): 
                res.append(subset[::])
                return
            # ALl subsets that include nums[i]
            subset.append(nums[i])
            backtrack(subset, i+1)
            subset.pop()
            
            # All subsets that don't include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(subset, i+1)

        backtrack([], 0) 
        return res 

