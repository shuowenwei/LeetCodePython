# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/stock-price-fluctuation/

refer to https://leetcode.com/problems/stock-price-fluctuation/discuss/1513324/Python3-hash-map-and-2-heaps

"""
from heapq import heappop, heappush

class StockPrice(object):

    def __init__(self):
        self.time2val = {}
        self.latest_timestamp = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.time2val[timestamp] = price
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
        heappush(self.max_heap, (-price, timestamp))
        heappush(self.min_heap, (price, timestamp))
        
    def current(self):
        """
        :rtype: int
        """
        return self.time2val[self.latest_timestamp]

    def maximum(self):
        """
        :rtype: int
        """
        while self.time2val[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heappop(self.max_heap)
        return - self.max_heap[0][0]
    
    def minimum(self):
        """
        :rtype: int
        """
        while self.time2val[self.min_heap[0][1]] != self.min_heap[0][0]:
            heappop(self.min_heap)
        return self.min_heap[0][0]
    

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
