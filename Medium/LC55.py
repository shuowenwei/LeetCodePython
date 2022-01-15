# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game/

https://labuladong.gitee.io/algo/3/27/105/

LC55, LC45 - greedy
LC1345
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        farthest = 0
        for i in range(n):
            # // 不断计算能跳到的最远距离
            farthest = max(farthest, i+nums[i])
            # early stop: e.g: [0]
            if farthest >= n-1:
                return True
            # // 可能碰到了 0，卡住跳不动了
            if farthest <= i:
                return False 
        return farthest >= n-1


        # my solution: Time Limit Exceeded
        """
        n = len(nums)
        res = [False]*n
        res[0] = True
        for i in range(n):
            if res[i] is True:
                for j in range(nums[i]+1):
                    if i+j < n:
                        res[i+j] = True
        return res[n-1]
        """