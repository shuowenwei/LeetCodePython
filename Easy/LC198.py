# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/house-robber/

https://labuladong.gitee.io/algo/3/25/95/
https://mp.weixin.qq.com/s/z44hk0MW14_mAQd7988mfw

LC198, LC213, LC337
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # my solutiion
        # if len(nums) < 3:
        #     return max(nums)
        # dp = [0]*len(nums) # dp[i] means max profit if rubbing [0...i] houses
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # return dp[len(nums)-1]
    
    
        # solution 1: dp with memo table, bottom up
        # // dp[i] = x 表示：
        # // 从第 i 间房子开始抢劫，最多能抢到的钱为 x
        # // base case: dp[n] = 0
        dp = [0]*(len(nums)+2)
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        return dp[0]

        """solution 2: dp with memo table, top down
        memo = [-1]*len(nums)
        def dp(nums, start):
            if start >= len(nums): # 当你走过了最后一间房子后，你就没得抢了，能抢到的钱显然是 0（base case）。
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(nums, start+1), dp(nums, start+2) + nums[start])
            memo[start] = res
            return res
        return dp(nums, 0)
        """
        