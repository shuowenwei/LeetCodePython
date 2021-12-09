# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/house-robber/

labuladong: https://mp.weixin.qq.com/s/z44hk0MW14_mAQd7988mfw

LC198, LC213, LC337

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1: dp with memo table, bottom up
        # // dp[i] = x 表示：
        # // 从第 i 间房子开始抢劫，最多能抢到的钱为 x
        # // base case: dp[n] = 0
        dp = [0]*(len(nums)+2)
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], +nums[i] + dp[i+2])
        return dp[0]

        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
            
        maxRob = []
        maxRob.append(nums[0])
        maxRob.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            betterChoice = max( maxRob[i-1], maxRob[i-2]+nums[i] )
            maxRob.append(betterChoice) 
        return maxRob[-1]
        """


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
        