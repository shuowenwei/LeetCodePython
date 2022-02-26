# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/continuous-subarray-sum/

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
        if nums == [0]:
            return k == 0
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = nums[i-1] + preSum[i-1]
        
        dctmode2index = {}
        for i in range(n+1):
            if i < n - 1 and nums[i] == 0 and nums[i+1] == 0:
                return True
            tmp_mode = preSum[i] % k
            if tmp_mode in dctmode2index:
                if i - dctmode2index[tmp_mode] > 1:
                    return True
            else:
                dctmode2index[tmp_mode] = i 
        return False 

        # Time Limit Exceeded
        # for i in range(n+1):
        #     if i < n - 1 and nums[i] == 0 and nums[i+1] == 0:
        #         return True
        #     for j in range(i):
        #         if preSum[i] - preSum[j] >= k and (preSum[i] - preSum[j]) % k == 0 and i - j > 1:
        #             return True
        # return False 