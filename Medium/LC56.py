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
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1])) # 2nd key doesn't matter 
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, n):
            # no overlap 
            if right < intervals[i][0]:
                res.append( [left, right] )
                left = intervals[i][0]
                right = intervals[i][1]
            # have some intersection/overlap, extend 'right'
            elif right >= intervals[i][0] and right < intervals[i][1]:
                right = intervals[i][1]
            # fully covered
            elif right >= intervals[i][1]:
                # pass
                continue
        res.append([left, right])
        return res