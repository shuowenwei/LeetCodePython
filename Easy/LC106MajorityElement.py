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
        d = {}
        for e in nums:
            if e not in d:
                d[e] = 0
            else:
                d[e] += 1
                
        for k,v in d.items():
            if v >= len(nums)/2:
                return int(k)  