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
        k = k%len(nums)
        self.reverse(nums,0,len(nums)-1)   
        #reverse the whole list, the same with nums.reverse()
        #nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        
    def reverse(self,nums,start,end):
        while(start<end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] =temp
            start += 1
            end -= 1


            
