# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/basic-calculator/

solution: https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.

"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
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
