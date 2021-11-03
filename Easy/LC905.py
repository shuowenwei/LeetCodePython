# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sort-array-by-parity/

"""

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        oddIndex = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0: # odd
                res.append(nums[i])
            else:
                oddIndex.append(i)
        
        return res + [nums[i] for i in oddIndex]
                
                