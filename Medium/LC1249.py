# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100

"""
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
