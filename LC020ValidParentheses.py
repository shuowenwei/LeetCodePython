# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-parentheses/

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False 
        stack = [] 
        for a in s: 
            if a in ['(', '[', '{']:
                stack.append(a)
                continue 
            if a == ')': 
                if stack and stack.pop() != '(':
                    return False
                continue     
            if a == ']': 
                if stack and stack.pop() != '[':
                    return False
                continue    
            if a == '}': 
                if stack and stack.pop() != '{':
                    return False
                continue    
            
        if not stack:  # if stack is empty then return True 
            return True
        else:
            return False 