# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

solution: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/313703/Python-3

LC41, LC268, LC287, LC442, LC448
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            a = abs(n) - 1 
            # print(a)
            if nums[a] > 0:
                nums[a] = nums[a] * -1 
                # print(nums)
            
        return [i+1 for i in range(len(nums)) if nums[i] > 0]