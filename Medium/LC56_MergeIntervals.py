# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-intervals

solution: 

https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python


"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = [] 
        intervals.sort(key=lambda x: x.start)
        for intvl in intervals: 
            if len(res) > 0 and intvl.start <= res[-1].end:
                res[-1].end = max(intvl.end, res[-1].end) 
            else: 
                res.append(intvl) 
        return res 