# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1] 
        foundStart = False
        for i in range(len(nums)):
            if nums[i] == target:
                foundStart = True 
                res[0] = i
                break

        if not foundStart:
            return res 
        
        for j in range(res[0], len(nums)): 
            if nums[j] == target: 
                res[1] = j 
                continue
            else: 
                return res
        return res
                