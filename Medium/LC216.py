# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combination-sum-iii/

- backtracking
LC78, LC77, LC46, LC90, LC47, LC39, LC40, LC216
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, 10)]
        res = []
        
        def backtracking(nums, n, k, start, path, trackingSum):
            if trackingSum == n:
                if len(path) == k:
                    res.append(path[::])
                    return
            for i in range(start, len(nums)):
                trackingSum += nums[i]
                path.append(nums[i])
                backtracking(nums, n, k, i + 1, path, trackingSum)
                trackingSum -= nums[i]
                path.pop()
                
        backtracking(nums, n, k, 0, [], 0)
        return res 