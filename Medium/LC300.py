# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-increasing-subsequence/

https://labuladong.gitee.io/algo/3/23/67/

LC300
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_table = [1]*(len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_table[i] = max(dp_table[i], dp_table[j]+1)
        # print(dp_table)
        return max(dp_table) # not dp_table[len(nums)-1]
