# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/kth-largest-element-in-an-array/

https://labuladong.gitee.io/algo/4/31/127/

LC215
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        res = 0
        for i in range(k):
            res = heapq.heappop(max_heap)
        return res 
