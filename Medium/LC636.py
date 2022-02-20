# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/exclusive-time-of-functions/

https://leetcode.com/problems/exclusive-time-of-functions/discuss/497890/Easy-to-understand-Python-solution

LC1834, LC636
"""
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        consumed_time = 0 
        for log in logs:
            fid, status, time = log.split(':')
            if status == 'start':
                stack.append((fid, status, time))
            elif status == 'end':
                pre_id, status, start_time = stack.pop() 
                # print(fid, status, time)
                # print(stack[-1][0], stack[-1][1], stack[-1][2])
                res[int(pre_id)] += int(time) + 1 - int(start_time)
                timeSpent = int(time) + 1 - int(start_time)
                if stack:
                    next_id, status, timeSpentByNextProcess = stack[-1]
                    res[int(next_id)] -= timeSpent 
        return res

