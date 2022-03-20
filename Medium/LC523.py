# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/continuous-subarray-sum/

LC523, LC560
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if '00' in ''.join([str(n) for n in nums]):
        #     return True
        # if nums == [0]:
        #     return k == 0
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = nums[i-1] + preSum[i-1]
            
        dictMod2index = {}
        for i in range(n+1):
            mod = preSum[i] % k 
            if mod not in dictMod2index:
                dictMod2index[mod] = i
            elif i - dictMod2index[mod] > 1:
                return True 
        return False 
