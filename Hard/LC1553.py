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
        # BFS is faster and saving more spaces 
        from collections import deque
        q = deque()
        q.append(n)
        step = 0 
        visited = set()
        while q:
            size = len(q)
            step += 1
            for i in range(size):
                x = q.popleft()
                if x % 3 == 0 and x/3 not in visited:
                    q.append(x/3)
                    visited.add(x/3)
                if x % 2 == 0 and x/2 not in visited:
                    q.append(x/2)
                    visited.add(x/2)
                if x-1 not in visited:
                    q.append(x-1)
                    visited.add(x-1)
                if x-1 == 0:
                    return step
        """ 
        # solution 2: this dp is essential DFS 
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
         
        # solution 3: Time Limit Exceeded
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