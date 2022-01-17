# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-element/

https://labuladong.gitee.io/algo/4/30/123/

LC26, LC83, LC27, LC283
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
            if nums[fast] != val:
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