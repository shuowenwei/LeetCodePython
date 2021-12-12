# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

labuladong: https://labuladong.gitee.io/algo/1/4/

LC46, LC51 

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