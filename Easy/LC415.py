# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-strings/

LC415, LC43
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        l1 = [int(n) for n in num1]
        l2 = [int(n) for n in num2]
        carry = 0
        while l1 and l2:
            tmp = l1.pop() + l2.pop() + carry 
            carry = tmp // 10
            res.append(tmp % 10)
        while l1:
            tmp = l1.pop() + carry 
            carry = tmp // 10
            res.append(tmp % 10)
        while l2:
            tmp = l2.pop() + carry 
            carry = tmp // 10
            res.append(tmp % 10)
            
        if carry > 0:
            res.append(carry)
        return ''.join([str(r) for r in res[::-1]])
