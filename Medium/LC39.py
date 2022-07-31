# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combination-sum/

LC39, LC40, LC1239
- backtracking
LC78, LC77, LC46, LC90, LC47, LC39, LC40
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def backtracking(candidates, target, start, trackSum, path):
            if target == trackSum:
                res.append(path[:])
                return 
            if target < trackSum: # all numbers in candidates are positive
                return 
            for i in range(start, len(candidates)):
                # All elements of candidates are distinct.
                path.append(candidates[i])
                trackSum += candidates[i]
                # here, must be i, this is replaceable
                backtracking(candidates, target, i, trackSum, path)
                path.pop()
                trackSum -= candidates[i]
                
        backtracking(candidates, target, 0, 0, [])
        return res 
