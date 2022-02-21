# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

LC46, LC47
- backtrack
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res_index = [] 
        nums_index = [i for i in range(len(nums))]
        def backtracking(nums_index, tmp):
            if len(tmp) == len(nums):
                res_index.append(tmp[::])
                return 
            for index in nums_index:
                if index in tmp:
                    continue
                tmp.append(index)
                backtracking(nums_index, tmp)
                tmp.pop()
                
        backtracking(nums_index, [])
        # print(nums_index)
        for index_combo in res_index:
            tmp = [nums[i] for i in index_combo]
            if tmp not in res:
                res.append(tmp)
        return res 