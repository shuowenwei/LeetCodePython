# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

LC001TwoSum_S1

https://leetcode.com/problems/two-sum/

https://labuladong.gitee.io/algo/1/13/

https://mp.weixin.qq.com/s/fSyJVvggxHq28a0SdmZm6Q

LC1, LC15, LC18
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictHashMap={}
        for i in range(len(nums)):
            neededVal = target - nums[i]
            # method 1: 
            if neededVal in dictHashMap: 
                return [dictHashMap[neededVal], i] 
            else:
                dictHashMap[ nums[i] ] = i

            # # method 2
            # if nums[i] not in dictHashMap:
            #     dictHashMap[ nums[i] ] = i
            # if neededVal in dictHashMap and i != dictHashMap[neededVal]:
            #     return [dictHashMap[neededVal], i] 