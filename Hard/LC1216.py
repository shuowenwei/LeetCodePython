# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-palindrome-iii/

LC680, LC125, LC1216=LC516
"""
class Solution(object):
    def validPalindrome(self, s, k):
        """
        :type s: str
        :rtype: bool
        """
        # refer to LC516
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
        return dp(s, 0, n-1) + k >= len(s)

        # same solution, but using a 2-d array
        """
        n = len(s)
        dp_table = [[0 for i in range(n)] for j in range(n)] # 0 if i < j 
        for i in range(n):
            dp_table[i][i] = 1 
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp_table[i][j] = dp_table[i+1][j-1] + 2
                else:
                    dp_table[i][j] = max( dp_table[i+1][j], dp_table[i][j-1] )
        return dp_table[0][n-1] + k >= len(s)
        """
        
        # https://www.youtube.com/watch?v=JnsLlZcZKus
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1, 0, -1):
            for j in range(i, n+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = 0 if j - i < 2 else dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + 1
        return dp[1][n] <= k
