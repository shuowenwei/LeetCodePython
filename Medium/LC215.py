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
        # solution 1: using a max_heap, and pop k times 
        from heapq import heapify, heappop
        max_heap = [-n for n in nums]
        heapify(max_heap)
        res = 0
        for i in range(k):
            res = heappop(max_heap)
        return res 
    
        # solution 2: using a min_heap, and maintain its size to be k 
        from heapq import heapify, heappop
        heapify(nums)
        res = 0
        print(nums)
        while len(nums) > k-1:
            res = heappop(nums)
        return res

        # solution 2: using a min_heap, and maintain its size to be k 
        from heapq import heapify, heappop, heappush
        min_heap = []
        for n in nums:
            heappush(min_heap, n)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]
    