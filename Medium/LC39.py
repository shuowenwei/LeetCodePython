# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combination-sum/

LC39, LC40
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def backtracking(nums, target, index, path):
            if target == 0:
                res.append(path[::])
                return
            for i in range(index, len(nums)):
                if nums[i] > target:
                    break
                path.append(nums[i])
                # here, must be i, this is replaceable
                backtracking(nums, target-nums[i], i, path) 
                path.pop()
        backtracking(candidates, target, 0, [])
        return res
