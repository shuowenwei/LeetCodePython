# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/meeting-rooms-ii/

https://labuladong.gitee.io/algo/3/26/100/
LC435, LC452 - greedy
"""
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0 
        points.sort(key=lambda x: x[1]) # x[1] is the close of the interval
        x = -2**32+1
        for i in range(len(points)):
            if x >= points[i][0]:
                res += 1
            else:
                x = points[i][1]
        return len(points) - res
    