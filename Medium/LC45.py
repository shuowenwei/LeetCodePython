# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game-ii/

https://labuladong.gitee.io/algo/3/27/105/

LC55, LC45 - greedy
LC1306, LC1345
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [2**32] * n
        dp[0] = 0
        for i, distance in enumerate(nums):
            for d in range(distance + 1): # don't forget '+1', since d will be [0, distance-1]
                if i + d < n:   
                    dp[i + d] = min(dp[i + d], dp[i] + 1)
        return dp[n-1]
            
        # solution 2: dp with memo table
        """
        dp_table = {}
        def dp(nums, p):
            n = len(nums) 
            if p >= n-1: 
                return 0
            if p in dp_table:
                return dp_table[p]
            
            res = 2**32
            for jump in range(1, nums[p]+1): # must start with 1 here
                res = min(res, 1 + dp(nums, p+jump))
                
            dp_table[p] = res 
            return res 
        return dp(nums, 0)
        """
        