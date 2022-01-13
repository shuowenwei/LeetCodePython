# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-palindromic-substring/

https://labuladong.gitee.io/algo/4/32/137/

LC234, LC5, LC1312, LC516
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPalindrome(s, i, j):
            n = len(s)
            while i>=0 and j<=n-1 and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j] # // 返回以 s[i] 和 s[j] 为中心的最长回文串: [i,j)
        n = len(s)
        res = ''
        for i in range(n):
            # // 返回以 s[i] 和 s[j] 为中心的最长回文串
            s1 = getPalindrome(s, i, i)
            # // 返回以 s[i] 和 s[i+1] 为中心的最长回文串
            s2 = getPalindrome(s, i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res
        
