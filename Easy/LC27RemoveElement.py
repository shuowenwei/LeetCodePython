# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-element/

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.


"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """
        if not nums:
            return 0 
        A = 0 
        newNums = [] 
        for i in range(len(nums)):
            print i 
            if nums[i] != val:
                newNums.append(nums[i])
                A += 1
        return A 
        """
        A = len(nums)
        while nums.count(val):
            print A-1 
            nums.remove(val)
        return len(nums)