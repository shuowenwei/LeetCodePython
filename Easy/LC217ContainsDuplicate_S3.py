# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/contains-duplicate/

"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        e = {} 
        for ele in nums:
            e[ele]=0
            if ele in nums:
                e[ele] += 1
        for k,v in e.items():
            if v > 1:
                return False
        return True 
        """
        if len(nums) == 0:
            return False
            
        sortArray = sorted(nums)
        for i in range(len(sortArray)-1):
            if sortArray[i] == sortArray[i+1]:
                return True
        return False 
            