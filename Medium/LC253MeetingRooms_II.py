# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen


solution: https://blog.csdn.net/yurenguowang/article/details/76665171

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        if intervals is None or len(intervals) == 0:
            return 0

        tmp = []
        # 标记起始点终止点
        for inter in intervals:
            tmp.append((inter.start, True))
            tmp.append((inter.end, False))

        # 排序
        tmp = sorted(tmp, key=lambda v: (v[0], v[1])) # False==0 should be first when time is the same. (True is 1)

        n = 0
        max_num = 0
        for arr in tmp:
            # 起始点+1
            if arr[1]:
                n += 1
            # 终止点-1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num


