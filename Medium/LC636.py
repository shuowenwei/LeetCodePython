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
        for log in logs:
            func_id, status, time = log.split(':')
            func_id = int(func_id)
            time = int(time)
            
            if status == 'start':
                stack.append((func_id, status, time))
            elif status == 'end': 
                pre_func_id, _, pre_time = stack.pop()
                assert pre_func_id == func_id, 'wrong func id, not matching' # just like '(' and ')'
                res[pre_func_id] += time + 1 - pre_time
                timeSpent = time + 1 - pre_time
                if stack:
                    next_func_id, _, _ = stack[-1]
                    res[next_func_id] -= timeSpent
            # print(res)
        return res 


# n = 2
# logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# sol = Solution()
# sol.exclusiveTime(n, logs)
