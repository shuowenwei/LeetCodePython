# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/expression-add-operators/

solution: https://leetcode.com/problems/expression-add-operators/submissions/

LC241, LC282, LC43, LC224, LC227, LC772, LC150
"""
# https://leetcode.com/problems/expression-add-operators/discuss/572099/C%2B%2BJavaPython-Backtracking-and-Evaluate-on-the-fly-Clean-and-Concise
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def backtracking(path, start, val, pre_val):
            if start == len(num):
                if val == target:
                    res.append(path)
                return 
            for i in range(start, len(num)):
                if num[start] == '0' and i > start: # must have i > start: "105", 5
                    break # Skip leading zero number
                cur_num = int(num[start: i + 1])
                if start == 0:
                    backtracking(path + str(cur_num), i+1, val + cur_num, cur_num)
                else:
                    backtracking(path+'+'+str(cur_num), i+1, val + cur_num, cur_num)
                    backtracking(path+'-'+str(cur_num), i+1, val - cur_num, -cur_num)
                    # e.g: 1+2*3*4
                    backtracking(path+'*'+str(cur_num), i+1, val - pre_val + pre_val*cur_num, pre_val*cur_num)

        backtracking('', 0, 0, 0)
        return res 
    
        # solution 2: Time Limit Exceeded
        def helper(s): # s is string
            num = 0
            sign = '+'
            stack = []
            for i, char in enumerate(s):
                char = s[i]
                if char.isdigit():
                    num = 10*num + int(char)
                if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    sign = char
                    num = 0
            return sum(stack)
        
        res = []
        def backtrack(num, start, path):
            if len(num) == start: 
                if helper(path) == target:
                    res.append(path)
                return
            for i in range(start, len(num)):
                if i > start and num[start] == '0':
                    break 
                cur_num = int(num[start: i + 1])
                if start == 0:
                    # First num, pick it without adding any operator, e.g. '105', 5 
                    backtrack(num, i+1, path+str(cur_num))
                else:
                    backtrack(num, i+1, path+'+'+str(cur_num))
                    backtrack(num, i+1, path+'-'+str(cur_num))
                    backtrack(num, i+1, path+'*'+str(cur_num))
        backtrack(num, 0, '')
        return res 