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

        """
        # solution 2: my solution, refer to my solution in LC198
        n = len(nums)
        if n < 4:
            return max(nums)
        # for nums[0...(n-2)]
        dp1 = [0]*(n-1) 
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        # for nums[1...(n-1)]
        dp2 = [0]*(n-1) 
        dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])
        print(dp1, dp2)
        return max(dp1[-1], dp2[-1])
        """