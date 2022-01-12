# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/burst-balloons/

https://labuladong.gitee.io/algo/3/25/91/
https://mp.weixin.qq.com/s/I0yo0XZamm-jMpG-_B3G8g

LC887, LC312
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # points = [0] * (n+2)
        # points[0], points[n+1] = 1, 1
        points = [1] + nums + [1]
        # dp_table[i][j] = x 表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x
        dp_table = [[0]*(n+2) for _ in range(n+2)] # dp_table[i][i] = 0
        # 对于任一dp[i][j]，我们希望所有dp[i][k]和dp[k][j]已经被计算
        for i in range(n, -1, -1):
            for j in range(i+1, n+2, 1):
                for k in range(i+1, j):
                    # 如果最后一个戳破气球k，dp[i][j]的值应该为：
                    dp_table[i][j] = max(dp_table[i][j], 
                                         dp_table[i][k] + 
                                         dp_table[k][j] + 
                                         points[i]*points[j]*points[k])
        # 题目要求的结果就是dp[0][n+1]的值
        return dp_table[0][n+1]
        
        
        """
        # solution 2 - by Shuowen, but 'Time Limit Exceeded'
        dp_table = {}
        res = []
        def dp(nums): 
            if len(nums) == 0:
                return 0 
            if len(nums) == 1:
                return 1*nums[0]*1
            # if len(nums) == 2:
            #     return nums[0]*nums[1] + max(nums)
            serilize_nums = '-'.join([str(n) for n in nums])
            if serilize_nums in dp_table:
                return dp_table[serilize_nums]
            res = 0 
            for i in range(len(nums)):
                if i == 0:
                    tmp = 1*nums[i]*nums[i+1]
                elif i == len(nums)-1:
                    tmp = nums[i-1]*nums[i]
                else:
                    tmp = nums[i-1]*nums[i]*nums[i+1]
                res = max(res, tmp + dp(nums[:i] + nums[i+1:]))
            dp_table[serilize_nums] = res
            return res
        return dp(nums)
        """