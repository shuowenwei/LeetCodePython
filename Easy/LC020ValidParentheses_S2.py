# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-parentheses/

"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True 
        res = [] 
        for e in s: 
            if e in ('(','[','{'):
                res.append(e)
            elif e == ')' and (len(res)==0 or res.pop() != '(') :
                return False
            elif e == ']' and (len(res)==0 or res.pop() != '['):
                return False
            elif e == '}' and (len(res)==0 or res.pop() != '{'):
                return False
            else:
                continue
        return len(res) == 0 
            