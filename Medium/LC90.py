# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subsets-ii/

https://www.youtube.com/watch?v=Vn2v6ajA7U0&list=UU_mYaQAE6-71rjSN6CeCA-g&index=4

LC698, LC465
LC51, LC37
- backtracking
LC78, LC77, LC46, LC90, LC47, LC39, LC40
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def backtracking(nums, start, tmp):
            res.append(tmp[:])
            for i in range(start, len(nums)):
                # // 剪枝逻辑，值相同的相邻树枝，只遍历第一条
                if i > start and nums[i] == nums[i-1]:
                    continue 
                tmp.append(nums[i])
                backtracking(nums, i+1, tmp)
                tmp.pop()
        backtracking(nums, 0, []) 
        return res 
    
        # solution 2: 
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
        """