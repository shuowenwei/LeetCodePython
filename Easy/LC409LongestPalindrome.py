# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-palindrome/

"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        single_Letter = False
        counterS = collections.Counter(s)
        for k, v in counterS.items():
            res += (v // 2) * 2
            if v % 2 != 0:
                single_Letter = True
        if single_Letter:     
            return res + 1
        else:
            return res
    