# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/delete-operation-for-two-strings/

https://labuladong.gitee.io/algo/3/24/78/
https://mp.weixin.qq.com/s/ZhPEchewfc03xWv9VP3msg

LC53, LC1143, LC583, LC712, LC72, LC516
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # solution 1: refer to LC1143, find the longest common subsequence first
        def longestCommonSubsequence(text1, text2):
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
        lcs = longestCommonSubsequence(word1, word2)
        return len(word1) + len(word2) - 2*lcs

        """
        # solution 2: refer to LC72
        dp_table = {}
        # 定义: dp(i, j) 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
        def dp(word1, word2, i, j):
            # base case 是 i 走完 s1 或 j 走完 s2, 可以直接返回另一个字符串剩下的长度。
            if i == -1: return j+1
            if j == -1: return i+1
            
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            if word1[i] == word2[j]:
                res = dp(word1, word2, i-1, j-1)
            else:
                res = 1 + min(dp(word1, word2, i, j-1), # delete: # 直接把 s[j] 这个字符删掉,前移 j, 继续跟 i 对比
                              dp(word1, word2, i-1, j)) # delete: # 直接把 s[i] 这个字符删掉,前移 i, 继续跟 j 对比
            dp_table[(i, j)] = res 
            return res
        return dp(word1, word2, len(word1)-1, len(word2)-1)
        """