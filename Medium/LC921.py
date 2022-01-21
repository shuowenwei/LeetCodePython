# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

https://labuladong.gitee.io/algo/4/32/138/

LC20, LC921, LC1541
"""
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # refer to LC1541
        res = 0
        left = 0 
        for ss in s:
            if ss == '(':
                left += 1
            if ss == ')':
                left -= 1
            if left < 0:
                res += 1
                left = 0
        return left + res 
                
