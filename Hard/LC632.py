# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution

"""
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from heapq import heapify, heappop, heappush
        hp = [(row[0], i, 0) for i, row in enumerate(nums)]
        # print(hp)
        heapify(hp)
        
        res = [-2**32, 2**32]
        right = max(row[0] for row in nums)
        while hp:
            left, i, j = heappop(hp)
            if right - left < res[1] - res[0]:
                res = [left, right]
            if j + 1 == len(nums[i]):
                return res 
            v = nums[i][j+1]
            right = max(right, v)
            heappush(hp, (v, i, j+1))
