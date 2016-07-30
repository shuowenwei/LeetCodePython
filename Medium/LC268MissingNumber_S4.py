# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/missing-number/

"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """ 
        #use Sum = (length+1)*length/2  
        length = len(nums)
        return length*(length+1)/2 - sum(nums)
        
        # use sort and Binary Search
        nums = sorted(nums)
        left = 0 
        right = len(nums)
        mid = (left + right)/2
        while left < right: 
            mid = (left + right)/2
            if nums[mid] > mid:
                right = mid 
            else:
                left = mid + 1 
        return left 
        """ 
        """
        # use XOR
        res = len(nums)  # why to initiate res to be the length of the input list????? 
        for i in range(len(nums)):
           res = res ^ i 
           res = res ^ nums[i]
        
        return res 
        """
        res = 0 
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res^len(nums)
        
        

