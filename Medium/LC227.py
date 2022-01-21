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
        num = 0
        sign = '+'
        stack = []
        for i in range(len(s)): 
            char = str(s[i])
            if char.isdigit():
                num = 10*num + int(char)

            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                # // 只要拿出前一个数字做对应运算即可
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre*num)
                elif sign == '/':
                    pre = stack.pop()
                    if pre >= 0:
                        stack.append(pre/num) # / is same to //
                    else:
                        stack.append(-(-pre/num)) # / is not same to //, don't have to deal with % 
                        # 3-5/2 = 3-2=1, but -5/2 = -3, so -5/2+1 =2, which is desired 
                # // 更新符号为当前符号，数字清零
                sign = char
                num = 0
        return sum(stack)


