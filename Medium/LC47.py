# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations-ii/

- backtracking
LC78, LC77, LC46, LC90, LC47
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
    
        # TODO, not passed 
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
                # // 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
                if i > 0 and nums[i] == nums[i-1] and not visited_index[i-1]:
                    continue
                tmp.append(nums[i])
                visited_index[i] = True
                backtracking(nums, tmp)
                tmp.pop()
                visited_index[i] = False
        backtracking(nums, [])
        return res 