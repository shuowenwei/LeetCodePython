# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-product-subarray/

"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        # 1. Edge Case : Negative * Negative = Positive
        # 2. So we need to keep track of minimum values also, as they can yield maximum values.
        global_max = prev_max = prev_min = nums[0]
        for n in nums[1:]:
            curr_min = min(prev_max*n, prev_min*n, n)
            curr_max = max(prev_max*n, prev_min*n, n)
            global_max= max(global_max, curr_max)#, curr_min)
            prev_max = curr_max
            prev_min = curr_min
        return global_max
