# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game-ii/

https://labuladong.gitee.io/algo/3/27/105/

LC55, LC45 - greedy
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = [2**32]*n
        res[0] = 0
        for i in range(n):
            for jump in range(nums[i]+1):
                # print(i, jump, ":", res)
                if i+jump < n:
                    res[i+jump] = min(res[i+jump], res[i] + 1)
        return res[n-1]
            
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
        