# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game-ii/

https://labuladong.gitee.io/algo/3/27/105/

LC55, LC45 - greedy
LC1306, LC1345

LC45, LC1024, LC1236 - greedy
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

        #solution 3: greedy, refer to https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
        jumps = 0
        curEnd = 0 
        curFarthest = 0 
        for i in range(len(nums) - 1): # here, must be "len(nums)-1", cannot reach the last index 
            curFarthest = max(curFarthest, i + nums[i])
            # print(i, curEnd, curFarthest, jumps)
            if i == curEnd:
                jumps += 1 
                curEnd = curFarthest
        return jumps
        
        # solution 3: refer to LC1024 solution 2
        covers = []
        for i, rg in enumerate(nums):
            covers.append([max(0, i), min(len(nums) - 1, i+rg)])
        covers.sort()
        
        time = len(nums) - 1 
        start = -1 
        end = 0 
        res = 0 
        for left, right in covers:
            if end >= time or left > end:
                break
            elif start < left <= end:
                res += 1
                start = end 
            end = max(end, right)
        return res if end >= time else -1