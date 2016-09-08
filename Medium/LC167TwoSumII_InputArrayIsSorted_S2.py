# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

solution reference: https://discuss.leetcode.com/topic/57114/c-o-n-two-pointer

"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while( left < right ):
            if numbers[left]+numbers[right] < target:
                left += 1
            elif numbers[left]+numbers[right] > target:
                right -= 1 
            else:
                return [left+1, right+1]
