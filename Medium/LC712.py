# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

https://labuladong.gitee.io/algo/3/24/78/
https://mp.weixin.qq.com/s/ZhPEchewfc03xWv9VP3msg

LC53, LC1143, LC583, LC712, LC72, LC516
"""
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp_table = {}
        # // 定义：将 s1[i..] 和 s2[j..] 删除成相同字符串，最小的 ASCII 码之和为 dp(s1, i, s2, j)。
        def dp(s1, s2, i, j):
            if i == len(s1):
                return sum([ord(s2[k]) for k in range(j, len(s2))])
            if j == len(s2):
                return sum([ord(s1[k]) for k in range(i, len(s1))])
            if (i, j) in dp_table:
                return dp_table[(i,j)]
            
            if s1[i] == s2[j]:
                res = dp(s1, s2, i+1, j+1)
            else:
                res = min(dp(s1, s2, i, j+1) + ord(s2[j]), 
                          dp(s1, s2, i+1, j) + ord(s1[i]))
            dp_table[(i, j)] = res
            return res
        return dp(s1, s2, 0, 0)