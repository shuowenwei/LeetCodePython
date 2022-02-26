# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/majority-element/

"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_count = collections.defaultdict(lambda:0)
        for e in nums:
            dict_count[e] += 1
            if dict_count[e] > len(nums)/2:
                return e

