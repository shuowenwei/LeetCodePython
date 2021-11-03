# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/search-insert-position/
"""
class Solution: 
    def searchInsert(self, nums: List[int], target: int) -> int: 
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)
        