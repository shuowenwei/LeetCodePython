# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-median-from-data-stream/

https://labuladong.gitee.io/algo/2/20/48/
https://mp.weixin.qq.com/s/oklQN_xjYy--_fbFkd9wMg

https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find

refer to: LC146, LC460, LC895, LC295

LC295, LC480
"""
from heapq import *

class MedianFinder(object): #the add operation is O(logn), The findMedian operation is O(1).

    def __init__(self):
        self.minHeap = [] # holding the larger part of the stream
#   ---------
#    \     /
#     \   /    larger part (assume always > or = the smaller part)
#      \ / -->minHeap
#    median
#      /\  -->maxHeap (all elements are negative)
#     /  \     smaller part
#    /    \
#   ---------
        self.maxHeap = [] # holding the smaller part of the stream

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # self.minHeap always contains 0 or 1 elements more than self.maxHeap
        if len(self.minHeap) > len(self.maxHeap):
            # trying to add num to self.maxHeap
            heappush(self.minHeap, num) # first add to self.minHeap
            minVal = heappop(self.minHeap) # then pop smallest val of self.minHeap
            heappush(self.maxHeap, -minVal) # add that smallest val to self.maxHeap
        else:
            # trying to add num to self.minHeap
            heappush(self.maxHeap, -num) # first add to self.maxHeap
            maxVal = -heappop(self.maxHeap) # then pop the max val of self.maxHeap
            heappush(self.minHeap, maxVal) # add the negative of that max val to self.maxHeap

    def findMedian(self): 
        """
        :rtype: float
        """
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        else: # they are == 
            return float(self.minHeap[0] - self.maxHeap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()




# my way
from heapq import heappop, heappush
class MedianFinder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = [] # always push a negative number into it  

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # always make len(self.max_heap) == len(self.min_heap)  or + 1
        if len(self.max_heap) == 0: # when self.max_heap is empty 
            heappush(self.max_heap, -num)
        elif len(self.max_heap) == len(self.min_heap):
            if num < -self.max_heap[0]: # max_heap should always have at least one element
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)
                heappush(self.max_heap, -heappop(self.min_heap))
        else:
            if num > -self.max_heap[0]: # max_heap should always have at least one element
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
                heappush(self.min_heap, -heappop(self.max_heap))
            
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return - self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()