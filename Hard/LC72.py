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
        dp_table = {}
        # 定义：dp(i, j) 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
        def dp(word1, word2, i, j):
            # base case 是 i 走完 s1 或 j 走完 s2，可以直接返回另一个字符串剩下的长度。
            if i == -1: return j+1
            if j == -1: return i+1
            
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            if word1[i] == word2[j]:
                res = dp(word1, word2, i-1, j-1)
            else:
                res = 1 + min(dp(word1, word2, i, j-1), # insert: 
                              # 直接在 s1[i] 插入一个和 s2[j] 一样的字符, 那么 s2[j] 就被匹配了，前移 j，继续跟 i 对比
                              dp(word1, word2, i-1, j), # delete: 
                              # 直接把 s[i] 这个字符删掉,前移 i，继续跟 j 对比
                              dp(word1, word2, i-1, j-1)) # replace: 
                              # 我直接把 s1[i] 替换成 s2[j]，这样它俩就匹配了, 同时前移 i，j 继续对比
            dp_table[(i, j)] = res 
            return res 
        return dp(word1, word2, len(word1)-1, len(word2)-1)


        
