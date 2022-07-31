# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/first-missing-positive/

https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation

LC41, LC268, LC287, LC442, LC448
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
             the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n
