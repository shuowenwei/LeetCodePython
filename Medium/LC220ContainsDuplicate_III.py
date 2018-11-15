# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/contains-duplicate-iii

solution: 

https://leetcode.com/problems/contains-duplicate-iii/discuss/61731/O(n)-Python-using-buckets-with-explanation-10-lines.

https://www.youtube.com/watch?v=yc4hCFzNNQc

"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        if k < 0 or t < 0 or len(nums) == 0:
            return False
        """
        for i in range(len(nums)):
            for j in range(i+1, min(len(nums), i+k+1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True 
        return False 
        """
        dictBucket = dict()
        for i in range(len(nums)):
            bucketNum = nums[i] // (t+1)
            if bucketNum in dictBucket and abs(dictBucket[bucketNum] - nums[i]) <= t: 
                return True
            if bucketNum-1 in dictBucket and abs(dictBucket[bucketNum-1] - nums[i]) <= t: 
                return True 
            if bucketNum+1 in dictBucket and abs(dictBucket[bucketNum+1] - nums[i]) <= t: 
                return True 
            dictBucket[bucketNum] = nums[i]
            
            if len(dictBucket)  > k: 
                index2Delete = nums[i-k] // (t+1)
                del dictBucket[index2Delete] 
        return False 