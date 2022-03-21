# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/


refer to LC698, LC465

LC1732, LC1986
"""
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        min_buckets = sum(tasks) // sessionTime
        tasks.sort(reverse=True)
        def backtrack(tasks, start, k, bucket):
            # print(tasks, start, k, bucket)
            if k == 0:
                residual[0] = bucket
                return all(used)
                # if False not in used:
                #     residual[0] = bucket
                #     return True
                # else:
                #     return False 
            if bucket == sessionTime:
                return backtrack(tasks, 0, k-1, 0)
            if all(used):
                residual[0] = 0
                return True
            min_unused_task = min([t for i, t in enumerate(tasks) if used[i] is False])
            if bucket + min_unused_task > sessionTime:
                return backtrack(tasks, 0, k-1, 0)
            for i in range(start, len(tasks)):
                if used[i] is True:
                    continue 
                if bucket + tasks[i] > sessionTime:
                    continue
                used[i] = True
                bucket += tasks[i]
                if backtrack(tasks, i + 1, k, bucket):
                    return True
                used[i] = False
                bucket -= tasks[i]
            return False
        
        for num_buckets in range(min_buckets, len(tasks) + 1):
            used = [False] * len(tasks)
            residual = [0]
            if backtrack(tasks, 0, num_buckets, 0) is True:
                if residual[0] == 0:
                    return num_buckets
                else:
                    return num_buckets + 1
