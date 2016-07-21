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
        # this is O(1) space and O(2n) running time 
        output=[] 
        n = len(nums)
        prod = 1 
        for i in range(0,n,1):
            output.append(prod)
            prod = prod * nums[i]
        
        prod = 1 
        for i in range(n-1,-1,-1):
            output[i] = output[i] * prod
            prod = prod * nums[i]
        return output 