# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combination-sum-ii/

https://leetcode.com/problems/combination-sum-ii/discuss/17020/Python-easy-to-understand-backtracking-solution

LC39, LC40, LC1239
- backtracking
LC78, LC77, LC46, LC90, LC47, LC39, LC40
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if target < trackSum: 
                return 
            
            for i in range(start, len(candidates)):
                # Each number in candidates may only be used once in the combination.
                # Note: The solution set must not contain duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue 
                path.append(candidates[i])
                trackSum += candidates[i]
                # here, must be i+1, not start+1, this is not full permutation
                backtracking(candidates, target, i + 1, trackSum, path)
                path.pop()
                trackSum -= candidates[i]

        backtracking(candidates, target, 0, 0, [])
        return res 