# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution 1: two pointers 
        left, right = 0, len(numbers)-1
        while left < right: 
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum < target:
                left += 1
            else:
                right -= 1
        """
        # solution 2: two pointers but faster 
        for i in xrange(len(numbers)):
            if i > 0 and numbers[i-1] == numbers[i]:
                continue
            newTarget = target - numbers[i] # do binary search this new target
            left, right = i+1, len(numbers)-1
            while left <= right:
                mid = (left + right) / 2 
                if newTarget == numbers[mid]:
                    return [i+1, mid+1]
                elif newTarget < numbers[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
        """ 