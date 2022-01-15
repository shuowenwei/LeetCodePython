# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-parentheses/

LC20, LC22
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s: 
            if p in {'(', '[', '{'}:
                stack.append(p)
            elif p == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif p == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif p == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                pass 
        return len(stack) == 0 
