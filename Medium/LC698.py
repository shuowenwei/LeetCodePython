# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

https://labuladong.gitee.io/algo/4/29/109/

LC698
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        each_sum = sum(nums)/k
        subset = [0]*k
        nums.sort(reverse=True) # move larger numbers front 
        print(nums)
        def backtrack(nums, index, each_sum):
            if index == len(nums):
                if len(set(subset)) == 1 and subset[0] == each_sum:
                    return True 
                else:
                    return False
            for i in range(k):
                if subset[i] + nums[index] > each_sum:
                    continue # pruning
                subset[i] += nums[index]
                if backtrack(nums, index+1, each_sum):
                    return True
                subset[i] -= nums[index]
        return backtrack(nums, 0, each_sum) 
            
