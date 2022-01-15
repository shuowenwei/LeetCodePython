# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

https://labuladong.gitee.io/algo/1/5/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC78, LC46, LC77, LC51
- backtrack
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        res = []
        # print(id(res), res, '--1--')
        def traverse(nums, track):
            if len(nums) == len(track):
                res.append(track[:])
                # res.append(copy.deepcopy(track))
                # print(id(res), res, '--2--')
                return
            for i in nums:
                if i in track:
                    continue 
                track.append(i)
                traverse(nums, track)
                track.pop()
        traverse(nums, [])
        # print(id(res), res, '--1--')
        return res