# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-strstr/

https://labuladong.gitee.io/algo/3/25/96/
LC28 - KMP string search
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import numpy as np
        def KMP(pat):
            M = len(pat)
            dp = np.zeros((M, 256))
            dp[0][ord(pat[0])] = 1 # base case 
            X = 0 # // 影子状态 X 初始为 0
            # // 构建状态转移图（稍改的更紧凑了）
            for j in range(1, M):
                for c in range(256):
                    dp[j][c] = int(dp[X][c])
                dp[j][ord(pat[j])] = int(j + 1)
                X = int(dp[X][ord(pat[j])]) # // 构建状态转移图（稍改的更紧凑了）
            return dp
        
        def search(txt, pat):
            M = len(pat)
            N = len(txt)
            dp = KMP(pat)
            j = 0 # // pat 的初始态为 0
            for i in range(N):
                j = int(dp[j][ord(txt[i])]) # could return 0.0
                if j == M:
                    return i-M+1
            return -1 
        
        if len(needle) == 0: # needle = ""
            return 0
        return search(haystack, needle)
            
            
        # solution 2: two pointers # Time Limit Exceeded
        # if needle == '':
        #     return 0
        # m, n = len(haystack), len(needle)
        # i, j = 0, 0
        # while i < m:
        #     if haystack[i] == needle[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         i = i-j+1
        #         j = 0
        #     if j == n:
        #         return i - n 
        # return -1
        
        # solution 3: passed: O(n-m)
        if needle == '':
            return 0
        m, n = len(haystack), len(needle)
        if n > m:
            return -1 
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1 