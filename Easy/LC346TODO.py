# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/moving-average-from-data-stream/

https://zhenyu0519.github.io/2020/07/08/lc346/

Time Complexity: O(N)
Space Complexity: O(N)
"""
class MovingAverage:
    
    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.runningSum = 0
        self.queue = collections.deque()
        self.size = size

    def next(self, val):
        if len(self.queue) == self.size:
            self.runningSum -= self.queue.popleft()
            self.queue.append(val)
            self.runningSum += val
            return self.runningSum / len(self.size)
        else:
            self.queue.append(val)
            self.runningSum += val 
            return self.runningSum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

