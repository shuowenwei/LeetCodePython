# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

LC001TwoSum_S1

https://leetcode.com/problems/two-sum/

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        dictHashMap={}
        length = len(nums)
        for i in range(length):
            if( nums[i] not in dictHashMap):
                dictHashMap[ nums[i] ] = i
                
            neededVal = target - nums[i] 
            if neededVal in dictHashMap and i != dictHashMap[neededVal]:
                return [dictHashMap[neededVal], i] 


