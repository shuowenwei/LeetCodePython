# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-covered-intervals/

https://labuladong.gitee.io/algo/4/32/138/

LC1288, LC56, LC986
"""
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        toDelete = 0 
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, n):
            # fully covered
            if left <= intervals[i][0] and right >= intervals[i][1]:
                toDelete += 1
            # have some intersection/overlap
            if right >= intervals[i][0] and right <= intervals[i][1]:
                left = intervals[i][0]
                right = intervals[i][1]
            # no overlap 
            if right < intervals[i][0]:
                left = intervals[i][0]
                right = intervals[i][1]
        return n-toDelete
    
        """
        # my modified solution: 
        toDelete = 0 
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, n):
            # fully covered
            if left <= intervals[i][0] and right >= intervals[i][1]:
                toDelete += 1
            else:
                left = intervals[i][0]
                right = intervals[i][1]
        return n-toDelete
        """