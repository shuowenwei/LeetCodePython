# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-valid-parentheses/

https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution

"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # def isValid(s):
        #     stack = []
        #     for char in s:
        #         if char == '(':
        #             stack.append(char)
        #         elif char == ')':
        #             if stack:
        #                 stack.pop()
        #             else:
        #                 return False
        #     return len(stack) == 0
        stack = []
        dp_table = [0] * (len(s) + 1) 
# let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship: dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack
        for index, c in enumerate(s):
            if c == '(':
                stack.append(index)
            else:
                if stack:
                    last_open_index = stack.pop()
                    dp_table[index+1] = dp_table[last_open_index] + (index - last_open_index + 1)
        return max(dp_table)
    
