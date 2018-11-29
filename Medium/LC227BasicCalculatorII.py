# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/basic-calculator-ii/

solution: https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.

"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"
        stack, num, sign = [], 0, "+" # since no "()", default the sign of the first number to be + 
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num*10 + ord(s[i])-ord("0") # ord(s[i])-ord("0") = int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)  # current num times the top element in the stack, and then append again 
                else: # '/'
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0: # if the top element in the stack (tmp) is a negative number 
                        stack.append(tmp//num+1)  # 3-5/2 = 3-2=1, but -5/2 = -3, so -5/2+1 =2, which is desired 
                    else:
                        stack.append(tmp//num) # no problem with positive numbers 
                sign = s[i]
                num = 0
        return sum(stack)
