# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-all-duplicates-in-an-array/

LC41, LC268, LC287, LC442, LC448
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution 1, use array as hash table, space O(n)
        res = []
        dctSeen = [0] * len(nums)
        for num in nums:
            if dctSeen[num-1] == 0: # [1...n] shift by 1 to [0...n-1]
                dctSeen[num-1] = 1 # marked as seen
            else:
                res.append(num)
        return res 

        # solution 2: 
        res = []
        for n in nums:
            if nums[abs(n)-1] < 0: # [1...n] shift by 1 to [0...n-1]
                # // 之前已经把对应索引的元素变成负数了，
                # // 这说明 num 重复出现了两次
                res.append(abs(n))
            else:
                nums[abs(n)-1] = -1 * nums[abs(n)-1]
        return res 