# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/fibonacci-number/

labuladong: https://labuladong.gitee.io/algo/1/3/

"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        dp_table = [0,1]
        for i in range(2, n+1):
            dp_table.append(res[i-1] + res[i-2])
        return dp_table[n]
        """
        dp_table = [0]*(n+1)
        dp_table[0] = 0
        if n > 0: # n could be 0
            dp_table[1] = 1
        for i in range(2, n+1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]
        return dp_table[n]