# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game-ii/

https://labuladong.gitee.io/algo/3/26/102/

LC55, LC45
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
            
        
