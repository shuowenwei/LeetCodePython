# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/my-calendar-iii/

LC729, LC731, LC732
LC253==LC732 - greedy - meeting room II 
"""
class MyCalendarThree(object):
    def insert(self, sorted_lst, e):
        if len(sorted_lst) == 0:
            return [e]
        # insert_index = len(sorted_lst)
        # for i in range(len(sorted_lst)):
        #     if sorted_lst[i] > e:
        #         insert_index = i 
        #         break
        # if insert_index == len(sorted_lst):
        #     return sorted_lst + [e]
        # else:
        #     return sorted_lst[:insert_index] + [e] + sorted_lst[insert_index:]
        left, right = 0, len(sorted_lst) - 1
        if sorted_lst[left] >= e:
            return [e] + sorted_lst
        if sorted_lst[right] <= e:
            return sorted_lst + [e]
        while left <= right:
            mid = left + (right - left) // 2
            if sorted_lst[mid] < e:
                left = mid + 1
            elif sorted_lst[mid] > e:
                right = mid - 1
            else: 
                return sorted_lst[:mid] + [e] + sorted_lst[mid:]
        return sorted_lst[:left] + [e] + sorted_lst[left:]

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
        self.starts = self.insert(self.starts, start)
        self.ends = self.insert(self.ends, end)
        # self.starts.append(start)
        # self.ends.append(end)
        # self.starts.sort()
        # self.ends.sort()
        self.numOfIntervals += 1
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
