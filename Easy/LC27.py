# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-element/

"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            else:
                nums[slow] = nums[fast]
                slow += 1 
        return slow      

        """ 
        # solution 2:
        val_indexes = [] 
        for i, v in enumerate(nums):
            if v == val:
                val_indexes.append(i)
        k = 0
        i = 0 # reset i
        while i < len(nums) - len(val_indexes):
            # print(k,i)
            if i+k not in val_indexes:
                nums[i] = nums[i+k]
                i += 1 
            if i+k in val_indexes:
                k += 1
        return len(nums) - len(val_indexes)
        
        """