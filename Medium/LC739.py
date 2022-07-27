# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/daily-temperatures/

https://labuladong.github.io/algo/2/21/60/

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
        stack = [] # index of highest temperature on the right
        for i in range(n - 1, -1, -1):
            cur_temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= cur_temp:
                stack.pop()
            # while stack:
            #     if temperatures[stack[-1]] <= cur_temp:
            #         stack.pop()
            #     else:
            #         break
            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
            
        return res