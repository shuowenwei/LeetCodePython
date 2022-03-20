# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-intervals

https://labuladong.gitee.io/algo/4/32/138/
https://mp.weixin.qq.com/s/Eb6ewVajH56cUlY9LetRJw

LC1288, LC56, LC986
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # refer to LC1288
        res = []
        intervals.sort(key = lambda x: (x[0], x[1]))
        start = intervals[0][0]
        end = intervals[0][0]
        for intvl in intervals:
            # have some intersection/overlap, extend 'right'
            if intvl[0] <= end:
                # start = min(start, intvl[0])
                end = max(end, intvl[1])
            else: 
            # no overlap 
                res.append([start, end]) 
                start = intvl[0]
                end = intvl[1]
        res.append([start, end]) 
        return res 
