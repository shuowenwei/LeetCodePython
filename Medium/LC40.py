# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combination-sum-ii/

https://leetcode.com/problems/combination-sum-ii/discuss/17020/Python-easy-to-understand-backtracking-solution
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backtracking(nums, target, index, path):
            if target == 0:
                res.append(path[::])
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    break
                path.append(nums[i])
                # here, must be i+1, not index+1, this is not full permutation
                backtracking(nums, target-nums[i], i+1, path) 
                path.pop()
        backtracking(sorted(candidates), target, 0, [])
        return res