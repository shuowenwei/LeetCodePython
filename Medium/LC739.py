# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/daily-temperatures/

https://labuladong.gitee.io/algo/2/20/48/

LC496, LC739, LC503
monotonic stack
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # while stack:
            #     if temperatures[stack[-1]] <= temperatures[i]:
            #         stack.pop()
            #     else:
            #         break
            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
            
        return res