# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

https://labuladong.gitee.io/algo/4/29/109/

LC698, LC78, LC46, LC77, LC22, LC659
LC51, LC37
- backtrack
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # solution 1: from the view of nums 
        # 先说第一个解法，也就是从数字的角度进行穷举，n 个数字，每个数字有 k 个桶可供选择，所以组合出的结果个数为 k^n，时间复杂度也就是 O(k^n)。
        if sum(nums) % k != 0:
            return False 
        each_sum = sum(nums)/k
        subset = [0]*k
        nums.sort(reverse=True) # move larger numbers front, for better pruning purpose
        def backtrack(nums, index, each_sum):
            if index == len(nums):
                if len(set(subset)) == 1 and subset[0] == each_sum:
                    return True 
                else:
                    return False
            for i in range(k):
                if subset[i] + nums[index] > each_sum:
                    continue # pruning here
                subset[i] += nums[index]
                if backtrack(nums, index+1, each_sum):
                    return True
                subset[i] -= nums[index]
        return backtrack(nums, 0, each_sum) 
            
        # solution 2: from the view of buckets/subsets -- this is way faster: 
        # 第二个解法，每个桶要遍历 n 个数字，选择「装入」或「不装入」，组合的结果有 2^n 种；而我们有 k 个桶，所以总的时间复杂度为 O(k*2^n)。
        if sum(nums) % k != 0:
            return False
        each_sum = sum(nums)/k
        used_nums = [False]*len(nums)
        nums.sort(reverse=True)
        def backtrack(nums, start, k, bucket, each_sum):
            if k == 0:
                return True 
            if bucket == each_sum:
                return backtrack(nums, 0, k-1, 0, each_sum)

            for i in range(start, len(nums)):
                if used_nums[i] is True: # already used
                    continue 
                if bucket + nums[i] > each_sum:
                    continue # pruning
                # // 做选择，将 nums[i] 装入当前桶中
                used_nums[i] = True
                bucket += nums[i]
                # // 递归穷举下一个数字是否装入当前桶
                if backtrack(nums, i+1, k, bucket, each_sum):
                    return True
                used_nums[i] = False
                bucket -= nums[i]
            return False
        return backtrack(nums, 0, k, 0, each_sum)
        