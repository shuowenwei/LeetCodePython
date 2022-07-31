# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

Solution:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14707/9-11-lines-O(log-n)

https://labuladong.gitee.io/algo/1/8/
https://labuladong.gitee.io/algo/2/21/57/

LC704, LC34, LC875, LC1101, LC410
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution, O(logn(n)), binary search 
        res = [-1, -1]
        # find left boundary
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1 
            if nums[mid] > target:
                right = mid - 1
        if left > len(nums)-1 or nums[left] != target: # didn't find, out of band
            return res 
        res[0] = left
        
        # find right boundary
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)/2 
            if nums[mid] == target:
                left = mid + 1
            if nums[mid] < target:
                left = mid + 1 
            if nums[mid] > target:
                right = mid - 1
        if right < 0 or nums[right] != target: # didn't find, out of band
            return res
        res[1] = right
        return res
        
        """
        # solution 2, O(n)
        res = [-1, -1] 
        foundStart = False
        for i in range(len(nums)):
            if nums[i] == target:
                foundStart = True 
                res[0] = i
                break

        if not foundStart:
            return res 
        """
        