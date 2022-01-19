# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subsets/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC78, LC46, LC77, LC22, LC659
LC51, LC37
- backtrack
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(nums, i, tmp):
            if i == len(nums):
                res.append(tmp[::])
                return            
            # do not put nums[i] in tmp
            backtrack(nums, i+1, tmp)
            
            # put nums[i] in tmp
            tmp.append(nums[i])
            backtrack(nums, i+1, tmp)
            tmp.pop()

        backtrack(nums, 0, [])
        return res 

        # solution 2: 
        """
        res = []
        def backtrack(nums, start, tmp):
            res.append(tmp[::])
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                backtrack(nums, i+1, tmp)
                tmp.pop()
        backtrack(nums, 0, [])
        return res 
        """