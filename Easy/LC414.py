# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/third-maximum-number/

"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) solution
        if len(set(nums)) < 3:
            return max(nums)

        firstMax, secondMax, thirdMax = min(nums), min(nums)-1, min(nums)-2
        
        for n in nums:
            if n > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = n 
            elif n < firstMax and n > secondMax:
                thirdMax = secondMax
                secondMax = n 
            elif n < secondMax and n > thirdMax:
                thirdMax = n 
            else:
                pass 
        return thirdMax