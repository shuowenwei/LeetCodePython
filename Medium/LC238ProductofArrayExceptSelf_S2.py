# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/product-of-array-except-self/

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # idea from https://discuss.leetcode.com/topic/47132/c-o-1-space-and-o-n-time 
        # this is O(1) space and O(1n) running time 
        n = len(nums)
        output=[1]*n 
        left = 1 
        right = 1
        for i in range(0, n, 1):
            output[i] = output[i] * left 
            left = left * nums[i] 
            output[n-i-1] = output[n-i-1] * right 
            right = right * nums[n-i-1] 
        return output 