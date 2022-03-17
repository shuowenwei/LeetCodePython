# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subarray-sum-equals-k

solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book

https://labuladong.gitee.io/algo/2/21/56/

LC303, LC304, LC560, LC528
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n+1):
            preSum[i] = nums[i-1] + preSum[i-1]
        
        res = 0 
        dict_hash = collections.defaultdict(int)
        for i in range(0, n+1):
            # for j in range(i):
            #     if preSum[i] - preSum[j] == k:  --> preSum[i] - k == preSum[j] 
            #         res += 1
            if preSum[i] - k in dict_hash:
                res += dict_hash[ preSum[i] - k ]
                
            dict_hash[ preSum[i] ] += 1 # not dict_hash[ preSum[i] - k ] += 1 !!! 
        return res