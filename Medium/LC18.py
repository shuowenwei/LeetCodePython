# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/4sum/submissions/

https://labuladong.gitee.io/algo/1/13/

https://mp.weixin.qq.com/s/fSyJVvggxHq28a0SdmZm6Q

LC1, LC15, LC18
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import copy 
        res = []
        for i in range(len(nums)-1):
            triplets = self.threeSum(nums[i+1:], target-nums[i])
            for tp in triplets: 
                tmp = [nums[i]]+tp 
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
        return res
    
    # code largely from LC15 
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)
        if nums is None or length <3:
            return res   
            
        nums.sort()
        # here should be len-2 
        for i in range(length-2): 
            # skip duplicate tuples 
            if( i!=0 and nums[i-1] == nums[i]):
                continue
            left = i + 1 
            right = length - 1
            while( left < right):
                threeSum = nums[i]+nums[left]+nums[right]
                if threeSum == target:
                    res.append( [nums[i], nums[left], nums[right]] )
                    left = left + 1
                    right = right - 1
                    # skip duplicate tuples 
                    while( left < right and nums[left] == nums[left-1] ):
                        left = left + 1 
                    # skip duplicate tuples 
                    while( left < right and nums[right] == nums[right+1] ):
                        right = right - 1
                if threeSum > target:
                    right = right - 1
                if threeSum < target:
                    left = left + 1 
        return res