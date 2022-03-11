# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/basic-calculator-iii/

https://ttzztt.gitbooks.io/lc/content/quant-dev/basic-calculator-iii.html
https://labuladong.gitee.io/algo/4/32/135/

LC241, LC282, LC43, LC224, LC227, LC772
"""
import collections
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # refer to LC224 and LC227
        def helper(s): # s is a list
            num = 0
            sign = '+'
            stack = []
            while len(s) > 0:
                char = s.popleft() # this is faster than using list(s)
                if char.isdigit():
                    num = 10*num + int(char)
                
                if char == '(':
                    num = helper(s)
                if (not char.isdigit() and char != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    # // 只要拿出前一个数字做对应运算即可
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # python 除法向 0 取整的写法
                        stack[-1] = int(stack[-1] / float(num)) # write like this               
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)
        return helper(collections.deque(s)) # this is faster than using list(s)
