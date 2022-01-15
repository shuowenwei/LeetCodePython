# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combinations/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC78, LC46, LC77, LC22
LC51, LC37
- backtrack
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(n, k, start, tmp):
            if len(tmp) == k:
                res.append(tmp[::])
                return 
            for i in range(start, n+1):
                tmp.append(i)
                backtrack(n, k, i+1, tmp)
                tmp.pop()
        backtrack(n, k, 1, [])
        return res 
        
        