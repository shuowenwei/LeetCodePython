# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/basic-calculator/

solution: https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.

https://labuladong.gitee.io/algo/4/32/136/

LC43, LC224, LC227, LC772, LC150
"""
import collections
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # refer to LC227
        def helper(s): # s is a list
            num = 0
            sign = '+'
            stack = []
            while len(s) > 0:
                char = s.popleft() # this is faster than using list(s)
                # if char == ' ': # wrong: "1 + 1 "
                #     continue
                if char.isdigit():
                    num = 10*num + int(char)
                if char == '(':
                    num = helper(s)
                if (not char.isdigit() and char != ' ') or len(s) == 0:
                # if (char in ('+','-',')') and char != ' ') or len(s) == 0:
                    if sign == '+':
                        # print('+', stack, char, sign)
                        stack.append(num)
                    elif sign == '-':
                        # print('-', stack, char, sign)
                        stack.append(-num)
                    """ refer to LC772 and LC227
                    # // 只要拿出前一个数字做对应运算即可
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # python 除法向 0 取整的写法
                        stack[-1] = int(stack[-1] / float(num)) # write like this               
                    """
                    sign = char # must be outside, since char can be ')'
                    num = 0
                    # print('after', stack, char, sign)
                if char == ')':
                    break # or "return sum(stack)" here
            return sum(stack)
        return helper(collections.deque(s)) # this is faster than using list(s)
        """
        # solution 2: https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
        res, num, sign, stack = 0, 0, 1, [] 
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss) # if multiple digit show up in a row: '123' -> 1*100+2*10+3
            elif ss in ["-", "+"]:
                res += sign*num # since no negative numbers, sign is "+" for the first num 
                num = 0 # reset num to 0, for the next input digit 
                sign = [-1, 1][ss=="+"] # if True ->1, False ->0: [-1, 1][0] or [-1, 1][1]
            elif ss == "(":
                stack.append(res) # save previous res 
                stack.append(sign) # save previous sign 
                sign, res = 1, 0 # reset sign and res 
            elif ss == ")": 
                res += sign*num # this is the res within the "()"
                res *= stack.pop() # get the previous/last sign before "("
                res += stack.pop() # get the previous/last res before  "("
                num = 0
        
        res += sign*num 
        return res
        """

"""
"(7)-(4+0)+(4)": 
(u'(', '+', [])
(u'7', '+', [])
(u')', '+', [])
(u'-', u'(', [7])
(u'(', u'-', [7])
(u'4', '+', [])
(u'+', '+', [])
(u'0', u'+', [4])
(u')', u'+', [4])
(u'+', u'(', [7, -4])
(u'(', u'+', [7, -4])
(u'4', '+', [])
(u')', '+', [])


(u'(', '+', [])
(u'7', '+', [])
(u')', '+', [])
(u'-', u'(', [0])
(u'(', u'-', [0])
(u'4', '+', [])
(u'+', '+', [])
(u'0', u'+', [4])
(u')', u'+', [4])
(u'+', u'(', [0, 0])
(u'(', u'+', [0, 0])
(u'4', '+', [])
(u')', '+', [])

""" 