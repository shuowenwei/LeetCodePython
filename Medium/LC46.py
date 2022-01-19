# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

https://labuladong.gitee.io/algo/1/5/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC78, LC46, LC77, LC22, LC659
LC51, LC37
- backtrack
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        def backtrack(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[::])
                # import copy
                # res.append(copy.deepcopy(track))
                return 
            for n in nums:
                if n in tmp:
                    continue
                tmp.append(n)
                backtrack(nums, tmp)
                tmp.pop()
        backtrack(nums, [])
        return res 