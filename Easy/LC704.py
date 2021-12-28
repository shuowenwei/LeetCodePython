# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-search/

https://labuladong.gitee.io/algo/1/8/
https://labuladong.gitee.io/algo/2/21/57/

LC704, LC34, LC875, LC1101, LC410
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
        while left <= right:
            mid = left + (right - left) / 2 # prevent possible overflow 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1 
        return -1