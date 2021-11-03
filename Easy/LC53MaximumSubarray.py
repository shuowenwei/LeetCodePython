# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = [0] * len(nums) 
        res[0] = nums[0] 
        max_res = res[0] 
        for i in range(1, len(res)): 
            res[i] = max(res[i-1]+nums[i], nums[i]) 
            max_res = max(max_res, res[i]) 
        return max_res 
    
    """ solution 2: 
        for i in range(1, len(res)): 
            if res[i-1] >= 0: 
                res[i] = nums[i] + res[i-1] 
            else: 
                res[i] = nums[i] 
        return max(res) 
    """
    