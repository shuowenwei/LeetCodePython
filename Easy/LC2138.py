# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/rearrange-spaces-between-words/

LC1592, LC68, LC2138
"""
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        segments = len(s) / k
        lastpart = len(s) % k
        for i in range(segments):
            res.append(s[i*k: i*k+k])
        if lastpart > 0:
            res.append(s[-lastpart:] + fill*(k-lastpart))
        return res