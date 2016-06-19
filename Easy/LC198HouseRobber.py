# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/house-robber/

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
            
        maxRob = []
        maxRob.append(nums[0])
        maxRob.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            betterChoice = max( maxRob[i-1], maxRob[i-2]+nums[i] )
            maxRob.append(betterChoice) 
        return maxRob[-1]