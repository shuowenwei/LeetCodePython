# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/missing-number/

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use Sum = (length+1)*length/2 

	length = len(nums)
        return length*(length+1)/2 - sum(nums)

