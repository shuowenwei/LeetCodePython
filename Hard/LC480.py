# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sliding-window-median/

https://leetcode.com/problems/sliding-window-median/discuss/1002124/Easy-to-understand-with-explanation-Python-Two-heaps-O(N-*-K)-and-O(K)

refer to: LC146, LC460, LC895, LC295

LC295, LC480, LC239
"""
class Solution(object):
    from heapq import heappush, heappop, heapify
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    """
    def rebalance_heap(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element than the min-heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
    """  
    # @staticmethod
    def remove_element_from_heap(self, heap, num):
        index = heap.index(num)
        heap[index] = heap[-1]
        # del heap[-1]
        heap.pop()
        if index < len(heap):
            heapify(heap)

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = len(nums)
        res = [0 for i in range(n-k+1)]
        for i in range(n):
            # len(max-heap) == len(min-heap) + 0 or 1
            if len(self.min_heap) == len(self.max_heap):
                heappush(self.min_heap, nums[i])
                heappush(self.max_heap, -heappop(self.min_heap))
            else:
                heappush(self.max_heap, -nums[i])
                heappush(self.min_heap, -heappop(self.max_heap))

            # add median to res
            if i - k + 1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    res[i - k + 1] = (-self.max_heap[0] + self.min_heap[0]) / 2.0
                else:
                    res[i - k + 1] = -self.max_heap[0]

                element_to_remove = nums[i - k + 1]
                if element_to_remove <= -self.max_heap[0]:
                    self.remove_element_from_heap(self.max_heap, -element_to_remove)
                    if len(self.max_heap) < len(self.min_heap):
                        heappush(self.max_heap, -heappop(self.min_heap))
                else:
                    self.remove_element_from_heap(self.min_heap, element_to_remove)
                    if len(self.max_heap) > len(self.min_heap) + 1:
                        heappush(self.min_heap, -heappop(self.max_heap))
                # self.rebalance_heap()
        return res 
