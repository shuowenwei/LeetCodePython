# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/rotate-array/

"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        # exceed time limits:
        k = k%len(nums)
        for i in range(k):
            self.rotateOnce(nums)
        return  
        
    def rotateOnce(self, nums):
        temp = nums[-1]
        for i in range(len(nums)-1):
            nums[len(nums)-i-1] = nums[len(nums)-i-2]
        nums[0]=temp 
        return
        """
        k = k%len(nums)
        temp = nums[-k:]  # save the last k items in the list 
        #nums[-(len(nums)-k):] = nums[:-k]  
        # move the first (length-k) items to the last (length-k) positions, nums[:-k] is the same with nums[:len(nums)-k]
        nums[-(len(nums)-k):] = nums[:len(nums)-k]
        nums[:len(temp)] = temp   # put the last k items from the original list back to the first k positions of the list 
        return 


            