# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/house-robber-ii/

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
        if len(nums) == 1: # nums = [1], expecting 1
            return nums[0]
        dp1 = [0]*(len(nums)+2)
        for i in range(len(nums)-2, -1, -1):
            dp1[i] = max(dp1[i+1], nums[i] + dp1[i+2])

        dp2 = [0]*(len(nums)+2)
        for i in range(len(nums)-1, 0, -1):
            dp2[i] = max(dp2[i+1], nums[i] + dp2[i+2])

        return max(dp1[0], dp2[1])


