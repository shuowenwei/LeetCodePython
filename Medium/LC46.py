# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

https://labuladong.gitee.io/algo/1/5/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC465
LC51, LC37
- backtracking
LC78, LC77, LC46, LC90, LC47, LC39, LC40
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        def backtracking(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return 
            for n in nums: # no dups in the nums 
                # // 已经存在 track 中的元素，不能重复选择
                if n in tmp:
                    continue
                tmp.append(n)
                backtracking(nums, tmp)
                tmp.pop()
        backtracking(nums, [])
        return res 
    
        # solution 2: refer to LC47
        visited_index = [False] * len(nums)
        nums.sort()
        res = []
        def backtracking(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            for i in range(len(nums)):
                # // 已经存在 track 中的元素，不能重复选择
                if visited_index[i]:
                    continue
                tmp.append(nums[i])
                visited_index[i] = True
                backtracking(nums, tmp)
                tmp.pop()
                visited_index[i] = False
        backtracking(nums, [])
        return res 