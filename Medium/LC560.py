# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subarray-sum-equals-k

solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book

https://labuladong.gitee.io/algo/2/21/53/

LC303, LC304, LC560
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # refer to LC303
        res = 0
        n = len(nums)    
        preSum = [0]*(n+1)
        # self.preSum[i] means sum(nums[0:i]), [0,...,i), not include nums[i]
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
            
        hast_table = dict()
        for i in range(1, n+1):
            if preSum[i] not in hast_table: 
                hast_table[preSum[i]] = 0
            if preSum[i]-k == 0: 
                res += 1 
            if preSum[i]-k in hast_table: 
                res += hast_table[preSum[i]-k]
            # must consider k == 0, then preSum[i] == preSum[j] - 0
            hast_table[preSum[i]] += 1            
        # print(preSum, hast_table)
        return res

        