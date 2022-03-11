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
        s = list(s) # convert to list, easy to change the item value
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

        # no stack
        res = ''
        left = 0 
        for char in s:
            if char == "(":
                left += 1
            elif char == ")":
                if left == 0:
                    continue
                else:
                    left -= 1
            res += char
        if left == 0:
            return res
        
        tmp = ''
        right = 0 
        for char in res[::-1]:
            if char == ')':
                right += 1
            elif char == '(':
                if right == 0:
                    continue
                else:
                    right -= 1
            tmp += char
        return tmp[::-1]
