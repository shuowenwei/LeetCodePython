# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-peak-element/

https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid 
            elif nums[mid] < nums[mid+1]:
                left = mid + 1 
            else:
                right = mid - 1
        return left if nums[left] >= nums[right] else right