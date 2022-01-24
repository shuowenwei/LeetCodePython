# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/exam-room/

solution
https://leetcode.com/problems/exam-room/discuss/139941/Python-O(log-n)-time-for-both-seat()-and-leave()-with-heapq-and-dicts-Detailed-explanation

"""
from heapq import heappop, heappush
class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.N = n 
        self.heap = []
        self.avail_first = {}
        self.avail_last = {}
        self.put_segment(0, self.N - 1)
        
    def put_segment(self, first, last): # first and last index of the available segment
        if first == 0 or last == self.N - 1:
            priority = last - first
        else:
            priority = (last - first) / 2
        
        segment = [-priority, first, last, True]
        self.avail_first[first] = segment
        self.avail_last[last] = segment
        heappush(self.heap, segment)
        
    def seat(self):
        """
        :rtype: int
        """
        while True:
            _, first, last, is_valid = heappop(self.heap)
            if is_valid:
                del self.avail_first[first]
                del self.avail_last[last]
                break 
                
        if first == 0:
            res = 0 
            if first != last:
                self.put_segment(first+1, last)
        elif last == self.N - 1:
            res = last 
            if first != last:
                self.put_segment(first, last-1)
        else:
            res = first + (last - first)/2
            if res > first:
                self.put_segment(first, res-1)
            if res < last:
                self.put_segment(res+1, last)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        first = p
        last = p
        left = p-1 # left segment's last index  
        right = p+1 # right segment's first index 
        # Deleting items in self.heap will break heap invariant and requires subsequent heapify() call that executes in O(n log n) time. Instead we can just mark segments as invalid by setting is_valid flag
        if left >= 0 and left in self.avail_last:
            segment_left = self.avail_last.pop(left)
            segment_left[3] = False
            first = segment_left[1] # update first
        if right < self.N and right in self.avail_first:
            segment_right = self.avail_first.pop(right)
            segment_right[3] = False
            last = segment_right[2] # update last

        self.put_segment(first, last)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
