# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak

"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = set(nums)
        res = 1
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    res = max(res, y - x + 1)
                    y = y + 1
        return res
                
