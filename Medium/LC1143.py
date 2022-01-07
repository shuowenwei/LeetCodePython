# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-common-subsequence/

https://labuladong.gitee.io/algo/3/24/78/
https://mp.weixin.qq.com/s/ZhPEchewfc03xWv9VP3msg

LC53, LC1143, LC583, LC712, LC72, LC516
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp_table = {}
        # 定义：计算 s1[i..] 和 s2[j..] 的最长公共子序列长度
        def dp(text1, text2, i, j):
            if i == len(text1) or j == len(text2):
                return 0 
            if (i,j) in dp_table:
                return dp_table[(i,j)]
            res = 0 
            if text1[i] == text2[j]:
                res = 1 + dp(text1, text2, i+1, j+1)
            else:
                res = max(dp(text1, text2, i, j+1), dp(text1, text2, i+1, j))
            dp_table[(i,j)] = res 
            return res 
        return dp(text1, text2, 0, 0)
