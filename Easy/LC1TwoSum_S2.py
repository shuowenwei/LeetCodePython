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
        dictHashMap={}
        length = len(nums)
        for i in range(length):
            neededVal = target - nums[i]

            """
            method 1
            
            if( nums[i] not in dictHashMap):
                dictHashMap[ nums[i] ] = i
            if neededVal in dictHashMap and i != dictHashMap[neededVal]:
                return [dictHashMap[neededVal], i] 
            """

            
            """
            method 2
            """
            if neededVal in dictHashMap: 
                return [dictHashMap[neededVal], i] 
            else:
                dictHashMap[ nums[i] ] = i


