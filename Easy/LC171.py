# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/excel-sheet-column-number/

LC168, LC171
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(columnTitle)
        for i in range(n):
            res += (ord(columnTitle[i]) - ord('A') + 1) * 26**(n-i-1)
        return res 