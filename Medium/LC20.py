# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/generate-parentheses/

https://labuladong.gitee.io/algo/4/29/112/

LC698, LC78, LC46, LC77, LC22
LC51, LC37
- backtrack
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        def backtrack(n, i, tmp):
            if n == i:
                return
            
        backtrack(n, 0, [])
        return res 
