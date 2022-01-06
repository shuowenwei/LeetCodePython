# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/edit-distance/

https://labuladong.gitee.io/algo/3/24/74/

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 定义：dp(i, j) 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
        def dp(word1, word2, i, j):
            # base case 是 i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度。
            if i == -1: return j+1
            if j == -1: return i+1
            
            if word1[i] == word2[j]:
                return dp(word1, word2, i-1, j-1)
            else:
                return 1 + min(dp(word1, word2, i, j-1), # insert
                               dp(word1, word2, i-1, j), # delete
                               dp(word1, word2, i-1, j-1)) # replace
        return dp(word1, word2, len(word1)-1, len(word2)-1)

        
