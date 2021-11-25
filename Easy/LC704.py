# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://labuladong.gitee.io/algo/1/8/

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) / 2 # prevent possible overflow 
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = left + (right - left) / 2
            elif nums[mid] > target:
                right = mid - 1 
                mid = left + (right - left) / 2
        return -1
