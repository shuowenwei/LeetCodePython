# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/my-calendar-ii/

https://leetcode.com/problems/my-calendar-ii/discuss/109530/N2-Python-Short-and-Elegant

LC729, LC731, LC732
"""
class MyCalendarTwo(object):
    
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
            
        # if not triple booking
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append( (max(start, s), min(end, e)) ) # max left, min right

        self.calendar.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)