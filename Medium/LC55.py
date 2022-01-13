# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game/

https://labuladong.gitee.io/algo/3/26/102/

LC55, LC45
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        res = [False]*n
        res[0] = True
        for i in range(n):
            if res[i] is True:
                for j in range(nums[i]):
                    res[i+j] = True
        return res[n-1]
