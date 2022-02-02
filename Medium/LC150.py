# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/evaluate-reverse-polish-notation/

LC241, LC282, LC43, LC224, LC227, LC772, LC150
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                num = int(t)
                stack.append(num)
            else:
                last1 = stack.pop()
                last2 = stack.pop()
                if t == '+':
                    stack.append(last2 + last1)
                elif t == '-':
                    stack.append(last2 - last1) 
                elif t == '*':
                    stack.append(last2 * last1)
                elif t == '/':
                    stack.append(int(last2 / float(last1))) # refer to LC227
            # print(stack)
        return stack.pop()
