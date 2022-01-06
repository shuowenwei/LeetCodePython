# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

https://labuladong.gitee.io/algo/3/23/72/

solution reference: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/139609/python-iterative-and-recursive-solution

backtracking vs dp 
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution 2: dp, must facter than backtracking
        if len(nums) == 0:
            return 0
        res = [0]
        dp_table = {}
        def dp(nums, i, diff):
            if i == len(nums):
                if diff == 0:
                    return 1
                return 0 
            if (i, diff) in dp_table:
                return dp_table[(i, diff)]
            
            res = dp(nums, i+1, diff+nums[i]) + dp(nums, i+1, diff-nums[i])
            dp_table[(i, diff)] = res 
            return res
        return dp(nums, 0, target)
        
        # solution 1: backtracking, Time Limit Exceeded, 时间复杂度为 O(2^N)，N 为 nums 的大小
        """
        if len(nums) == 0:
            return 0
        res = [0]
        dp_table = {}
        def backtrack(nums, i, diff):
            if i == len(nums):
                if diff == 0:
                    res[0] += 1
                return
            for sign in (-1, 1):
                diff += sign*nums[i]
                backtrack(nums, i+1, diff)
                diff -= sign*nums[i]
                
        backtrack(nums, 0, target)
        return res[0]
        """