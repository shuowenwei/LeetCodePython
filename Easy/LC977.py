# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/squares-of-a-sorted-array/

"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        if nums[0] >= 0: # [0, 1, 2, 3]
            return [n**2 for n in nums]
        if nums[-1] <= 0: # [-3, -2, -1, 0]
            return [n**2 for n in nums[::-1]]
        
        for i in range(len(nums)): 
            if nums[i] > 0: # nums[i] is positive 
                negative_nums = nums[:i]
                positive_nums = nums[i:] # nums[i] is in the positive_nums
                break

        new_nums = []
        while negative_nums and positive_nums:    
            if abs(negative_nums[-1]) > positive_nums[0]:
                new_nums.append(positive_nums.pop(0))
            else:
                new_nums.append(negative_nums.pop())
        if positive_nums: 
            new_nums += positive_nums
        if negative_nums: 
            new_nums += [abs(n) for n in negative_nums[::-1]]
        return [n**2 for n in new_nums]
        """
        # solution 2, much slower 
        return sorted([n**2 for n in nums])