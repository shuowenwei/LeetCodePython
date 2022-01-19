# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

Time Limit Exceeded
"""
class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_table = {}
        upper_bound = [i for i in range(n+1)]
        def dp(n):
            if n <= 2: # 1-> 1, 2 -> 2
                return n
            if n in dp_table:
                return dp_table[n]
            res = n + 1
            if n % 3 == 0:
                res = min(res, 1 + dp(n/3))
            if n % 2 == 0:
                res = min(res, 1 + dp(n/2))
            res = min(res, 1 + dp(n-1))
            dp_table[n] = res
            return res 
        return dp(n)
        """ Time Limit Exceeded
        res = [i for i in range(n+1)]
        for i in range(1, n+1):
            res[i] = min(res[i], res[i-1]+1)
            if 2*i < n+1:
                res[2*i] = min(res[2*i], res[i]+1)
            else:
                continue
            if 3*i < n+1:
                res[3*i] = min(res[3*i], res[i]+1)
        return res[n]
        """
        
