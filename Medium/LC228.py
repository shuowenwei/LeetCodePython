# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/summary-ranges/

"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # another solution 
        stack = [[0,0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[stack[-1][1]] + 1:
                interval = stack.pop()
                stack.append([interval[0], i])                  
            else:
                stack.append([i, i])
        res = []
        for start, end in stack: 
            if start == end:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start]) + '->' + str(nums[end]))
        return res