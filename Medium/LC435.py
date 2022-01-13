# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/non-overlapping-intervals/

https://labuladong.gitee.io/algo/3/26/99/

LC435, LC452, LC253 - greedy
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = 0 
        intervals.sort(key=lambda x: x[1]) # x[1] is the close of the interval
        x = -2**32+1
        for i in range(len(intervals)):
            if x > intervals[i][0]:
                res += 1
            else:
                x = intervals[i][1]
        return res 
