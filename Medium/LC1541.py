# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

https://labuladong.gitee.io/algo/4/32/138/

LC20, LC921, LC1541, LC1963, LC301
"""
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # refer to LC921
        res = 0 
        needRight = 0
        for char in s:
            if char == '(':
                needRight += 2
                if needRight % 2 == 1: # e.g: "()())" 
                    res += 1 # insert a ')'
                    needRight -= 1
            elif char == ')':
                needRight -= 1
                if needRight == -1:
                    res += 1 # insert a '('
                    needRight = 1 # AKA needRight + 2 = -1 + 2 = 1
                    
        return res + needRight 