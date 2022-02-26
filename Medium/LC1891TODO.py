# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/cutting-ribbons/

https://walkccc.me/LeetCode/problems/1891/
"""
class Solution(object):
    def maxLength(self, ribbons, k):
        def isCutPossible(length):
            count = 0
            for ribbon in ribbons:
                count += ribbon // length
            return count >= k

        l = 1
        r = sum(ribbons) // k + 1

        while l < r:
            m = (l + r) // 2
        if not isCutPossible(m):
            r = m
        else:
            l = m + 1
        return l - 1

