# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subsets/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC659
LC51, LC37
- backtracking
LC78, LC77, LC46, LC90, LC47, LC39, LC40
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtracking(nums, start, tmp):
            # // 前序位置，每个节点的值都是一个子集
            res.append(tmp[::])
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                #  // 通过 start 参数控制树枝的遍历，避免产生重复的子集
                backtracking(nums, i+1, tmp)
                tmp.pop()
        backtracking(nums, 0, [])
        return res 

        # solution when interview with FB:
        """
        res = []
        def backtracking(nums, start, tmp):
            if start == len(nums):
                if tmp not in res:
                    res.append(tmp[:])
                return 
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                backtrack(nums, i+1, tmp)
                tmp.pop()
                backtrack(nums, i+1, tmp)
        backtrack(nums, 0, [])
        return res 
        """