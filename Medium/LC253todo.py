# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/meeting-rooms-ii/

https://labuladong.gitee.io/algo/3/26/100/

LC435, LC452, LC253, LC1024 - greedy
"""
class Solution(object):
    def minMeetingRooms(self, meetings):
        """
        :type meetings: List[List[int]]
        :rtype: int
        """
        n = len(meetings)
        begins = [m[0] for m in meetings]
        ends = [m[1] for m in meetings]
        begins.sort()
        ends.sort()
        res, i, j = 0, 0, 0
        count = 0 
        while i < n and j < n: 
            if begins[i] < ends[j]:
                count += 1 # // 扫描到一个红点
                i += 1
            else:
                count -= 1 # // 扫描到一个绿点
                j += 1
            res = max(res, count)
        return res 