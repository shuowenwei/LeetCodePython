# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

https://labuladong.gitee.io/algo/3/23/72/

backtrack vs dp vs backpacking problem
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution 2: dp, must facter than backtrack
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
        
        # solution 1: backtrack, Time Limit Exceeded, 时间复杂度为 O(2^N)，N 为 nums 的大小
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
        # solution 3:
        """
        # sum(subsetA) - sum(subsetB) = target
        # sum(subsetA) + sum(subsetA) = target + sum(subsetA) + sum(subsetB) 
        # sum(subsetA) = ( target + sum(nums) )/2
        sums = sum(nums) + target
        if sums < target or sums % 2 == 1 or sums < 0: # example: [100] -200
            return 0 
        else:
            sums = sums/2
        # dp[i][j] = x 表示，若只在前 i 个物品中选择，若当前背包的容量为 j，则最多有 x 种方法可以恰好装满背包。
        dp = [[0 for i in range(sums+1)] for j in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(sums+1): 
                if j >= nums[i-1]:
                    # // 两种选择的结果之和
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    # // 背包的空间不足，只能选择不装物品 i
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][sums]
        """