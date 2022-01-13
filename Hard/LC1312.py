# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

https://labuladong.gitee.io/algo/3/26/100/

LC234, LC5, LC1312, LC516
"""
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_table = {}
        def dp(s, i, j):
            if i >= j: # '==' does not work, error: index out of range
                return 0 # base case
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            if s[i] == s[j]:
                res = dp(s, i+1, j-1) 
            else:
                res = min(dp(s, i, j-1), dp(s, i+1, j)) + 1 # insert once, either left or right
            dp_table[(i, j)] = res 
            return res
        return dp(s, 0, len(s)-1)

        """
        # solution 2:
        n = len(s)
        dp_table = [[0]*n for _ in range(n)]
        # hence base case dp_table[i][i] = 0 is covered
        for i in range(n-2, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp_table[i][j] = dp_table[i+1][j-1]
                else:
                    dp_table[i][j] = min(dp_table[i+1][j], dp_table[i][j-1]) + 1
        return dp_table[0][n-1]
        """