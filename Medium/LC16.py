# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/3sum-closest/

"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        
        def twoSum(nums, start, target):
            low = start
            high = len(nums) - 1
            local_delta = 2 ** 32
            while low < high:
                twoSum = nums[low] + nums[high]
                if abs(target - twoSum) < abs(local_delta):
                    local_delta = target - twoSum
                    res = target - local_delta
                if twoSum > target:
                    high -= 1
                else:
                    low += 1
            return res
        
        delta = 2**32
        res = 0
        for i in range(0, n-2):
            threeSum = nums[i] + twoSum(nums, i + 1, target - nums[i])
            if abs(target - threeSum) < abs(delta):
                delta = target - threeSum
                res = threeSum
        return res 
