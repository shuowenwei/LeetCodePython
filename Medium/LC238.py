# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/product-of-array-except-self/

https://leetcode.com/problems/product-of-array-except-self/discuss/65625/Python-solution-(Accepted)-O(n)-time-O(1)-space

"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # time: O(n)
        # space: O(1)
        output = []
        n = len(nums)
        product = 1
        for i in range(n):
            output.append(product)
            product = product * nums[i]
        product = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * product
            product = product * nums[i]
        return output 