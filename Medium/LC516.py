# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-palindromic-subsequence

https://labuladong.gitee.io/algo/3/24/81/

https://mp.weixin.qq.com/s/zNai1pzXHeB2tQE6AdOXTA

LC53, LC1143, LC583, LC712, LC72, LC516 - edit string / substring
LC234, LC5, LC1312, LC516 - Palindromic LC680, LC125, LC1216=LC516
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_table = {}
        n = len(s)
        def dp(s, i, j): # 在子串s[i..j]中，最长回文子序列的长度为 dp_table[(i,j)]
            if i > j: 
                return 0 
            if i == j:
                return 1
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            # 状态转移方程
            if s[i] == s[j]:
                res = dp(s, i+1, j-1) + 2
            else:
                res = max( dp(s, i+1, j), dp(s, i, j-1) )
            dp_table[(i, j)] = res
            return res
        return dp(s, 0, n-1)

        # same solution, but using a 2-d array
        """
        n = len(s)
        dp_table = [[0 for i in range(n)] for j in range(n)] # 0 if i < j 
        for i in range(n):
            dp_table[i][i] = 1 
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp_table[i][j] = dp_table[i+1][j-1] + 2
                else:
                    dp_table[i][j] = max( dp_table[i+1][j], dp_table[i][j-1] )
        return dp_table[0][n-1]
        """