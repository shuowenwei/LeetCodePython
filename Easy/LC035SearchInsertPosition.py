# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/search-insert-position/
"""
class Solution: 
    def searchInsert(self, nums: List[int], target: int) -> int: 
        left, right = 0, len(nums)-1
        if target < nums[left]:
            return left
        if target > nums[right]:
            return right + 1
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target: 
                return mid 
            if nums[mid] < target < nums[mid+1]:
                return mid + 1
            if nums[mid] < target: 
                left = mid + 1  
            if nums[mid] > target:
                right = mid
        return left 
        
        