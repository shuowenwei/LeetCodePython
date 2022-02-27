# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/1436502/Python-Binary-Search-with-Picture-Clean-and-Concise

LC162, LC153
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(log(n))
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1
                
        # my solution 2: O(n)
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                return nums[i]
        else:
            return nums[0]