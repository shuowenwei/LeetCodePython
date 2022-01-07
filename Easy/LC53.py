# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-subarray/

https://labuladong.gitee.io/algo/3/24/77/

LC53, LC1143, LC583, LC712, LC72, LC516
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 以 nums[i] 为结尾的「最大子数组和」为 dp[i]。
        dp_table = [0]*len(nums)
        
        dp_table[0] = nums[0]
        for i in range(1, len(nums)):
            dp_table[i] = max(nums[i], nums[i] + dp_table[i-1])
        return max(dp_table)