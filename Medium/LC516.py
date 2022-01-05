# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-palindromic-subsequence

https://mp.weixin.qq.com/s/zNai1pzXHeB2tQE6AdOXTA

LC516
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_table = {}
        n = len(s)
        def dp(s, i, j): # 在子串s[i..j]中，最长回文子序列的长度为dp[i][j] 
            if i > j: 
                return 0 
            if i == j:
                return 1
            if (i,j) in dp_table:
                return dp_table[(i,j)]
            # 状态转移方程
            if s[i] == s[j]:
                res = dp(s, i+1, j-1) + 2
            else:
                res = max( dp(s, i+1, j), dp(s, i, j-1) )
            dp_table[(i,j)] = res
            return res
        return dp(s, 0, n-1)
