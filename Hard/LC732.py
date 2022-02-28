# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/my-calendar-iii/

LC729, LC731, LC732
LC253==LC732 - greedy - meeting room II 
"""
class MyCalendarThree(object):
    
    def __init__(self):
        self.starts = []
        self.ends = []
        self.numOfIntervals = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.starts.append(start)
        self.ends.append(end)
        self.numOfIntervals += 1
        self.starts.sort()
        self.ends.sort()
        res, i, j = 0, 0, 0
        count = 0 
        while i < self.numOfIntervals and j < self.numOfIntervals: 
            if self.starts[i] < self.ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res 

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
