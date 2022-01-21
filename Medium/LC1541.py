# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

https://labuladong.gitee.io/algo/4/32/138/

LC20, LC921, LC1541
"""
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # refer to LC921
        res = 0
        left = 0 
        for ss in s:
            if ss == '(':
                left += 2
                if left % 2 == 1: # e.g: "(()))(()))()())))"
                    # // 插入一个右括号
                    res += 1
                    left -= 1 
            if ss == ')':
                left -= 1
                if left == -1:
                    res += 1
                    left = 1
        return res + left
                
