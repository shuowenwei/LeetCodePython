# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/different-ways-to-add-parentheses/

"""
class Solution(object):
    def __init__(self):
        self.dp_table = {}
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression in self.dp_table:
            return self.dp_table[expression]
        n = len(expression)
        res = []
        for i in range(n):
            sign = expression[i]
            if sign in ('-', '+', '*'):
                # /****** 分 ******/
                # // 以运算符为中心，分割成两个字符串，分别递归计算
                left = self.diffWaysToCompute(expression[0:i]) # not including i
                right = self.diffWaysToCompute(expression[i+1:])
                # /****** 治 ******/
                # // 通过子问题的结果，合成原问题的结果
                for l in left:
                    for r in right:
                        if sign == '-':
                            res.append(l - r)
                        elif sign == '+':
                            res.append(l + r)
                        elif sign == '*':
                            res.append(l * r)
                        else:
                            pass
                # print('left', left, ' -- ', sign, ' -- right ', right, '-->', res)
        # // base case
        # // 如果 res 为空，说明算式是一个数字，没有运算符
        if len(res) == 0:
            res.append(int(expression))
        self.dp_table[expression] = res
        return res
    
expression = "2*3-4*5"
ob = Solution()
ob.diffWaysToCompute(expression)

('left', [4], ' -- ', u'*', ' -- right ', [5], '-->', [20])
('left', [3], ' -- ', u'-', ' -- right ', [20], '-->', [-17])
('left', [3], ' -- ', u'-', ' -- right ', [4], '-->', [-1])
('left', [-1], ' -- ', u'*', ' -- right ', [5], '-->', [-17, -5])
('left', [2], ' -- ', u'*', ' -- right ', [-17, -5], '-->', [-34, -10])
('left', [2], ' -- ', u'*', ' -- right ', [3], '-->', [6])
('left', [6], ' -- ', u'-', ' -- right ', [20], '-->', [-34, -10, -14])
('left', [2], ' -- ', u'*', ' -- right ', [-1], '-->', [-2])
('left', [6], ' -- ', u'-', ' -- right ', [4], '-->', [-2, 2])
('left', [-2, 2], ' -- ', u'*', ' -- right ', [5], '-->', [-34, -10, -14, -10, 10])
